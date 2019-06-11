# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       Clockwise printing matrix
   Description:
   Author:           God
   date：            2018/10/8
-------------------------------------------------
   Change Activity:  2018/10/8
-------------------------------------------------
"""
__author__ = 'God'


class Solution:
    # matrix类型为二维列表，需要返回列表
    def spiralOrder(self, matrix):
        result = []
        while matrix:
            result += matrix.pop(0)
            if not matrix:
                break
            matrix = self.getNewMatrix(matrix)
        return result

    def getNewMatrix(self, m):
        res = []
        for i in range(len(m[0])-1, -1, -1):
            res.append([x[i] for x in m])
        return res


if __name__ == '__main__':
    list = [[1]]
    print(Solution().printMatrix(list))