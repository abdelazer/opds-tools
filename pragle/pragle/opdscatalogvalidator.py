#!/usr/bin/env python
# encoding: utf-8
"""
opdscatalogvalidator.py

Created by Keith Fahlgren on Fri Jun  4 22:36:22 PDT 2010
"""

import logging
import os.path

from lxml import etree

log = logging.getLogger(__name__)

class OPDSCatalogValidator(object):
    def __init__(self):
        schemas_dir = os.path.join(os.path.dirname(__file__), 'schemas')
        opds_catalog_rng = os.path.join(schemas_dir, 'opds_catalog_feed.rng')
        self.validator = etree.RelaxNG(etree.parse(opds_catalog_rng))
        self.error_log = []

    def is_valid(self, xml_or_xml_fn):
        """Validate the OPDS Catalog at the supplied filename against the OPDS Catalog schemas"""
        try:
            xml = xml_or_xml_fn if 'xpath' in dir(xml_or_xml_fn) else etree.parse(xml_or_xml_fn)
            valid = self.validator.validate(xml)
            if valid:
                return True
            else:
                self.error_log = self.validator.error_log
                return False
        except Exception, e:
            log.warn(e)
            self.error_log.append(e)
            return False
