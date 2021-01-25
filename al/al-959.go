// 由斜杠划分区域
// medium
/*
* 在由 1 x 1 方格组成的 N x N 网格 grid 中，每个 1 x 1 方块由 /、\ 或空格构成。这些字符会将方块划分为一些共边的区域。
*
* （请注意，反斜杠字符是转义的，因此 \ 用 "\\" 表示。）。
*
* 返回区域的数目。
*
*
*
* 示例 1：
*
* 输入：
* [
*   " /",
*   "/ "
* ]
* 输出：2
* 解释：2x2 网格如下：
* 	------------
* 	|	      /	|
* 	|	   /	|
* 	|   /		|
* 	|/			|
* 	-------------
* 示例 2：
*
* 输入：
* [
*   " /",
*   "  "
* ]
* 输出：1
* 解释：2x2 网格如下：
* 	------------
* 	|	      /	|
* 	|	   /	|
* 	|   		|
* 	|			|
* 	-------------
*
* 示例 3：
*
* 输入：
* [
*   "\\/",
*   "/\\"
* ]
* 输出：4
* 解释：（回想一下，因为 \ 字符是转义的，所以 "\\/" 表示 \/，而 "/\\" 表示 /\。）
* 2x2 网格如下：
*
* 示例 4：
*
* 输入：
* [
*   "/\\",
*   "\\/"
* ]
* 输出：5
* 解释：（回想一下，因为 \ 字符是转义的，所以 "/\\" 表示 /\，而 "\\/" 表示 \/。）
* 2x2 网格如下：
*
* 示例 5：
*
* 输入：
* [
*   "//",
*   "/ "
* ]
* 输出：3
* 解释：2x2 网格如下：
*
*
*
* 提示：
*
* 1 <= grid.length == grid[0].length <= 30
* grid[i][j] 是 '/'、'\'、或 ' '。
*
* 来源：力扣（LeetCode）
* 链接：https://leetcode-cn.com/problems/regions-cut-by-slashes
* 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*
* -------------------------------------------------------
* 题解：并查集
* 每一块 1 x 1 的网格，两条对角线相交，可以划分出 4 个小三角形。如果给一个空白网格画个 '/'，那么会分出左上/右下俩三角形，
* 是 4 个小三角形中，由左上俩小三角连通和右下俩小三角连通起来的。所以此题可以看做 4 * n * n 个小三角形的连通问题，即并查集问题。
*
* 一个网格中的小三角形连通问题解决了，接下来是要看不同网格中的连通问题。两个网格来说，左右分布的网格，无论是 '/' 分割，还是 '\' 分割，
* 左网格的右小三角和右网格的左小三角一定连通。上下分布的网格，上网格的下小三角和下网格的上小三角一定连通。
* 所以每个相邻的网格临边小三角互相连通就可以了，此题结束。
 */

package main

import "fmt"

func main() {
	grid := []string{"/\\", "\\/"}
	fmt.Println(regionsBySlashes(grid))
}

type unionFind struct {
	fa    []int
	count int
}

func newUF(n int) *unionFind {
	fa := make([]int, n)
	for i := range fa {
		fa[i] = i
	}
	uf := &unionFind{fa, n}
	return uf
}

func (uf *unionFind) find(node int) int {
	pa := node
	for uf.fa[pa] != pa {
		pa = uf.fa[pa]
	}
	if uf.fa[node] != pa {
		uf.fa[node] = pa
	}
	return pa
}

func (uf *unionFind) union(from, to int) {
	fFrom, fTo := uf.find(from), uf.find(to)
	if fFrom != fTo {
		if fFrom < fTo {
			uf.fa[fTo] = fFrom
		} else {
			uf.fa[fFrom] = fTo
		}
		uf.count--
	}
}

func regionsBySlashes(grid []string) int {
	n := len(grid)
	uf := newUF(4 * n * n)
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			idx := i*n + j
			if i < n-1 {
				bottom := idx + n
				uf.union(idx*4+2, bottom*4)
			}
			if j < n-1 {
				right := idx + 1
				uf.union(idx*4+1, right*4+3)
			}
			if grid[i][j] == '/' {
				uf.union(idx*4, idx*4+3)
				uf.union(idx*4+1, idx*4+2)
			} else if grid[i][j] == '\\' {
				uf.union(idx*4, idx*4+1)
				uf.union(idx*4+2, idx*4+3)
			} else {
				uf.union(idx*4, idx*4+1)
				uf.union(idx*4+1, idx*4+2)
				uf.union(idx*4+2, idx*4+3)
			}
		}
	}
	return uf.count
}
