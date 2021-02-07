// 最小体力消耗路径
// medium
/*
* 你准备参加一场远足活动。给你一个二维 rows x columns 的地图 heights ，其中 heights[row][col] 表示格子 (row, col) 的高度。一开始你在最左上角的格子 (0, 0) ，且你希望去最右下角的格子 (rows-1, columns-1) （注意下标从 0 开始编号）。你每次可以往 上，下，左，右 四个方向之一移动，你想要找到耗费 体力 最小的一条路径。
*
* 一条路径耗费的 体力值 是路径上相邻格子之间 高度差绝对值 的 最大值 决定的。
*
* 请你返回从左上角走到右下角的最小 体力消耗值 。
*
* 示例 1：
*
*    (1)  2	  2
*
*    (3)  8	  2
*
*    (5) (3) (5)
*
*
* 输入：heights = [[1,2,2],[3,8,2],[5,3,5]]
* 输出：2
* 解释：路径 [1,3,5,3,5] 连续格子的差值绝对值最大为 2 。
* 这条路径比路径 [1,2,2,2,5] 更优，因为另一条路径差值最大值为 3 。
* 示例 2：
*
*
*
* 输入：heights = [[1,2,3],[3,8,4],[5,3,5]]
* 输出：1
* 解释：路径 [1,2,3,4,5] 的相邻格子差值绝对值最大为 1 ，比路径 [1,3,5,3,5] 更优。
* 示例 3：
*
*
* 输入：heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
* 输出：0
* 解释：上图所示路径不需要消耗任何体力。
*
*
* 提示：
*
* rows == heights.length
* columns == heights[i].length
* 1 <= rows, columns <= 100
* 1 <= heights[i][j] <= 106
*
* 来源：力扣（LeetCode）
* 链接：https://leetcode-cn.com/problems/path-with-minimum-effort
* 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*
* ------------------------------------------------------
* 题解：并查集，Dijkstra
* 并查集的方法是将所有的点都遍历一遍，并且邻接点之间构建一个边edge，再以最小生成树的方式，给edges排个序，
* 然后按顺序做归并，每次归并后如果 (0,0) 点和 (m,n) 点连通了，那么就将本次归并的边的距离输出即可。
*
 */

package main

import (
	"fmt"
	"sort"
)

func main() {
	// heights := [][]int{{1, 2, 2}, {3, 8, 2}, {5, 3, 5}}
	heights := [][]int{{4, 3, 4, 10, 5, 5, 9, 2}, {10, 8, 2, 10, 9, 7, 5, 6}, {5, 8, 10, 10, 10, 7, 4, 2}, {5, 1, 3, 1, 1, 3, 1, 9}, {6, 4, 10, 6, 10, 9, 4, 6}}
	fmt.Println(minimumEffortPath(heights))
}

type edge struct {
	v, w, dist int
}

func minimumEffortPath(heights [][]int) int {
	m, n := len(heights), len(heights[0])
	edges := []edge{}

	fa := make([]int, m*n)
	find := func(x int) int {
		fx := x
		for fa[fx] != fx {
			fx = fa[fx]
		}
		if fa[x] != fx {
			fa[x] = fx
		}
		return fx
	}
	union := func(x, y int) {
		fx, fy := find(x), find(y)
		if fx != fy {
			if fx < fy {
				fa[fy] = fx
			} else {
				fa[fx] = fy
			}
		}
	}
	sameSet := func(x, y int) bool {
		fx, fy := find(x), find(y)
		return fx == fy
	}

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			id := i*n + j
			fa[id] = id
			if i > 0 {
				edges = append(edges, edge{id - n, id, abs(heights[i-1][j] - heights[i][j])})
			}
			if j > 0 {
				edges = append(edges, edge{id - 1, id, abs(heights[i][j-1] - heights[i][j])})
			}
		}
	}
	sort.Slice(edges, func(i, j int) bool { return edges[i].dist < edges[j].dist })

	for _, edge := range edges {
		union(edge.v, edge.w)
		if sameSet(0, m*n-1) {
			return edge.dist
		}
	}
	return 0
}

func abs(v int) int {
	if v < 0 {
		return -v
	}
	return v
}
