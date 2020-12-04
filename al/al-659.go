// 分割数组为连续子序列
// medium
/*
* 给你一个按升序排序的整数数组 num（可能包含重复数字），请你将它们分割成一个或多个子序列，其中每个子序列都由连续整数组成且长度至少为 3 。
*
* 如果可以完成上述分割，则返回 true ；否则，返回 false 。
*
* 示例 1：
*
* 输入: [1,2,3,3,4,5]
* 输出: True
* 解释:
* 你可以分割出这样两个连续子序列 :
* 1, 2, 3
* 3, 4, 5
*
*
* 示例 2：
*
* 输入: [1,2,3,3,4,4,5,5]
* 输出: True
* 解释:
* 你可以分割出这样两个连续子序列 :
* 1, 2, 3, 4, 5
* 3, 4, 5
*
*
* 示例 3：
*
* 输入: [1,2,3,4,4,5]
* 输出: False
*
*
* 提示：
*
* 输入的数组长度范围为 [1, 10000]
*
* 来源：力扣（LeetCode）
* 链接：https://leetcode-cn.com/problems/split-array-into-consecutive-subsequences
* 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*
* ------------------------------------------------------
* 题解：贪心
* 此题给的用例都是升序的连续的数字，不是单纯升序排序的，所以利用这个条件展开思路，我知道当前 v 就能得到 v+1 和 v+2，
* 因为是连续的，只要这俩数在数组里就一定能得到。现需要两个map，一个(countMap)用来记录给每个数字计数，因为会有重复，
* 一个(endMap)用来记录以当前数字结尾的有效的子序列有多少个。
*
* 有了这两个map后，只需从头遍历nums，判断当前 num 的前一个数 num-1是否有以它为结尾的子序列，即查endMap[num-1]是否大于0。
*
* 1.如果有，那么就贪心的把当前 num 加到这个子序列的后面，所以endMap[num-1]要 -1，
* 因为这个子序列现在是以 num 结尾的，然后endMap[num] +1，同时因为用了当前num，所以countMap[num] -1。
*
* 2.如果没有，那么需要判断 countMap[num+1], countMap[num+2] 是否大于0，即是否有后两个数，有的话就贪心的与当前数组成新的子序列，
* 同时更新各位的 countMap状态和结尾的 endMap状态
*
* 3.如果上两个都不满足，那么就return false
*
* 注意：遍历nums的时候需要先判下当前num的countMap记录是否大于0，因为在第2判断会超前消费两个数，会改变他们的countMap状态
*
* 此题的关键在于是分成子序列而不是子串，我可以提前消费后面的某个数，这就是贪心所在，通过countMap先把一个序列分出来，即判断2
* 我不需要知道某个数在后面的哪个位置出现，我只需知道这个数在数组里存在就ok了。
*
 */

package main

import "fmt"

func main() {
	para := []int{1, 2, 3, 3, 4, 4, 5, 5}
	fmt.Println(isPossible(para))
}

func isPossible(nums []int) bool {
	countMap := map[int]int{}
	for _, v := range nums {
		countMap[v] += 1
	}
	endMap := map[int]int{}
	for _, v := range nums {
		if countMap[v] == 0 {
			continue
		}
		if endMap[v-1] > 0 {
			endMap[v] += 1
			endMap[v-1] -= 1
			countMap[v] -= 1
		} else if countMap[v+1] > 0 && countMap[v+2] > 0 {
			countMap[v] -= 1
			countMap[v+1] -= 1
			countMap[v+2] -= 1
			endMap[v+2] += 1
		} else {
			return false
		}
	}
	return true
}
