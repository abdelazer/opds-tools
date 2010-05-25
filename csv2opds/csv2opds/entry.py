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

from csv2opds import CSV_TEMPLATE_HEADERS

log = logging.getLogger(__name__)

ISBN_CLEAN = re.compile('[^0-9xX]')

class Entry(object):
    def __init__(self, data_row, uuid_master):
        self.data = {}
        self.uuid_master = uuid_master
        for ix, item in enumerate(data_row):
            header_key = CSV_TEMPLATE_HEADERS[ix]
            clean_value = item
            if header_key == 'isbn':
                clean_value = re.sub(ISBN_CLEAN, '', item)
            elif header_key == 'authors':
                clean_value = [a.strip() for a in item.split(',')]
            elif header_key == 'acquisition_url':
                clean_value = item
                if item.endswith('epub'):
                    self.acquisition_type = 'application/epub+zip'
                elif item.endswith('pdf'):
                    self.acquisition_type = 'application/pdf'
                elif item.endswith('mobi'):
                    self.acquisition_type = "application/x-mobipocket-ebook" 

            self.data[header_key] = clean_value
        self._set_identifiers()

    def __getattr__(self, key): 
        if self.__dict__.has_key(key):
            return self.__dict__[key]
        elif key in CSV_TEMPLATE_HEADERS:
            if self.data.has_key(key):
                return self.data[key]
            else:
                return None

    def __repr__(self):
        return '<Entry %s with data %s>' % (self.urn, self.data.keys())

    def _set_identifiers(self):
        self.identifiers = []
        entry_uuid = None
        if self.isbn is not None:
            entry_uuid = uuid.uuid3(self.uuid_master, isbn)
            self.identifiers.append('urn:isbn:%s' % isbn)
        else:
            entry_uuid = uuid.uuid3(self.uuid_master, ''.join(self.authors) + self.title)
        self.urn = 'urn:uuid:%s' % entry_uuid

