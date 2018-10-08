# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       test
   Description:
   Author:           God
   date：            2018/9/27
-------------------------------------------------
   Change Activity:  2018/9/27
-------------------------------------------------
"""
__author__ = 'God'


# -*- coding:utf-8 -*-
'''
1
1+1 = 2
1+2+1 = 4
1+2+4+1 = 8
......
'''

# class Solution:
#     # 返回合并后列表
#     def Merge(self, pHead1, pHead2):
#         # write code here
#         newHead = ListNode(0)
#         p = newHead
#         while pHead1 or pHead2:
#             if pHead1.val < pHead2.val:
#                 newPoint = ListNode(pHead1.val)
#                 pHead1 = pHead1.next
#                 p.next = newPoint
#                 p = p.next
#             elif pHead1.val > pHead2.val:
#                 newPoint = ListNode(pHead2.val)
#                 pHead2 = pHead2.next
#                 p.next = newPoint
#                 p = p.next
#             else:
#                 newPoint = ListNode(pHead1.val)
#                 pHead1 = pHead1.next
#                 p.next = newPoint
#                 p = p.next
#                 newPoint = ListNode(pHead2.val)
#                 pHead2 = pHead2.next
#                 p.next = newPoint
#                 p = p.next
#         if pHead1:
#             while pHead1:
#                 newPoint = ListNode(pHead1.val)
#                 pHead1 = pHead1.next
#                 p.next = newPoint
#                 p = p.next
#         if pHead2:
#             while pHead2:
#                 newPoint = ListNode(pHead2.val)
#                 pHead2 = pHead2.next
#                 p.next = newPoint
#                 p = p.next
#         return newHead.next


# def addHello(func):
#
#     def wrapped():
#         return 'Hello,' + func()
#
#     return wrapped
#
# @addHello
# def name():
#     return 'Mike'
#
# print(name())


# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def SearchSimiler(self, p1, p2):
        if p2 is None:
            return True
        if p1 is None:
            return p1 == p2
        flag = False
        if p1.val == p2.val:
            flag = self.SearchSimiler(p1.left, p2.left) and self.SearchSimiler(p1.right, p2.right)
        return flag or self.SearchSimiler(p1.left, p2) or self.SearchSimiler(p1.right, p2)
    def HasSubtree(self, pRoot1, pRoot2):
        """
        :param pRoot1: TreeNode
        :param pRoot2: TreeNode
        :return:
        """
        # write code here
        if pRoot1 is None or pRoot2 is None:
            return False
        return self.SearchSimiler(pRoot1, pRoot2)
