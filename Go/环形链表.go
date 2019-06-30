package main

type ListNode struct {
	Val  int
	Next *ListNode
}

// 快慢指针法
func hasCycle(head *ListNode) bool {
	if head == nil {
		return false
	}
	quick, slow := head.Next, head
	for quick != nil && slow != nil && quick.Next != nil {
		if quick == slow {
			return true
		}
		quick = quick.Next.Next
		slow = slow.Next
	}
	return false
}

// map法
func hasCycle(head *ListNode) bool {
	dict := make(map[*ListNode]int)
	for {
		if head == nil {
			return false
		}
		if dict[head] != 0 {
			return true
		} else {
			dict[head] = head.Val
		}
		head = head.Next
	}
}

func main() {
	test := &ListNode{Val: 1}
	hasCycle(test)
}
