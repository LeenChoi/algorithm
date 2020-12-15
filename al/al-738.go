// 单调递增的数字
// medium
/*
* 给定一个非负整数 N，找出小于或等于 N 的最大的整数，同时这个整数需要满足其各个位数上的数字是单调递增。
*
* （当且仅当每个相邻位数上的数字 x 和 y 满足 x <= y 时，我们称这个整数是单调递增的。）
*
* 示例 1:
*
* 输入: N = 10
* 输出: 9
* 示例 2:
*
* 输入: N = 1234
* 输出: 1234
* 示例 3:
*
* 输入: N = 332
* 输出: 299
* 说明: N 是在 [0, 10^9] 范围内的一个整数。
*
* 来源：力扣（LeetCode）
* 链接：https://leetcode-cn.com/problems/monotone-increasing-digits
* 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*
* ----------------------------------------------------------------
* 题解：贪心
* 首先将数字转成数组方便遍历，然后按位比较，找到后一位比前一位小的位。然后再倒序遍历回来，判断当前位是否小于前一位，
* 是就将前一位 -1，直到找到当前位大于前一位的那一位。之后再正序遍历回去，将后面的每一位都置成 9。
*
 */

package main

import (
	"fmt"
	"strconv"
)

func main() {
	fmt.Println(monotoneIncreasingDigits(332))
}

func monotoneIncreasingDigits(N int) int {
	s := []byte(strconv.Itoa(N))
	i := 1
	for i < len(s) && s[i] >= s[i-1] {
		i++
	}
	if i < len(s) {
		for i-1 >= 0 && s[i] < s[i-1] {
			s[i-1]--
			i--
		}
		for i++; i < len(s); i++ {
			s[i] = '9'
		}
	}
	ans, _ := strconv.Atoi(string(s))
	return ans
}
