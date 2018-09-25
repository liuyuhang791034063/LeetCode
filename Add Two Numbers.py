# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       Add Two Numbers
   Description:
   Author:           God
   date：            2018/9/19
-------------------------------------------------
   Change Activity:  2018/9/19
-------------------------------------------------
"""
__author__ = 'God'


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 方法一
# class Solution:
#     def getNum(self, testList):
#         """
#         :type testList: list
#         """
#         try:
#             num = testList.pop(0)
#         except IndexError:
#             num = 0
#         return num
#
#     def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         '''
#         遍历链表，把数存在列表，然后列表操作之后再创建新链表
#         '''
#         list1 = []
#         list2 = []
#         list3 = []
#         while l1:
#             list1.append(l1.val)
#             l1 = l1.next
#         while l2:
#             list2.append(l2.val)
#             l2 = l2.next
#
#         n1 = self.getNum(list1)
#         n2 = self.getNum(list2)
#         n3 = 0
#         while True:
#             if n1+n2+n3 > 9:
#                 list3.append((n1+n2+n3) % 10)
#                 n3 = 1
#             else:
#                 list3.append(n1+n2+n3)
#                 n3 = 0
#             if list1.__len__() is 0 and list2.__len__() is 0:
#                 if n3 is 1:
#                     list3.append(1)
#                 break
#             n1 = self.getNum(list1)
#             n2 = self.getNum(list2)
#
#         n = len(list3)
#         for i in range(n):
#             if i == 0:
#                 h3 = ListNode(list3[i])
#                 l3 = h3
#             else:
#                 l3.next = ListNode(list3[i])
#                 l3 = l3.next
#         l3.next = None
#         return h3

# 方法二
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 两种特殊情况
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        head = ListNode(0)
        l = head
        carry = 0
        # 当两个链表为空并且无进位，则退出循环
        while l1 or l2 or carry:
            # 每次循环开始，将进位给sum，并且进位清零
            sum, carry = carry, 0
            if l1 is not None:
                sum += l1.val
                l1 = l1.next
            if l2 is not None:
                sum += l2.val
                l2 = l2.next
            # 如果sum大于9，则进位
            if sum > 9:
                carry = 1
                sum -= 10
            # 创建新节点
            l.next = ListNode(sum)
            l = l.next
        return head


# list获取链表
def getLineGraph(list):
    n = len(list)
    for i in range(n):
        if i == 0:
            head = ListNode(list[i])
            t = head
        else:
            t.next = ListNode(list[i])
            t = t.next
    return head


if __name__ == '__main__':
    list1 = [1]
    list2 = [9, 9]
    l1 = getLineGraph(list1)
    l2 = getLineGraph(list2)
    t = Solution()
    l3 = t.addTwoNumbers(l1, l2)
    while l3:
        print(l3.val)
        l3 = l3.next