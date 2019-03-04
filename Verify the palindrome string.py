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
        if s is "":
            return True
        l, r = 0, len(s)-1
        while l < r:
            while True:
                if 'A' <= s[l] <= 'Z' or 'a' <= s[l] <= 'z':
                    break
                else:
                    l += 1
            while True:
                if 'A' <= s[r] <= 'Z' or 'a' <= s[r] <= 'z':
                    break
                else:
                    r -= 1
            if abs(ord(s[l]) - ord(s[r])) == 32 or abs(ord(s[l]) - ord(s[r])) == 0:
                l += 1
                r -= 1
            else:
                return False
        return True


print(Solution().isPalindrome("race a car"))