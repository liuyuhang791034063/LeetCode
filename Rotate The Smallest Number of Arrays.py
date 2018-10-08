# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       Rotate The Smallest Number of Arrays
   Description:
   Author:           God
   date：            2018/9/27
-------------------------------------------------
   Change Activity:  2018/9/27
-------------------------------------------------
"""
__author__ = 'God'


# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if len(rotateArray) == 0:
            return 0
        for i in range(len(rotateArray)):
            if rotateArray[i] > rotateArray[i+1]:
                return rotateArray[i+1]
        return rotateArray[0]