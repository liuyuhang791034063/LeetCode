class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = 1
        res_str = s[0]

        def fun(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return s[left+1:right], right - left - 1

        for i in range(len(s)):
            one_s, one = fun(s, i, i)
            two_s, two = fun(s, i, i + 1)

            temp = one_s if one > two else two_s

            if len(temp) >= res:
                res = len(temp)
                res_str = temp

        return ''.join(res_str)


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        res = []
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]

        for r in range(1, len(s)):
            for l in range(r):
                if s[l] == s[r] and (r - l <= 2 or dp[l+1][r-1]):
                    dp[l][r] = True
                    if r-l+1 > len(res):
                        res = s[l:r+1]

        return res



if __name__ == '__main__':
    Solution().longestPalindrome("babad")