# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       Remove Duplicates from Sorted List II
   Description:
   Author:           God
   date：            2018/9/26
-------------------------------------------------
   Change Activity:  2018/9/26
-------------------------------------------------
"""
__author__ = 'God'


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# class Solution(object):
#     def deleteDuplicates(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         # 顺序表
#         only_list = []
#         # 哈希表
#         only_dict = {}
#
#         # 新头节点
#         head2 = ListNode(0)
#         p = head2
#         while head:
#             if head.val in only_dict:
#                 only_dict[head.val] += 1
#             else:
#                 only_list.append(head.val)
#                 only_dict[head.val] = 1
#             head = head.next
#         for i in only_list:
#             if only_dict[i] == 1:
#                 new = ListNode(i)
#                 p.next = new
#                 p = p.next
#         return head2.next

# class Solution(object):
#     def deleteDuplicates(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         '''
#         双节点同时遍历，如果两个节点不同，且前节点没有被标记，即加入新链表
#         '''
#         # 新链表头节点
#         head2 = ListNode(0)
#         p = head2
#
#         # 标记列表
#         o_list = []
#         if head is None:
#             return head
#         if head.next is None:
#             return head
#
#         first, second = head, head.next
#
#         while second:
#             if first.val == second.val:
#                 o_list.append(first.val)
#             else:
#                 if first.val not in o_list:
#                     new = ListNode(first.val)
#                     p.next = new
#                     p = p.next
#                     if second.next is None:
#                         new = ListNode(second.val)
#                         p.next = new
#                         p = p.next
#                 else:
#                     if second.next is None:
#                         new = ListNode(second.val)
#                         p.next = new
#                         p = p.next
#             first, second = second, second.next
#         return head2.next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        head2 = ListNode(0)
        p = head2

        while head:
            if head.next and head.next.val == head.val:
                val = head.val
                while head and head.val == val:
                    head = head.next
                p.next = head
            else:
                p.next = head
                p = head
                head = head.next
        return head2.next

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
    head = getLineGraph([1,2,3,3,4,4,5])
    head2 = Solution().deleteDuplicates(head)