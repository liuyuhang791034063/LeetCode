# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       3Sum Closest
   Description:
   Author:           God
   date：            2018/12/19
-------------------------------------------------
   Change Activity:  2018/12/19
-------------------------------------------------
"""
__author__ = 'God'


class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            l = i + 1
            r = len(nums) - 1
            if nums[i] + nums[l] + nums[l+1] > target:
                res.append(nums[i] + nums[l] + nums[l+1])
                break
            elif nums[i] + nums[r] + nums[r-1] < target:
                res.append(nums[i] + nums[r] + nums[r-1])
            else:
                while l < r:
                    temp = nums[i] + nums[l] + nums[r]
                    res.append(temp)
                    if temp > target:
                        r -= 1
                    elif temp < target:
                        l += 1
                    else:
                        return target
        res.sort(key=lambda x: abs(x-target))
        return res[0]