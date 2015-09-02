#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: tao
# @Date:   2015-09-02 13:45:59
# @Last Modified by:   tao
# @Last Modified time: 2015-09-02 16:14:41

from __future__ import print_function, unicode_literals, absolute_import

from .base import BaseFrame
from chaofeng.g import mark
from chaofeng.ui import EastAsiaTextInput
from chaofeng.ui import Password
import chaofeng.ascii as ac
from .. import resource as res
from ..controllers import user
from . import register


@mark('welcome')
class Welcome(BaseFrame):

    def initialize(self):
        # self.write('Welcome to Guest BBS')
        # self.write(''.join([ac.clear, ac.move2(22, 1)]))
        self.session.charset = 'utf8'
        self.set_title(res.welcome_title)
        self.write(''.join([ac.move2(22, 1)]))

        while True:
            username_inputer = self.load(EastAsiaTextInput)
            username = username_inputer.readln(prompt=res.please_enter_username)
            if not username:
                continue
            elif username == res.register_user_name:
                self.goto('register')
            password_inputer = self.load(Password)
            password = password_inputer.readln(prompt=res.please_enter_password)
            if user.login(username, password):
                self.goto('main_menu')
            else:
                continue
            # if username in USER_POOL:
            #     if USER_POOL[username] != password:
            #         self.wrong(u'用户名与密码不匹配！')
            #         continue
            #     self.success(res.login_success)
            # else:
            #     if len(USER_POOL) >= MAX_REGISTER:
            #         self.wrong(u'对不起，已达最大注册人数！')
            #         self.close()
            #     self.success(u'注册新用户！')
            #     USER_POOL[username] = password
            #     MSG_BOX[username] = u'欢迎使用！您还没有留言！'
            # break
        self.session['username'] = username
        self.pause()
        # self.goto('main_menu')
