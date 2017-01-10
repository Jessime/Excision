# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 15:50:23 2016

@author: jessime
"""

import os
import subprocess as sp
import importlib
import traceback

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
        gc_txt = 'results/tutorial/gc.txt'
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
                with open('results/tutorial/gc.txt') as infile:
                    result = infile.read()
                    if not result:
                        self.semantics_error1 = 'There is nothing in the file you created.'
                    elif result != '42%\n':
                        self.semantics_error1 = 'Your answer is not correct.'
                    else:
                        self.semantics_error1 = 'Good job! There was no error!'

    def tutorial_sum(self):
        pass

    def tutorial_hint1(self):
        new = self.temp_copy(self)
        try:
            user_import = importlib.import_module(new.split('.')[0])
            result = user_import.squared_sum([1,2])
            if result == 5:
                self.hint_solved1 = True
                
        except Exception:
            print(traceback.format_exc())
        
        self.temp_del(self, new)
            
    def tutorial_hint2(self):
        pass
    
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
    def process_post(self, form_name):
        """Execute the method name corresponding to a given POST form name."""
        vars(self)[form_name](self)

class Data():
    """Resposible for keeping track of the state of the app."""

    submission_form = None
    script = None