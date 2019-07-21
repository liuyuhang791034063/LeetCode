package main

import "fmt"

// 最简单的查找
func lengthOfLongestSubstring(s string) int {
	res := 1
	if len(s) == 0 {
		return res
	}
	left, right := 0, 1
	for left < len(s) && right < len(s) {
		if findStringIndex(s[left:right], string(s[right])) == -1 {
			//fmt.Println(right)
			right++
			sum := right - left
			if sum > res {
				res = sum
			}
		} else {
			left++
			right = left + 1
		}
	}

	return res
}

func findStringIndex(s string, char string) int {
	for i := 0; i < len(s); i++ {
		if char == string(s[i]) {
			return i
		}
	}
	return -1
}

// 优化过后 相当于滑动窗口
func lengthOfLongestSubstring(s string) int {
	dict := make([]int, 128)
	res := 0
	for i, j := 0, 0; i < len(s) && j < len(s); j++ {
		if dict[s[j]] > i {
			i = dict[s[j]]
		}
		num := j - i + 1
		if num > res {
			res = num
		}
		dict[s[j]] = j + 1
	}
	return res
}

func main() {
	fmt.Println(lengthOfLongestSubstring("adawndiwnd"))
}
