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

class TestOpds(object):
    def setup(self):
        self.author = str(uuid.uuid4())
        self.filedir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'files'))
        self.tempdir = tempfile.mkdtemp()
        self.simple_csv_fn = os.path.join(self.filedir, 'simple.csv')
        self._write_simple_csv(self.simple_csv_fn)
        self.opds = csv2opds.Opds(self.simple_csv_fn, self.author)
        atom_rng_fn = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'schemas', 'atom.rng'))
        self.atom_validator = etree.RelaxNG(etree.parse(atom_rng_fn))

    def test_init(self):
        """A CSV file should be able to be opened"""
        opds = csv2opds.Opds(self.simple_csv_fn, self.author)
        assert opds

    def test_output_something(self):
        """An OPDS Catalog should be able to be outputted to a directory"""
        self.opds.output_catalog(self.tempdir)
        catalog_files = glob.glob(self.tempdir + '/*.xml')
        assert len(catalog_files) > 0


    def test_output_is_xml(self):
        """An OPDS Catalog should be outputted as well-formed XML"""
        self.opds.output_catalog(self.tempdir)
        catalog_files = glob.glob(self.tempdir + '/*.xml')
        for f in catalog_files:
            xml = etree.parse(f)
            assert xml

    def test_output_is_a_feed(self):
        """An OPDS Catalog should be outputted as a set of Atom feeds"""
        self.opds.output_catalog(self.tempdir)
        catalog_files = glob.glob(self.tempdir + '/*.xml')
        for f in catalog_files:
            xml = etree.parse(f)
            xml_root_tag = xml.getroot().tag
            expected = '{http://www.w3.org/2005/Atom}feed'
            assert_equal(expected, xml_root_tag)


    def test_output_is_valid_atom(self):
        """An OPDS Catalog should be outputted as a set of valid Atom feeds"""
        self.opds.output_catalog(self.tempdir)
        catalog_files = glob.glob(self.tempdir + '/*.xml')
        for f in catalog_files:
            xml = etree.parse(f)
            try:
                assert self.atom_validator.validate(xml)
            except AssertionError:
                error_log = self.atom_validator.error_log
                log.warn('Validation errors:\n%s' % error_log)
                raise

    def test_output_has_crawlable(self):
        """An OPDS Catalog should include a crawlable representation"""
        self.opds.output_catalog(self.tempdir)
        catalog_fn = glob.glob(self.tempdir + '/*.xml')[0]
        xml = etree.parse(catalog_fn)
        crawlable_links = len(xml.xpath('atom:link[@rel="http://opds-spec.org/crawlable"]', namespaces=NSS))
        expected = 1
        assert_equal(expected, crawlable_links)

    def test_output_has_crawlable(self):
        """A Crawlable OPDS Catalog should include an Entry for every row in the input CSV"""
        self.opds.output_catalog(self.tempdir)
        catalog_fn = os.path.join(self.tempdir, csv2opds.ROOT_CATALOG['output'])
        xml = etree.parse(catalog_fn)
        crawlable_link_href = xml.xpath('atom:link[@rel="http://opds-spec.org/crawlable"]/@href', namespaces=NSS)[0]
        crawlable_fn = os.path.join(self.tempdir, crawlable_link_href)
        crawlable_xml = etree.parse(crawlable_fn)
        entries = len(crawlable_xml.xpath('atom:entry', namespaces=NSS))
        expected = 2
        assert_equal(expected, entries)


    def teardown(self):
        shutil.rmtree(self.tempdir)

    def _write_simple_csv(self, csv_fn):
        writer = csv.writer(open(csv_fn, "wb")) 
        headers = ('ISBN', 'Title', 'Authors (all first last, joined by commas, no ands)', 'Publication Date (YYYY-MM-DD)', 'Publisher', 'Price (empty for free)', 'Currency', 'ePub URL', 'PDF URL', 'Mobi URL', 'Cover Thumbnail URL', 'Language', 'Description (text, less than 2000 chars)', 'Rights', 'Publisher ID', 'Rank', 'On Featured List? (blank for no)')
        row1 = ('978-0-00-000000-0', 'A Year of Breakfasts', 'Liza Daly', '2009-09-23', 'Threepress', '12.50', 'USD', 'http://threepress.org/examples/opds/downloads/1.epub', '', '', 'http://threepress.org/examples/opds/covers/1.thumb.jpg', 'en', "Today was waffle day! I had a waffle and decaf coffee and orange juice. Normally I have one and a half waffles, but today there was less waffle batter than usual and I wasn't very hungry because I ate a lot of food last night so I only had one waffle and that was fine.", 'Copyright \xa9 2009 Liza Daly', 'http://threepress.org/examples/opds/identifiers/1', '2', '')
        row2 = ('9780000000010', 'Collaborative Works Rock', 'Keith Fahlgren, Liza Daly, Elizabeth Fahlgren', '2007-11-01', 'Threepress', '', '', 'http://threepress.org/examples/opds/downloads/2.epub', 'http://threepress.org/examples/opds/downloads/2.pdf', '', '', 'en', 'A gripping thriller.', '', 'http://threepress.org/examples/opds/identifiers/2', '1', 'y')
        #FIXME
        #row3 = ('', u'R\x8edacteurix, une Histoire', u'Liz\x87 D\x89ly', '1899', 'Troispresse', '9.99', 'EUR', 'http://threepress.org/examples/opds/downloads/3.epub', 'http://threepress.org/examples/opds/downloads/3.pdf', 'http://threepress.org/examples/opds/downloads/3.mobi', 'http://threepress.org/examples/opds/covers/3.thumb.png', 'fr', 'http://threepress.org/examples/opds/covers/3.thumb.png', '', 'http://threepress.org/examples/opds/identifiers/3', '', '')

        writer.writerow(headers)
        writer.writerow(row1)
        writer.writerow(row2)
        #writer.writerow(row3)
