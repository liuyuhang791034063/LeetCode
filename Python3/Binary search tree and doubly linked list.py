# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       Binary search tree and doubly linked list
   Description:
   Author:           God
   date：            2018/10/21
-------------------------------------------------
   Change Activity:  2018/10/21
-------------------------------------------------
"""
__author__ = 'God'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Convert(self, pRootOfTree):
        if not pRootOfTree:
            return
        self.mid = []
        self.middle(pRootOfTree)
        for i in range(len(self.mid)-1):
            self.mid[i].right = self.mid[i+1]
            self.mid[i+1].left = self.mid[i]

        return self.mid[0]

    def middle(self, root):
        if not root:
            return
        self.middle(root.left)
        self.mid.append(root)
        self.middle(root.right)