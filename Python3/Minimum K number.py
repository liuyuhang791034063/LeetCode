# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       Minimum K number
   Description:
   Author:           God
   date：            2018/10/23
-------------------------------------------------
   Change Activity:  2018/10/23
-------------------------------------------------
"""
__author__ = 'God'


class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        tinput.sort()
        return tinput[:k] if k <= len(tinput) else []