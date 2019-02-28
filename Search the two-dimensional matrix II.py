class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # 第一种粗暴的方法
        for i in matrix:
            if target in i:
                return True
        return False

        # 搜索过程 从最上边 最右边开始逼近
        if not matrix:
            return False

        h = len(matrix)
        w = len(matrix[0])

        x = 0
        y = w - 1

        while x < h and y >= 0:
            if matrix[x][y]>target:
                y -= 1
            elif matrix[x][y]<target:
                x += 1
            elif matrix[x][y] == target:
                return True
        return False
