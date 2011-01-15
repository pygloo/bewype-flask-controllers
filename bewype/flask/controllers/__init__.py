#!/usr/bin/env python

__import__('pkg_resources').declare_namespace(__name__)

# bewype import
from bewype.config import _obj as c
#
from bewype.flask import app
#
import bewype.flask.controllers.info
import bewype.flask.controllers.upload

def run():
    # load config
    c.init_config_obj()
    # prepare run values
    _debug = c.core.debug.as_bool()
    # do run
    app.run(debug=_debug)

