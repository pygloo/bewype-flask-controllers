#!/usr/bin/env python
# -*- coding: utf-8 -*-

# python import
import os

# flask import
from flask import request

# bewype import
from bewype import config, tools
from bewype.flask import app

@app.route('/upload', methods=['POST'])
def upload():
    # get file object from request
    _file = request.files['file']
    # get unique file name
    _filename = tools.random_str(24)
    # get uploads path
    _uploads_path = config.Config().get('path>uploads')
    # do save
    _file.save(os.path.join(_uploads_path, _filename))
    # return generated file name
    return _filename

