// 分割回文串
// medium
/*
* 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。
*
* 回文串 是正着读和反着读都一样的字符串。
*
* 示例 1：
*
* 输入：s = "aab"
* 输出：[["a","a","b"],["aa","b"]]
* 示例 2：
*
* 输入：s = "a"
* 输出：[["a"]]
*
*
* 提示：
*
* 1 <= s.length <= 16
* s 仅由小写英文字母组成
*
* 来源：力扣（LeetCode）
* 链接：https://leetcode-cn.com/problems/palindrome-partitioning
* 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*
* ------------------------------------------------
* 题解：动态规划 + 回溯
* 做一个表 g 记录 s[i:j+1] 是否为回文串，表示 g[i][j]，状态转移方程为 g[i][j] = s[i] == s[j] && g[i+1][j-1]。
* 有了这个表，就可以遍历 s，开始回溯输出答案。
 */

package main

import "fmt"

func main() {
	s := "cbbbccc"
	fmt.Println(partition(s))
}

func partition(s string) [][]string {
	n := len(s)
	g := make([][]bool, n)
	for i := range g {
		g[i] = make([]bool, n)
		for j := range g[i] {
			g[i][j] = true
		}
	}

	for i := n - 1; i >= 0; i-- {
		for j := i + 1; j < n; j++ {
			g[i][j] = s[i] == s[j] && g[i+1][j-1]
		}
	}

	ans := [][]string{}

	var backstrack func(i, j int, arr []string)
	backstrack = func(i, j int, arr []string) {
		if g[i][j] {
			tmp := append(arr, s[i:j+1])
			newarr := tmp[:len(tmp):len(tmp)] // append 如果没超过 arr 本身容量，那么就会和其他指针共享这块内存，导致不可预测的覆盖，所以截断下

			if j == n-1 {
				ans = append(ans, newarr)
			} else {
				backstrack(j+1, j+1, newarr)
			}
		}
		if j < n-1 {
			backstrack(i, j+1, arr)
		}
	}
	backstrack(0, 0, []string{})
	return ans
}
