// 132模式
// medium
/*
* 给定一个整数序列：a1, a2, ..., an，一个132模式的子序列 ai, aj, ak 被定义为：当 i < j < k 时，ai < ak < aj。设计一个算法，当给定有 n 个数字的序列时，验证这个序列中是否含有132模式的子序列。
*
* 注意：n 的值小于15000。
*
* 示例1:
*
* 输入: [1, 2, 3, 4]
*
* 输出: False
*
* 解释: 序列中不存在132模式的子序列。
* 示例 2:
*
* 输入: [3, 1, 4, 2]
*
* 输出: True
*
* 解释: 序列中有 1 个132模式的子序列： [1, 4, 2].
* 示例 3:
*
* 输入: [-1, 3, 2, 0]
*
* 输出: True
*
* 解释: 序列中有 3 个132模式的的子序列: [-1, 3, 2], [-1, 3, 0] 和 [-1, 2, 0].
*
* 来源：力扣（LeetCode）
* 链接：https://leetcode-cn.com/problems/132-pattern
* 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*
* ---------------------------------------------------------------------
* 题解：前缀最小 + 栈
* 朴素想法 i，j，k 挨个遍历找符合题意的 132 子序列，但需要 On3 复杂度，不可取。
* 因为只需要找出来是否有 132 子序列，而不是一一列出，所以只要找到一个保证比 j 小的 i 即可，所以先做一个前缀最小队列 min[],
* 这样通过查 min[j] 直接能找到小于 nums[j] 的数。
*
* 那么 k 怎么找？k 要满足大于 min[j] (即 nums[i])，且小于 nums[j]。
*
* 做一个栈，nums 从右往左遍历，将 num 压栈，栈内元素是要从上到下单调递增的，也就是说栈顶元素是最小。
* 遍历 nums 的时候，当前 num 如果小于已入栈的栈顶，那么当前 num 直接压栈，
* 表明当前 num 往后的数(即栈顶) 比它大，不可能构成 132 子序列，
*
* 如果 num 比栈顶大，说明有可能构成 132 子序列，这时需要判断下当前 num 和他的 min 是否相等，相等就跳过，
* 如果不相等则需要将栈顶和 min 做个比较，如果栈顶大于 min 说明 132 成立，返回 true，
* 如果栈顶小于 min，那就成了 231 不满足，需要出栈，看看往后有没有能满足 132 的元素，因为栈内是单调递增的，所以后面的数都要比当前的栈顶大。
* 如果后续的栈内元素都出栈了或者栈顶比 num 大了，说明当前 num 后续的数中都没有满足 132 的数，那么 nums 继续向前遍历，重复上述过程即可，
* 无需将出栈过的数重新入栈，因为在刚才的 num 这个位置，这些入栈的数不成立，那么对于前面的 nums 这些肯定还不成立。
*
* 出栈的数都是比 min 大的，因为是前缀最小，所以当前 num 之前的所有 nums 他们的 min 只能大于等于当前 num 的 min，
* 所以出栈的这些数，同样对于前面的那些 nums 是不能够成立 132 结构的。
*
* 出栈后继续上述循环即可，结果 nums 都遍历完都没有找到 132 的话，则返回 false
*
 */

package main

import (
	"fmt"
	"math"
)

func main() {
	nums := []int{3, 5, 0, 3, 4}
	fmt.Println(find132pattern(nums))
}

func find132pattern(nums []int) bool {
	min := math.MaxInt64
	minArr := make([]int, len(nums))
	for i := 0; i < len(nums); i++ {
		if nums[i] < min {
			min = nums[i]
		}
		minArr[i] = min
	}

	stack := []int{}
	for i := len(nums) - 1; i >= 0; i-- {
		if len(stack) == 0 || stack[len(stack)-1] > nums[i] {
			stack = append(stack, nums[i])
		} else if stack[len(stack)-1] < nums[i] {
			if nums[i] == minArr[i] {
				continue
			}
			if stack[len(stack)-1] <= minArr[i] {
				stack = stack[:len(stack)-1]
				i++
			} else if stack[len(stack)-1] > minArr[i] {
				return true
			}
		}
	}
	return false
}
