#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: tao
# @Date:   2015-09-02 12:42:48
# @Last Modified by:   tao
# @Last Modified time: 2015-09-02 16:32:48

from __future__ import print_function, unicode_literals, absolute_import

from .views.welcome import Welcome
from chaofeng import Server
from mongoengine import connect
import logging
logging.basicConfig(level=logging.DEBUG)


def main():
    connect(db="guest",
            host='mongodb://localhost/')
    s = Server(Welcome)
    s.run()
