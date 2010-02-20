#!/usr/bin/env python
# encoding: utf-8
"""
test_opds.py

Created by Keith Fahlgren on Sat Feb 20 07:52:48 PST 2010
Copyright (c) 2010 Threepress Consulting Inc. All rights reserved.
"""

import os
import csv2opds

from nose.tools import *

class TestOpds(object):
    def setup(self):
        self.filedir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'files'))

    def test_init(self):
        """A CSV file should be able to be opened"""
        file = os.path.join(self.filedir, 'simple.csv')
        opds = csv2opds.Opds(file)
        assert opds

