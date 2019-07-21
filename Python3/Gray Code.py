# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       Gray Code
   Description:
   Author:           God
   date：            2019/1/26
-------------------------------------------------
   Change Activity:  2019/1/26
-------------------------------------------------
"""
__author__ = 'God'

'''
格雷码就是一个二进制的数字系统
主要的特点就是两个连续的数值之间仅有一个位数是有差别的

可以通过n ^ n/2 来生成
1 ^ 0 = 001 ^ 000 = 001
2 ^ 1 = 010 ^ 001 = 011 
3 ^ 1 = 011 ^ 001 = 010
4 ^ 2 = 100 ^ 010 = 110
5 ^ 2 = 101 ^ 010 = 111
'''


class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        for i in range(1 << n):
            res.append(i ^ i >> 1)
        return res

    def grayCode2(self, n):
        return [i ^ i >> 1 for i in range(1 << n)]
