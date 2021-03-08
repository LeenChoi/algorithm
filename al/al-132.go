// 分割回文串 II
// hard
/*
* 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是回文。
*
* 返回符合要求的 最少分割次数 。
*
* 示例 1：
*
* 输入：s = "aab"
* 输出：1
* 解释：只需一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。
* 示例 2：
*
* 输入：s = "a"
* 输出：0
* 示例 3：
*
* 输入：s = "ab"
* 输出：1
*
*
* 提示：
*
* 1 <= s.length <= 2000
* s 仅由小写英文字母组成
*
* 来源：力扣（LeetCode）
* 链接：https://leetcode-cn.com/problems/palindrome-partitioning-ii
* 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*
* ------------------------------------------------------------
* 题解: 动态规划
* 设 f[i] 为 s 0~i 切割回文串的最少次数，那么当 s[i] ~ s[j] 为回文串时，有状态转移方程 f[j] = min(f[j], f[i] + 1)
* 现只要能拿到 s[i:j+1] 是否为回文串的判断即可。
*
* 有个预处理方法，设 g[i][j] 表示 s[i:j+1] 是否为回文串，那么有状态转移方程 g[i][j] = s[i] == s[j] && g[i+1][j-1]，
* 可将 s 遍历一遍，做一个初始化表 g，然后上述第一个的 dp 过程中，找 s[i:j+1] 是否为回文串，可在 O(1) 内返回。
*
* 最后，输出 f[n-1] 即可。
*
 */

package main

import (
	"fmt"
	"math"
)

func main() {
	s := "aab"
	fmt.Println(minCut(s))
}

func minCut(s string) int {
	n := len(s)
	g := make([][]bool, n)
	for i := range g {
		g[i] = make([]bool, n)
		for j := range g[i] {
			g[i][j] = true // 初始为 true，方便后面的状态转移
		}
	}
	for i := n - 1; i >= 0; i-- {
		for j := i + 1; j < n; j++ {
			g[i][j] = s[i] == s[j] && g[i+1][j-1]
		}
	}

	f := make([]int, n)
	for j := 0; j < n; j++ {
		if g[0][j] { // 如果整块是回文，不用切
			continue
		}
		f[j] = math.MaxInt64
		for i := 0; i < j; i++ {
			if g[i+1][j] && f[i]+1 < f[j] {
				f[j] = f[i] + 1
			}
		}
	}
	return f[n-1]
}
