class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals = sorted(intervals, key=lambda x: x[0])

        res = []

        for interval in intervals:
            if not res or res[-1][-1] < interval[0]:
                res.append(interval)
            else:
                res[-1][-1] = max(res[-1][-1], interval[-1])
        return res


if __name__ == '__main__':
    a = Solution()
    a.merge([[1,3],[2,6],[8,10],[15,18]])