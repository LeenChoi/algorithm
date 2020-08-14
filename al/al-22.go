// 括号生成
// medium
/*
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

示例：

输入：n = 3
输出：[
       "((()))",
       "(()())",
       "(())()",
       "()(())",
       "()()()"
     ]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/generate-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

-------------------------------------
题解：递归回溯
先说暴力思路，暴力解法是可劲儿先填 “(” 然后再填 “)”, 判断填满后的字符串是否有效，然后输出到结果集
回溯解法是把暴力解法中无脑顺序填 "("，")" 的过程剪枝，把无效的递归删掉

具体剪枝判断就是，"(" 的个数不能超过 n 个，")" 的个数不能超过 "("，顺序填充"(", ")" 只要满足这个条件，那么最终一定是有效串
然后递归就可以了，递归过程自动就规避了无效串的递归，从而实现剪枝回溯

*/

package main

import (
	"fmt"
	"strings"
)

func generateParenthesis(n int) []string {
	stack, ans := []string{}, []string{}
	return recursion(stack, ans, 0, 0, n)
}

func recursion(stack, ans []string, left, right, n int) []string {
	if len(stack) == 2*n {
		s := strings.Join(stack, "")
		ans = append(ans, s)
		return ans
	}
	if left < n {
		newStack := append(stack, "(")
		ans = recursion(newStack, ans, left+1, right, n)
	}
	if right < left {
		newStack := append(stack, ")")
		ans = recursion(newStack, ans, left, right+1, n)
	}
	return ans
}

func main() {
	ans := generateParenthesis(3)
	fmt.Printf("%q\n", ans)
}
