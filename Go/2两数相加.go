package main

import "container/list"

type ListNode struct {
	Val  int
	Next *ListNode
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	carry := 0
	res := &ListNode{}
	cur := res
	var x, y int
	for l1 != nil || l2 != nil {
		if l1 != nil {
			x = l1.Val
		} else {
			x = 0
		}
		if l2 != nil {
			y = l2.Val
		} else {
			y = 0
		}
		sum := carry + x + y
		carry = sum / 10
		cur.Next = &ListNode{Val: sum % 10}
		cur = cur.Next
		if l1 != nil {
			l1 = l1.Next
		}
		if l2 != nil {
			l2 = l2.Next
		}

	}
	if carry > 0 {
		cur.Next = &ListNode{Val: carry}
	}
	return res.Next
}
