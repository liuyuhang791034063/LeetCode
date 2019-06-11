# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       Remove Duplicates from Sorted Array
   Description:
   Author:           God
   date：            2018/12/28
-------------------------------------------------
   Change Activity:  2018/12/28
-------------------------------------------------
"""
__author__ = 'God'


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 1:
            return len(nums)
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i+1