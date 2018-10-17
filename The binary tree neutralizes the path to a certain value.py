# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       The binary tree neutralizes the path to a certain value
   Description:
   Author:           God
   date：            2018/10/17
-------------------------------------------------
   Change Activity:  2018/10/17
-------------------------------------------------
"""
__author__ = 'God'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        if root is None:
            return []

        res = []

        def fun(root, path, number):
            number += root.val

            path.append(root)

            # 判断是否为叶节点
            ifLeft = root.left is None and root.right is None

            if number == expectNumber and ifLeft:
                nums = []
                for i in path:
                    nums.append(i.val)
                res.append(nums)

            # 判断小于的时候继续查找
            if number < expectNumber:
                if root.left:
                    fun(root.left, path, number)
                if root.right:
                    fun(root.right, path, number)

            # 结尾的时候需要弹出这个已经判断过的点
            path.pop()

        fun(root, [], 0)
        return res


class Solution:
    def FindPath(self, root, expectNumber):
        def fun(root):
            if root:
                b.append(root.val)
                if not root.left and not root.right and sum(b) == expectNumber:
                    a.append(b[:])
                else:
                    fun(root.left), fun(root.right)
                b.pop()
        a, b = [], []
        fun(root)
        return a

