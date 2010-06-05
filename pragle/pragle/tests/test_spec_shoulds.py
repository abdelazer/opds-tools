#!/usr/bin/env python
# encoding: utf-8
"""
test_spec_shoulds.py

Created by Keith Fahlgren on Fri Jun  4 23:01:14 PDT 2010
"""


import logging
import os.path

from nose.tools import *
from nose.plugins.skip import SkipTest

import pragle.opdscatalogvalidator


log = logging.getLogger(__name__)

class TestSpecShoulds(object):

    def test_should_produce_opds_catalog_feed_documents_and_opds_catalog_entry_documents_that_are_conformant_to_both_atom_and_the_opds_catalog_relax_ng_schemas(self):
        """[SPEC] Producers of OPDS Catalogs SHOULD produce OPDS Catalog Feed Documents and OPDS Catalog Entry Documents that are conformant to both Atom and the OPDS Catalog RELAX NG schemas"""
        raise SkipTest

    def test_should_contain_an_atom_link_element_with_a_link_relation_of_start_which_references_the_opds_catalog_root_resource(self):
        """[SPEC] Each OPDS Catalog Feed Document SHOULD contain an atom:link element with a link relation of start, which references the OPDS Catalog Root Resource"""
        raise SkipTest

    def test_should_include_a_brief_description_of_the_linked_resource(self):
        """[SPEC] [In a Navigation Feed] [e]ach Atom Entry's atom:content SHOULD include a brief description of the linked Resource"""
        raise SkipTest

    def test_should_use_the_type_attribute_application_atom_xml_type_feed_profile_opds_catalog_navigation(self):
        """[SPEC] Links to Navigation Feeds SHOULD use the type attribute application/atom+xml;type=feed;profile=opds-catalog"""
        raise SkipTest

    def test_should_be_used_if_no_other_relation_to_a_navigation_feed_is_more_appropriate(self):
        """[SPEC] The relation subsection SHOULD be used if no other relation [to a Navigation Feed] is more appropriate"""
        raise SkipTest

    def test_should_use_the_type_attribute_application_atom_xml_type_feed_profile_opds_catalog_acquisition(self):
        """[SPEC] Links to Acquisition Feeds SHOULD use the type attribute application/atom+xml;type=feed;profile=opds-catalog"""
        raise SkipTest

    def test_should_include_links_to_other_available_acquisition_and_navigation_feeds_and_other_related_resources(self):
        """[SPEC] OPDS Catalog Feed Documents SHOULD include links to other available Acquisition and Navigation Feeds and other related Resources"""
        raise SkipTest

    def test_should_use_the_media_type_associated_to_opds_catalogs_application_atom_xml_type_feed_profile_opds_catalog(self):
        """[SPEC] In an OpenSearch description document, the search interface SHOULD use the media type associated to OPDS Catalogs: application/atom+xml;type=feed;profile=opds-catalog"""
        raise SkipTest

    def test_should_contain_one_atom_link_element_with_a_rel_attribute_value_of_self(self):
        """[SPEC] OPDS Catalog Feed Documents SHOULD contain one atom:link element with a rel attribute value of self"""
        raise SkipTest

    def test_should_include_the_following_metadata_elements_if_available_atom_category_atom_rights_dc_extent_dc_identifier_dc_issued_dc_language_dc_publisher_and_opds_price(self):
        """[SPEC] Partial Catalog Entries SHOULD include the following metadata elements, if available: atom:category, atom:rights, dc:extent, dc:identifier, dc:issued, dc:language, dc:publisher, and opds:price"""
        raise SkipTest

    def test_should_be_used_to_identify_the_represented_publication_if_appropriate_metadata_is_available(self):
        """[SPEC] [In an OPDS Catalog Entry] [o]ne or more dc:identifier elements SHOULD be used to identify the represented Publication, if appropriate metadata is available"""
        raise SkipTest

    def test_should_be_used_to_indicate_the_first_publication_date_of_the_publication(self):
        """[SPEC] [In an OPDS Catalog Entry] [a] dc:issued element SHOULD be used to indicate the first publication date of the Publication"""
        raise SkipTest

    def test_should_use_atom_author_to_represent_the_publication_s_creators_(self):
        """[SPEC] OPDS Catalog Entries SHOULD use atom:author to represent the Publication's creators """
        raise SkipTest

    def test_should_use_atom_category_to_represent_the_publication_s_category_keywords_key_phrases_or_classification_codes_(self):
        """[SPEC] OPDS Catalog Entries SHOULD use atom:category to represent the Publication's category, keywords, key phrases, or classification codes """
        raise SkipTest

    def test_should_use_atom_rights_to_represent_rights_held_in_and_over_the_publication_(self):
        """[SPEC] OPDS Catalog Entries SHOULD use atom:rights to represent rights held in and over the Publication """
        raise SkipTest

    def test_should_use_atom_summary_and_or_atom_content_to_describe_the_publication_(self):
        """[SPEC] OPDS Catalog Entries SHOULD use atom:summary and/or atom:content to describe the Publication """
        raise SkipTest

    def test_should_include_either_atom_summary_or_atom_content_elements_or_both_to_provide_a_description_summary_abstract_or_excerpt_of_the_publication(self):
        """[SPEC] OPDS Catalog Entries SHOULD include either atom:summary or atom:content elements or both to provide a description, summary, abstract, or excerpt of the Publication"""
        raise SkipTest

    def test_should_be_included_in_the_complete_catalog_entry(self):
        """[SPEC] If an OPDS Catalog Entry includes both atom:content and atom:summary ... [b]oth elements SHOULD be included in the Complete Catalog Entry"""
        raise SkipTest

    def test_should_include_links_to_related_entry_documents(self):
        """[SPEC] OPDS Catalog Entry Documents SHOULD include links to related Entry Documents"""
        raise SkipTest

    def test_should_be_120_pixels(self):
        """[SPEC] The maximum size of the longest dimension of http://opds-spec.org/thumbnail images SHOULD be 120 pixels"""
        raise SkipTest

    def test_should_represent_the_media_type_of_the_first_resource_a_client_must_dereference_to_begin_the_acquisition(self):
        """[SPEC] If the Publication is available using Indirect Acquisition, the type attribute of the Acquisition Link SHOULD represent the media type of the first Resource a client must dereference to begin the acquisition"""
        raise SkipTest

    def test_should_use_a_different_value_for_the_type_attribute_or_dc_format_child_of_the_acquisition_link_than_the_same_format_without_digital_rights_management(self):
        """[SPEC] Publications in a format using Digital Rights Management SHOULD use a different value for the type attribute or dc:format child of the Acquisition Link than the same format without Digital Rights Management"""
        raise SkipTest

    def test_should_use_partial_catalog_entries_in_all_acquisition_feeds_except_complete_acquisition_feeds(self):
        """[SPEC] OPDS Catalog providers SHOULD use Partial Catalog Entries in all Acquisition Feeds except Complete Acquisition Feeds"""
        raise SkipTest

    def test_should_contain_an_atom_link_element_with_a_the_relation_of_http_opds_spec_org_crawlable_that_references_the_complete_acquisition_feed_resource(self):
        """[SPEC] If available, each OPDS Catalog Feed Document in the OPDS Catalog SHOULD contain an atom:link element with a the relation of http://opds-spec.org/crawlable that references the Complete Acquisition Feed Resource"""
        raise SkipTest

    def test_should_use_a_compressed_content_encoding_when_transmitting_complete_acquisition_feeds_over_http(self):
        """[SPEC] OPDS Catalog providers SHOULD use a compressed Content-Encoding when transmitting Complete Acquisition Feeds over HTTP"""
        raise SkipTest

    def test_should_use_the_type_parameter(self):
        """[SPEC] Publishers of OPDS Catalogs SHOULD use the type parameter"""
        raise SkipTest

    def test_should_use_a_profile_parameter(self):
        """[SPEC] Relations to OPDS Catalog Feed Document and OPDS Catalog Entry Document Resources SHOULD use a profile parameter"""
        raise SkipTest

    def test_should_be_application_atom_xml_type_entry_profile_opds_catalog(self):
        """[SPEC] The complete media type for a relation to an OPDS Catalog Entry Document Resource SHOULD be: application/atom+xml;type=entry;profile=opds-catalog"""
        raise SkipTest

    def test_should_be_application_atom_xml_type_feed_profile_opds_catalog(self):
        """[SPEC] The complete media type for a relation to an OPDS Catalog Feed Document Resource SHOULD be: application/atom+xml;type=feed;profile=opds-catalog"""
        raise SkipTest

