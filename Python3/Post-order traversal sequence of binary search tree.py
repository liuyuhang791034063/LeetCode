# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       Post-order traversal sequence of binary search tree
   Description:
   Author:           God
   date：            2018/10/9
-------------------------------------------------
   Change Activity:  2018/10/9
-------------------------------------------------
"""
__author__ = 'God'


# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        if sequence == []:
            return False
        if len(sequence) == 1 or len(sequence) == 2:
            return True
        else:
            root = sequence.pop(-1)
            sign = 0
            note = 0
            flag = 0
            for i in range(len(sequence)):
                if sign is 0 and sequence[i] > root:
                    note = i
                    sign = -1
                if sequence[i] > root:
                    sign = 1
                    flag += 1
                if (sign == 1) and (sequence[i] < root):
                    return False
            if sign is 0:
                note = i
            if flag == len(sequence):
                note = 1
            return self.VerifySquenceOfBST(sequence[:note]) and self.VerifySquenceOfBST(sequence[note:])


class Solution:
    def VerifySquenceOfBST(self, sequence):
        if sequence == []:
            return False
        if len(sequence) == 1 or len(sequence) == 2:
            return True
        else:
            root = sequence.pop(-1)
            sign = 0
            for i in range(len(sequence)):
                if sequence[i] > root:
                    sign = 1
                if (sign == 1) and (sequence[i] < root):
                    return False
            return self.VerifySquenceOfBST(sequence[:i]) and self.VerifySquenceOfBST(sequence[i:])


if __name__ == '__main__':
    print(Solution().VerifySquenceOfBST([5,4,3,2,1]))
