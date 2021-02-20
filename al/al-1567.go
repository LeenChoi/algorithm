// 乘积为正数的最长子数组长度
// medium
/*
* 给你一个整数数组 nums ，请你求出乘积为正数的最长子数组的长度。
*
* 一个数组的子数组是由原数组中零个或者更多个连续数字组成的数组。
*
* 请你返回乘积为正数的最长子数组长度。
*
* 示例  1：
*
* 输入：nums = [1,-2,-3,4]
* 输出：4
* 解释：数组本身乘积就是正数，值为 24 。
* 示例 2：
*
* 输入：nums = [0,1,-2,-3,-4]
* 输出：3
* 解释：最长乘积为正数的子数组为 [1,-2,-3] ，乘积为 6 。
* 注意，我们不能把 0 也包括到子数组中，因为这样乘积为 0 ，不是正数。
* 示例 3：
*
* 输入：nums = [-1,-2,-3,0,1]
* 输出：2
* 解释：乘积为正数的最长子数组是 [-1,-2] 或者 [-2,-3] 。
* 示例 4：
*
* 输入：nums = [-1,2]
* 输出：1
* 示例 5：
*
* 输入：nums = [1,2,3,5,-6,4,0,10]
* 输出：4
*
*
* 提示：
*
* 1 <= nums.length <= 10^5
* -10^9 <= nums[i] <= 10^9
*
* 来源：力扣（LeetCode）
* 链接：https://leetcode-cn.com/problems/maximum-length-of-subarray-with-positive-product
* 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*
* ------------------------------------------------
* 题解：贪心，动态规划
* 此题题解是动态规划，标签写着贪心，我试着贪心去做，但不知是否是贪心
* 做 l, r 指针，r 向右一直走，直到碰到 0，或者队列的尾停下，r 移动的同时维护着[l, r]子串的乘积的正负号，以及为正数的最长长度 len
* 当 r 停下后，l 开始向右收敛，找出或许以 r 为结尾的子串中存在最长子串，像 [-1,1,1,1,1,1] 这种, 直到 r - l < len。
*
* 有一个可以确定的是，最长子串不可能出现在 (l, r) 内，只能是以 l 或 r 为边界的子串，可以反证，
* 如果 [l, r] 内的某个子串 [k, t] 是最长子串，那么 k-1 位置和 t+1 位置一定是负数，那么[k, t]就不是最长子串，
* 应该是 [k-1, t+1]，与上述发生矛盾。
*
* 按上述步骤，l 收敛完，如果 r 的位置现在是 0，那么 r 跳过 0，重复上述过程，如果 r 是队列尾，那么跳出循环，结束。
*
 */

package main

import "fmt"

func main() {
	// nums := []int{1, -2, -3, 4}
	nums := []int{0, 1, -2, -3, -4}
	// nums := []int{-1, -2, -3, 0, 1}
	// nums := []int{1, 2, 3, 5, -6, 4, 0, 10}
	// nums := []int{-1, 2}
	fmt.Println(getMaxLen(nums))
}

func getMaxLen(nums []int) int {
	cnt := 0
	l, r := 0, 0
	flag := 1
	direction := 1
	for r <= len(nums) {
		if direction == 1 {
			if r == len(nums) || nums[r] == 0 {
				direction = 0
				continue
			}
			if nums[r] < 0 {
				flag = -flag
			}
			if flag > 0 {
				cnt = max(cnt, r-l+1)
			}
			r++
		} else {
			if r-l <= cnt {
				flag = 1
				direction = 1
				r++
				l = r
				continue
			}
			if nums[l] < 0 {
				flag = -flag
			}
			if flag > 0 {
				cnt = max(cnt, r-l-1)
			}
			l++
		}
	}
	return cnt
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}
