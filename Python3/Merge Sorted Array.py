# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       Merge Sorted Array
   Description:
   Author:           God
   date：            2019/1/25
-------------------------------------------------
   Change Activity:  2019/1/25
-------------------------------------------------
"""
__author__ = 'God'


class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        # 从后往前算的方法
        p = m + n - 1
        m -= 1
        n -= 1
        while m >= 0 and n >= 0:
            if nums1[m] > nums2[n]:
                nums1[p] = nums1[m]
                m -= 1
            else:
                nums1[p] = nums2[n]
                n -= 1
            p -= 1

        while n >= 0:
            nums1[p] = nums2[n]
            n -= 1
            p -= 1

        # 快捷办法
        nums1[m:] = nums2
        nums1.sort()

Solution().merge([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3)