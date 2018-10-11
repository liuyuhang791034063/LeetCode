# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       Push-in, pop-up sequence of the stack
   Description:
   Author:           God
   date：            2018/10/11
-------------------------------------------------
   Change Activity:  2018/10/11
-------------------------------------------------
"""
__author__ = 'God'


class Solution:
    def IsPopOrder(self, pushV, popV):
        if len(pushV) is 0:
            return False
        j = 0
        stack = list()
        for i in pushV:
            stack.append(i)
            while j < len(popV) and popV[j] == stack[-1]:
                stack.pop()
                j += 1
        if len(stack) is 0:
            return True
        return False


if __name__ == '__main__':
    print(Solution().IsPopOrder([1,2,3,4,5],[4,5,3,2,1]))