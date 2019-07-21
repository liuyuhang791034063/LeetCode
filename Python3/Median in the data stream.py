# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       Median in the data stream
   Description:
   Author:           God
   date：            2018/11/30
-------------------------------------------------
   Change Activity:  2018/11/30
-------------------------------------------------
"""
__author__ = 'God'


class Solution:
    def __init__(self):
        self.arr = []

    def Insert(self, num):
        self.arr.append(num)
        self.arr.sort()

    def GetMedian(self, fuck):
        arr_length = len(self.arr)
        if arr_length % 2 == 1:
            return self.arr[arr_length//2]
        return (self.arr[arr_length//2] + self.arr[(arr_length//2)-1])/2.0
