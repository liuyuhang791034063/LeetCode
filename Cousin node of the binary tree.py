# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       Cousin node of the binary tree
   Description:
   Author:           God
   date：            2019/2/17
-------------------------------------------------
   Change Activity:  2019/2/17
-------------------------------------------------
"""
__author__ = 'God'


"""
在二叉树中，根节点位于深度 0 处，每个深度为 k 的节点的子节点位于深度 k+1 处。

如果二叉树的两个节点深度相同，但父节点不同，则它们是一对堂兄弟节点。

我们给出了具有唯一值的二叉树的根节点 root，以及树中两个不同节点的值 x 和 y。

只有与值 x 和 y 对应的节点是堂兄弟节点时，才返回 true。否则，返回 false。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isCousins(self, root: 'TreeNode', x: 'int', y: 'int') -> 'bool':
        self.x = x
        self.y = y
        self.x_father = None
        self.y_father = None
        self.x_depth = -1
        self.y_depth = -1
        self.bianLi(root, 0)
        if self.x_depth is self.y_depth and self.x_father is not self.y_father:
            return True
        else:
            return False

    def bianLi(self, root, depth):
        if root is None:
            return
        root_left_val = root.left.val if root.left else None
        root_right_val = root.right.val if root.right else None
        if self.x is root_left_val or self.x is root_right_val:
            self.x_depth = depth+1
            self.x_father = root
        if self.y is root_left_val or self.y is root_right_val:
            self.y_father = root
            self.y_depth = depth+1
        if root.left:
            self.bianLi(root.left, depth+1)
        if root.right:
            self.bianLi(root.right, depth+1)


if __name__ == '__main__':
    node = TreeNode(1)
    node.left = TreeNode(2)
    node.right = TreeNode(3)
    node.left.right = TreeNode(4)
    node.right.right = TreeNode(5)
    print(Solution().isCousins(node, 5, 4))