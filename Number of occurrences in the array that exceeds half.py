# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       1
   Description:
   Author:           God
   date：            2018/10/23
-------------------------------------------------
   Change Activity:  2018/10/23
-------------------------------------------------
"""
__author__ = 'God'

from collections import Counter


class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        max = Counter(numbers).most_common(1)[0]
        return max[0] if max[1] >= len(numbers)/2 else 0
