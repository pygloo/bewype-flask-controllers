#!/usr/bin/env python
# -*- coding: utf-8 -*-

# bewype import
from bewype import config
from bewype.flask import app

if __name__ == '__main__':
    # get debug flag
    _debug = config.Config().get_bool("main>debug")
    # run
    app.run(debug=_debug)

