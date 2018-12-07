# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       Longest Substring Without Repeating Characters
   Description:
   Author:           God
   date：            2018/12/7
-------------------------------------------------
   Change Activity:  2018/12/7
-------------------------------------------------
"""
__author__ = 'God'


# class Solution:
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         left, right, res = 0, 0, 0
#         flag = 0
#         temp = []
#         s_length = len(s)
#         while right < s_length:
#             number = s[right]
#             if number not in temp:
#                 temp.append(number)
#                 right += 1
#                 if right - left > res:
#                     res = right - left
#             else:
#                 left = s[left:right+1].index(number) + len(s[:left+1])
#                 temp = [i for i in s[left:right+1]]
#                 right += 1
#         return res


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = res = 0
        temp = {}

        for i in range(len(s)):
            if s[i] in temp and start <= temp[s[i]]:
                start = temp[s[i]] + 1
            else:
                res = max(res, i - start + 1)
            temp[s[i]] = i

        return res


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring("loddktdji"))