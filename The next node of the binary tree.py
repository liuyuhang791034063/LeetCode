# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       The next node of the binary tree
   Description:
   Author:           God
   date：            2018/11/7
-------------------------------------------------
   Change Activity:  2018/11/7
-------------------------------------------------
"""
__author__ = 'God'


class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    def GetNext(self, pNode):
        # 如果为空节点
        if not pNode:
            return None
        # 如果该节点存在有子树
        if pNode.right != None:
            pNode = pNode.right
            while pNode.left != None:
                pNode = pNode.left
            return pNode
        # 如果不存在右子树 就朝父节点查找
        while pNode.next != None:
            proot = pNode.next
            if proot.left == pNode:
                return proot
            pNode = pNode.next
        return None


class Solution:
    def GetNext(self, pNode):
        TempNode = pNode
        while pNode.next:
            pNode = pNode.next
        self.l = []
        self.middle(pNode)
        return self.l[self.l.index(TempNode)+1] if self.l.index(TempNode) != len(self.l)-1 else None

    def middle(self, pNode):
        if not pNode:
            return
        self.middle(pNode.left)
        self.l.append(pNode)
        self.middle(pNode.right)