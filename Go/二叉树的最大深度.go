package main

import (
	"container/list"
	"fmt"
	"math"
)

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

/*
	递归方法 求出左子树和右子树中的最大值 再加1
*/
//func maxDepth(root *TreeNode) int {
//	if root == nil {
//		return 0
//	} else {
//		return int(math.Max(float64(maxDepth(root.Left)), float64(maxDepth(root.Right))) + 1)
//	}
//}

/*
	迭代方法 使用栈 每次弹出父节点和高度 并且存入子节点和高度
*/
type MaxNode struct {
	Level int
	Node  *TreeNode
}

func maxDepth(root *TreeNode) int {
	stack := list.New()
	depth := 0
	if root == nil {
		return depth
	}
	stack.PushBack(MaxNode{1, root})
	for stack.Len() != 0 {
		f := stack.Back()
		stack.Remove(f)
		curr, p := f.Value.(MaxNode).Level, f.Value.(MaxNode).Node
		depth = int(math.Max(float64(depth), float64(curr)))
		if p.Left != nil {
			stack.PushBack(MaxNode{curr + 1, p.Left})
		}
		if p.Right != nil {
			stack.PushBack(MaxNode{curr + 1, p.Right})
		}
	}
	return depth
}

func main() {
	temp := TreeNode{Val: 1, Left: nil, Right: nil}
	fmt.Println(maxDepth(&temp))
}
