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
        return self.depth(pRoot)

    def depth(root):
        if root is None:
            return 0
        dq = list()
        dq.append((root, 1))
        while dq:
            node, layer = dq.pop(0)
            deep = layer
            if node.left:
                dq.append((node.left, layer + 1))
            if node.right:
                dq.append((node.right, layer + 1))
        return deep