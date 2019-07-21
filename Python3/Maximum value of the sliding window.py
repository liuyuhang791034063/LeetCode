# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       Maximum value of the sliding window
   Description:
   Author:           God
   date：            2018/12/2
-------------------------------------------------
   Change Activity:  2018/12/2
-------------------------------------------------
"""
__author__ = 'God'


class Solution:
    def maxInWindows(self, num, size):
        if not num or not size or len(num) < size:
            return []

        temp = []
        for i in range(size):
            temp.append(num.pop(0))
        res = []
        while num:
            res.append(max(temp))
            temp.pop(0)
            temp.append(num.pop(0))
        res.append(max(temp))
        return res


print(Solution().maxInWindows([2, 3, 4, 2, 6, 2, 5, 1], 0))