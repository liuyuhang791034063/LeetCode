# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       Left rotation string
   Description:
   Author:           God
   date：            2018/10/30
-------------------------------------------------
   Change Activity:  2018/10/30
-------------------------------------------------
"""
__author__ = 'God'


class Solution:
    def LeftRotateString(self, s, n):
        return s[n:] + s[:n]


class Solution1:
    def LeftRotateString(self, s, n):
        l = len(s)
        if l == 0:
            return ""
        n = n % l
        s = s + s
        return s[n:n+l]


if __name__ == '__main__':
    print(Solution().LeftRotateString('123123',2))