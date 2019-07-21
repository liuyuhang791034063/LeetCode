# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       Ugly Number
   Description:
   Author:           God
   date：            2018/10/16
-------------------------------------------------
   Change Activity:  2018/10/16
-------------------------------------------------
"""
__author__ = 'God'


class Solution:
    def GetUglyNumber_Solution(self, index):
        if index == 0:
            return 0
        res = [1]
        index2 = index3 = index5 = 0
        for i in range(1, index):
            u2 = res[index2] * 2
            u3 = res[index3] * 3
            u5 = res[index5] * 5
            res.append(min(u2, min(u3, u5)))
            if res[i]/2 == res[index2]:
                index2 += 1
            if res[i]/3 == res[index3]:
                index3 += 1
            if res[i]/5 == res[index5]:
                index5 += 1
        return res.pop()


print(Solution().GetUglyNumber_Solution(0))