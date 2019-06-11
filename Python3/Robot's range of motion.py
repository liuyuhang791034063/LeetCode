# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       Robot's range of motion
   Description:
   Author:           God
   date：            2018/12/5
-------------------------------------------------
   Change Activity:  2018/12/5
-------------------------------------------------
"""
__author__ = 'God'


class Solution:
    def movingCount(self, threshold, rows, cols):
        self.rows, self.cols = rows, cols
        self.set = set()
        self.search(threshold, 0, 0)
        return len(self.set)

    def judge(self, threshold, i, j):
        return sum(map(int, list(str(i)))) + sum(map(int, list(str(j)))) <= threshold

    def search(self, threshold, i, j):
        if not self.judge(threshold, i, j) or (i, j) in self.set:
            return
        self.set.add((i, j))
        if i != self.rows - 1:
            self.search(threshold, i+1, j)
        if j != self.cols - 1:
            self.search(threshold, i, j+1)