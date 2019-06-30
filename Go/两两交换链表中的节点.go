package main

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func swapPairs(head *ListNode) *ListNode {
	pre := &ListNode{}
	res := pre
	pre.Next = head
	for pre.Next != nil && pre.Next.Next != nil {
		a := pre.Next
		b := pre.Next.Next
		pre.Next, b.Next, a.Next = b, a, b.Next
		pre = a
	}
	return res.Next
}
