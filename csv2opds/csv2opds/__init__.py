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


log = logging.getLogger(__name__)

NSS = {'atom': 'http://www.w3.org/2005/Atom',
       'opds': 'http://opds-spec.org/2010/catalog'
      } 
CSV_TEMPLATE_HEADERS = ['title', 'authors', 'acquisition_url', 'description'
                       ]
                        #'isbn', 'pubdate', 'publisher', 'price', 'currency', 
                        #'ePub_url', 'pdf_url', 'mobi_url', 'cover_thumbnail_url', 
                        #'language', 'description', 'rights', 'publisher_id', 'rank', 'featured']
UUID_KEY = uuid.UUID('31cce9f0-ed0f-4ce0-a4e5-da331ed7341e')

CATALOGS = {'root': 'opds.xml',
            'crawlable': 'crawlable.xml',
            'new': 'new.xml',
            'featured': 'featured.xml',
            'popular': 'popular.xml',
            'alphabetical': 'alpha.xml',
            'authors': 'authors.xml',
           }
CATALOG_TYPE = "application/atom+xml;type=feed;profile=opds-catalog"
DEFAULT_TITLE = 'OPDS Catalog'

import csv2opds.entry

class Opds(object):
    def __init__(self, csv_fn, options):
        self.author = options.author
        self.root_title = options.title if options.title else DEFAULT_TITLE

        template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'templates'))
        self.template_loader = genshi.template.TemplateLoader([template_dir])

        self.uuid_master = uuid.uuid3(UUID_KEY, self.author)
        self.entries = self.entries_from_csv(csv_fn, self.uuid_master)
        self.featured_catalog = any([e.featured for e in self.entries])
        self.new_catalog = any([e.pubdate for e in self.entries])
        self.popular_catalog = any([e.rank for e in self.entries])

    def entries_from_csv(self, csv_fn, uuid_master):
        entries = []
        csv_file = open(csv_fn)
        sample = csv_file.read(1024)
        csv_dialect = csv.Sniffer().sniff(sample)
        csv_file.seek(0)
        for row in list(csv.reader(csv_file, dialect=csv_dialect))[1:]: # Always has a heading row
            e = entry.Entry(row, uuid_master)
            entries.append(e)
        csv_file.close()
        return entries

    def output_catalog(self, output_dir):
        self._generate_root(output_dir)
        self._generate_crawlable(output_dir)

    def _generate_root(self, output_dir):
        root_fn = os.path.join(output_dir, CATALOGS['root'])
        f = open(root_fn, 'w')
        tmpl = self.template_loader.load(CATALOGS['root'])
        root_uuid = uuid.uuid3(self.uuid_master, CATALOGS['root'])
        root_urn = 'urn:uuid:' + str(root_uuid)
        catalogs = {}
        for k, v in CATALOGS.iteritems():
            nav_entry_uuid = uuid.uuid3(root_uuid, v)
            nav_entry_urn = 'urn:uuid:' + str(nav_entry_uuid)
            catalogs[k] = [v, nav_entry_urn]
        tmpl_vars = {'feed_author': self.author,
                     'catalogs': catalogs,
                     'title': self.root_title,
                     'featured_catalog': self.featured_catalog,
                     'new_catalog': self.new_catalog,
                     'popular_catalog': self.popular_catalog,
                     'atom_id': root_urn,
                    }
        output = tmpl.generate(**tmpl_vars)
        f.write(output.render())
        f.close()

    def _generate_crawlable(self, output_dir):
        crawlable_fn = os.path.join(output_dir, CATALOGS['crawlable'])
        f = open(crawlable_fn, 'w')
        tmpl = self.template_loader.load(CATALOGS['crawlable'])
        crawlable_urn = 'urn:uuid:' + str(uuid.uuid3(self.uuid_master, CATALOGS['crawlable']))
        tmpl_vars = {'feed_author': self.author,
                     'catalogs': CATALOGS,
                     'entries': self.entries,
                     'atom_id': crawlable_urn,
                    }
        output = tmpl.generate(**tmpl_vars)
        f.write(output.render())
        f.close()
