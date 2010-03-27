#!/usr/bin/env python
# encoding: utf-8
"""
test_opds.py

Created by Keith Fahlgren on Sat Feb 20 07:52:48 PST 2010
Copyright (c) 2010 Threepress Consulting Inc. All rights reserved.
"""


import csv
import glob
import logging
import os
import shutil
import tempfile
import uuid

from lxml import etree
from nose.tools import *

import csv2opds
from csv2opds import NSS

log = logging.getLogger(__name__)
class DummyOptions(object):
    def __init__(self):
        self.title = None
        self.author = None

    def __setattr__(self, name, value):
        self.__dict__[name] = value

class TestOpds(object):
    def setup(self):
        self.filedir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'files'))
        self.tempdir = tempfile.mkdtemp()

        self.options = DummyOptions()
        self.options.author = str(uuid.uuid4())
        self.options.title  = str(uuid.uuid4())

        self.rich_csv_fn = os.path.join(self.filedir, 'rich.csv')
        self._write_rich_csv(self.rich_csv_fn)
        self.opds = csv2opds.Opds(self.rich_csv_fn, self.options)
        self.opds.output_catalog(self.tempdir)
        self.catalog_files = glob.glob(self.tempdir + '/*.xml')

        atom_rng_fn = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'schemas', 'atom.rng'))
        self.atom_validator = etree.RelaxNG(etree.parse(atom_rng_fn))

    def teardown(self):
        shutil.rmtree(self.tempdir)


    def test_init(self):
        """A CSV file should be able to be opened"""
        options = DummyOptions()
        options.author = str(uuid.uuid4())
        opds = csv2opds.Opds(self.rich_csv_fn, options)
        assert opds

    def test_output_something(self):
        """An OPDS Catalog should be able to be outputted to a directory"""
        assert len(self.catalog_files) > 0

    def test_sparse_input(self):
        """An OPDS Catalog should be able to be created from a very minimal CSV file"""
        tempdir = tempfile.mkdtemp()
        csv_fn = os.path.join(self.filedir, 'sparse.csv')
        self._write_sparse_csv(csv_fn)
        options = DummyOptions()
        options.author = str(uuid.uuid4())
        opds = csv2opds.Opds(csv_fn, options)
        opds.output_catalog(tempdir)
        catalog_files = glob.glob(tempdir + '/*.xml')
        assert len(catalog_files) > 0

    def test_output_is_xml(self):
        """An OPDS Catalog should be outputted as well-formed XML"""
        for xml in self._catalog_files_as_xml():
            assert xml

    def test_output_is_a_feed(self):
        """An OPDS Catalog should be outputted as a set of Atom feeds"""
        for xml in self._catalog_files_as_xml():
            xml_root_tag = xml.getroot().tag
            expected = '{http://www.w3.org/2005/Atom}feed'
            assert_equal(expected, xml_root_tag)

    def test_links_include_profile(self):
        """An OPDS Catalog should use a profile media type parameter when linking to another Catalog"""
        for xml in self._catalog_files_as_xml():
            for link in xml.xpath('atom:link[starts-with(@type, "application/atom+xml")]', namespaces=NSS):
                assert ';profile=opds-catalog' in link.get('type')

    def test_root_catalog_title(self):
        """The Root OPDS Catalog should use the specified title"""
        xml = self._root_catalog_as_xml()
        actual_title = xml.xpath('/atom:feed/atom:title/text()', namespaces=NSS)[0]
        assert_equals(self.options.title, actual_title)

    def test_output_is_valid_atom(self):
        """An OPDS Catalog should be outputted as a set of valid Atom feeds"""
        for xml in self._catalog_files_as_xml():
            try:
                assert self.atom_validator.validate(xml)
            except AssertionError:
                error_log = self.atom_validator.error_log
                log.warn('Validation errors:\n%s' % error_log)
                raise

    def test_output_has_crawlable(self):
        """An OPDS Catalog should include a crawlable representation"""
        xml = self._root_catalog_as_xml()
        crawlable_links = len(xml.xpath('atom:link[@rel="http://opds-spec.org/crawlable"]', namespaces=NSS))
        expected = 1
        assert_equal(expected, crawlable_links)

    def test_rich_output_has_new_relation(self):
        """A rich OPDS Catalog should include a relation to a Publication Collection of new titles"""
        xml = self._root_catalog_as_xml()
        relations = len(xml.xpath('atom:link[@rel="http://opds-spec.org/new"]', namespaces=NSS))
        expected = 1
        assert_equal(expected, relations)

    def test_output_has_crawlable(self):
        """A Crawlable OPDS Catalog should include an Entry for every row in the input CSV"""
        xml = self._root_catalog_as_xml()
        crawlable_link_href = xml.xpath('atom:link[@rel="http://opds-spec.org/crawlable"]/@href', namespaces=NSS)[0]
        crawlable_fn = os.path.join(self.tempdir, crawlable_link_href)
        crawlable_xml = etree.parse(crawlable_fn)
        entries = len(crawlable_xml.xpath('atom:entry', namespaces=NSS))
        expected = 3
        assert_equal(expected, entries)

    def _root_catalog_as_xml(self):
        root_catalog_fn = os.path.join(self.tempdir, csv2opds.ROOT_CATALOG['output'])
        xml = etree.parse(root_catalog_fn)
        return xml

    def _catalog_files_as_xml(self):
        catalog_files = glob.glob(self.tempdir + '/*.xml')
        catalogs_as_xml = []
        for f in catalog_files:
            xml = etree.parse(f)
            catalogs_as_xml.append(xml)
        return catalogs_as_xml

    def _write_sparse_csv(self, csv_fn):
        writer = csv.writer(open(csv_fn, "wb")) 
        headers = ('ISBN',              'Title',                     'Authors (all first last, joined by commas, no ands)', 'Publication Date (YYYY-MM-DD)', 'Publisher',   'Price (empty for free)', 'Currency', 'ePub URL',                                             'PDF URL', 'Mobi URL', 'Cover Thumbnail URL', 'Language', 'Description (text, less than 2000 chars)', 'Rights', 'Publisher ID', 'Rank', 'On Featured List? (blank for no)')
        row1    = ('978-0-00-000000-0', 'A Year of Breakfasts',      'Liza Daly',                                           '2009-09-23',                    'Threepress',  '',                       '',         'http://threepress.org/examples/opds/downloads/1.epub', '',        '',         '',                    '',         "Today was waffle day!",                    '',       '',             '',     '')
        row2    = ('9780000000010',     'Collaborative Works Rock',  'Keith Fahlgren, Liza Daly, Elizabeth Fahlgren',       '2007-11-01',                    'Threepress',  '',                       '',         'http://threepress.org/examples/opds/downloads/2.epub', '',        '',         '',                    '',         'A gripping thriller.',                     '',       '',             '',     '')
        row3    = ('',                  'Redacteurix, une Histoire', 'Liza Daly',                                           '1899',                          'Troispresse', '',                       '',         'http://threepress.org/examples/opds/downloads/3.epub', '',        '',         '',                    '',         'A mystery of Gallic intensity',            '',       '',             '',     '')

        writer.writerow(headers)
        writer.writerow(row1)
        writer.writerow(row2)
        writer.writerow(row3)

    def _write_rich_csv(self, csv_fn):
        writer = csv.writer(open(csv_fn, "wb")) 
        headers = ('ISBN',              'Title',                     'Authors (all first last, joined by commas, no ands)', 'Publication Date (YYYY-MM-DD)', 'Publisher',   'Price (empty for free)', 'Currency', 'ePub URL',                                             'PDF URL',                                             'Mobi URL',                                             'Cover Thumbnail URL',                                    'Language', 'Description (text, less than 2000 chars)',                                                                                                                                                                                                                                      'Rights',                        'Publisher ID',                                      'Rank', 'On Featured List? (blank for no)')
        row1    = ('978-0-00-000000-0', 'A Year of Breakfasts',      'Liza Daly',                                           '2009-09-23',                    'Threepress',  '12.50',                  'USD',      'http://threepress.org/examples/opds/downloads/1.epub', '',                                                    '',                                                     '',                                                       '',         "Today was waffle day! I had a waffle and decaf coffee and orange juice. Normally I have one and a half waffles, but today there was less waffle batter than usual and I wasn't very hungry because I ate a lot of food last night so I only had one waffle and that was fine.", 'Copyright \xa9 2009 Liza Daly', 'http://threepress.org/examples/opds/identifiers/1', '2',    '')
        row2    = ('9780000000010',     'Collaborative Works Rock',  'Keith Fahlgren, Liza Daly, Elizabeth Fahlgren',       '2007-11-01',                    'Threepress',  '',                       '',         '',                                                     'http://threepress.org/examples/opds/downloads/2.pdf', '',                                                     '',                                                       'en',       'A gripping thriller.',                                                                                                                                                                                                                                                          '',                              'http://threepress.org/examples/opds/identifiers/2', '1',    'y')
        row3    = ('',                  'Redacteurix, une Histoire', 'Liza Daly',                                           '1899',                          'Troispresse', '9.99',                   'EUR',      'http://threepress.org/examples/opds/downloads/3.epub', 'http://threepress.org/examples/opds/downloads/3.pdf', 'http://threepress.org/examples/opds/downloads/3.mobi', 'http://threepress.org/examples/opds/covers/3.thumb.png', 'fr',       'A mystery of Gallic intensity',                                                                                                                                                                                                                                                 '',                              'http://threepress.org/examples/opds/identifiers/3', '',     'y')
        # FIXME: Unicode
        #row3 = ('', u'R\x8edacteurix, une Histoire', u'Liz\x87 D\x89ly', '1899', 'Troispresse', '9.99', 'EUR', 'http://threepress.org/examples/opds/downloads/3.epub', 'http://threepress.org/examples/opds/downloads/3.pdf', 'http://threepress.org/examples/opds/downloads/3.mobi', 'http://threepress.org/examples/opds/covers/3.thumb.png', 'fr', 'http://threepress.org/examples/opds/covers/3.thumb.png', '', 'http://threepress.org/examples/opds/identifiers/3', '', '')

        writer.writerow(headers)
        writer.writerow(row1)
        writer.writerow(row2)
        writer.writerow(row3)
