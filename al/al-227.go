// 基本计算器 II
// medium
/*
* 给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。
*
* 整数除法仅保留整数部分。
*
* 示例 1：
*
* 输入：s = "3+2*2"
* 输出：7
* 示例 2：
*
* 输入：s = " 3/2 "
* 输出：1
* 示例 3：
*
* 输入：s = " 3+5 / 2 "
* 输出：5
*
*
* 提示：
*
* 1 <= s.length <= 3 * 105
* s 由整数和算符 ('+', '-', '*', '/') 组成，中间由一些空格隔开
* s 表示一个 有效表达式
* 表达式中的所有整数都是非负整数，且在范围 [0, 231 - 1] 内
* 题目数据保证答案是一个 32-bit 整数
*
* 来源：力扣（LeetCode）
* 链接：https://leetcode-cn.com/problems/basic-calculator-ii
* 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*
* -----------------------------------------------
* 题解：栈
* 做一个栈，将每次遍历到的数计算后直接入栈，如果数字前的符号是 '+' 那么直接入栈，如果是 '-' 取反后入栈，
* 如果是 '*' '/' 那么就将此数字和栈顶的数字计算后重新入栈。
*
* 最后栈内数字全部累加即可。
*
 */

package main

import "fmt"

func main() {
	s := "1*2-3/4+5*6-7*8+9/10"
	fmt.Println(calculate2(s))
}

func calculate(s string) int {
	ops := []int{}
	n := len(s)
	num := 0
	for i := 0; i < n; {
		if s[i] == ' ' {
			i++
		} else if s[i] == '+' || s[i] == '-' || s[i] == '*' || s[i] == '/' {
			if len(ops) > 0 {
				operate := ops[len(ops)-1]
				if operate == 3 || operate == 4 {
					tmp := ops[len(ops)-2]
					ops = ops[:len(ops)-2]
					num = calc(tmp, num, operate)
				}
			}
			if s[i] == '+' {
				ops = append(ops, num, 1)
			} else if s[i] == '-' {
				ops = append(ops, num, 2)
			} else if s[i] == '*' {
				ops = append(ops, num, 3)
			} else {
				ops = append(ops, num, 4)
			}
			i++
		} else {
			num = 0
			for ; i < n && s[i] >= '0' && s[i] <= '9'; i++ {
				num = num*10 + int(s[i]-'0')
			}
		}
	}
	if len(ops) > 0 {
		operate := ops[len(ops)-1]
		if operate == 3 || operate == 4 {
			ops = ops[:len(ops)-1]
			ops[len(ops)-1] = calc(ops[len(ops)-1], num, operate)
		} else {
			ops = append(ops, num)
		}
		ans := ops[0]
		fmt.Println(ops)
		for i := 1; i < len(ops); i += 2 {
			ans = calc(ans, ops[i+1], ops[i])
		}
		num = ans
	}

	return num
}

func calc(x, y int, oper int) int {
	ans := 0
	switch oper {
	case 1:
		ans = x + y
	case 2:
		ans = x - y
	case 3:
		ans = x * y
	case 4:
		ans = x / y
	}
	return ans
}

// 官方
func calculate2(s string) int {
	stack := []int{}
	n := len(s)
	preSign := byte('+')
	num := 0
	for i := 0; i < n; {
		if s[i] == ' ' {
			i++
			continue
		}
		for ; i < n && s[i] >= '0' && s[i] <= '9'; i++ {
			num = num*10 + int(s[i]-'0')
		}
		switch preSign {
		case '+':
			stack = append(stack, num)
		case '-':
			stack = append(stack, -num)
		case '*':
			stack[len(stack)-1] = stack[len(stack)-1] * num
		case '/':
			stack[len(stack)-1] = stack[len(stack)-1] / num
		}
		if i < n {
			preSign = s[i]
		}
		num = 0
		i++
	}
	ans := 0
	for _, v := range stack {
		ans += v
	}
	return ans
}
