# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       Linked List Cycle
   Description:
   Author:           God
   date：            2018/9/25
-------------------------------------------------
   Change Activity:  2018/9/25
-------------------------------------------------
"""
__author__ = 'God'


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # 空或者单一个的时候
        if head == None or head.next == None:
            return False

        first = second = head
        while second and second.next:
            first = first.next
            second = second.next.next
            if first == second:
                return True
        return False
