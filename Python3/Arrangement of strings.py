# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       Arrangement of strings
   Description:
   Author:           God
   date：            2018/10/17
-------------------------------------------------
   Change Activity:  2018/10/17
-------------------------------------------------
"""
import itertools

__author__ = 'God'


# 直接使用itertools中的permutations方法对元素全排列
class Solution:
    def Permutation(self, ss):
        res = []
        for i in itertools.permutations(ss):
            if ''.join(i) not in res:
                res.append(''.join(i))
        return res


# 递归遍历
class Solution:
    def Permutation(self, ss):
        if not ss:
            return []
        res = []
        self.fun(ss, res, '')
        return sorted(list(set(res)))

    def fun(self, ss, res, string):
        if not ss:
            res.append(string)
        for i in range(len(ss)):
            self.fun(ss[:i] + ss[i + 1:], res, string + ss[i])


# LeetCode
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        for i in itertools.permutations(nums):
            res.append(i)
        return res