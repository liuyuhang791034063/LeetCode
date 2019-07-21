# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       Children's games
   Description:
   Author:           God
   date：            2018/10/31
-------------------------------------------------
   Change Activity:  2018/10/31
-------------------------------------------------
"""
__author__ = 'God'

'''
约瑟夫环
'''
class Solution:
    def LastRemaining_Solution(self, n, m):
        if n == 0:
            return -1
        quan = list(range(n))
        i = 0
        temp = 1
        while len(quan) > 1:
            i = i % len(quan)
            if temp == m:
                temp = 1
                quan.pop(i)
            temp += 1
            i += 1
        return quan.pop()


if __name__ == '__main__':
    print(Solution().LastRemaining_Solution(5, 3))
