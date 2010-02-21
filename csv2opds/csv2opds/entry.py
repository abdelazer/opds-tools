#!/usr/bin/env python
# encoding: utf-8
"""
entry.py

Created by Keith Fahlgren on Sat Feb 20 09:59:38 PST 2010
Copyright (c) 2010 Threepress Consulting Inc. All rights reserved.
"""

import logging
import os
import re
import uuid

log = logging.getLogger(__name__)

ISBN_CLEAN = re.compile('[^0-9xX]')

class Entry(object):
    def __init__(self, csv_dict_row, uuid_master):
        self.title = csv_dict_row['title']
        self.content = csv_dict_row['description']

        self.identifiers = []
        isbn = re.sub(ISBN_CLEAN, '', csv_dict_row['isbn'])
        self.authors = [a.strip() for a in csv_dict_row['authors'].split(',')]
        if isbn:
            self.entry_uuid = uuid.uuid3(uuid_master, isbn)
            self.identifiers.append('urn:isbn:%s' % isbn)
        else:
            self.entry_uuid = uuid.uuid3(uuid_master, ''.join(self.authors) + self.title)
        self.urn = 'urn:uuid:%s' % self.entry_uuid
