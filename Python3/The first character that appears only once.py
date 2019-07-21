# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       The first character that appears only once
   Description:
   Author:           God
   date：            2018/10/24
-------------------------------------------------
   Change Activity:  2018/10/24
-------------------------------------------------
"""
__author__ = 'God'


from collections import Counter


class Solution:
    def FirstNotRepeatingChar(self, s):
        c = {}
        for i in s:
            if i in c:
                c[i] += 1
            else:
                c[i] = 1
        for index, i in enumerate(s):
            if c[i] is 1:
                return index
        return -1

    # 一行版本
    def FirstNotRepeatingChar_onerow(self, s):
        return s.index(list(filter(lambda x: s.count(x) == 1, s))[0]) if s else -1

    # 异或
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in nums:
            res ^= i
        return res


if __name__ == '__main__':
    print(Solution().FirstNotRepeatingChar('google'))