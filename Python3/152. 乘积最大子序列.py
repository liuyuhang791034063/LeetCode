class Solution:
    def maxProduct(self, nums) -> int:
        res, imin, imax = -111111111, 1, 1

        for i in nums:
            if i < 0:
                imin, imax = imax, imin

            imin = min(i, imin*i)
            imax = max(i, imax*i)

            res = max(res, imax)

        return res


if __name__ == "__main__":
    print(Solution().maxProduct([-3, -4]))
