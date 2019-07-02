package main

import (
	"container/list"
	"fmt"
)

type MyQueue struct {
	input  list.List
	output list.List
}

/** Initialize your data structure here. */
func Constructor() MyQueue {
	return MyQueue{}
}

/** Push element x to the back of queue. */
func (this *MyQueue) Push(x int) {
	this.input.PushBack(x)
}

/** Removes the element from in front of queue and returns that element. */
func (this *MyQueue) Pop() int {
	if this.output.Len() == 0 {
		for this.input.Len() != 0 {
			this.output.PushBack(this.input.Back().Value)
			this.input.Remove(this.input.Back())
		}
	}
	res := this.output.Back()
	this.output.Remove(res)
	return res.Value.(int)
}

/** Get the front element. */
func (this *MyQueue) Peek() int {
	if this.output.Len() == 0 {
		for this.input.Len() != 0 {
			this.output.PushBack(this.input.Back().Value)
			this.input.Remove(this.input.Back())
		}
	}
	return this.output.Back().Value.(int)
}

/** Returns whether the queue is empty. */
func (this *MyQueue) Empty() bool {
	if this.output.Len() == 0 && this.input.Len() == 0 {
		return true
	}
	return false
}

func main() {
	obj := Constructor()
	obj.Push(1)
	fmt.Println(obj.Peek())
	fmt.Println(obj.Pop())
	fmt.Println(obj.Empty())
}
