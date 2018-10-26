# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       Reverse order in array
   Description:
   Author:           God
   date：            2018/10/25
-------------------------------------------------
   Change Activity:  2018/10/25
-------------------------------------------------
"""
from functools import reduce

__author__ = 'God'


class Solution:
    def InversePairs(self, data):
        return self.sort(data[:], 0, len(data)-1, data[:]) % 1000000007

    def sort(self, temp, left, right, data):
        if right - left < 1:
            return 0
        if right - left == 1:
            if data[left] < data[right]:
                return 0
            else:
                temp[left], temp[right] = data[right], data[left]
                return 1
        mid = (left + right) // 2
        res = self.sort(data, left, mid, temp) + self.sort(data, mid+1, right, temp)

        i = left
        j = mid + 1
        index = left

        while i <= mid and j <= right:
            if data[i] <= data[j]:
                temp[index] = data[i]
                i += 1
            else:
                temp[index] = data[j]
                res += mid - i + 1
                j += 1
            index += 1
        while i <= mid:
            temp[index] = data[i]
            i += 1
            index += 1
        while j <= right:
            temp[index] = data[j]
            j += 1
            index += 1
        return res


# 超时
class Solution1:
    def InversePairs(self, data):
        Sortdata = self.quick_sort(data)
        res = 0
        for i in Sortdata:
            res += data.index(i)
            data.pop(data.index(i))
        return res

    def quick_sort(self, data):
        if len(data) < 2:
            return data
        left = self.quick_sort([i for i in data[1:] if i <= data[0]])
        right = self.quick_sort([j for j in data[1:] if j > data[0]])
        return left + [data[0]] + right


if __name__ == '__main__':
    print(Solution1().InversePairs([1,2,3,4,5,6,7,0]))
