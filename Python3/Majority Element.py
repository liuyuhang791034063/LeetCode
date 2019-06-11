class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 排序后输出第len/2个
        nums.sort()
        return nums[len(nums)//2]

        # 自己版本
        if len(nums) == 1:
            return nums[0]
        level = len(nums)/2
        levelDict = {}
        for i in nums:
            if i not in levelDict:
                levelDict[i] = 1
            else:
                levelDict[i] += 1
                if levelDict[i] > level:
                    return i
        # 摩尔投票
        count = 0
        now = None
        max = len(nums) / 2
        for i in nums:
            if count == 0:
                now = i
                count = 1
            elif count > max:
                return now
            elif i == now:
                count += 1
            else:
                count -= 1
        return now


if __name__ == '__main__':
    print(Solution().majorityElement([1,2,1,2,1,2,1,2,1]))