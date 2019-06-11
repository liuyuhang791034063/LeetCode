# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       The first non-repeating character in the character stream
   Description:
   Author:           God
   date：            2018/11/2
-------------------------------------------------
   Change Activity:  2018/11/2
-------------------------------------------------
"""
__author__ = 'God'


class Solution:
    # 返回对应char
    def __init__(self):
        self.s = ''

    def FirstAppearingOnce(self):
        res = list(filter(lambda c: self.s.count(c) == 1, self.s))
        return res[0] if res else '#'

    def Insert(self, char):
        self.s += char