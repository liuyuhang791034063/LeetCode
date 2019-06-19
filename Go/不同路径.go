package main

import (
	"fmt"
	"math"
	"time"
)

/*
	经典的动态规划 dp[i][j] = dp[i-1][j] + dp[i][j-1]
*/
func uniquePaths(m int, n int) int {
	var dp [101][101]int
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if i == 0 || j == 0 {
				dp[i][j] = 1
			} else {
				dp[i][j] = dp[i-1][j] + dp[i][j-1]
			}
		}
	}
	return dp[m-1][n-1]
}

func rec_opt(arr []int, i int) int {
	if i == 0 {
		return arr[0]
	} else if i == 1 {
		return int(math.Max(float64(arr[0]), float64(arr[1])))
	} else {
		return int(math.Max(float64(rec_opt(arr, i-2)+arr[i]), float64(rec_opt(arr, i-1))))
	}
}

func dp_opt(arr []int) int {
	opt := arr
	for i := 2; i < len(arr); i++ {
		opt[i] = int(math.Max(float64(opt[i-2]+arr[i]), float64(opt[i-1])))
	}
	return opt[len(arr)-1]
}

func main() {
	fmt.Println(uniquePaths(3, 2))
	fmt.Println(rec_opt([]int{1, 2, 4, 1, 7, 8, 3}, 6))
	fmt.Println(time.Now())
	fmt.Println("Spend time is ")
	fmt.Println(time.Now())
	fmt.Println(time.Now())
	fmt.Println(dp_opt([]int{1, 2, 4, 1, 7, 8, 3}))
	fmt.Println(time.Now())
}
