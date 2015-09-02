#!/usr/bin/env python
# coding: utf-8

from __future__ import division, absolute_import
from __future__ import print_function, unicode_literals

from ..models.user import User
import logging
from datetime import datetime
import md5

def register(name, passwd, email):
    passwd = md5.md5(passwd).hexdigest()
    count = User.objects(name=name).count()
    if count > 0:
        raise Exception("username has been used")
    user = User(name=name, password=passwd, email=email,
                create_at=datetime.now())
    logging.info("%r %r %r %r registered",
                 user, user.name, user.email, user.create_at)
    user.save()


def login(name, passwd):
    passwd = md5.md5(passwd).hexdigest()
    count = User.objects(name=name, password=passwd).count()
    return count == 1
