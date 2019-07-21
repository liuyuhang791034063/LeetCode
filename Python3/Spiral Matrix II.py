# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       Spiral Matrix II
   Description:
   Author:           God
   date：            2019/1/11
-------------------------------------------------
   Change Activity:  2019/1/11
-------------------------------------------------
"""
__author__ = 'God'


class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0 for _ in range(n)] for _ in range(n)]
        i, number = 0, 1
        while i <= n // 2:  # i记录的是半层数
            if number <= n**2:
                for j in range(i, n-i):     # 横向遍历(需要根据半层数 多一层就多了外面一圈 遍历需要少遍历一个)
                    res[i][j] = number
                    number += 1
            if number <= n**2:
                for j in range(i+1, n-i):   # 纵向遍历(需要根据半层数确定二维位置 然后向下遍历 遍历个数需要半层数确定)
                    res[j][n-i-1] = number
                    number += 1
            if number <= n**2:
                for j in range(n-i-2, -1+i, -1):    # 横向遍历(需要根据半层数确定二维位置 然后向左遍历 遍历个数需要半层数确定)
                    res[n-i-1][j] = number
                    number += 1
            if number <= n**2:              # 纵向遍历(需要根据半层数确定二维位置 然后向上遍历 遍历个数需要半层数确定)
                for j in range(n-i-2, i, -1):
                    res[j][i] = number
                    number += 1
            i += 1
        return res