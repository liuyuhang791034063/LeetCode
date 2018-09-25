# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       Linked List Cycle II
   Description:
   Author:           God
   date：            2018/9/25
-------------------------------------------------
   Change Activity:  2018/9/25
-------------------------------------------------
"""
__author__ = 'God'


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        if head.next is None:
            return None
        first = second = head
        while second and second.next:
            first = first.next
            second = second.next.next
            if first == second:
                p = head
                while first != p:
                    p = p.next
                    first = first.next
                return p
        return None
