# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       Flip the binary tree
   Description:
   Author:           God
   date：            2018/10/16
-------------------------------------------------
   Change Activity:  2018/10/16
-------------------------------------------------
"""
__author__ = 'God'


class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None :
            return
        tmp = root.left
        root.left = root.right
        root.right = tmp
        self.invertTree(root.left)
        self.invertTree(root.right) # root.left, root.right = root.right, root.left
        return root
