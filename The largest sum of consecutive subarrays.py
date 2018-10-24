# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       The largest sum of consecutive subarrays
   Description:
   Author:           God
   date：            2018/10/24
-------------------------------------------------
   Change Activity:  2018/10/24
-------------------------------------------------
"""
__author__ = 'God'

'''
尝试使用前后节点遍历列表
'''


class Solution:
    def FindGreatestSumOfSubArray(self, array):
        if not array:
            return 0
        temp = 0
        resMax = -0xffffffff
        for i in array:
            if temp <= 0:  # 如果之前的和小于零,则让和等于现在i值
                temp = i
            else:
                temp += i
            if temp > resMax:
                resMax = temp
        return resMax


if __name__ == '__main__':
    a = Solution().FindGreatestSumOfSubArray([1, -2, 3, 10, -4, 7, 2, -5])
    print(a)