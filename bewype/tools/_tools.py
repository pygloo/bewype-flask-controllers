#!/usr/bin/env python
# -*- coding: utf-8 -*-

# python import
import random, string

def random_str(length):
    return ''.join(random.choice(string.letters) for i in xrange(length))

