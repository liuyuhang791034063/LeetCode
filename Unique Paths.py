# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       Unique Paths
   Description:
   Author:           God
   date：            2019/1/22
-------------------------------------------------
   Change Activity:  2019/1/22
-------------------------------------------------
"""
__author__ = 'God'


class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        num = [[0 for i in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    num[i][j] = 1
                else:
                    num[i][j] = num[i-1][j] + num[i][j-1]
        return num[m-1][n-1]