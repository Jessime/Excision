# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 15:50:23 2016

@author: jessime
"""

from os.path import isfile
import subprocess as sp

class Tutorial():
    script = None
    syntax_error1 = None
    semantics_error1 = None
    hint_solved1 = False
    hint_solved2 = False
    syntax_error2 = None
    semantics_error2 = None


    def tutorial_gc(self):
        cmd = 'python {} ATATATATGGGGGC'.format(self.script)
        try:
            sp.run(cmd.split(), stderr=sp.PIPE, check=True)
        except sp.CalledProcessError as e:
            self.syntax_error1 = e.stderr.decode("utf-8")
        if self.syntax_error1 is None:
            if not isfile('results/tutorial/gc.txt'):
                self.semantics_error1 = 'Your program did not produce a file in the proper location'
            else:
                with open('results/tutorial/gc.txt') as infile:
                    result = infile.read()
                    if not result:
                        self.semantics_error1 = 'There is nothing in the file you created'
                    elif result != '42%\n':
                        self.semantics_error1 = 'Your answer is not correct.'
                    else:
                        self.semantics_error1 = 'Good job! There was no error!'

    def tutorial_sum(self):
        pass

    def tutorial_hint1(self):
        pass

    def tutorial_hint2(self):
        pass

    @classmethod
    def process_post(self, form_name):
        name2func = {'tutorial_gc': self.tutorial_gc,
                     'tutorial_sum': self.tutorial_sum,
                     'tutorial_hint1': self.tutorial_hint1,
                     'tutorial_hint2': self.tutorial_hint2}
        name2func[form_name](self)

class Data():
    """Resposible for keeping track of the state of the app."""

    submission_form = None
    script = None