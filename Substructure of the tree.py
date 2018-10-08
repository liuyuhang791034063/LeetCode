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
        # B树为空，则存在
        if p2 is None:
            return True
        if p1 is None:
            return p1 == p2
        flag = False
        if p1.val == p2.val:
            # 查找该节点的左右节点
            flag = self.SearchSimiler(p1.left, p2.left) and self.SearchSimiler(p1.right, p2.right)
        # 如果flag为True，返回True，否则继续从左节点开始查找，如果还失败，从右节点开始查找
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


class Solution:
    def __init__(self):
        self.Root1_list = []
        self.Root2_list = []

    def Createtreelist(self, root, note):
        if root is None:
            return
        if note is True:
            self.Root1_list.append(root.val)
            self.Createtreelist(root.left, True)
            self.Createtreelist(root.right, True)
        else:
            self.Root2_list.append(root.val)
            self.Createtreelist(root.left, False)
            self.Createtreelist(root.right, False)

    def HasSubtree(self, pRoot1, pRoot2):
        """
        :param pRoot1: TreeNode
        :param pRoot2: TreeNode
        :return:
        """
        self.Createtreelist(pRoot1, True)
        self.Createtreelist(pRoot2, False)
        p = self.Root2_list
        q = self.Root1_list
        # 如果为空树直接返回 false
        if len(p) is 0:
            return False
        note2 = 0
        for i in range(len(q)):
            if note2 == len(p):
                break
            if q[i] == p[note2]:
                note2 += 1
            else:
                if q[i] == p[0]:
                    continue
                note2 = 0
        if note2 == len(p):
            return True
        return False


if __name__ == '__main__':
    p1 = TreeNode(8)
    p1.left = TreeNode(8)
    p1.right = TreeNode(7)
    temp = p1.left
    temp.left = TreeNode(9)
    temp.right = TreeNode(2)
    temp = temp.right
    temp.left = TreeNode(4)
    temp.right = TreeNode(7)
    p2 = TreeNode(8)
    p2.left = TreeNode(9)
    p2.right = TreeNode(2)
    print(Solution().HasSubtree(p1, p2))