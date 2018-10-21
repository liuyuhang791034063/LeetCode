# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       Replication of complex linked lists
   Description:
   Author:           God
   date：            2018/10/17
-------------------------------------------------
   Change Activity:  2018/10/17
-------------------------------------------------
"""
__author__ = 'God'


class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        if not pHead:
            return
        newnode = RandomListNode(pHead.label)
        newnode.random = pHead.random
        newnode.next = self.Clone(pHead.next)
        return newnode
