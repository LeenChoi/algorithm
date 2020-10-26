// 有多少小于当前数字的数字
// easy
/*
* 给你一个数组 nums，对于其中每个元素 nums[i]，请你统计数组中比它小的所有数字的数目。
*
* 换而言之，对于每个 nums[i] 你必须计算出有效的 j 的数量，其中 j 满足 j != i 且 nums[j] < nums[i] 。
*
* 以数组形式返回答案。
*
*
*
* 示例 1：
*
* 输入：nums = [8,1,2,2,3]
* 输出：[4,0,1,1,3]
* 解释：
* 对于 nums[0]=8 存在四个比它小的数字：（1，2，2 和 3）。
* 对于 nums[1]=1 不存在比它小的数字。
* 对于 nums[2]=2 存在一个比它小的数字：（1）。
* 对于 nums[3]=2 存在一个比它小的数字：（1）。
* 对于 nums[4]=3 存在三个比它小的数字：（1，2 和 2）。
* 示例 2：
*
* 输入：nums = [6,5,4,8]
* 输出：[2,1,0,3]
* 示例 3：
*
* 输入：nums = [7,7,7,7]
* 输出：[0,0,0,0]
*
*
* 提示：
*
* 2 <= nums.length <= 500
* 0 <= nums[i] <= 100
*
* 来源：力扣（LeetCode）
* 链接：https://leetcode-cn.com/problems/how-many-numbers-are-smaller-than-the-current-number
* 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*
* ---------------------------------------------------
* 题解：排序，哈希表
* 一次排序，每个元素带着自己的下标，这样排序后的数组下标即是小于这个元素的个数，然后找他原来的下标，输出答案即可，
* 注意，如果有相同元素，需要特殊处理下，因为排序后的下标不同
*
* 哈希表方法是将每个元素出现的次数记录下来，然后对每个元素计算有多少个小于他的元素。因为条件给的元素最大不超过100
* 所以可以用长度为100的数组记录出现的次数，这样数组记录本身就是有序的了，然后遍历这个数字依次累加，就能得出每个元素的
* 小于他的元素个数，然后按照原始数组的排列顺序输出即可
*
 */

package main

import "fmt"

func main() {
	v := []int{8, 1, 2, 2, 3}
	fmt.Println(smallerNumbersThanCurrent(v))
}

func smallerNumbersThanCurrent(nums []int) []int {
	cnt := [101]int{}
	_max := 0
	for _, v := range nums {
		cnt[v]++
		if v > _max {
			_max = v
		}
	}
	for i := 1; i <= _max; i++ {
		cnt[i] += cnt[i-1]
	}
	ans := []int{}
	for _, v := range nums {
		if v > 0 {
			ans = append(ans, cnt[v-1])
		} else {
			ans = append(ans, 0)
		}
	}
	return ans
}
