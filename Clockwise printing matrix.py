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
    def printMatrix(self, matrix):
        # write code here
        result = []
        while matrix:
            result += matrix.pop(0)
            if not matrix or not matrix[0]:
                break
            matrix = self.getNewMatrix(matrix)
        return result

    def getNewMatrix(self, m):
        height = len(m[0])
        note = height-1
        result = []
        for i in range(height):
            temp = []
            for j in m:
                temp.append(j[note])
            result.append(temp)
            note -= 1
        return result


if __name__ == '__main__':
    list = [[1]]
    print(Solution().printMatrix(list))