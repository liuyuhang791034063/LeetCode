# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       Balanced binary tree
   Description:
   Author:           God
   date：            2018/10/11
-------------------------------------------------
   Change Activity:  2018/10/11
-------------------------------------------------
"""
__author__ = 'God'


class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        return self.fun(pRoot) is not -1

    def fun(self, node):
        if node is None:
            return 0
        left = self.fun(node.left)
        if left is -1:
            return -1
        right = self.fun(node.right)
        if right is -1:
            return -1
        if abs(left - right) > 1:
            return max(left, right) + 1
        else:
            return -1
