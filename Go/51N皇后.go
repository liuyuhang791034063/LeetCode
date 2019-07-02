package main

import "fmt"

var number int
var result_queue []int
var resutl [][]string

func solveNQueens(n int) [][]string {
	number = n
	result_queue = make([]int, n)
	resutl = make([][]string, 0)
	for i := 0; i < number; i++ {
		result_queue[i] = -1
	}
	fun(0)
	fmt.Println(resutl)
	return resutl
}

func fun(row int) {
	if row == number {
		makeResult()
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

func makeResult() {

	var str []string
	for i := 0; i < number; i++ {
		var s string
		for j := 0; j < number; j++ {
			if result_queue[i] == j {
				s += "Q"
			} else {
				s += "."
			}
		}
		str = append(str, s)
	}
	resutl = append(resutl, str)
}

func main() {
	solveNQueens(1)
}
