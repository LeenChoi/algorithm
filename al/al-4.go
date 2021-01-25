// 寻找两个正序数组的中位数
// hard
/*
* 给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的中位数。
*
* 进阶：你能设计一个时间复杂度为 O(log (m+n)) 的算法解决此问题吗？
*
* 示例 1：
*
* 输入：nums1 = [1,3], nums2 = [2]
* 输出：2.00000
* 解释：合并数组 = [1,2,3] ，中位数 2
* 示例 2：
*
* 输入：nums1 = [1,2], nums2 = [3,4]
* 输出：2.50000
* 解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
* 示例 3：
*
* 输入：nums1 = [0,0], nums2 = [0,0]
* 输出：0.00000
* 示例 4：
*
* 输入：nums1 = [], nums2 = [1]
* 输出：1.00000
* 示例 5：
*
* 输入：nums1 = [2], nums2 = []
* 输出：2.00000
*
*
* 提示：
*
* nums1.length == m
* nums2.length == n
* 0 <= m <= 1000
* 0 <= n <= 1000
* 1 <= m + n <= 2000
* -106 <= nums1[i], nums2[i] <= 106
*
* 来源：力扣（LeetCode）
* 链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays
* 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*
* -----------------------------------------------------------------
* 题解：二分查找
* 此题可以看做两段数组合成后第 k = length / 2 大的数。两数组做归并然后直接就能找到这个第 k 数，但是复杂度要 O(m+n)
* 题目要求用 O(log(m+n)) 那就需要二分法了。
* 此题二分法的做法是，在两数组分别记一个指针，然后如果找第 k 个数，那么两数组指针分别往前走 k/2-1 步，判断此时两元素的值，
* 小的那一数组，指针走过的元素可以排除掉了，更新它的指针到新的位置，然后 k 减去已走过的步数，再继续上述操作。
*
* 这是什么过程？
* 比如，我想找第 6 个数，当指针走到 A[1], B[1] 位置的时候，如果A[1] 比 B[1] 小，那么他一定比 A[2], B[2] 更小
* 那么 A 的这部分可以排除掉了，因为这些数肯定比第 k 数小，然后从各自的指针位置，再走剩余的步数，最后剩余 1 步的时候
* 判断 A，B 里的俩数谁更小即可。
*
* 举个例子
*
* A: 1 3 4 9
* B: 1 2 3 4 5 6 7 8 9
* 长度 13，k = 7
*
* 先走 k/2 = 3 步，走到 k/2-1 = 2 的位置，即 A[2], B[2]
* A: 1 3 4 9
* 	   |
* B: 1 2 3 4 5 6 7 8 9
* 	   |
*
* B 更小，排除 B，更新 k 为 k - k/2 = 4，指针各自从各自位置向前走 k/2 = 2 步，
* A: 1 3 4 9
* 	 |
* B:[1 2 3]4 5 6 7 8 9
* 		   |
*
* A 更小，排除 A，更新 k 为 k - k/2 = 2, 指针各自走 k/2 = 1步
* A:[1 3]4 9
* 	   |
* B:[1 2 3]4 5 6 7 8 9
* 		 |
*
* A,B 相同，此时订个规则相同情况排除 A 即可, k 更新为 k - k/2 = 1, k == 1 时判断直接输出两者更小者
* A:[1 3 4]9
* 	   	 |
* B:[1 2 3]4 5 6 7 8 9
* 		 |
*
* B 更小，所以第 k 数为 B[3] = 4
*
 */

package main

import "fmt"

func main() {
	nums1 := []int{1, 3, 4}
	nums2 := []int{2}
	fmt.Println(findMedianSortedArrays(nums1, nums2))
}

func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
	length := len(nums1) + len(nums2)
	if length%2 == 1 {
		return float64(getKthMinNum(nums1, nums2, length/2+1)) // +1 是表示第k个数，length /2 得出来的实际是下标值
	} else {
		return (float64(getKthMinNum(nums1, nums2, length/2)) + float64(getKthMinNum(nums1, nums2, length/2+1))) / 2.0
	}
}

func getKthMinNum(nums1, nums2 []int, k int) int {
	index1, index2 := 0, 0
	for {
		if index1 == len(nums1) {
			return nums2[index2+k-1]
		}
		if index2 == len(nums2) {
			return nums1[index1+k-1]
		}
		if k == 1 {
			return min(nums1[index1], nums2[index2])
		}
		step := k / 2
		step1 := min(step, len(nums1)-index1)
		step2 := min(step, len(nums2)-index2)
		if nums1[index1+step1-1] <= nums2[index2+step2-1] {
			index1 += step1
			k = k - step1
		} else {
			index2 += step2
			k = k - step2
		}
	}
}

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}
