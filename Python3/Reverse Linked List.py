"""
反转一个单链表
"""


"""
迭代方式
"""


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #变态写法
        p, temp = head, None
        while p:
            temp, temp.next, p = p, temp, p.next
        return temp
        # 一般写法
        if head == None or head.next == None:
            return head
        p, q, temp = head, head.next, None
        p.next = None
        while q:
            temp = q.next
            q.next = p
            q, p = temp, q
        return p


"""
递归方式 就是一步一步到倒数第二个节点 然后将倒数第一个的next修改为倒数第二个
"""


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        newHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newHead


