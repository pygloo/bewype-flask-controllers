# (C) Copyright 2010 Bewype <http://www.bewype.org>

# python import
import json, os

# flask import
from flask import request

# bewype import
from bewype import tools
from bewype.config import c
from bewype.flask import app

def _get_file_info( file_ ):
    # check file content type
    _content_type = file_.content_type
    # is it s an image we get some info.
    if '/' in _content_type\
    and _content_type.split('/')[0] == 'image':
        #  prepare data
        file_.stream.seek(0)
        _data = file_.stream.read()
        # get file (img) info
        _type, _width, _height = tools.get_image_info(_data)
        # return info
        return  {
                'contentType': _content_type,
                'imgHeight': _height,
                'imgWidth' : _width
                }
    # nothing for standard files yet
    else:
        return {
                'contentType': _content_type
                }

@app.route('/upload', methods=['POST'])
def upload():
    # get file object from request
    _file = request.files['file']
    # get unique file name
    _file_name = tools.random_str(24)
    # do save
    _file.save(os.path.join(c.path.uploads, _file_name))
    # get some info about this file
    _file_info = _get_file_info(_file)
    _file_info['fileName'] = _file_name
    # return generated file name
    return json.dumps(_file_info)

