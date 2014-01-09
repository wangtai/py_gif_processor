#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Last modified: Wang Tai (i@wangtai.me)

"""
"""

__revision__ = '0.1'

from unittest import TestCase

class simpleTest(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testExample(self):
        from gif_thumb import create_thumb
        import os
        for root, dirs, files in os.walk('test'):
            for file_name in files:
                path = os.path.join(root, file_name)
                thumbnail_path = os.path.join(root, file_name + '.jpg')
                create_thumb(path, thumbnail_path)
        self.assertEqual(1, 1)

    def testOther(self):
        self.assertNotEqual(0, 1)

if '__main__' == __name__:
    import unittest
    unittest.main()

