# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       Median of Two Sorted Arrays
   Description:
   Author:           God
   date：            2018/12/10
-------------------------------------------------
   Change Activity:  2018/12/10
-------------------------------------------------
"""
__author__ = 'God'


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1 += nums2
        nums1 = sorted(nums1)
        return (nums1[len(nums1)//2]+nums1[-(len(nums1)//2+1)])/2