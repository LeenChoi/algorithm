// 不同的子序列
// hard
/*
* 给定一个字符串 s 和一个字符串 t ，计算在 s 的子序列中 t 出现的个数。
*
* 字符串的一个 子序列 是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。（例如，"ACE" 是 "ABCDE" 的一个子序列，而 "AEC" 不是）
*
* 题目数据保证答案符合 32 位带符号整数范围。
*
*
* 示例 1：
*
* 输入：s = "rabbbit", t = "rabbit"
* 输出：3
* 解释：
* 如下图所示, 有 3 种可以从 s 中得到 "rabbit" 的方案。
* (上箭头符号 ^ 表示选取的字母)
* rabbbit
* ^^^^ ^^
* rabbbit
* ^^ ^^^^
* rabbbit
* ^^^ ^^^
* 示例 2：
*
* 输入：s = "babgbag", t = "bag"
* 输出：5
* 解释：
* 如下图所示, 有 5 种可以从 s 中得到 "bag" 的方案。
* (上箭头符号 ^ 表示选取的字母)
* babgbag
* ^^ ^
* babgbag
* ^^    ^
* babgbag
* ^    ^^
* babgbag
*   ^  ^^
* babgbag
*     ^^^
*
*
* 提示：
*
* 0 <= s.length, t.length <= 1000
* s 和 t 由英文字母组成
*
* 来源：力扣（LeetCode）
* 链接：https://leetcode-cn.com/problems/distinct-subsequences
* 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*
* -----------------------------------------------------------
* 题解：动态规划
*
* 设 dp[i][j] 记录 s[i:] 子串的子序列里能匹配多少个 t[j:] 子串，那么：
* 当 s[i] == t[j] 时，分两种情况
* 1. 如果 s[i] 和 t[j] 能匹配上，dp[i][j] = dp[i+1][j+1]
* 2. 如果 s[i] 和 t[j] 不匹配，比如上面例子的 s: rabbbit  t: rabbit，虽然都是 'b' 相同，但如果 s 后面的两个 'b'
*                                             ^           ^
* 	和 t 的两个 'b' 已经匹配过，那么这次的就不能再匹配。所以此时的 dp[i][j] 应该等于 dp[i+1][j]
* 上两种匹配情况叠加就是 dp[i][j] 的值，即 dp[i+i][j] + dp[i+1][j+1]
*
* 当 s[i] != t[j] 时，和上面的第二种情况一样，dp[i][j] = dp[i+1][j]
*
* 所以状态转移方程为:  s[i] == t[j] => dp[i][j] = dp[i+i][j] + dp[i+1][j+1]
* 				  s[i] != t[j] => dp[i][j] = dp[i+i][j]
*
* 注意：因为空字符串也是子串，也能匹配，所以初始化 dp 时要考虑进去，要默认 1
* 即  for i in 0 ~ len(s) : dp[i][len(t)] = 1
*
 */

package main

import "fmt"

func main() {
	s := "babgbag"
	t := "bag"
	fmt.Println(numDistinct(s, t))
}

func numDistinct(s string, t string) int {
	m, n := len(s), len(t)
	dp := make([][]int, m+1)
	for i := range dp {
		dp[i] = make([]int, n+1)
	}
	for i := 0; i <= m; i++ {
		dp[i][n] = 1
	}
	for i := m - 1; i >= 0; i-- {
		for j := n - 1; j >= 0; j-- {
			if s[i] == t[j] {
				dp[i][j] = dp[i+1][j+1] + dp[i+1][j]
			} else {
				dp[i][j] = dp[i+1][j]
			}
		}
	}
	return dp[0][0]
}
