#!/usr/bin/env python
# encoding: utf-8
"""
test_spec_should_nots.py

Created by Keith Fahlgren on Fri Jun  4 23:02:15 PDT 2010
"""

import logging
import os.path

from nose.tools import *
from nose.plugins.skip import SkipTest

import pragle.opdscatalogvalidator


log = logging.getLogger(__name__)

class TestSpecShouldNots(object):

    def test_should_not_use_dc_creator_to_represent_the_publication_s_creators_(self):
        """[SPEC] OPDS Catalog Entries ... SHOULD NOT use dc:creator [to represent the Publication's creators]"""
        raise SkipTest

    def test_should_not_use_dc_subject_to_represent_the_publication_s_category_keywords_key_phrases_or_classification_codes_(self):
        """[SPEC] OPDS Catalog Entries ... SHOULD NOT use dc:subject [to represent the Publication's category, keywords, key phrases, or classification codes]"""
        raise SkipTest

    def test_should_not_use_dc_rights_to_represent_rights_held_in_and_over_the_publication_(self):
        """[SPEC] OPDS Catalog Entries ... SHOULD NOT use dc:rights [to represent rights held in and over the Publication]"""
        raise SkipTest

    def test_should_not_use_dc_description_or_dc_abstract_to_describe_the_publication_(self):
        """[SPEC] OPDS Catalog Entries ... SHOULD NOT use dc:description or dc:abstract [to describe the Publication]"""
        raise SkipTest

    def test_should_not_duplicate_the_content_of_atom_title_or_atom_content(self):
        """[SPEC] [A]n atom:summary element ... SHOULD NOT duplicate the content of atom:title or atom:content"""
        raise SkipTest

    def test_should_not_be_included_in_the_partial_catalog_entry(self):
        """[SPEC] If an OPDS Catalog Entry includes both atom:content and atom:summary, the atom:content SHOULD NOT be included in the Partial Catalog Entry"""
        raise SkipTest

    def test_should_not_be_provided_for_a_single_opds_catalog_entry(self):
        """[SPEC] More than one atom:link with either [http://opds-spec.org/cover or http://opds-spec.org/thumbnail] relation SHOULD NOT be provided for a single OPDS Catalog Entry"""
        raise SkipTest

