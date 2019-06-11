# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       Arrange the array into the smallest number
   Description:
   Author:           God
   date：            2018/10/15
-------------------------------------------------
   Change Activity:  2018/10/15
-------------------------------------------------
"""
__author__ = 'God'


class Solution:
    def PrintMinNumber(self, numbers):
        b = map(str, numbers)
        b.sort(lambda x, y: cmp(x+y, y+x))
        return ''.join(b)


if __name__ == '__main__':
    Solution().PrintMinNumber([3, 32, 321])