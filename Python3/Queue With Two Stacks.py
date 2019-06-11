# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       test
   Description:
   Author:           God
   date：            2018/9/27
-------------------------------------------------
   Change Activity:  2018/9/27
-------------------------------------------------
"""
__author__ = 'God'


# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        self.stack1.append(node)

    def pop(self):
        if len(self.stack2) == 0:
            if len(self.stack1) == 0:
                return None
            elif len(self.stack1) == 1:
                return self.stack1.pop()
            else:
                while len(self.stack1):
                    self.stack2.append(self.stack1.pop())
                return self.stack2.pop()
        else:
            return self.stack2.pop()

