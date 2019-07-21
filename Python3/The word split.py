# coding=utf-8
"""
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

说明：

拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
"""


# class Solution(object):
#     def wordBreak(self, s, wordDict):
#         """
#         :type s: str
#         :type wordDict: List[str]
#         :rtype: bool
#         """
#         n = len(s)
#         dp = [False] * (n + 1)
#         dp[0] = True
#         for i in range(n):
#             for j in range(i, -1, -1):
#                 print(j, i, s[j:i + 1], dp)
#                 if dp[j] and s[j:i + 1] in wordDict:
#                     dp[i + 1] = True
#                     break
#             print('-----loop-----')
#         return dp[n]

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        l = set()
        for d in wordDict:
            l.add(len(d))

        dp = [0 for x in s]
        for i in range(1, len(s)+1):
            if s[0:i] in wordDict:
                dp[i-1] = 1

        for i in range(1, len(s)):
            if dp[i] == 0:
                for k in l:
                    if i >= k and dp[i-k] == 1 and s[i-k+1:i+1] in wordDict:
                        dp[i] = 1
                        break

        return dp[-1] == 1


if __name__ == '__main__':
    s = "leetcode"
    wordDict = ["leet", "code"]
    print(Solution().wordBreak("aaaaaaa", ["aaaa","aaa"]))
    # print(Solution().wordBreak(s, wordDict))