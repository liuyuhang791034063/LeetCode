# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       The Stack has min function
   Description:
   Author:           God
   date：            2018/10/11
-------------------------------------------------
   Change Activity:  2018/10/11
-------------------------------------------------
"""
__author__ = 'God'
from sys import maxsize
# -*- coding:utf-8 -*-


class Solution:
    def __init__(self):
        self.stack = []
        self.minNode = maxsize

    def push(self, node):
        if node < self.minNode:
            self.minNode = node
        self.stack.append(node)

    def pop(self):
        res = self.stack.pop()
        self.minNode = min(self.stack)
        return res

    def top(self):
        return self.stack[-1]

    def min(self):
        return self.minNode
