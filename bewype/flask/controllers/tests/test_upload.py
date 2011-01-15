#!/usr/bin/env python
# -*- coding: utf-8 -*-

# python import
import json, os, unittest
from StringIO import StringIO

# werkzeug import
from werkzeug import EnvironBuilder, Request, run_wsgi_app

# bewype import
from bewype.config import c
from bewype.flask.controllers import upload


class UploadTestCase(unittest.TestCase):

    def setUp(self):
        # upload file path
        self.upload_file_path = None

    def tearDown(self):
        # remove uploaded path
        if self.upload_file_path is not None\
        and os.path.exists(self.upload_file_path):
            os.remove(self.upload_file_path)

    def test_upload(self):
        # prepare form data
        _data = {'file': (StringIO('This is a test'), 'dummy.txt')}
        # build environ
        _builder = EnvironBuilder('/upload', method='POST', data=_data)
        _environ = _builder.get_environ()
        # call
        _app_iter, _status, _headers = run_wsgi_app(upload.app, _environ)
        # parse response
        for _i in _app_iter:
            # load data
            _data = json.loads(_i)
            # get filename
            _content_type = _data['contentType']
            _file_name = _data['fileName']
        # set upload path main var for removal
        self.upload_file_path = os.path.join(c.path.uploads, _file_name)
        # check content type
        assert _content_type == 'text/plain',\
                'Found: %s' % _content_type
        # check was uploaded
        assert os.path.exists(self.upload_file_path),\
                'Found: %s' % self.upload_file_path
        # open file
        _f = open(self.upload_file_path)
        # check content
        assert _f.read() == 'This is a test'
        _f.close()


if __name__ == '__main__':
    unittest.main()
