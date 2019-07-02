package main

import "fmt"

/*
	双重循环的方法 最简单的方法
*/
//func twoSum(nums []int, target int) []int {
//	for i_index, i := range nums {
//		for j_index, j := range nums[i_index+1:] {
//			if i+j == target {
//				return []int{i_index, j_index+i_index+1}
//			}
//		}
//	}
//	return []int{}
//}

/*
	使用map存储遍历过的值和索引 如果减数存在于map中 返回索引数组
*/
func twoSum(nums []int, target int) []int {
	var ret []int
	m := make(map[int]int, len(nums))
	for k, v := range nums {
		if i, ok := m[target-v]; ok {
			ret = []int{k, i}
			break
		}
		m[v] = k
	}
	return ret
}

func main() {
	nums := []int{3, 2, 4}
	fmt.Println(twoSum(nums, 6))
}
