#!/usr/bin/env python
# encoding: utf-8
"""
__init__.py

Created by Keith Fahlgren on Sat Feb 20 08:02:24 PST 2010
Copyright (c) 2010 Threepress Consulting Inc. All rights reserved.
"""

import logging
import os
import uuid

import genshi.template 

log = logging.getLogger(__name__)

UUID_KEY = uuid.UUID('31cce9f0-ed0f-4ce0-a4e5-da331ed7341e')

class Opds(object):

    def __init__(self, csv_file, author):
        template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'templates'))
        self.template_loader = genshi.template.TemplateLoader([template_dir])
        self.author = author
        self.uuid_master = uuid.uuid3(UUID_KEY, self.author)

    def output_catalog(self, output_dir):
        catalog_root_fn = os.path.join(output_dir, 'opds.xml')
        f = open(catalog_root_fn, 'w')
        tmpl = self.template_loader.load('root.xml')
        root_urn = 'urn:uuid:' + str(uuid.uuid3(self.uuid_master, 'root.xml'))
        output = tmpl.generate(feed_author=self.author, atom_id=root_urn)
        f.write(output.render())
        f.close()
