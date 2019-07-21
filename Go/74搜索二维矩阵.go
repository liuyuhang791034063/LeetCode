package main

import "fmt"

func searchMatrix(matrix [][]int, target int) bool {
	if len(matrix) == 0 {
		return false
	}
	m := len(matrix)
	n := len(matrix[0])
	i, j := 0, m*n-1
	mid := (i + j) / 2
	for i <= j {
		mid = (i + j) / 2
		if matrix[mid/n][mid%n] == target {
			return true
		} else if matrix[mid/n][mid%n] > target {
			j = mid - 1
		} else {
			i = mid + 1
		}
	}
	return false
}

func main() {
	fmt.Println(1 / 2)
}
