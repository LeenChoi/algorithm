// 螺旋矩阵 II
// medium
/*
* 给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。
*
* 示例 1：
*
* 	1	2	3
*
* 	8	9	4
*
* 	7	6	5
*
* 输入：n = 3
* 输出：[[1,2,3],[8,9,4],[7,6,5]]
* 示例 2：
*
* 输入：n = 1
* 输出：[[1]]
*
*
* 提示：
*
* 1 <= n <= 20
*
* 来源：力扣（LeetCode）
* 链接：https://leetcode-cn.com/problems/spiral-matrix-ii
* 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*
* -----------------------------------------------------
* 题解：
* 没什么难的，模拟就完了
 */

package main

import "fmt"

func main() {
	fmt.Println(generateMatrix(3))
}

func generateMatrix(n int) [][]int {
	matrix := make([][]int, n)
	for i := range matrix {
		matrix[i] = make([]int, n)
	}
	direction := 0
	inc := 1
	i, j := 0, 0
	for inc <= n*n {
		matrix[i][j] = inc
		switch direction {
		case 0:
			if j == n-1 || matrix[i][j+1] != 0 {
				direction = (direction + 1) % 4
				i++
			} else {
				j++
			}
		case 1:
			if i == n-1 || matrix[i+1][j] != 0 {
				direction = (direction + 1) % 4
				j--
			} else {
				i++
			}
		case 2:
			if j == 0 || matrix[i][j-1] != 0 {
				direction = (direction + 1) % 4
				i--
			} else {
				j--
			}
		case 3:
			if i == 0 || matrix[i-1][j] != 0 {
				direction = (direction + 1) % 4
				j++
			} else {
				i--
			}
		}
		inc++
	}
	return matrix
}
