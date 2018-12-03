# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       Path in the matrix
   Description:
   Author:           God
   date：            2018/12/3
-------------------------------------------------
   Change Activity:  2018/12/3
-------------------------------------------------
"""
__author__ = 'God'


class Solution:
    def hasPath(self, matrix, rows, cols, path):
        self.col, self.row = cols, rows
        matrix = [list(matrix[cols * i:cols * i + cols]) for i in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == path[0]:
                    self.b = False
                    self.search(matrix, path[1:], [(i, j)], i, j)
                    if self.b:
                        return True
        return False

    def search(self, matrix, word, exists, i, j):
        if word == '':
            self.b = True
            return

        if j != 0 and (i, j-1) not in exists and matrix[i][j-1] == word[0]:
            self.search(matrix, word[1:], exists+[(i, j-1)], i, j-1)

        if i != 0 and (i-1, j) not in exists and matrix[i-1][j] == word[0]:
            self.search(matrix, word[1:], exists+[(i-1, j)], i-1, j)

        if j != self.col - 1 and (i, j+1) not in exists and matrix[i][j+1] == word[0]:
            self.search(matrix, word[1:], exists+[(i, j+1)], i, j+1)

        if i != self.row - 1 and (i+1, j) not in exists and matrix[i+1][j] == word[0]:
            self.search(matrix, word[1:], exists+[(i+1, j)], i+1, j)