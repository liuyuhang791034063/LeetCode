# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       Flip word sequence column
   Description:
   Author:           God
   date：            2018/10/30
-------------------------------------------------
   Change Activity:  2018/10/30
-------------------------------------------------
"""
__author__ = 'God'


class Solution:
    def ReverseSentence(self, s):
        return ' '.join(s.split(' ')[::-1])


if __name__ == '__main__':
    print(Solution().ReverseSentence('student. a am I'))