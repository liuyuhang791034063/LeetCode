# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       Reverse Integer
   Description:
   Author:           God
   date：            2018/12/11
-------------------------------------------------
   Change Activity:  2018/12/11
-------------------------------------------------
"""
__author__ = 'God'


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 0
        if x < 0:
            flag = 1

        temp = list(str(abs(x)))
        temp.reverse()
        temp = ''.join(temp)
        res = -1 * int(temp) if flag else int(temp)
        if res >= -1 * pow(2, 31) and res <= pow(2, 31) - 1:
            return res
        else:
            return 0

print(Solution().reverse(-123))