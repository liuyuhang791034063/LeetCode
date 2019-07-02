package main

import "fmt"

var result int
var number int
var result_queue []int

func totalNQueens(n int) int {
	number = n
	result = 0
	result_queue = make([]int, n)
	for i := 0; i < number; i++ {
		result_queue[i] = -1
	}
	fun(0)
	return result
}

func fun(row int) {
	if row == number {
		result++
		return

	}
	for i := 0; i < number; i++ {
		if isOk(row, i) {
			result_queue[row] = i
			fun(row + 1)
		}
	}
}

func isOk(row, column int) bool {
	left, right := column-1, column+1
	for i := row - 1; i >= 0; i-- {
		if result_queue[i] == column {
			return false
		}
		if left >= 0 {
			if result_queue[i] == left {
				return false
			}
		}
		if right < number {
			if result_queue[i] == right {
				return false
			}
		}
		left--
		right++
	}
	return true
}

func main() {
	fmt.Println(totalNQueens(1))
}
