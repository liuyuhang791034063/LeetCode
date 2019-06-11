# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       Best Time to Buy and Sell Stock
   Description:
   Author:           God
   date：            2019/1/28
-------------------------------------------------
   Change Activity:  2019/1/28
-------------------------------------------------
"""
__author__ = 'God'


'''
整体上思路就是一遍循环 每次
    如果碰到比当前最小的还小的数 就替换当前最小的数
    如果碰到比当前最小的还大的数 就计算两个数的差值 如果大于返回值 则替换
'''


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_num, max_num = 999999, 0
        for i in prices:
            min_num = min(min_num, i)
            max_num = max(max_num, i-min_num)
        return max_num

    def maxProfit2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        min_num = prices[0]
        res = 0
        for i in prices:
            if i < min_num:
                min_num = i
            else:
                res = max(res, i - min_num)
        return res
