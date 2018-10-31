# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       Playing cards straight
   Description:
   Author:           God
   date：            2018/10/31
-------------------------------------------------
   Change Activity:  2018/10/31
-------------------------------------------------
"""
__author__ = 'God'

'''
1.计算王的个数
2.排序
3.计算相隔数字的差值和
4.如果出现重复数字直接返回false
'''
class Solution:
    def IsContinuous(self, numbers):
        if not numbers:
            return False
        Kings = numbers.count(0)
        numbers.sort()
        temp = 0
        for i in range(Kings, len(numbers)-1):
            if numbers[i] == numbers[i+1]:
                return False
            temp += numbers[i+1] - numbers[i] - 1
        return True if temp <= Kings or temp == 0 else False
