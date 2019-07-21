# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       The first public node of the two linked lists
   Description:
   Author:           God
   date：            2018/10/15
-------------------------------------------------
   Change Activity:  2018/10/15
-------------------------------------------------
"""
__author__ = 'God'

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        p1 = pHead1
        p2 = pHead2
        while p1 != p2:
            p1 = pHead2 if p1 is None else p1.next
            p2 = pHead1 if p2 is None else p2.next
        return p1


class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        list1 = []
        while pHead1:
            list1.append(pHead1.val)
            pHead1 = pHead1.next
        while pHead2:
            if pHead2.val in list1:
                return pHead2
            pHead2 = pHead2.next
        return None
