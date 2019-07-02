package main

import (
	"container/list"
	"fmt"
)

func isValid(s string) bool {
	if s == "" {
		return true
	}
	stack := new(list.List)
	dict := map[string]string{")": "(", "}": "{", "]": "["}
	for _, i := range s {
		if dict[string(i)] == "" {
			stack.PushBack(string(i))
		} else if stack.Len() == 0 || stack.Back().Value != dict[string(i)] {
			return false
		} else {
			stack.Remove(stack.Back())
		}
	}
	return stack.Len() == 0
}

func main() {
	fmt.Println(isValid(""))
}
