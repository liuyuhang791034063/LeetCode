# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       Merge k Sorted Lists
   Description:
   Author:           God
   date：            2018/12/27
-------------------------------------------------
   Change Activity:  2018/12/27
-------------------------------------------------
"""
__author__ = 'God'


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        res = []
        for listNode in lists:
            while listNode:
                res.append(listNode.val)
                listNode = listNode.next
        resNode = ListNode(0)
        tempNode = resNode
        res.sort()
        for i in res:
            tempNode.next = ListNode(i)
            tempNode = tempNode.next
        return resNode.next