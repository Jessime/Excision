#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 23:15:47 2016

@author: jessime
"""
import sys
from PyQt5.QtWidgets import (QMainWindow, QFileDialog, QApplication)

class SelectScript(QMainWindow):

    def __init__(self):
        super().__init__()

        self.file = self.initUI()


    def initUI(self):
        fname = QFileDialog.getOpenFileName(self, 'Select Script')
        if fname[0]:
            return fname[0]

def pick():
    """Pick a file."""
    #Creating the app is necessary to avoid "Must construct a QApplication before a QWidget" error.
    app = QApplication(sys.argv)
    picker = SelectScript()
    picker.close()
    return picker.file

if __name__ == '__main__':
    print(pick())
