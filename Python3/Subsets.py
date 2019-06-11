# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       Subsets
   Description:
   Author:           God
   date：            2019/1/24
-------------------------------------------------
   Change Activity:  2019/1/24
-------------------------------------------------
"""
__author__ = 'God'


class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for num in nums:
            for temp in res[:]:
                x = temp[:]
                x.append(num)
                res.append(x)
        return res


Solution().subsets([1,2,3])