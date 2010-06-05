#!/usr/bin/env python
# encoding: utf-8
"""
test_spec_musts.py

Created by Keith Fahlgren on Fri Jun  4 23:02:01 PDT 2010
"""

import logging
import os.path

from nose.tools import *
from nose.plugins.skip import SkipTest

import pragle.opdscatalogvalidator


log = logging.getLogger(__name__)

class TestSpecShoulds(object):

    def test_must_be__namespace_well_formed__(self):
        """[SPEC] OPDS Catalog Feed Documents and OPDS Catalog Entry Documents MUST be "namespace-well-formed" """
        raise SkipTest

    def test_must_either_be_an_acquisition_feed_or_a_navigation_feed(self):
        """[SPEC] Every OPDS Catalog Feed Document MUST either be an Acquisition Feed or a Navigation Feed"""
        raise SkipTest

    def test_must_have_one_and_only_one_opds_catalog_root(self):
        """[SPEC] Every OPDS Catalog MUST have one and only one OPDS Catalog Root"""
        raise SkipTest

    def test_must_use_the_search_relation_value(self):
        """[SPEC] Links to OpenSearch Description documents MUST use the search relation value"""
        raise SkipTest

    def test_must_use_____the_application_opensearchdescription_xml_media_type(self):
        """[SPEC] Links to OpenSearch Description documents MUST use ... the application/opensearchdescription+xml media type"""
        raise SkipTest

    def test_must_include_at_least_one_acquisition_link(self):
        """[SPEC] Each OPDS Catalog Entry Document MUST include at least one Acquisition Link"""
        raise SkipTest

    def test_must_include_an_alternate_link_relation_referencing_the_complete_catalog_entry_resource(self):
        """[SPEC] A Partial Catalog Entry MUST include an alternate link relation referencing the Complete Catalog Entry Resource"""
        raise SkipTest

    def test_must_use_the_type_attribute_application_atom_xml_type_entry_profile_opds_catalog(self):
        """[SPEC] A Partial Catalog Entry MUST include an alternate link relation ... and that atom:link MUST use the type attribute application/atom+xml;type=entry;profile=opds-catalog"""
        raise SkipTest

    def test_must_include_all_metadata_elements(self):
        """[SPEC] Any Catalog Entry without a link to a Complete Catalog Entry MUST include all metadata elements"""
        raise SkipTest

    def test_must_be_identified_by_an_atom_id(self):
        """[SPEC] OPDS Catalog Entries MUST be identified by an atom:id"""
        raise SkipTest

    def test_must_include_an_atom_updated_element(self):
        """[SPEC] OPDS Catalog Entries MUST include an atom:updated element"""
        raise SkipTest

    def test_must_inlcude_an_atom_title(self):
        """[SPEC] OPDS Catalog Entries MUST inlcude an atom:title"""
        raise SkipTest

    def test_must_be_created_in_a_way_that_assures_uniqueness(self):
        """[SPEC] An atom:id identifying an OPDS Catalog Entry ... MUST be created in a way that assures uniqueness"""
        raise SkipTest

    def test_must_be_text(self):
        """[SPEC] The content of an atom:summary element MUST be text"""
        raise SkipTest

    def test_must_use_one_of_the_following_relations_for_these_images__http___opds_spec_org_cover__http___opds_spec_org_thumbnail(self):
        """[SPEC] OPDS Catalog Entries [with] atom:links to images ... [and] [t]hese atom:links MUST use one of the following relations for these images: http://opds-spec.org/cover, http://opds-spec.org/thumbnail"""
        raise SkipTest

    def test_must_include_a_type_attribute_of_image_gif__image_jpeg__or_image_png(self):
        """[SPEC] OPDS Catalog Entries [with] atom:links to images ... MUST include a type attribute of image/gif, image/jpeg, or image/png"""
        raise SkipTest

    def test_must_be_in_gif__jpeg__or_png_format__if_linked_from_an_opds_catalog_entry_using_one_of_the_following_relations_for_these_images__http___opds_spec_org_cover__http___opds_spec_org_thumbnail_(self):
        """[SPEC] [I]mage Resources MUST be in GIF, JPEG, or PNG format [if linked from an OPDS Catalog Entry using one of the following relations for these images: http://opds-spec.org/cover, http://opds-spec.org/thumbnail]"""
        raise SkipTest

    def test_must_contain_one_opds_price_element(self):
        """[SPEC] atom:link elements with a rel attribute value of http://opds-spec.org/acquisition/buy MUST contain one opds:price element"""
        raise SkipTest

    def test_must_be_an_alphabetic_code_from_iso4217(self):
        """[SPEC] On the opds:price element, the value of the currencycode attribute MUST be an Alphabetic code from ISO4217"""
        raise SkipTest

    def test_must_include_a_type_attribute(self):
        """[SPEC] All Acquisition Links MUST include a type attribute"""
        raise SkipTest

    def test_must_conform_to_the_syntax_of_a_mime_media_type(self):
        """[SPEC] All Acquisition Links MUST include a type attribute [and] ... the value of the type attribute MUST conform to the syntax of a MIME media type"""
        raise SkipTest

    def test_must_represent_the_media_type_of_the_publication_resource_itself(self):
        """[SPEC] If the Publication is available using Direct Acquisition, the type attribute of the Acquisition Link MUST represent the media type of the Publication Resource itself"""
        raise SkipTest

    def test_must_contain_the_same_content_value_as_the_type_parameter_of_its_parent(self):
        """[SPEC] For Acquisition Links using Direct Acquisition, the dc:format element MUST contain the same content value as the type parameter of its parent"""
        raise SkipTest

    def test_must_contain_one_or_more_dc_format_elements(self):
        """[SPEC] [Acquisition Links using Indirect Acquisition] MUST contain one or more dc:format elements"""
        raise SkipTest

    def test_must_be_ordered_by_atom_updated__with_the_most_recently_updated_atom_entries_coming_first_in_the_document_order(self):
        """[SPEC] [In] a Complete Acquisition Feed ... each OPDS Catalog Entry MUST be ordered by atom:updated, with the most recently updated Atom Entries coming first in the document order"""
        raise SkipTest

    def test_must_include_a_fh_complete_element(self):
        """[SPEC] A Complete Acquisition Feed MUST include a fh:complete element"""
        raise SkipTest

    def test_must_include_complete_catalog_entries_when_serializing_a_complete_acquisition_feed(self):
        """[SPEC] OPDS Catalog providers MUST include Complete Catalog Entries when serializing a Complete Acquisition Feed"""
        raise SkipTest

