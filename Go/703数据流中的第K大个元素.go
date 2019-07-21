package main

import (
	"container/heap"
	"fmt"
)

type KthLargest struct {
	minHeap []int
	nums    int
}

func (h KthLargest) Len() int {
	return len(h.minHeap)
}

func (h KthLargest) Less(i, j int) bool {
	return h.minHeap[i] < h.minHeap[j]
}

func (h *KthLargest) Swap(i, j int) {
	h.minHeap[i], h.minHeap[j] = h.minHeap[j], h.minHeap[i]
}

func (h *KthLargest) Pop() interface{} {
	old := h.minHeap
	n := len(old)
	x := old[n-1]
	h.minHeap = old[0 : n-1]
	return x
}

func (h *KthLargest) Push(x interface{}) {
	h.minHeap = append(h.minHeap, x.(int))
}

func Constructor(k int, nums []int) KthLargest {
	kl := KthLargest{nums: k}
	for _, i := range nums {
		kl.Add(i)
	}
	return kl
}

func (this *KthLargest) Add(val int) int {
	if this.Len() < this.nums {
		heap.Push(this, val)
	} else {
		temp := heap.Pop(this)
		if val > temp.(int) {
			heap.Push(this, val)
		} else {
			heap.Push(this, temp.(int))
		}
	}
	temp := heap.Pop(this)
	heap.Push(this, temp.(int))
	return temp.(int)
}

func main() {
	a := Constructor(3, []int{4, 5, 8, 2})
	fmt.Println(
		a.Add(3),
		a.Add(5),
		a.Add(10),
		a.Add(9),
		a.Add(4))
}
