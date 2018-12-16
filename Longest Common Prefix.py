# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       Longest Common Prefix
   Description:
   Author:           God
   date：            2018/12/16
-------------------------------------------------
   Change Activity:  2018/12/16
-------------------------------------------------
"""
__author__ = 'God'


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        length = min(list(map(len, strs)))
        if length == 0:
            return ''
        res = ''
        flag = True
        for i in range(length):
            for j in strs[1:]:
                if j[i] != strs[0][i]:
                    flag = False
                    break
            if flag is False:
                break
            res += strs[0][i]
        return res