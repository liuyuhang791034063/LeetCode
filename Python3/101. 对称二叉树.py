# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 递归
# class Solution:
#     def isSymmetric(self, root: TreeNode) -> bool:
#         def check(left, right):
#             if not left and not right:
#                 return True
#             elif not left or not right:
#                 return False

#             if left.val != right.val:
#                 return False

#             return check(left.left, right.right) and check(left.right, right.left)

#         return check(root, root

# 非递归
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        queue = [root]

        while queue:
            next_q = []
            temp = []

            for node in queue:
                if not node:
                    temp.append(None)
                    continue
                next_q.append(node.left)
                next_q.append(node.right)

                temp.append(node.val)

            if temp != temp[::-1]:
                return False
            queue = next_q

        return True