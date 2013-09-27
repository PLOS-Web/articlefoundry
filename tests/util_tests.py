import os

from lxml import etree

import logging
import articlefoundry.logging_config  # noqa
logger = logging.getLogger(__name__)

import unittest
from articlefoundry.util import *

class TestSIFuncs(unittest.TestCase):
    
    def setUp(self):
        self.meta_filename = os.path.join(os.path.split(__file__)[0],
                                      'pone_PONE-D-13-27833.xml')
        self.meta_file = file(self.meta_filename)
        parser = etree.XMLParser(recover=True)
        self.meta_etree = etree.parse(self.meta_file, parser)
        
    def test_get_si_links(self):
        logger.debug("SI links: %s" % get_si_links_from_meta(self.meta_etree))

    def test_get_fig_links(self):
        logger.debug("FIG links: %s" % get_fig_links_from_meta(self.meta_etree))
