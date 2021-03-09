// 最大正方形
// medium
/*
* 在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。
*
* 示例 1：
*
* 	1	0	1	0	0
*
* 	1	0  [1	1]	1
*
* 	1	1  [1	1]	1
*
* 	1	0	0	1	0
*
* 输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
* 输出：4
*
* 示例 2：
*
* 	0  [1]
*
*  [1]  0
*
*
* 输入：matrix = [["0","1"],["1","0"]]
* 输出：1
*
* 示例 3：
*
* 输入：matrix = [["0"]]
* 输出：0
*
*
* 提示：
*
* m == matrix.length
* n == matrix[i].length
* 1 <= m, n <= 300
* matrix[i][j] 为 '0' 或 '1'
*
* 来源：力扣（LeetCode）
* 链接：https://leetcode-cn.com/problems/maximal-square
* 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*
* -----------------------------------------------------------------------
* 题解：动态规划
* 找好关系就ok，记录一个当前元素左边连续 1 的长度和上面连续 1 的长度，还有自己能构成正方形的最大边长。
* 状态转移时，自己的两个臂和左上元素的正方形边长做比较，得出自己能构成正方形的最长边长。
* 最后，所有元素中最长的正方形即可
*
 */

package main

import "fmt"

func main() {
	// matrix := [][]byte{[]byte{'1', '0', '1', '0', '0'}, []byte{'1', '0', '1', '1', '1'}, []byte{'1', '1', '1', '1', '1'}, []byte{'1', '0', '0', '1', '0'}}
	// matrix := [][]byte{[]byte{'1'}}
	// matrix := [][]byte{[]byte{'1', '0', '1', '0'}, []byte{'1', '0', '1', '1'}, []byte{'1', '0', '1', '1'}, []byte{'1', '1', '1', '1'}}
	matrix := [][]byte{[]byte{'1', '0', '1', '0', '0', '1', '1', '1', '0'}, []byte{'1', '1', '1', '0', '0', '0', '0', '0', '1'}, []byte{'0', '0', '1', '1', '0', '0', '0', '1', '1'}, []byte{'0', '1', '1', '0', '0', '1', '0', '0', '1'}, []byte{'1', '1', '0', '1', '1', '0', '0', '1', '0'}, []byte{'0', '1', '1', '1', '1', '1', '1', '0', '1'}, []byte{'1', '0', '1', '1', '1', '0', '0', '1', '0'}, []byte{'1', '1', '1', '0', '1', '0', '0', '0', '1'}, []byte{'0', '1', '1', '1', '1', '0', '0', '1', '0'}, []byte{'1', '0', '0', '1', '1', '1', '0', '0', '0'}}
	fmt.Println(maximalSquare(matrix))
}

func maximalSquare(matrix [][]byte) int {
	cur := make([][3]int, len(matrix[0]))
	pre := make([][3]int, len(matrix[0]))
	ans := 0
	for i := range matrix {
		for j := range matrix[i] {
			var state [3]int
			if matrix[i][j] == '0' {
				state = [3]int{}
			} else {
				state = [3]int{1, 1, 1}
			}
			if j-1 >= 0 && matrix[i][j-1] == '1' && matrix[i][j] == '1' {
				state[0] += cur[j-1][0]
			}
			if i-1 >= 0 && matrix[i-1][j] == '1' && matrix[i][j] == '1' {
				state[1] += pre[j][1]
			}
			if i-1 >= 0 && j-1 >= 0 {
				state[2] = min([]int{state[0], state[1], pre[j-1][2] + 1})
			}
			ans = max(ans, state[2]*state[2])
			cur[j] = state
		}
		cur, pre = pre, cur
	}
	return ans
}

func min(arr []int) int {
	ret := arr[0]
	for i := 1; i < len(arr); i++ {
		if arr[i] < ret {
			ret = arr[i]
		}
	}
	return ret
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}
