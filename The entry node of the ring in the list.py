# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       The entry node of the ring in the list
   Description:
   Author:           God
   date：            2018/11/5
-------------------------------------------------
   Change Activity:  2018/11/5
-------------------------------------------------
"""
__author__ = 'God'


class Solution:
    def EntryNodeOfLoop(self, pHead):
        if pHead is None or pHead.next is None:
            return None
        d1 = {}
        while pHead:
            if pHead in d1:
                return pHead
            else:
                d1[pHead] = pHead.next
            pHead = pHead.next
        return None