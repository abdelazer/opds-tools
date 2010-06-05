#!/usr/bin/env python
# encoding: utf-8
"""
opdscatalogvalidator.py

Created by Keith Fahlgren on Fri Jun  4 22:36:22 PDT 2010
"""


import logging

import pkg_resources import resource_string
from lxml import etree

log = logging.getLogger(__name__)

class OPDSCatalogValidator(object):
    def __init__(self):
        foo_config = resource_stream(__name__, 'foo.conf')
        self.validator = etree.RelaxNG(etree.parse(OPDS_CATALOG_RNG))
        self.error_log = []

    def is_valid(self):
        """Validate the OPDS Catalog at the supplied filename against the OPDS Catalog schemas"""
        valid = self.validator.validate(icml)
        if valid:
            return True
        else:
            self.error_log = self.validator.error_log
            return False
