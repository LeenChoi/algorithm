// 二维区域和检索 - 矩阵不可变
// medium
/*
* 给定一个二维矩阵，计算其子矩形范围内元素的总和，该子矩阵的左上角为 (row1, col1) ，右下角为 (row2, col2) 。
*
* 上图子矩阵左上角 (row1, col1) = (2, 1) ，右下角(row2, col2) = (4, 3)，该子矩形内元素的总和为 8。
*
*
* 示例：
*
* 给定 matrix = [
*   [3, 0, 1, 4, 2],
*   [5, 6, 3, 2, 1],
*   [1, 2, 0, 1, 5],
*   [4, 1, 0, 1, 7],
*   [1, 0, 3, 0, 5]
* ]
*
* sumRegion(2, 1, 4, 3) -> 8
* sumRegion(1, 1, 2, 2) -> 11
* sumRegion(1, 2, 2, 4) -> 12
*
*
* 提示：
*
* 你可以假设矩阵不可变。
* 会多次调用 sumRegion 方法。
* 你可以假设 row1 ≤ row2 且 col1 ≤ col2 。
*
* 来源：力扣（LeetCode）
* 链接：https://leetcode-cn.com/problems/range-sum-query-2d-immutable
* 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*
* --------------------------------------------------------------
* 题解：动态规划 + 前缀和
* 朴素想法直接遍历子矩阵就ok，但很慢，官方应该没把矩阵构造的时间算进去，只计算了子矩阵求和的时间，
* 那么此题的解题方向应该在重构造，轻求解。
*
* 重构造，快速求和的方法，第一反应那就是前缀和。此题做一个二维的前缀和，每个元素当前的前缀和是以他为右下角的子矩阵的和。
* 那么 r1c1 - r2c2 子矩阵的和就是 sum[r2][c2] - sum[r1-1][c2] - sum[r2][c1-1] + sum[r1][c1]
*
 */

package main

import "fmt"

func main() {
	// matrix := [][]int{[]int{3, 0, 1, 4, 2}, []int{5, 6, 3, 2, 1}, []int{1, 2, 0, 1, 5}, []int{4, 1, 0, 1, 7}, []int{1, 0, 3, 0, 5}}
	matrix := [][]int{}
	obj := Constructor(matrix)
	fmt.Println(obj.SumRegion(2, 1, 4, 3))
}

type NumMatrix struct {
	sumMatrix [][]int
}

func Constructor(matrix [][]int) NumMatrix {
	m := len(matrix)
	sumMatrix := make([][]int, m)
	if m == 0 {
		return NumMatrix{sumMatrix}
	}
	n := len(matrix[0])
	for i := range sumMatrix {
		sumMatrix[i] = make([]int, n)
	}
	for i := range matrix {
		rowSum := 0
		for j := range matrix[i] {
			rowSum += matrix[i][j]
			sumMatrix[i][j] = rowSum
			if i > 0 {
				sumMatrix[i][j] += sumMatrix[i-1][j]
			}
		}
	}
	return NumMatrix{sumMatrix}
}

func (this *NumMatrix) SumRegion(row1 int, col1 int, row2 int, col2 int) int {
	if len(this.sumMatrix) == 0 {
		return 0
	}
	ans := this.sumMatrix[row2][col2]
	if row1 > 0 {
		ans -= this.sumMatrix[row1-1][col2]
	}
	if col1 > 0 {
		ans -= this.sumMatrix[row2][col1-1]
	}
	if row1 > 0 && col1 > 0 {
		ans += this.sumMatrix[row1-1][col1-1]
	}
	return ans
}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * obj := Constructor(matrix);
 * param_1 := obj.SumRegion(row1,col1,row2,col2);
 */
