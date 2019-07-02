package main

type ListNode struct {
	Val  int
	Next *ListNode
}

// 非递归版
func reverseList(head *ListNode) *ListNode {
	var cur, prev *ListNode
	cur = head
	for cur != nil {
		cur.Next, prev, cur = prev, cur, cur.Next
	}
	return prev
}

// 递归版
func reverseList(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}
	node := reverseList(head.Next)
	head.Next.Next = head
	head.Next = nil

	return node
}

func main() {

}
