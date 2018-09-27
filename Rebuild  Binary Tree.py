# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       teste
   Description:
   Author:           God
   date：            2018/9/26
-------------------------------------------------
   Change Activity:  2018/9/26
-------------------------------------------------
"""
__author__ = 'God'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        """
        :param pre: List
        :param tin: List
        :return: TreeNode
        """
        if len(pre) == 0:
            return None
        if len(pre) == 1:
            return TreeNode(pre[0])

        # 中左 中右
        zz, zy = tin[:tin.index(pre[0])], tin[tin.index(pre[0]) + 1:]

        # 前左 前右
        qz, qy = pre[1:len(zz)+1], pre[len(zz)+1:]

        res = TreeNode(pre[0])
        res.left = Solution().reConstructBinaryTree(qz, zz)
        res.right = Solution().reConstructBinaryTree(qy, zy)
