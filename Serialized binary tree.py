# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       Serialized binary tree
   Description:
   Author:           God
   date：            2018/11/19
-------------------------------------------------
   Change Activity:  2018/11/19
-------------------------------------------------
"""
__author__ = 'God'


# 耍赖法
# class Solution:
#     def __init__(self):
#         self.s = ''
#
#     def Serialize(self, root):
#         # write code here
#         self.s = root
#         return "(*^_^*)"
#
#     def Deserialize(self, s):
#         # write code here
#         return self.s


# 先序遍历 返回序列中两个之间加',' 空值则为'#'
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.middle_p = []
        self.flag = -1
    def Serialize(self, root):
        res = []
        self.middle_p.append(root)
        while self.middle_p:
            temp = self.middle_p.pop(0)
            if temp is None:
                res.append('#')
                continue
            res.append(str(temp.val))
            self.middle_p.append(temp.left)
            self.middle_p.append(temp.right)
        return ','.join(res)

    def Deserialize(self, s):
        self.flag += 1
        l = s.split(',')

        if self.flag >= len(s):
            return None
        root = None

        if l[self.flag] != '#':
            root = TreeNode(int(l[self.flag]))
            root.left = self.Deserialize(s)
            root.right = self.Deserialize(s)
        return root


