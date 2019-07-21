# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       The length of Binary Tree
   Description:
   Author:           God
   date：            2018/10/10
-------------------------------------------------
   Change Activity:  2018/10/10
-------------------------------------------------
"""
__author__ = 'God'


class Solution:
    def TreeDepth(self, pRoot):
        if pRoot is None:
            return 0
        return max(1+self.TreeDepth(pRoot.left), 1+self.TreeDepth(pRoot.right))


class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if pRoot is None:
            return 0
        stack = []
        if pRoot is not None:
            stack.append((1, pRoot))
        res_depth = 0
        while stack:
            depth, pRoot = stack.pop()
            if pRoot is not None:
                res_depth = max(res_depth, depth)
                stack.append((depth + 1, pRoot.left))
                stack.append((depth + 1, pRoot.right))

        return res_depth
