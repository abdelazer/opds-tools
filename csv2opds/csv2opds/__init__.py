#!/usr/bin/env python
# encoding: utf-8
"""
__init__.py

Created by Keith Fahlgren on Sat Feb 20 08:02:24 PST 2010
Copyright (c) 2010 Threepress Consulting Inc. All rights reserved.
"""

import csv
import logging
import os
import uuid

import genshi.template 

import entry

log = logging.getLogger(__name__)

UUID_KEY = uuid.UUID('31cce9f0-ed0f-4ce0-a4e5-da331ed7341e')
NSS = {'atom': 'http://www.w3.org/2005/Atom',
       'opds': 'http://opds-spec.org/2010/catalog'
      } 
ROOT_CATALOG = {'template': 'root.xml',
                'output':   'opds.xml'}
CRAWLABLE_CATALOG = {'template': 'crawlable.xml',
                     'output':   'crawlable.xml'}
CSV_TEMPLATE_HEADERS = ['isbn', 'title', 'authors', 'pubdate', 'publisher', 'price', 'currency', 
                        'ePub_url', 'pdf_url', 'mobi_url', 'cover_thumbnail_url', 
                        'language', 'description', 'rights', 'publisher_id', 'rank', 'featured']

class Opds(object):
    def __init__(self, csv_fn, catalog_author):
        template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'templates'))
        self.template_loader = genshi.template.TemplateLoader([template_dir])
        self.author = catalog_author
        self.uuid_master = uuid.uuid3(UUID_KEY, self.author)
        self.entries = self.entries_from_csv(csv_fn, self.uuid_master)

    def entries_from_csv(self, csv_fn, uuid_master):
        entries = []
        csv_file = open(csv_fn)
        sample = csv_file.read(1024)
        csv_dialect = csv.Sniffer().sniff(sample)
        csv_file.seek(0)
        for row in list(csv.DictReader(csv_file, fieldnames=CSV_TEMPLATE_HEADERS, dialect=csv_dialect))[1:]: # Always has a heading row
            e = entry.Entry(row, uuid_master)
            entries.append(e)
        csv_file.close()
        return entries

    def output_catalog(self, output_dir):
        self._generate_root(output_dir)
        self._generate_crawlable(output_dir)

    def _generate_root(self, output_dir):
        root_fn = os.path.join(output_dir, ROOT_CATALOG['output'])
        f = open(root_fn, 'w')
        tmpl = self.template_loader.load(ROOT_CATALOG['template'])
        root_urn = 'urn:uuid:' + str(uuid.uuid3(self.uuid_master, ROOT_CATALOG['template']))
        tmpl_vars = {'feed_author': self.author,
                     'root': ROOT_CATALOG['output'],
                     'crawlable': CRAWLABLE_CATALOG['output'],
                     'atom_id': root_urn,
                    }
        output = tmpl.generate(**tmpl_vars)
        f.write(output.render())
        f.close()

    def _generate_crawlable(self, output_dir):
        crawlable_fn = os.path.join(output_dir, CRAWLABLE_CATALOG['output'])
        f = open(crawlable_fn, 'w')
        tmpl = self.template_loader.load(CRAWLABLE_CATALOG['template'])
        crawlable_urn = 'urn:uuid:' + str(uuid.uuid3(self.uuid_master, CRAWLABLE_CATALOG['template']))
        tmpl_vars = {'feed_author': self.author,
                     'root': ROOT_CATALOG['output'],
                     'entries': self.entries,
                     'atom_id': crawlable_urn,
                    }
        output = tmpl.generate(**tmpl_vars)
        f.write(output.render())
        f.close()
