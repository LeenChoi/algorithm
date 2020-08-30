// 反转字符串中的单词 III
// easy
/*
* 给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。
*
* 示例：
*
* 输入："Let's take LeetCode contest"
* 输出："s'teL ekat edoCteeL tsetnoc"
*
*
* 提示：
*
* 在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。
*
* 来源：力扣（LeetCode）
* 链接：https://leetcode-cn.com/problems/reverse-words-in-a-string-iii
* 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

 */

package main

import "fmt"

func main() {
	ret := reverseWords("Let's take LeetCode contest")
	fmt.Println(ret)
}

func reverseWords(s string) string {
	begin := -1
	ret := []byte{}
	for i := range s {
		if s[i] == ' ' {
			tmp := convert(begin, i, s)
			ret = append(ret, tmp...)
			ret = append(ret, ' ')
			begin = i
		}
	}
	tmp := convert(begin, len(s), s)
	ret = append(ret, tmp...)
	return string(ret)
}

func convert(start, end int, s string) []byte {
	ret := []byte{}
	for i := end - 1; i > start; i-- {
		ret = append(ret, s[i])
	}
	return ret
}
