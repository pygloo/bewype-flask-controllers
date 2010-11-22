#!/usr/bin/env python
# -*- coding: utf-8 -*-

__import__('pkg_resources').declare_namespace(__name__)

# bewype import
from bewype import config
from bewype.flask import app

import bewype.flask.controllers.info
import bewype.flask.controllers.upload

def run():
    # prepare run values
    _debug = config.Config().get_bool('main>debug')
    # do run
    app.run(debug=_debug)

