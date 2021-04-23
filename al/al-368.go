// 最大整除子集
/*
* 给你一个由 无重复 正整数组成的集合 nums ，请你找出并返回其中最大的整除子集 answer ，子集中每一元素对 (answer[i], answer[j]) 都应当满足：
* answer[i] % answer[j] == 0 ，或
* answer[j] % answer[i] == 0
* 如果存在多个有效解子集，返回其中任何一个均可。
*
*
*
* 示例 1：
*
* 输入：nums = [1,2,3]
* 输出：[1,2]
* 解释：[1,3] 也会被视为正确答案。
* 示例 2：
*
* 输入：nums = [1,2,4,8]
* 输出：[1,2,4,8]
*
*
* 提示：
*
* 1 <= nums.length <= 1000
* 1 <= nums[i] <= 2 * 109
* nums 中的所有整数 互不相同
*
* 来源：力扣（LeetCode）
* 链接：https://leetcode-cn.com/problems/largest-divisible-subset
* 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*
* -------------------------------------------------------------
* 题解：动态规划
*
* 假设 dp[i] 表示包含当前 nums[i] 的最大整数子集的长度，即这个子集必须是以 nums[i] 为最大整数的子集。所以每一项 dp 值默认为 1。
* 状态转移方程为，当遍历到 nums[i] 时，每一个 nums[j] (j: 0 ~ i-1)，若能整除掉 nums[i], 那么 dp[i] 的值可以更新为
* dp[j] + 1 和 dp[i] 本身两者最大值。
*
* 得到 dp 数组的同时需要记录下最大子集长度 maxSize，需要反向找到拥有最长子集的那个 nums[i]，然后从这个整数开始倒推最长子集数组。
* 倒推的步骤为，首先通过 maxSize 找到nums[i]，将nums[i] 输出到结果集，然后 maxSize - 1，继续找 maxSize 对应的下一个 nums[i]。
* 注意，此时的 nums[i] 需要判断下能否整除上一个nums[i]。
*
* 有个简便的方法就是，记一个 maxVal，初始为 0，然后每次通过 maxSize 找 nums[i] 时，同时判断 maxVal % nums[i] == 0
*
 */

package main

import (
	"fmt"
	"sort"
)

func main() {
	nums := []int{2, 4, 7, 8, 9, 12, 16, 20}
	fmt.Println(largestDivisibleSubset(nums))
}

func largestDivisibleSubset(nums []int) []int {
	dp := make([]int, len(nums))
	for i := range dp {
		dp[i] = 1
	}

	maxSize := 1
	sort.Slice(nums, func(i, j int) bool { return nums[i] < nums[j] })
	for i := 1; i < len(nums); i++ {
		for j := 0; j < i; j++ {
			if nums[i]%nums[j] == 0 {
				dp[i] = max(dp[i], dp[j]+1)
				maxSize = max(maxSize, dp[i])
			}
		}
	}

	maxVal := 0
	ans := []int{}
	for i := len(nums) - 1; i >= 0; i-- {
		if dp[i] == maxSize && maxVal%nums[i] == 0 {
			ans = append(ans, nums[i])
			maxVal = nums[i]
			maxSize--
		}
	}

	return ans
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}
