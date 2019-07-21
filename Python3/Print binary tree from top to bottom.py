# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       Print binary tree from top to bottom
   Description:
   Author:           God
   date：            2018/10/11
-------------------------------------------------
   Change Activity:  2018/10/11
-------------------------------------------------
"""
__author__ = 'God'


class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if root is None:
            return []
        queue = list()
        res = list()
        queue.append(root)
        while queue:
            head = queue.pop(0)
            res.append(head.val)
            if head.left:
                queue.append(head.left)
            if head.right:
                queue.append(head.right)
        return res