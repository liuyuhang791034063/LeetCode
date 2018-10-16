# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       Building a product array
   Description:
   Author:           God
   date：            2018/10/16
-------------------------------------------------
   Change Activity:  2018/10/16
-------------------------------------------------
"""
__author__ = 'God'


class Solution:
    def multiply(self, A):
        B = []
        for i in A:
            self.node = 0
            B.append(reduce(lambda x, y: x*1 if y == i and self.fun(y, i) else x*y, A))
        return B

    def fun(self, number, i):
        if self.node == 0 and i == number:
            self.node = 1
            return True
        return False
