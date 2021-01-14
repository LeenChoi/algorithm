// 可被 5 整除的二进制前缀
// easy
/*
* 给定由若干 0 和 1 组成的数组 A。我们定义 N_i：从 A[0] 到 A[i] 的第 i 个子数组被解释为一个二进制数（从最高有效位到最低有效位）。
*
* 返回布尔值列表 answer，只有当 N_i 可以被 5 整除时，答案 answer[i] 为 true，否则为 false。
*
*
*
* 示例 1：
*
* 输入：[0,1,1]
* 输出：[true,false,false]
* 解释：
* 输入数字为 0, 01, 011；也就是十进制中的 0, 1, 3 。只有第一个数可以被 5 整除，因此 answer[0] 为真。
* 示例 2：
*
* 输入：[1,1,1]
* 输出：[false,false,false]
* 示例 3：
*
* 输入：[0,1,1,1,1,1]
* 输出：[true,false,false,false,true,false]
* 示例 4：
*
* 输入：[1,1,1,0,1]
* 输出：[false,false,false,false,false]
*
*
* 提示：
*
* 1 <= A.length <= 30000
* A[i] 为 0 或 1
*
* 来源：力扣（LeetCode）
* 链接：https://leetcode-cn.com/problems/binary-prefix-divisible-by-5
* 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*
* ---------------------------------------------------------------
* 题解：
* 从最高位开始，减 101，余数加到下一轮计算，如果到某个位，最终结果为0，那么从开始到这个位置的二进制数就是能被 5(101) 整除。
* 模拟这个过程即可，我是按位遍历将数组转成了 10 进制整数，然后与 5 相减。
*
 */

package main

import "fmt"

func main() {
	// A := []int{0, 1, 1, 1, 1, 1}
	// A := []int{1, 0, 0, 1, 0, 1}
	A := []int{1, 1, 0, 1, 1, 1}
	fmt.Println(prefixesDivBy5(A))
}

func prefixesDivBy5(A []int) []bool {
	sum := 0
	ans := make([]bool, len(A))
	for i := range A {
		sum = sum*2 + A[i]
		fmt.Println(sum)
		if sum >= 5 {
			sum -= 5
		}
		if sum == 0 {
			ans[i] = true
		}
	}
	return ans
}
