# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       Find Common Characters
   Description:
   Author:           God
   date：            2019/3/3
-------------------------------------------------
   Change Activity:  2019/3/3
-------------------------------------------------
"""
__author__ = 'God'


"""
给定仅有小写字母组成的字符串数组 A，返回列表中的每个字符串中都显示的全部字符（包括重复字符）组成的列表。例如，如果一个字符在每个字符串中出现 3 次，但不是 4 次，则需要在最终答案中包含该字符 3 次。

你可以按任意顺序返回答案。
"""


class Solution:
    def commonChars(self, A):
        res = []
        chardict = {}
        for i in A[0]:
            if i in chardict:
                chardict[i] += 1
            else:
                chardict[i] = 1
        for k, v in chardict.items():
            flag = 0
            minmun = v
            for j in A[1:]:
                if j.count(k) == 0:
                    flag = 1
                    break
                elif j.count(k) < minmun:
                    minmun = j.count(k)
            if flag == 0:
                while minmun != 0:
                    res.append(k)
                    minmun -= 1
        return res


print(Solution().commonChars(["bella","label","roller"]))