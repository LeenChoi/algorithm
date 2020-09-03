// N 皇后
// hard
/*
* n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
*
*  口 口 口 ■ 口 口 口 口
*  口 口 口 口 口 口 ■ 口
*  口 口 ■ 口 口 口 口 口
*  口 口 口 口 口 口 口 ■
*  口 ■ 口 口 口 口 口 口
*  口 口 口 口 ■ 口 口 口
*  ■ 口 口 口 口 口 口 口
*  口 口 口 口 口 ■ 口 口
*
*
* 上图为 8 皇后问题的一种解法。
*
* 给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。
*
* 每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
*
*
*
* 示例：
*
* 输入：4
* 输出：[
*  [".Q..",  // 解法 1
*   "...Q",
*   "Q...",
*   "..Q."],
*
*  ["..Q.",  // 解法 2
*   "Q...",
*   "...Q",
*   ".Q.."]
* ]
* 解释: 4 皇后问题存在两个不同的解法。
*
*
* 提示：
*
* 皇后彼此不能相互攻击，也就是说：任何两个皇后都不能处于同一条横行、纵行或斜线上。
*
* 来源：力扣（LeetCode）
* 链接：https://leetcode-cn.com/problems/n-queens
* 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*
* --------------------------------------------------------
* 题解：回溯
* 其实挺简单，我们想给每一行放一颗皇后，判断下要放的那个位置的列，左斜，右斜方向有没有其他皇后即可
* 这三个方向的判断用三个 bool 型 map 就可以，因为我们是假设按行放皇后，所以行就不用判断了，
* 最后三个方向上的的判断都满足可以放棋，那么用一个数组记录下行与列的关系即可。
*
* 然后就是回溯算法执行就可以了
*
* 还有一个空间优化的方法，上面我用了三个 map 去记录状态，但是这种bool型map，而且 key 还都是从 0 开始递增的
* 这种结构可以优化成二进制掩码，所以上面三个 map 可以用三个 int 值代替，判断的时候做位运算判断即可
*
 */

package main

import "fmt"

func main() {
	ret := solveNQueens(4)
	fmt.Println(ret)
}

func solveNQueens(n int) [][]string {
	columns := make(map[int]bool)
	diagonal1, diagonal2 := make(map[int]bool), make(map[int]bool)
	queens := make([]int, n)
	for i := range queens {
		queens[i] = -1
	}
	ans := [][]string{}

	var search func(row, n int)
	search = func(row, n int) {
		if row == n {
			ans = append(ans, genBoard(queens, n))
		}
		for i := 0; i < n; i++ {
			if _, ok := columns[i]; ok {
				continue
			}
			key1 := row - i
			if _, ok := diagonal1[key1]; ok {
				continue
			}
			key2 := row + i
			if _, ok := diagonal2[key2]; ok {
				continue
			}
			queens[i] = row
			columns[i] = true
			diagonal1[key1] = true
			diagonal2[key2] = true
			search(row+1, n)
			queens[i] = -1
			delete(columns, i)
			delete(diagonal1, key1)
			delete(diagonal2, key2)
		}
	}
	search(0, n)
	return ans
}

func genBoard(queens []int, n int) []string {
	ret := make([]string, n)
	for i := 0; i < n; i++ {
		str := ""
		for j := 0; j < n; j++ {
			if j == i {
				str = str + "Q"
			} else {
				str = str + "."
			}
		}
		ret[queens[i]] = str
	}
	return ret
}
