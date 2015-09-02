#!/usr/bin/env python
# coding: utf-8

from __future__ import division, absolute_import
from __future__ import print_function, unicode_literals

from .base import BaseFrame
from chaofeng.g import mark
from chaofeng.ui import Password
from chaofeng.ui import EastAsiaTextInput
import chaofeng.ascii as ac
from .. import resource as res
from ..controllers import user


@mark('register')
class Register(BaseFrame):
    def initialize(self):
        self.set_title(res.register_welcome_message)
        self.write(''.join([ac.move2(22, 1)]))
        while True:
            username_inputer = self.load(EastAsiaTextInput)
            name = username_inputer.readln(prompt=res.please_enter_username)
            if not name:
                continue
            pass_inputer = self.load(Password)
            password = pass_inputer.readln(prompt=res.please_enter_password)
            if not password:
                continue

            email_inputer = self.load(EastAsiaTextInput)
            email = email_inputer.readln(prompt=res.please_enter_email)

            if not email:
                continue
            user.register(name, password, email)
            self.goto('welcome')
