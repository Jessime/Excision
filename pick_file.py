#!/usr/bin/env python2
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

        self.initUI()


    def initUI(self):
        fname = QFileDialog.getOpenFileName(self, 'Select Script')
        if fname[0]:
            print(fname[0])
            return fname[0]


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = SelectScript()
    ex.close()