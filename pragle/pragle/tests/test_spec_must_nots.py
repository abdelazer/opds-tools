#!/usr/bin/env python
# encoding: utf-8
"""
test_spec_must_nots.py

Created by Keith Fahlgren on Fri Jun  4 23:01:53 PDT 2010
"""

import logging
import os.path

from nose.tools import *
from nose.plugins.skip import SkipTest

import pragle.opdscatalogvalidator


log = logging.getLogger(__name__)

class TestSpecShoulds(object):

    def test_must_not_contain_opds_catalog_entries(self):
        """[SPEC] A Navigation Feed MUST NOT contain OPDS Catalog Entries"""
        raise SkipTest

    def test_must_not_identify_the_opds_catalog_entry(self):
        """[SPEC] dc:identifier elements ... MUST NOT identify the OPDS Catalog Entry"""
        raise SkipTest

    def test_must_not_represent_any_date_related_to_the_opds_catalog_entry(self):
        """[SPEC] A dc:issued element ... MUST NOT represent any date related to the OPDS Catalog Entry"""
        raise SkipTest

    def test_must_not_use_dc_title(self):
        """[SPEC] OPDS Catalog Entries ... MUST NOT use dc:title"""
        raise SkipTest

    def test_must_not_change_when_the_opds_catalog_entry_is__relocated__migrated__syndicated__republished__exported__or_imported(self):
        """[SPEC] An atom:id identifying an OPDS Catalog Entry MUST NOT change when the OPDS Catalog Entry is "relocated, migrated, syndicated, republished, exported, or imported"""
        raise SkipTest

