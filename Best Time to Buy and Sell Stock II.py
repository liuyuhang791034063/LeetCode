# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       Best Time to Buy and Sell Stock II
   Description:
   Author:           God
   date：            2019/1/29
-------------------------------------------------
   Change Activity:  2019/1/29
-------------------------------------------------
"""
__author__ = 'God'

'''
从头到尾遍历一遍 如果出现后面一天大于前面一天就记录下来
'''


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        for index in range(len(prices)-1):
            temp = prices[index+1] - prices[index]
            if temp > 0:
                res += temp
        return res