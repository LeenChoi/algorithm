// 最长湍流子数组
// medium
/*
* 当 A 的子数组 A[i], A[i+1], ..., A[j] 满足下列条件时，我们称其为湍流子数组：
*
* 若 i <= k < j，当 k 为奇数时， A[k] > A[k+1]，且当 k 为偶数时，A[k] < A[k+1]；
* 或 若 i <= k < j，当 k 为偶数时，A[k] > A[k+1] ，且当 k 为奇数时， A[k] < A[k+1]。
* 也就是说，如果比较符号在子数组中的每个相邻元素对之间翻转，则该子数组是湍流子数组。
*
* 返回 A 的最大湍流子数组的长度。
*
*
*
* 示例 1：
*
* 输入：[9,4,2,10,7,8,8,1,9]
* 输出：5
* 解释：(A[1] > A[2] < A[3] > A[4] < A[5])
* 示例 2：
*
* 输入：[4,8,12,16]
* 输出：2
* 示例 3：
*
* 输入：[100]
* 输出：1
*
*
* 提示：
*
* 1 <= A.length <= 40000
* 0 <= A[i] <= 10^9
*
* 来源：力扣（LeetCode）
* 链接：https://leetcode-cn.com/problems/longest-turbulent-subarray
* 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*
* -----------------------------------------------------------
* 题解：滑动窗口
* 直接上滑动窗口，套 l, r 指针，判断前后元素相减后的符号，如果相反则 r 继续前进，如果相同则 l = r - 1，
* 如果前后元素相同，无法产生波浪，这时 l = r 即可。
*
 */

package main

import "fmt"

func main() {
	arr := []int{9, 4, 2, 10, 7, 8, 8, 1, 9}
	fmt.Println(maxTurbulenceSize(arr))
}

func maxTurbulenceSize(arr []int) int {
	l := 0
	ans := 1
	flag := -1
	for r := 1; r < len(arr); r++ {
		if arr[r]-arr[r-1] < 0 {
			if flag == 0 {
				l = r - 1
			}
			ans = max(ans, r-l+1)
			flag = 0
		} else if arr[r]-arr[r-1] > 0 {
			if flag == 1 {
				l = r - 1
			}
			ans = max(ans, r-l+1)
			flag = 1
		} else {
			l = r
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
