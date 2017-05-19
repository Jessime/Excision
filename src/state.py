# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 15:50:23 2016

@author: jessime
"""

import os
import subprocess as sp
import importlib
import traceback
import numpy as np

from shutil import copyfile

class Tutorial():
    script = None
    syntax_error1 = None
    semantics_error1 = None
    hint_solved1 = False
    hint_solved2 = False
    syntax_error2 = None
    semantics_error2 = None

    def tutorial_gc(self):
        gc_txt = '../results/tutorial/gc.txt'
        if os.path.isfile(gc_txt):
            os.remove(gc_txt)

        cmd = 'python {} ATATATATGGGGGC'.format(self.script)
        try:
            sp.run(cmd.split(), stderr=sp.PIPE, check=True)
        except sp.CalledProcessError as e:
            self.syntax_error1 = e.stderr.decode("utf-8")
        if self.syntax_error1 is None:
            if not os.path.isfile(gc_txt):
                self.semantics_error1 = 'Your program did not produce a file in the proper location.'
            else:
                with open(gc_txt) as infile:
                    result = infile.read()
                if not result:
                    self.semantics_error1 = 'There is nothing in the file you created.'
                elif result != '42%\n':
                    self.semantics_error1 = 'Your answer is not correct.'

        result = (self.semantics_error1 is None) and (self.syntax_error1 is None)
        return result

    def tutorial_sum(self):
        sum_txt = '../results/tutorial/sum.txt'
        if os.path.isfile(sum_txt):
            os.remove(sum_txt)

        #generate temp data
        rand = np.random.randint(-10, 10, [10, 10])
        max_val = max(rand.sum(0).max(), rand.sum(1).max())
        rand_file = '../results/sum_rand.txt'
        np.savetxt(rand_file, rand, delimiter=',')

        cmd = 'python {} {}'.format(self.script, rand_file)
        try:
            sp.run(cmd.split(), stderr=sp.PIPE, check=True)
        except sp.CalledProcessError as e:
            self.syntax_error2 = e.stderr.decode("utf-8")
        if self.syntax_error2 is None:
            if not os.path.isfile(sum_txt):
                self.semantics_error2 = 'Your program did not produce a file in the proper location.'
            else:
                with open(sum_txt) as infile:
                    result = infile.read().strip()
                if not result:
                    self.semantics_error2 = 'There is nothing in the file you created.'
                elif result != str(max_val):
                    self.semantics_error2 = 'Your answer is not correct.'

        result = (self.semantics_error2 is None) and (self.syntax_error2 is None)
        return result

    def tutorial_task1(self):
        new = self.temp_copy(self)
        try:
            user_import = importlib.import_module(new.split('.')[0])
            result1 = user_import.squared_sum([1, 2, 3])
            result2 = user_import.squared_sum([-1, 3])
            if result1 == 14 and result2 == 10:
                self.hint_solved1 = True

        except Exception:
            print(traceback.format_exc())

        self.temp_del(self, new)
        return self.hint_solved1

    def tutorial_task2(self):
        new = self.temp_copy(self)
        try:
            user_import = importlib.import_module(new.split('.')[0])
            result1 = user_import.seen([1, 2, 3], [1,2,3,4,4,5, 'what'])
            result2 = user_import.seen(['s', 9], ['s', 9])
            if set(result1) == set(['what', 4, 5]) and result2 == []:
                self.hint_solved2 = True

        except Exception:
            print(traceback.format_exc())
        self.temp_del(self, new)
        return self.hint_solved2

    def temp_copy(self):
        """Creates a copy of a user file into the src dir to be imported"""
        new = os.path.basename(self.script)
        copyfile(self.script, new)
        return new

    def temp_del(self, temp):
        """Delete file created by temp_copy."""
        if os.path.isfile(temp):
            os.remove(temp)

    @classmethod
    def process_request(self, func_name):
        """Execute the method corresponding to func_name."""
        result = vars(self)[func_name](self)
        return result

class Data():
    """Resposible for keeping track of the state of the app."""

    submission_form = None
    script = None
