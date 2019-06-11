# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       Merge Two Sorted Lists
   Description:
   Author:           God
   date：            2018/12/26
-------------------------------------------------
   Change Activity:  2018/12/26
-------------------------------------------------
"""
__author__ = 'God'


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 or not l2:
            return l1 if not l2 else l2
        res_node = ListNode(0)
        temp_node = res_node
        while l1 and l2:
            if l1.val <= l2.val:
                temp_node.next = l1
                l1 = l1.next
            else:
                temp_node.next = l2
                l2 = l2.next
            temp_node = temp_node.next
        if l1 is not None:
            temp_node.next = l1
        if l2 is not None:
            temp_node.next = l2
        return res_node.next
