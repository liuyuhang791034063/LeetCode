# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       Rotate List
   Description:
   Author:           God
   date：            2019/1/17
-------------------------------------------------
   Change Activity:  2019/1/17
-------------------------------------------------
"""
__author__ = 'God'


class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next or k == 0:
            return []
        head_number = 0
        head_temp = head
        while head_temp:
            head_number += 1
            head_temp = head_temp.next
        k = k % head_number
        if k == 0:
            return head
        temp = 0
        head_temp = head
        new_head = None
        while head_temp:
            temp += 1
            if head_number - temp == k:
                new_head = head_temp.next
                head_temp.next = None
            head_temp = head_temp.next
        new_temp = new_head
        while new_temp.next:
            new_temp = new_temp.next
        new_temp.next = head
        return new_head