# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       Print binary trees in zigzag order
   Description:
   Author:           God
   date：            2018/11/9
-------------------------------------------------
   Change Activity:  2018/11/9
-------------------------------------------------
"""

__author__ = 'God'


class Solution:
    def Print(self, pRoot):
        if not pRoot:
            return []
        res = []
        que = []
        que.append(pRoot)
        node = 0
        while que:
            l = []
            res_res = []
            node += 1
            if node % 2 == 1:
                while que:
                    l.append(que.pop())
                for i in l:
                    res_res.append(i.val)
                    if i.left:
                        que.append(i.left)
                    if i.right:
                        que.append(i.right)
            else:
                while que:
                    l.append(que.pop())
                for i in l:
                    res_res.append(i.val)
                    if i.right:
                        que.append(i.right)
                    if i.left:
                        que.append(i.left)
            res.append(res_res)
        return res


