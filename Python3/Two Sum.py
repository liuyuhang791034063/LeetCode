# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       Two Sum
   Description:
   Author:           God
   date：            2018/9/19
-------------------------------------------------
   Change Activity:  2018/9/19
-------------------------------------------------
"""
__author__ = 'God'


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 获取nums长度
        n = len(nums)
        # 创建索引字典
        d = {}
        # 遍历nums，每一次将与遍历数符合的数存入字典
        for i in range(n):
            # 得到符合的数
            sb = target - nums[i]
            if nums[i] in d.keys():
                # 如果存在，说明可以组成组合
                return d[nums[i]], i
            else:
                # 不存在，加入
                d[sb] = i


if __name__ == '__main__':
    llist = [2, 7, 11, 15]
    s = Solution()
    print(s.twoSum(llist, 9))
