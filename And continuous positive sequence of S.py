# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       And continuous positive sequence of S
   Description:
   Author:           God
   date：            2018/10/26
-------------------------------------------------
   Change Activity:  2018/10/26
-------------------------------------------------
"""
__author__ = 'God'

# 两重循环
class Solution:
    def FindContinuousSequence(self, tsum):
        res = []
        for i in range(1, tsum//2+1):
            sum = 0
            for j in range(i, tsum//2+2):
                sum += j
                if sum == tsum:
                    res.append(list(range(i, j+1)))
        return res


#前后指针
class Solution:
    def FindContinuousSequence(self, tsum):
        low = 1
        quick = 2
        res = []
        while quick > low:
            esum = sum(range(low, quick+1))
            if esum == tsum:
                res.append(list(range(low, quick+1)))
                low += 1
            elif esum < tsum:
                quick += 1
            else:
                low += 1
        return res
