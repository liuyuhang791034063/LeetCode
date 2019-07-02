package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

// 快慢指针法
func detectCycle(head *ListNode) *ListNode {
	if head == nil {
		return nil
	}
	quick, slow := head.Next, head
	for quick != nil && slow != nil && quick.Next != nil {
		if quick == slow {
			return quick
		}
		quick = quick.Next.Next
		slow = slow.Next
	}
	return nil
}

// map法
func detectCycle(head *ListNode) *ListNode {
	dict := make(map[*ListNode]int)
	for {
		if head == nil {
			return nil
		}
		if dict[head] != 0 {
			break
		} else {
			dict[head] = head.Val
		}
		head = head.Next
	}
	return head
}

func main() {
	test := &ListNode{Val: 1, Next: &ListNode{Val: 1}}
	fmt.Println(detectCycle(test))
}
