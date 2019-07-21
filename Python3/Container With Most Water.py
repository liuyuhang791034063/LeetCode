# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       Container With Most Water
   Description:
   Author:           God
   date：            2018/12/15
-------------------------------------------------
   Change Activity:  2018/12/15
-------------------------------------------------
"""
__author__ = 'God'


class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        if len(height) == 2:
            return min(height[0], height[1])

        s = []
        i = 0
        j = len(height) - 1
        while i < j:
            temp = (j - i) * min(height[i], height[j])
            s.append(temp)
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return max(s)