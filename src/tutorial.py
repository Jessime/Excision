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

    def tutorial_gc(self):
        error = None
        gc_txt = '../results/tutorial/gc.txt'
        if os.path.isfile(gc_txt):
            os.remove(gc_txt)

        cmd = 'python {} ATATATATGGGGGC'.format(self.script)
        try:
            sp.run(cmd.split(), stderr=sp.PIPE, check=True)
        except sp.CalledProcessError as e:
            error = e.stderr.decode("utf-8")
        if error is None:
            if not os.path.isfile(gc_txt):
                error = 'Your program did not produce a file in the proper location.'
            else:
                with open(gc_txt) as infile:
                    result = infile.read().strip()
                if not result:
                    error = 'There is nothing in the file you created.'
                elif result != '42%':
                    error = 'Your answer is not correct.'

        success = error is None
        return success, error

    def tutorial_sum(self):
        error = None
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
            error = e.stderr.decode("utf-8")
        if error is None:
            if not os.path.isfile(sum_txt):
                error = 'Your program did not produce a file in the proper location.'
            else:
                with open(sum_txt) as infile:
                    result = infile.read().strip()
                if not result:
                    error = 'There is nothing in the file you created.'
                elif result != str(max_val):
                    error = 'Your answer is not correct.'

        success = error is None
        return success, error

    def tutorial_task1(self):
        error = None
        new = self.temp_copy(self)

        try:
            user_import = importlib.import_module(new.split('.')[0])
            result1 = user_import.squared_sum([1, 2, 3])
            result2 = user_import.squared_sum([-1, 3])
            if result1 != 14 or result2 != 10:
                error = 'Your answer is not correct.'

        except Exception:
            error = traceback.format_exc()

        self.temp_del(self, new)
        success = error is None
        return success, error

    def tutorial_task2(self):
        error = None
        new = self.temp_copy(self)

        try:
            user_import = importlib.import_module(new.split('.')[0])
            result1 = set(user_import.seen([1, 2, 3], [1,2,3,4,4,5, 'what']))
            result2 = user_import.seen(['s', 9], ['s', 9])
            if result1 != set(['what', 4, 5]) or result2 != []:
                error = 'Your answer is not correct.'

        except Exception:
            error = traceback.format_exc()

        self.temp_del(self, new)
        success = error is None
        return success, error

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
