# coding=utf-8
"""
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
说明：本题中，我们将空字符串定义为有效的回文串。
"""


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        """
        最笨的方法
        """
        if s is "":
            return True
        l, r = 0, len(s)-1
        f1, f2 = 0, 0
        while l < r:
            while l < r:
                if 'A' <= s[l] <= 'Z' or 'a' <= s[l] <= 'z' or '0' <= s[l] <= '9':
                    if '0' <= s[l] <= '9':
                        f1 = 1
                    else:
                        f1 = 0
                    break
                else:
                    l += 1
            while l < r:
                if 'A' <= s[r] <= 'Z' or 'a' <= s[r] <= 'z' or '0' <= s[r] <= '9':
                    if '0' <= s[r] <= '9':
                        f2 = 1
                    else:
                        f2 = 0
                    break
                else:
                    r -= 1
                    if l is r:
                        if '0' <= s[r] <= '9':
                            f2 = 1
                        else:
                            f2 = 0
            if f1 is not f2:
                return False
            if abs(ord(s[l]) - ord(s[r])) == 32 or abs(ord(s[l]) - ord(s[r])) == 0:
                l += 1
                r -= 1
            else:
                return False
        return True

        """
        python内置str的检查函数
        """
        s = [c for c in s if c.isalpha() or c.isdigit()]
        if len(s) <= 1:
            return True
        l, r = 0, len(s)-1
        while l < r:
            if s[l].lower() != s[r].lower():
                return False
            i, j = i+1, j-1
        return True


str1 = ".,"
print(Solution().isPalindrome(str1))