#!/usr/bin/env python
# -*- coding: utf-8 -*-

# python import
import unittest

# bewype import
from bewype.flask.controllers import info

class InfoTestCase(unittest.TestCase):

    def setUp(self):
        self.app = info.app.test_client()

    def tearDown(self):
        pass

    def test_upload(self):
        _response = self.app.get('/info')
        assert 'It\'s Working!' == _response.data

if __name__ == '__main__':
    unittest.main()

