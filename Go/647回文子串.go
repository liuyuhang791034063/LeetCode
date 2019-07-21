package main

func countSubstrings(s string) int {
	res := 0
	for i := 0; i < len(s); i++ {
		res += testHui(s, i, i)
		res += testHui(s, i, i+1)
	}
	return res
}

func testHui(s string, start, end int) int {
	count := 0
	for start >= 0 && end < len(s) && s[start] == s[end] {
		count++
		start--
		end++
	}
	return count
}
