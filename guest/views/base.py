#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: tao
# @Date:   2015-09-02 13:49:04
# @Last Modified by:   tao
# @Last Modified time: 2015-09-02 13:51:29

from __future__ import print_function, unicode_literals, absolute_import
from chaofeng import Frame
import chaofeng.ascii as ac
from chaofeng.ui import SimpleTextBox

class BaseFrame(Frame):

    pause_prompt = '%s%s%s%s' % (ac.move2(24, 20),
                                 ac.outlook(ac.art_code['yellow'],
                                            ac.art_code['blink']),
                                 '任意键继续', ac.reset)

    def set_title(self, msg):
        self.write(''.join([ac.clear, ac.move2(1, 1), msg]))

    def wrong(self, msg):
        self.writeln(u'%s%s%s' % (ac.red, msg, ac.reset))

    def warnning(self, msg):
        self.writeln(u'%s%s%s' % (ac.yellow, msg, ac.reset))

    def success(self, msg):
        self.writeln(u'%s%s%s' % (ac.green, msg, ac.reset))

    def pause(self):
        super(BaseFrame, self).pause(prompt=self.pause_prompt)
