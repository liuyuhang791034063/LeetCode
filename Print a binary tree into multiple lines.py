# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       Print a binary tree into multiple lines
   Description:
   Author:           God
   date：            2018/11/9
-------------------------------------------------
   Change Activity:  2018/11/9
-------------------------------------------------
"""
__author__ = 'God'


class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        if not pRoot:
            return []
        res, l = [], []
        l.append(pRoot)
        while l:
            temp = []
            ress = []
            l.reverse()
            while l:
                temp.append(l.pop())
            for i in temp:
                ress.append(i.val)
                if i.left:
                    l.append(i.left)
                if i.right:
                    l.append(i.right)
            res.append(ress)
        return res