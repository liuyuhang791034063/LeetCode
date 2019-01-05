# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       The largest sum of consecutive subarrays
   Description:
   Author:           God
   date：            2018/10/24
-------------------------------------------------
   Change Activity:  2018/10/24
-------------------------------------------------
"""
__author__ = 'God'


'''On的办法'''


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_sum = 0
        res = -float("inf")

        for i in nums:
            num_sum += i
            if num_sum > res:
                res = num_sum
            if num_sum < 0:
                num_sum = 0

"""
分治法
python效率极低
"""


class Solution:
    def subMaxSubArray(self, nums, low, high):
        if low == high:
            return nums[low]
        mid = (low + high) // 2
        leftvalue = self.subMaxSubArray(nums, low, mid)
        rightvalue = self.subMaxSubArray(nums, mid+1, high)
        midleft = nums[mid]
        sumleft = nums[mid]
        i = mid-1
        while i >= low:
            sumleft += nums[i]
            i -= 1
            if midleft < sumleft:
                midleft = sumleft
        midright = nums[mid+1]
        sumright = nums[mid+1]
        i = mid+2
        while i <= high:
            sumright += nums[i]
            i += 1
            if midright < sumright:
                midright = sumright
        midvalue = midleft + midright
        if midvalue >= leftvalue and midvalue >= rightvalue:
            return midvalue
        elif leftvalue >= midvalue and leftvalue >= rightvalue:
            return leftvalue
        else:
            return rightvalue

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.subMaxSubArray(nums, 0, len(nums)-1)


if __name__ == '__main__':
    a = Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
    print(a)