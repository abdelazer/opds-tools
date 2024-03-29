#!/usr/bin/env python
# encoding: utf-8
"""
test_opdscatalogvalidator.py

Created by Keith Fahlgren on Fri Jun  4 22:36:46 PDT 2010
"""

import glob
import logging
import os.path

from lxml import etree

from nose.tools import *

import pragle.opdscatalogvalidator


log = logging.getLogger(__name__)

class TestOPDSCatalogValidator(object):
    def setup(self):
        self.testfiles_dir = os.path.join(os.path.dirname(__file__), 'files')
        self.opds_validator = pragle.opdscatalogvalidator.OPDSCatalogValidator()

    def test_valid_fn(self):
        """OPDS Catalog Documents should be able to be validated by filename"""
        xml_fn = os.path.join(self.testfiles_dir, 'catalog.root.canonical.xml')
        valid = self.opds_validator.is_valid(xml_fn)
        assert valid

    def test_valid_xml(self):
        """OPDS Catalog Documents should be able to be validated from parsed XML input"""
        xml_fn = os.path.join(self.testfiles_dir, 'catalog.root.canonical.xml')
        xml = etree.parse(xml_fn)
        valid = self.opds_validator.is_valid(xml)
        assert valid


    def test_valid_canonical(self):
        """All OPDS Catalog Documents collected for canonical examples in other tests should pass validation"""
        canonical_fn_glob = os.path.join(self.testfiles_dir, '*canonical*.xml')
        for xml_fn in glob.glob(canonical_fn_glob):
            log.debug('Attempting validation of %s' % xml_fn)
            valid = self.opds_validator.is_valid(xml_fn)
            if not(valid):
                error_log = self.opds_validator.error_log
                log.debug('Validation errors:\n%s' % error_log)
                raise AssertionError

    def test_valid_smoke(self):
        """All valid OPDS Catalog Documents collected for smoketesting should pass validation"""
        smoke_dir = os.path.join(self.testfiles_dir, 'smoke')
        smoke_fn_glob = os.path.join(smoke_dir, '*.valid*.xml')
        for xml_fn in glob.glob(smoke_fn_glob):
            log.debug('Attempting validation of %s' % xml_fn)
            valid = self.opds_validator.is_valid(xml_fn)
            if not(valid):
                error_log = self.opds_validator.error_log
                log.debug('Validation errors:\n%s' % error_log)
                raise AssertionError

    def test_invalid_smoke(self):
        """All invalid OPDS Catalog Documents collected for smoketesting should not pass validation"""
        smoke_dir = os.path.join(self.testfiles_dir, 'smoke')
        smoke_fn_glob = os.path.join(smoke_dir, '*.invalid*.xml')
        for xml_fn in glob.glob(smoke_fn_glob):
            log.debug('Attempting validation of %s' % xml_fn)
            valid = self.opds_validator.is_valid(xml_fn)
            assert not(valid)

