# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       The number of times the number appears in the sorted array
   Description:
   Author:           God
   date：            2018/10/26
-------------------------------------------------
   Change Activity:  2018/10/26
-------------------------------------------------
"""
__author__ = 'God'


class Solution:
    def GetNumberOfK(self, data, k):
        if len(data) == 0:
            return 0
        if len(data) == 1 and data[0] != k:
            return 0
        left = 0
        right = len(data) - 1
        first_k = 0
        while left <= right:
            mid = (left + right) // 2
            if data[mid] < k:
                left = mid + 1
            elif data[mid] > k:
                right = mid - 1
            else:
                if mid == 0:
                    first_k = 0
                    break
                elif data[mid-1] != k:
                    first_k = mid
                    break
                else:
                    right = mid - 1
        left = 0
        right = len(data) - 1
        last_k = -1
        while left <= right:
            mid = (left + right) // 2
            if data[mid] < k:
                left = mid + 1
            elif data[mid] > k:
                right = mid - 1
            else:
                if mid == len(data) - 1:
                    last_k = len(data) - 1
                    break
                elif data[mid+1] != k:
                    last_k = mid
                    break
                else:
                    left = mid + 1
        return last_k - first_k + 1
