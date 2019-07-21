# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       Valid Parentheses
   Description:
   Author:           God
   date：            2018/12/20
-------------------------------------------------
   Change Activity:  2018/12/20
-------------------------------------------------
"""
__author__ = 'God'


# method 1
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mapper = {')': '(', '}': '{', ']': '['}
        stack = []
        for char in s:
            if char in mapper.values():
                stack.append(char)
            elif stack == [] or stack.pop() != mapper[char]:
                return False
        return not stack


# method 2
class stack(list):
    def peek(self):
        return self.__getitem__(self.__len__() - 1)


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == '':
            return True
        s1 = stack()
        for i in s:
            if len(s1) == 0:
                s1.append(i)
            elif self.compare(s1.peek(),i):
                s1.pop()
            else:
                s1.append(i)
        return len(s1) == 0

    def compare(self, c1, c2):
        return c1 == '{' and c2 == '}' or c1 == '[' and c2 == ']' or c1 == '(' and c2 == ')'