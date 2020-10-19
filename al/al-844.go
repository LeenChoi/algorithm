// 比较含退格的字符串
// easy
/*
* 给定 S 和 T 两个字符串，当它们分别被输入到空白的文本编辑器后，判断二者是否相等，并返回结果。 # 代表退格字符。
*
* 注意：如果对空文本输入退格字符，文本继续为空。
*
* 示例 1：
*
* 输入：S = "ab#c", T = "ad#c"
* 输出：true
* 解释：S 和 T 都会变成 “ac”。
* 示例 2：
*
* 输入：S = "ab##", T = "c#d#"
* 输出：true
* 解释：S 和 T 都会变成 “”。
* 示例 3：
*
* 输入：S = "a##c", T = "#a#c"
* 输出：true
* 解释：S 和 T 都会变成 “c”。
* 示例 4：
*
* 输入：S = "a#c", T = "b"
* 输出：false
* 解释：S 会变成 “c”，但 T 仍然是 “b”。
*
*
* 提示：
*
* 1 <= S.length <= 200
* 1 <= T.length <= 200
* S 和 T 只含有小写字母以及字符 '#'。
*
* 来源：力扣（LeetCode）
* 链接：https://leetcode-cn.com/problems/backspace-string-compare
* 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*
* ------------------------------------------------------
* 题解：从后往前遍历 双指针
* 俩字符串，从后往前遍历，如果遇到'#'则记一下退格步数，然后指针往前移动。如果不是'#'，那么看下退格步数是否有剩余，再前移
* 最终定格到某个字符后，比较俩字符串的当前字符是否相等，若相等则继续上一步，不相等则返回false，最终判断俩指针是否都 < 0 即可
*
 */

package main

import "fmt"

func main() {
	// S := "ab##"
	// T := "c#d#"
	S := "ab#b#c"
	T := "aa#b##c"
	flag := backspaceCompare(S, T)
	fmt.Println(flag)
}

func backspaceCompare(S string, T string) bool {
	i, j := len(S)-1, len(T)-1
	stepi, stepj := 0, 0
	for {
		for i >= 0 {
			if S[i] == '#' {
				stepi += 1
				i -= 1
			} else if stepi > 0 {
				stepi -= 1
				i -= 1
			} else {
				break
			}
		}

		for j >= 0 {
			if T[j] == '#' {
				stepj += 1
				j -= 1
			} else if stepj > 0 {
				stepj -= 1
				j -= 1
			} else {
				break
			}
		}
		if i < 0 && j >= 0 || i >= 0 && j < 0 {
			return false
		} else if i < 0 && j < 0 {
			return true
		}
		if S[i] == T[j] {
			i -= 1
			j -= 1
			continue
		}
		return false
	}
}
