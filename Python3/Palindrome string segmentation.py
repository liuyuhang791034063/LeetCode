# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       Palindrome string segmentation
   Description:
   Author:           God
   date：            2019/3/6
-------------------------------------------------
   Change Activity:  2019/3/6
-------------------------------------------------
"""
__author__ = 'God'


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if len(s) == 0:
            return []
        else:
            res = []
            self.find(s, [], res)
        return res

    def find(self, s, cur, res):
        if len(s) == 0:
            res.append(cur)
        for i in range(1, len(s)+1):
            if self.check(s[:i]):
                self.find(s[i:], cur + [s[:i]], res)

    @staticmethod
    def check(s):
        if len(s) == 0:
            return False
        l, r = 0, len(s)-1
        while l <= r:
            if s[l] != s[r]:
                return False
            else:
                l, r = l+1, r-1
        return True


if __name__ == '__main__':
    print(Solution().partition("aab"))