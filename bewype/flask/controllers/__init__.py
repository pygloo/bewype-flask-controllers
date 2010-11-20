#!/usr/bin/env python
# -*- coding: utf-8 -*-

__import__('pkg_resources').declare_namespace(__name__)

# bewype import
from bewype.flask import app

import bewype.flask.controllers.info
import bewype.flask.controllers.upload

