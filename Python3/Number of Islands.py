# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       Number of Islands
   Description:
   Author:           God
   date：            2018/12/21
-------------------------------------------------
   Change Activity:  2018/12/21
-------------------------------------------------
"""
__author__ = 'God'


class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    self.dfs(grid, i, j)
        return count

    def dfs(self, grid, i, j):
        grid[i][j] = '0'
        if i-1 >= 0 and grid[i-1][j] == '1':
            self.dfs(grid, i-1, j)
        if j+1 < len(grid[0]) and grid[i][j+1] == '1':
            self.dfs(grid, i, j+1)
        if i+1 < len(grid) and grid[i+1][j] == '1':
            self.dfs(grid, i+1, j)
        if j-1 >= 0 and grid[i][j-1] == '1':
            self.dfs(grid, i, j-1)