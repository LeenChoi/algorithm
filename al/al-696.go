// 计数二进制子串
// easy

/*
给定一个字符串 s，计算具有相同数量0和1的非空(连续)子字符串的数量，并且这些子字符串中的所有0和所有1都是组合在一起的。

重复出现的子串要计算它们出现的次数。

示例 1 :
输入: "00110011"
输出: 6
解释: 有6个子串具有相同数量的连续1和0：“0011”，“01”，“1100”，“10”，“0011” 和 “01”。

请注意，一些重复出现的子串要计算它们出现的次数。

另外，“00110011”不是有效的子串，因为所有的0（和1）没有组合在一起。

示例 2 :

输入: "10101"
输出: 4
解释: 有4个子串：“10”，“01”，“10”，“01”，它们具有相同数量的连续1和0。
注意：

s.length 在1到50,000之间。
s 只包含“0”或“1”字符。

--------------------------------------------------
题解:
计算 '0' 或 '1' 的个数，"00110011" 做个 [2,2,2,2] 数组，然后这个数组的没两厢的 min值就是他们能构成的最多对数

*/

package main

import "fmt"

func main() {
	fmt.Printf("%d\n", countBinarySubstrings("00110011"))
}

func countBinarySubstrings(s string) int {
	counts := []int{}
	ans, count := 0, 0
	ptr := 0
	var cur rune
	for _, ch := range s {
		if cur == 0 || cur != ch {
			if cur != 0 {
				counts = append(counts, count)
				if ptr-1 >= 0 {
					ans += min(counts[ptr-1], counts[ptr])
				}
				ptr++
			}
			cur = ch
			count = 0
		}
		count++
	}
	counts = append(counts, count)
	if ptr-1 >= 0 {
		ans += min(counts[ptr-1], counts[ptr])
	}
	return ans
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
