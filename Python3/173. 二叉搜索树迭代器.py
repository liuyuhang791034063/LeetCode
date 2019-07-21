class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.data = []
        while root:
            self.data.append(root)
            root = root.left

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        node = self.data.pop()
        right = node.right
        while right:
            self.data.append(right)
            right = right.left

        return node.val

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return len(self.data) != 0


