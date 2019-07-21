# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       Delete duplicate nodes in the linked list
   Description:
   Author:           God
   date：            2018/11/5
-------------------------------------------------
   Change Activity:  2018/11/5
-------------------------------------------------
"""
__author__ = 'God'

'''
暴力遍历
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplication(self, pHead):
        res = []
        while pHead:
            res.append(pHead.val)
            pHead = pHead.next
        res = filter(lambda x: res.count(x) == 1, res)
        rhead = ListNode(0)
        t = rhead
        for i in res:
            new = ListNode(i)
            t.next, t = new, new
        return rhead.next
