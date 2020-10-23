#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 Prashant Anantharaman <prashant.anantharaman@sri.com> %>
#
"""

"""
import unittest
from key_management_server import *

class LearningCase(unittest.TestCase):
    maxDiff = None
    def testGenerator(self):
        self.assertEqual(generate_macaroons("device1", "sony").serialize(), u'MDAxN2xvY2F0aW9uIGxvY2FsaG9zdAowMDE0aWRlbnRpZmllciBzb255CjAwMTBjaWQgZGV2aWNlMQowMDIyY2lkIFZhbGlkIHRpbGw6IDE1OTk1MzQ2NzEuNTgKMDAyZnNpZ25hdHVyZSDyNquZPHmj5m_F6CATUUpJ_Epr3y4tQMGpwnpDOIMfYAo')

def main():
    unittest.main()

if __name__ == "__main__":
    main()
