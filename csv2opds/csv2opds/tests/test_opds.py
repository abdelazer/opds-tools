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
from nose.plugins.skip import SkipTest

import csv2opds
from csv2opds import CSV_TEMPLATE_HEADERS, NSS

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

        self.minimum_csv_fn = os.path.join(self.filedir, 'minimum.csv')
        self.minimum_data = [
            ["A Year of Breakfasts",     "Liza Daly",                                   "http://threepress.org/examples/opds/downloads/1.epub"],
            ["Collaborative Works Rock", "Ed Summers, Hadrien Gardeur, Peter Brantley", "http://threepress.org/examples/opds/downloads/2.pdf"],
        ]
        self._write_csv(self.minimum_csv_fn, self.minimum_data)

        self.minimum_opds = csv2opds.Opds(self.minimum_csv_fn, self.options)
        self.minimum_opds.output_catalog(self.tempdir)
        self.catalog_files = glob.glob(self.tempdir + '/*.xml')

        atom_rng_fn = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'schemas', 'atom.rng'))
        self.atom_validator = etree.RelaxNG(etree.parse(atom_rng_fn))

    def teardown(self):
        shutil.rmtree(self.tempdir)

    def test_init(self):
        """A CSV file should be able to create an OPDS Catalog"""
        options = DummyOptions()
        options.author = str(uuid.uuid4())
        opds = csv2opds.Opds(self.minimum_csv_fn, options)
        assert opds

    def test_output_something(self):
        """An OPDS Catalog should be able to be outputted to a directory"""
        assert len(self.catalog_files) > 0

    def test_sparse_input(self):
        """An OPDS Catalog should be able to be created from a very minimal CSV file"""
        assert self.minimum_opds

    def test_output_is_xml(self):
        """All OPDS Catalogs Feed documents should be well-formed XML"""
        for xml in self._catalog_files_as_xml():
            assert xml

    def test_output_is_a_feed(self):
        """All OPDS Catalog Feed Documents should be Atom feeds"""
        for xml in self._catalog_files_as_xml():
            xml_root_tag = xml.getroot().tag
            expected = '{http://www.w3.org/2005/Atom}feed'
            assert_equal(expected, xml_root_tag)

    def test_links_include_profile(self):
        """All OPDS Catalog Feed Documents should use a profile media type parameter when linking to another part of the Catalog"""
        for xml in self._catalog_files_as_xml():
            for link in xml.xpath('atom:link[starts-with(@type, "application/atom+xml")]', namespaces=NSS):
                assert ';profile=opds-catalog' in link.get('type')

    def test_start_links_in_all_catalogs(self):
        """All OPDS Catalog Feed Documents should link to the OPDS Catalog Root"""
        for xml in self._catalog_files_as_xml():
            link = xml.xpath('atom:link[@type = "%s"][@rel="start"]' % csv2opds.CATALOG_TYPE, namespaces=NSS)[0]
            actual = link.get('href')
            expected = csv2opds.CATALOGS['root']
            assert_equals(expected, actual)

    def test_root_catalog_title(self):
        """An OPDS Catalog Root should use the specified title"""
        xml = self._root_catalog_as_xml()
        actual_title = xml.xpath('/atom:feed/atom:title/text()', namespaces=NSS)[0]
        assert_equals(self.options.title, actual_title)

    def test_root_catalog_hierarchical(self):
        """An OPDS Catalog Root should be a Navigation Feed"""
        xml = self._root_catalog_as_xml()
        acquisition_links = len(xml.xpath('/atom:feed/atom:entry/atom:link[starts-with(@rel, "http://opds-spec.org/acquisition")]', namespaces=NSS))
        expected = 0
        assert_equals(expected, acquisition_links)


    def test_output_is_valid_atom(self):
        """All OPDS Catalog Feeds Documents should be valid Atom feeds"""
        for xml in self._catalog_files_as_xml():
            try:
                assert self.atom_validator.validate(xml)
            except AssertionError:
                error_log = self.atom_validator.error_log
                log.warn('Validation errors:\n%s' % error_log)
                raise

    def test_output_has_crawlable(self):
        """An OPDS Catalog should include a Complete Acquisition Feed"""
        xml = self._root_catalog_as_xml()
        crawlable_links = len(xml.xpath('atom:link[@rel="http://opds-spec.org/crawlable"]', namespaces=NSS))
        expected = 1
        assert_equal(expected, crawlable_links)

    def test_rich_output_has_popular_relation(self):
        """A complex OPDS Catalog should include a "popular" Acquisition Feed"""
        raise SkipTest
        xml = self._root_catalog_as_xml()
        relations = len(xml.xpath('atom:link[@rel="http://opds-spec.org/popular"]', namespaces=NSS))
        expected = 1
        assert_equal(expected, relations)

    def test_rich_output_has_new_relation(self):
        """A complex OPDS Catalog should include a "new" Acquisition Feed"""
        raise SkipTest
        xml = self._root_catalog_as_xml()
        relations = len(xml.xpath('atom:link[@rel="http://opds-spec.org/new"]', namespaces=NSS))
        expected = 1
        assert_equal(expected, relations)

    def test_rich_output_has_featured_relation(self):
        """A complex OPDS Catalog should include a "featured" Acquisition Feed"""
        raise SkipTest
        xml = self._root_catalog_as_xml()
        relations = len(xml.xpath('atom:link[@rel="http://opds-spec.org/featured"]', namespaces=NSS))
        expected = 1
        assert_equal(expected, relations)

    def test_output_complete(self):
        """A Complete Acquisition Feed should include exactly as many OPDS Catalog Entries as the input"""
        xml = self._root_catalog_as_xml()
        crawlable_link_href = xml.xpath('/atom:feed/atom:link[@rel="http://opds-spec.org/crawlable"]/@href', namespaces=NSS)[0]
        crawlable_fn = os.path.join(self.tempdir, crawlable_link_href)
        crawlable_xml = etree.parse(crawlable_fn)
        entries = len(crawlable_xml.xpath('atom:entry', namespaces=NSS))
        expected = len(self.minimum_data)
        assert_equal(expected, entries)

    def test_links_in_all_feeds(self):
        """All OPDS Catalog Feed Documents should have at least one link"""
        for xml in self._catalog_files_as_xml():
            links = len(xml.xpath('/atom:feed/atom:entry/atom:link', namespaces=NSS))
            expected = 1
            try:
                assert expected <= links
            except AssertionError:
                log.debug(etree.tostring(xml))
                raise

    def test_navigation_links_in_navigation_feeds(self):
        """All Navigation Feeds should not include any Acquisition Links"""
        for xml in self._catalog_files_as_xml():
            if len(xml.xpath('/atom:feed/atom:entry[@type="application/atom+xml;type=feed;profile=opds-catalog"]', namespaces=NSS)) > 0:
                acquisition_links = len(xml.xpath('/atom:feed/atom:entry/atom:link[starts-with(@rel, "http://opds-spec.org/acquisition")]', namespaces=NSS))
                expected = 0
                assert_equals(expected, acquisition_links)

    def test_acqusition_links_in_acqusition_feeds(self):
        """All Acquisition Feeds should include at least one Acquisition Link in each OPDS Catalog Entry"""
        for xml in self._catalog_files_as_xml():
            if len(xml.xpath('/atom:feed/atom:entry/atom:link[@type="application/atom+xml;type=feed;profile=opds-catalog"]', namespaces=NSS)) == 0:
                acquisition_links = len(xml.xpath('/atom:feed/atom:entry/atom:link[starts-with(@rel, "http://opds-spec.org/acquisition")]', namespaces=NSS))
                expected = len(xml.xpath('/atom:feed/atom:entry', namespaces=NSS))
                try:
                    assert expected <= acquisition_links
                except AssertionError:
                    log.debug(etree.tostring(xml))
                    raise

    def _root_catalog_as_xml(self):
        root_catalog_fn = os.path.join(self.tempdir, csv2opds.CATALOGS['root'])
        xml = etree.parse(root_catalog_fn)
        return xml

    def _catalog_files_as_xml(self):
        catalog_files = glob.glob(self.tempdir + '/*.xml')
        catalogs_as_xml = []
        for f in catalog_files:
            xml = etree.parse(f)
            catalogs_as_xml.append(xml)
        return catalogs_as_xml

    def _write_csv(self, csv_fn, data):
        writer = csv.writer(open(csv_fn, "wb")) 
        headers = CSV_TEMPLATE_HEADERS[0:len(data[0])]
        writer.writerow(headers)
        for title_data in data:
            writer.writerow(title_data)
