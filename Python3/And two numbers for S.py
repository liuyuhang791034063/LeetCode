# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       And two numbers for S
   Description:
   Author:           God
   date：            2018/10/29
-------------------------------------------------
   Change Activity:  2018/10/29
-------------------------------------------------
"""
__author__ = 'God'


class Solution:
    def FindNumbersWithSum(self, array, tsum):
        if not array:
            return []
        for i in range(len(array)-1):
            low = array[i]
            if low >= tsum//2:
                break
            try:
                array.index(tsum-low)
                return [low, tsum-low]
            except ValueError:
                continue
        return []


class Solution1:
    def FindNumbersWithSum(self, array, tsum):
        i, j = 0, len(array)-1
        while i < j:
            if array[i] + array[j] == tsum:
                return [array[i], array[j]]
            while i < j and array[i] + array[j] > tsum:
                j -= 1
            while i < j and array[i] + array[j] < tsum:
                i += 1
        return []


if __name__ == '__main__':
    print(Solution1().FindNumbersWithSum([],21))