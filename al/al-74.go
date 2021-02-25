// 搜索二维矩阵
// medium
/*
* 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
*
* 每行中的整数从左到右按升序排列。
* 每行的第一个整数大于前一行的最后一个整数。
*
*
* 示例 1：
* 	1  | 3  | 5  | 7
* 	-----------------
* 	10 | 11 | 16 | 20
* 	-----------------
* 	23 | 30 | 34 | 60
*
* 输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
* 输出：true
* 示例 2：
*
*
* 输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
* 输出：false
*
*
* 提示：
*
* m == matrix.length
* n == matrix[i].length
* 1 <= m, n <= 100
* -104 <= matrix[i][j], target <= 104
*
* 来源：力扣（LeetCode）
* 链接：https://leetcode-cn.com/problems/search-a-2d-matrix
* 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*
* -----------------------------------------------------------
* 题解：二分查找
* 给每个矩阵元素定一个 id，将矩阵展开成线性列表，然后进行二分查找即可
*
 */

package main

import "fmt"

func main() {
	matrix := [][]int{[]int{1, 3, 5, 7}, []int{10, 11, 16, 20}, []int{23, 30, 34, 60}}
	target := 3
	fmt.Println(searchMatrix(matrix, target))
}

func searchMatrix(matrix [][]int, target int) bool {
	n, m := len(matrix), len(matrix[0])
	getNum := func(id int) int {
		x := id / m
		y := id % m
		return matrix[x][y]
	}

	l, r := 0, m*n-1
	for l < r {
		mid := (l + r) / 2
		midNum := getNum(mid)
		if target <= midNum {
			r = mid
		} else {
			l = mid + 1
		}
	}
	return target == getNum(l)
}
