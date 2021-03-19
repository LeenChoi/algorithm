// 数组中重复的数据
// medium
/*
* 给定一个整数数组 a，其中1 ≤ a[i] ≤ n （n为数组长度）, 其中有些元素出现两次而其他元素出现一次。
*
* 找到所有出现两次的元素。
*
* 你可以不用到任何额外空间并在O(n)时间复杂度内解决这个问题吗？
*
* 示例：
*
* 输入:
* [4,3,2,7,8,2,3,1]
*
* 输出:
* [2,3]
*
* 来源：力扣（LeetCode）
* 链接：https://leetcode-cn.com/problems/find-all-duplicates-in-an-array
* 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*
* ----------------------------------------------------
* 题解：
* 首先我是对号入座的方法去弄的，因为 a[i] 是 1 ~ n 的，不会超过数组长度值，所以遍历一遍数组，当前数 num 移到它对应的
* 索引位置 num-1，与其数做替换。反复做替换，直到正确的值被替换到当前索引位，或者当前数与它对应位置的数重复了。
* 整个替换一遍后，输出下标和其数不一样的元素就ok。
*
* 但是上述方法不是严格的 O(n)
*
* 标记法可以在严格的 O(n) 内做出来。具体做法是遍历数组，把当前数对应索引位的数字取负数，表示当前数已经访问过，
* 当标记到某个索引位时如果这位索引上的数是负数，那么表示该索引对应的数字 index+1 重复了，直接输出即可
*
 */

package main

import "fmt"

func main() {
	nums := []int{4, 3, 2, 7, 8, 2, 3, 1}
	fmt.Println(findDuplicates2(nums))
}

func findDuplicates(nums []int) []int {
	for i := 0; i < len(nums); {
		if nums[i] == i+1 {
			i++
			continue
		}

		num := nums[i]
		if nums[i] == nums[num-1] {
			i++
			continue
		}
		nums[i], nums[num-1] = nums[num-1], nums[i]
	}

	ans := []int{}
	for i := range nums {
		if nums[i] != i+1 {
			ans = append(ans, nums[i])
		}
	}
	return ans
}

func findDuplicates2(nums []int) []int {
	ans := []int{}
	for _, num := range nums {
		num = abs(num)
		if nums[num-1] > 0 {
			nums[num-1] = -nums[num]
		} else {
			ans = append(ans, num)
		}
	}
	return ans
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}
