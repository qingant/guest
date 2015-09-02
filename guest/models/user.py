#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: tao
# @Date:   2015-09-02 16:21:55
# @Last Modified by:   tao
# @Last Modified time: 2015-09-02 16:31:21

from __future__ import print_function, unicode_literals, absolute_import
from mongoengine import Document
from mongoengine import StringField
import mongoengine


class User(Document):
    name = StringField(required=True, max_length=50)
    email = StringField(required=True, max_length=100)
    password = StringField(required=True, max_length=20)
    nick = StringField(max_length=50)
    description = StringField()
    signature = StringField(max_length=1024)
    create_at = mongoengine.DateTimeField(required=True)
    last_login_at = mongoengine.DateTimeField()
