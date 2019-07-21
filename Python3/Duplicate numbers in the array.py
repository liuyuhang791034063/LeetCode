# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       Duplicate numbers in the array
   Description:
   Author:           God
   date：            2018/11/1
-------------------------------------------------
   Change Activity:  2018/11/1
-------------------------------------------------
"""
__author__ = 'God'


"""

"""
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        d = dict()
        for i in numbers:
            if i in d:
                duplication[0] = i
                return True
            d[i] = 1
        return False