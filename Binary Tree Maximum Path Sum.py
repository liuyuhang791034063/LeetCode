# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       Binary Tree Maximum Path Sum
   Description:
   Author:           God
   date：            2019/2/13
-------------------------------------------------
   Change Activity:  2019/2/13
-------------------------------------------------
"""
__author__ = 'God'


class Solution:
    res = -100000000000

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.getMax(root)
        return self.res

    def getMax(self, root):
        if root is None:
            return 0
        left = max(0, self.getMax(root.left))
        right = max(0, self.getMax(root.right))  # 如果子树路径和为负则应当置0表示最大路径不包含子树
        self.res = max(self.res, root.val + left + right)  # 判断在该节点包含左右子树的路径和是否大于当前最大路径和
        return max(left, right) + root.val