// 检查一个字符串是否可以打破另一个字符串
// medium
/*
* 给你两个字符串 s1 和 s2 ，它们长度相等，请你检查是否存在一个 s1  的排列可以打破 s2 的一个排列，或者是否存在一个 s2 的排列可以打破 s1 的一个排列。
*
* 字符串 x 可以打破字符串 y （两者长度都为 n ）需满足对于所有 i（在 0 到 n - 1 之间）都有 x[i] >= y[i]（字典序意义下的顺序）。
*
* 示例 1：
*
* 输入：s1 = "abc", s2 = "xya"
* 输出：true
* 解释："ayx" 是 s2="xya" 的一个排列，"abc" 是字符串 s1="abc" 的一个排列，且 "ayx" 可以打破 "abc" 。
* 示例 2：
*
* 输入：s1 = "abe", s2 = "acd"
* 输出：false
* 解释：s1="abe" 的所有排列包括："abe"，"aeb"，"bae"，"bea"，"eab" 和 "eba" ，s2="acd" 的所有排列包括："acd"，"adc"，"cad"，"cda"，"dac" 和 "dca"。然而没有任何 s1 的排列可以打破 s2 的排列。也没有 s2 的排列能打破 s1 的排列。
* 示例 3：
*
* 输入：s1 = "leetcodee", s2 = "interview"
* 输出：true
*
*
* 提示：
*
* s1.length == n
* s2.length == n
* 1 <= n <= 10^5
* 所有字符串都只包含小写英文字母。
*
* 来源：力扣（LeetCode）
* 链接：https://leetcode-cn.com/problems/check-if-a-string-can-break-another-string
* 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*
* ------------------------------------------------------------------
* 题解：贪心
* 两个字符串排个序，然后再逐位比较打破，很简单的题。
*
* 官方标签给的贪心算法，不知怎么贪心了。。。 可能不需要考虑全排列，直接字符从小到大逐个比较是贪心过程？
*
 */

package main

import (
	"fmt"
	"sort"
)

func main() {
	fmt.Println(checkIfCanBreak("leetcodee", "interview"))
}

func checkIfCanBreak(s1 string, s2 string) bool {
	rs1, rs2 := []rune(s1), []rune(s2)
	sort.Slice(rs1, func(i, j int) bool { return rs1[i] < rs1[j] })
	sort.Slice(rs2, func(i, j int) bool { return rs2[i] < rs2[j] })
	flag := 0
	for i := 0; i < len(rs1); i++ {
		if rs1[i] < rs2[i] {
			if flag == 0 {
				flag = 1
			} else if flag == 2 {
				return false
			}
		} else if rs1[i] > rs2[i] {
			if flag == 0 {
				flag = 2
			} else if flag == 1 {
				return false
			}
		}
	}
	return true
}
