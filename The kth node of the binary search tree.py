# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       The kth node of the binary search tree
   Description:
   Author:           God
   date：            2018/11/29
-------------------------------------------------
   Change Activity:  2018/11/29
-------------------------------------------------
"""
__author__ = 'God'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# class Solution:
#     def __init__(self):
#         self.node_list = []
#     # 返回对应节点TreeNode
#
#     def KthNode(self, pRoot, k):
#         if not pRoot or k == 0:
#             return None
#         self.middle(pRoot)
#         if k >= len(self.node_list):
#             return None
#         return self.node_list[k-1]
#
#     def middle(self, pRoot):
#         if not pRoot:
#             return
#         self.middle(pRoot.left)
#         self.node_list.append(pRoot)
#         self.middle(pRoot.right)


class Solution:
    def __init__(self):
        self.flag = 0
        self.res = None
    # 返回对应节点TreeNode

    def KthNode(self, pRoot, k):
        if not pRoot or k == 0:
            return
        self.KthNode(pRoot.left, k)
        self.flag += 1
        if self.flag == k:
            self.res = pRoot
        self.KthNode(pRoot.right, k)
        return self.res