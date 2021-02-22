// Z 字形变换
// medium
/*
* 将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。
*
* 比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：
*
* P   A   H   N
* A P L S I I G
* Y   I   R
* 之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。
*
* 请你实现这个将字符串进行指定行数变换的函数：
*
* string convert(string s, int numRows);
*
*
* 示例 1：
*
* 输入：s = "PAYPALISHIRING", numRows = 3
* 输出："PAHNAPLSIIGYIR"
* 示例 2：
* 输入：s = "PAYPALISHIRING", numRows = 4
* 输出："PINALSIGYAHRPI"
* 解释：
* P     I    N
* A   L S  I G
* Y A   H R
* P     I
* 示例 3：
*
* 输入：s = "A", numRows = 1
* 输出："A"
*
*
* 提示：
*
* 1 <= s.length <= 1000
* s 由英文字母（小写和大写）、',' 和 '.' 组成
* 1 <= numRows <= 1000
*
*
* 来源：力扣（LeetCode）
* 链接：https://leetcode-cn.com/problems/zigzag-conversion
* 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*
* --------------------------------------------------------
* 题解：
* Z字排列后的字符串，每个字符和原字符串是有对应关系的，通过对应关系按规则直接构造结果队列即可。
* 关系就是，Z字排列后，可以将结果队列分成 n 列组合，每列组合是 |/ 型，这样的话原队列分成 numRows 行新队列，
* 可以分成每组 zLen = numRows + (numRows - 2) 的 n 个组合，然后按行构造结果队列就ok。
*
 */

package main

import "fmt"

func main() {
	s := "PAYPALISHIRING"
	numRows := 1
	fmt.Println(convert(s, numRows))
}

func convert(s string, numRows int) string {
	ans := []uint8{}
	zLen := numRows + (numRows - 2)
	if numRows == 1 {
		zLen = 1
	}
	for i := 0; i < numRows; i++ {
		j := i
		for j < len(s) {
			ans = append(ans, s[j])
			if i > 0 && i < numRows-1 {
				ori := j - (j % zLen)
				neighbor := ori + zLen - i
				if neighbor < len(s) {
					ans = append(ans, s[neighbor])
				}
			}
			j += zLen
		}
	}
	return string(ans)
}
