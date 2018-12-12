# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       Palindrome Number
   Description:
   Author:           God
   date：            2018/12/12
-------------------------------------------------
   Change Activity:  2018/12/12
-------------------------------------------------
"""
__author__ = 'God'


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x)[::-1] == str(x)

print(Solution().isPalindrome(121))
