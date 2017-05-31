import os
import json

from pickle import load

from level_markdown import parse

class State():

    PACKAGE = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    config_path = os.path.join(PACKAGE, 'config.json')
    config = json.load(open(config_path))
    lvl_num = config['current_level']['num']
    lvl_title = config['current_level']['title']
    script = None
    error_types = {'missing_file': 'Error: No file produced at Excision/results/{}.txt.',
                   'empty_file': 'Error: There is nothing in the file you created.',
                   'bad_type': 'Error: Your answer cannot be converted into a {}.',
                   'incorrect': 'Error: Your answer is incorrect.'}

    with open('cmds.txt') as infile:
        cmd_list = [line.strip() for line in infile.readlines()]
    correct_answers = load(open('correct.pkl', 'rb'))

    @classmethod
    def update_config(self):
        """If the user sucessfully completes a level, save the game."""
        self.lvl_num += 1
        infile = 'static/story/level{}.md'.format(self.lvl_num)
        sections = parse(infile)
        self.lvl_title = sections['title']
        self.config['current_level'] = {'num':self.lvl_num, 'title':self.lvl_title}
        json.dump(open(config_path, 'w'))

    @classmethod
    def process_request(self, func_name):
        """Execute the method corresponding to func_name."""
        result = vars(self)[func_name](self)
        return result

    def try_running(self):
        #TODO For loop here if we want multiple tests
        cmd = self.cmd_list[self.lvl_num].format(self.script)
        try:
            sp.run(cmd.split(), stderr=sp.PIPE, check=True)
        except sp.CalledProcessError as e:
            error = e.stderr.decode("utf-8")

    def check_results(self, outfile, error):
        with open(outfile) as outfile:
            result = outfile.read().strip()
        if not result:
            error = self.error_types['empty_file']
        if not error and result != self.correct_answers[self.lvl_num]:
            error = self.error_types['incorrect']
        return error

    def problem(self):
        success = False
        error = None
        outfile = 'results/{}.txt'.format(self.lvl_num)
        if os.path.isfile(outfile):
            os.remove(outfile)
        else:
            error = self.error_types['missing_file'].format(self.lvl_num)
            return success, error

        error = self.try_running()
        if error is None:
            error = self.check_results(outfile, error)

        success = error is None
        return success, error

    #TODO Tasks
