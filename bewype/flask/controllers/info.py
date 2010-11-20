#!/usr/bin/env python
# -*- coding: utf-8 -*-

# bewype import
from bewype.flask import app

@app.route('/info')
def info():
    return "It's Working!"

