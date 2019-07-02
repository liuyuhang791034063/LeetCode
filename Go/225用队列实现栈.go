package main

import (
	"container/list"
	"fmt"
)

type MyStack struct {
	list list.List
}

/** Initialize your data structure here. */
func Constructor() MyStack {
	return MyStack{}
}

/** Push element x onto stack. */
func (this *MyStack) Push(x int) {
	this.list.PushBack(x)
}

/** Removes the element on top of the stack and returns that element. */
func (this *MyStack) Pop() int {
	if this.list.Len() != 1 {
		for i := 0; i < this.list.Len()-1; i++ {
			temp := this.list.Front()
			this.list.Remove(temp)
			this.list.PushBack(temp.Value)
		}
	}
	res := this.list.Front()
	this.list.Remove(res)
	return res.Value.(int)
}

/** Get the top element. */
func (this *MyStack) Top() int {
	if this.list.Len() != 1 {
		for i := 0; i < this.list.Len()-1; i++ {
			temp := this.list.Front()
			this.list.Remove(temp)
			this.list.PushBack(temp.Value)
		}
	}
	res := this.list.Front()
	this.list.Remove(res)
	this.list.PushBack(res.Value)
	return res.Value.(int)
}

/** Returns whether the stack is empty. */
func (this *MyStack) Empty() bool {
	if this.list.Len() == 0 {
		return true
	} else {
		return false
	}
}

func main() {
	stack := Constructor()
	fmt.Println(stack)
}
