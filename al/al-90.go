// 子集 II
// medium
/*
* 给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。
*
* 解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。
*
* 示例 1：
*
* 输入：nums = [1,2,2]
* 输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]
*
* 示例 2：
*
* 输入：nums = [0]
* 输出：[[],[0]]
*
*
* 提示：
*
* 1 <= nums.length <= 10
* -10 <= nums[i] <= 10
*
* 来源：力扣（LeetCode）
* 链接：https://leetcode-cn.com/problems/subsets-ii
* 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*
* -----------------------------------------------------
* 题解：回溯 + 剪枝去重
*
* 因为要去重，[1,2,2] 里选择第一第二个数，和选择第一第三个数是同样的，需要去重掉。
* 那么首先就需要给数组排个序，让相同的数彼此挨着，然后回溯遍历这个数组。
*
* 回溯遍历过程分两步，一是不选择当前数字，二是选择。选择当前数之前需要判下前一个数有没有选择，如果没选择说明不想要那个数，
* 那么如果当前数和上一个数相等，同样也不要这个数，跳过，这就是剪枝去重的过程。
*
 */

package main

import (
	"fmt"
	"sort"
)

func main() {
	nums := []int{1, 2, 2}
	fmt.Println(subsetsWithDup(nums))
}

func subsetsWithDup(nums []int) [][]int {
	ans := [][]int{}
	t := []int{}
	sort.Slice(nums, func(i, j int) bool { return nums[i] < nums[j] })

	var backstrack func(choosed bool, cur int)
	backstrack = func(choosed bool, cur int) {
		if cur >= len(nums) {
			tmp := append([]int{}, t...)
			ans = append(ans, tmp)
			return
		}
		// 不选当前数直接跳过
		backstrack(false, cur+1)

		// 选当前数之前判下，前一次有没有选，如果没选表明前一个数是不想选的
		// 那么如果当前数和前一个数相等，同样不选，跳过
		if !choosed && cur > 0 && nums[cur-1] == nums[cur] {
			return
		}
		t = append(t, nums[cur])
		backstrack(true, cur+1)
		// 记得回溯
		t = t[:len(t)-1]
	}
	backstrack(false, 0)
	return ans
}
