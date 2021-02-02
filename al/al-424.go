// 替换后的最长重复字符
// medium
/*
* 给你一个仅由大写英文字母组成的字符串，你可以将任意位置上的字符替换成另外的字符，总共可最多替换 k 次。在执行上述操作后，找到包含重复字母的最长子串的长度。
*
* 注意：字符串长度 和 k 不会超过 104。
*
*
* 示例 1：
*
* 输入：s = "ABAB", k = 2
* 输出：4
* 解释：用两个'A'替换为两个'B',反之亦然。
* 示例 2：
*
* 输入：s = "AABABBA", k = 1
* 输出：4
* 解释：
* 将中间的一个'A'替换为'B',字符串变为 "AABBBBA"。
* 子串 "BBBB" 有最长重复字母, 答案为 4。
*
* 来源：力扣（LeetCode）
* 链接：https://leetcode-cn.com/problems/longest-repeating-character-replacement
* 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*
* ---------------------------------------------------------
* 题解：滑动窗口
* 右指针向右移动，走过的字母分别计数，当不满足题意的时候左指针向右收敛，并且对应的字母计数 -1。
* 左指针向右收敛有个巧妙的方法，当右指针向右一步发现不满足题意的时候，左指针也向右只收敛一步即可，
* 一直不满足的话，左指针一直跟着右指针向右移动一步，这样能保证窗口持有最大长度，
* 窗口里其他字符比 k 多多少个其实对结果没有任何影响，窗口只在少于 k 时向右增长。
* 最终 s 总长度减去左指针位置即是答案。
*
 */

package main

import "fmt"

func main() {
	s := "AABABBA"
	fmt.Println(characterReplacement(s, 1))
}

func characterReplacement(s string, k int) int {
	left, maxCnt := 0, 0
	record := [26]int{}
	for right, ch := range s {
		record[ch-'A']++
		maxCnt = max(maxCnt, record[ch-'A'])
		if right-left+1-maxCnt > k {
			record[s[left]-'A']--
			left++
		}
	}
	return len(s) - left
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}
