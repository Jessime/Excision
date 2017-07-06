import os
import sys
import json
import markdown
import subprocess as sp
import numpy as np
import pandas as pd

from flask import Markup
from pickle import load
from importlib import import_module, reload
from shutil import copyfile
from traceback import format_exc

from level_markdown import parse, change_log

class State():
    """

    Parameters
    ----------
    lvl_data : dict
        An example schema for lvl_data is:
        {level_number : {'problem':{'cmd': 'command',
                                    'answer': 'answer'
                                   },
                         'task1':{'func': 'function_name',
                                  'tests': [[arg1, arg2, arg3],
                                            [arg1, arg2, arg3],
                                            [arg1, arg2, arg3]
                                           ],
                                  'answers': [answer1, answer2, answer3]
                                 }
                         'task2':{'func': 'function_name',
                                  'tests': [[arg1, arg2],
                                            [arg1, arg2]
                                           ]
                                  'answers': [answer1, answer2]
                                 }
                         'task2':{'func': 'function_name',
                                  'tests': [[arg1, arg2, arg3]
                                           ]
                                  'answers': [answer1]
                                 }
                        }
        }
    """

    PACKAGE = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    config_path = os.path.join(PACKAGE, 'config.json')

    try:
        config = json.load(open(config_path))
    except FileNotFoundError:
        config = {"current_level": {"num": 1, "title": "DECISIONS"}}
        json.dump(config, open(config_path, 'w'))

    lvl_num_top = config['current_level']['num']
    lvl_num_active = lvl_num_top
    lvl_title = config['current_level']['title']
    script = None
    error_types = {'missing_file': 'Error: No file produced at Excision/results/{}.txt.',
                   'empty_file': 'Error: There is nothing in the file you created.',
                   'bad_type': 'Error: Your result may need to be a {} not a {}.',
                   'incorrect': 'Error: Your answer is incorrect.',
                   'task_test': 'Error: The function gave an incorrect answer on a test.',
                   'no_func': 'Error: The file does not contain the correct function name.'}

    lvl_data = load(open('levels.pkl', 'rb'))
    changes = change_log()
    _sections = None

    @classmethod
    def get_sections(self, lvl_num):
        no_markup = {'title', 'subtitle', 'img'}
        infile = 'static/story/level{}.md'.format(lvl_num)
        sec_dict = parse(infile)
        changes = change_log()
        sec_dict = {**sec_dict, **changes}
        marked_dict = {}
        for k, v in sec_dict.items():
            if k not in no_markup:
                v = self.markup_str(self, v)
            marked_dict[k] = v
        return marked_dict

    @classmethod
    def update_config(self):
        """If the user sucessfully completes a level, save the game."""
        self.lvl_num_top += 1
        infile = 'static/story/level{}.md'.format(self.lvl_num_top)
        sections = parse(infile)
        self.lvl_title = sections['title']
        self.config['current_level'] = {'num':self.lvl_num_top, 'title':self.lvl_title}
        json.dump(self.config, open(self.config_path, 'w'))

    @classmethod
    def process_request(self, func_name):
        """Execute the method corresponding to func_name."""
        result = vars(self)[func_name](self)
        return result

    def markup_str(self, string):
        """Prepares a markdown formatted string for insertion into jinja template."""
        markup = Markup(markdown.markdown(string))
        return markup

    def temp_copy(self):
        """Creates a copy of a user file into the src dir to be imported"""
        new = os.path.basename(self.script)
        copyfile(self.script, new)
        return new

    def temp_del(self, temp):
        """Delete file created by temp_copy."""
        if os.path.isfile(temp):
            os.remove(temp)

    def try_running_problem(self, cmd):
        error = None
        #TODO For loop here if we want multiple tests
        try:
            print(cmd.split())
            sp.run(cmd.split(), stderr=sp.PIPE, check=True)
        except sp.CalledProcessError as e:
            error = e.stderr.decode("utf-8")
        return error

    def check_result(self, outfile, error, ans):
        with open(outfile) as outfile:
            result = outfile.read().strip()
        if not result:
            error = self.error_types['empty_file']
        if not error and result != ans:
            error = self.error_types['incorrect']
        return error

    def problem(self):
        success = False
        error = None
        outfile = '../results/{}.txt'.format(self.lvl_num_active) #TODO edit to represent current displayed problem; temp state?
        data = self.lvl_data[self.lvl_num_active]['problem'] #TODO edit to represent current displayed problem; temp state?
        if os.path.isfile(outfile):
            os.remove(outfile)

        error = self.try_running_problem(self, data['cmd'].format(self.script))

        if not os.path.isfile(outfile) and error is None:
            error = self.error_types['missing_file'].format(self.lvl_num_active) #TODO edit to represent current displayed problem; temp state?
            return success, error

        if error is None:
            error = self.check_result(self, outfile, error, data['answer'])

        success = error is None
        return success, error

    def check_task_result(self, result, ans):
        error = None
        if isinstance(ans, np.ndarray):
            equal = np.array_equal(result, ans)
        elif isinstance(ans, pd.DataFrame):
            equal = ans.equals(result)
        else:
            equal = result == ans
        if not equal:
            error = self.error_types['task_test']
            if type(result) != type(ans):
                error = self.error_types['bad_type']
                error = error.format(type(ans), type(result))

        return error

    def try_running_function(self, new, data):
        error = None
        module_name = new.split('.')[0]
        try:
            if module_name in sys.modules:
                user_import = reload(sys.modules[module_name])
            else:
                user_import = import_module(module_name)
            if data['func'] not in vars(user_import):
                error = self.error_types['no_func']
                return error

            func = vars(user_import)[data['func']]
            for test, ans in zip(data['tests'], data['answers']):
                test = [p.copy() if isinstance(p, np.ndarray) else p for p in test]
                result = func(*test)
                error = self.check_task_result(self, result, ans)
                if error is not None:
                    break

        except Exception:
            error = format_exc()
        return error

    def task_test(self, task):
        error = None
        new = self.temp_copy(self)
        data = self.lvl_data[self.lvl_num_active][task] #TODO edit to represent current displayed problem; temp state?
        error = self.try_running_function(self, new, data)
        self.temp_del(self, new)
        success = error is None
        return success, error

    def task1(self):
        return self.task_test(self, 'task1')

    def task2(self):
        return self.task_test(self, 'task2')

    def task3(self):
        return self.task_test(self, 'task3')
