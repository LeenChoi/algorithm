// 连接所有点的最小费用
// medium
/*
* 给你一个points 数组，表示 2D 平面上的一些点，其中 points[i] = [xi, yi] 。
*
* 连接点 [xi, yi] 和点 [xj, yj] 的费用为它们之间的 曼哈顿距离 ：|xi - xj| + |yi - yj| ，其中 |val| 表示 val 的绝对值。
*
* 请你返回将所有点连接的最小总费用。只有任意两点之间 有且仅有 一条简单路径时，才认为所有点都已连接。
*
* 示例 1：
*
* 输入：points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
* 输出：20
* 解释：
*
* 我们可以按照上图所示连接所有点得到最小总费用，总费用为 20 。
* 注意到任意两个点之间只有唯一一条路径互相到达。
* 示例 2：
*
* 输入：points = [[3,12],[-2,5],[-4,1]]
* 输出：18
* 示例 3：
*
* 输入：points = [[0,0],[1,1],[1,0],[-1,1]]
* 输出：4
* 示例 4：
*
* 输入：points = [[-1000000,-1000000],[1000000,1000000]]
* 输出：4000000
* 示例 5：
*
* 输入：points = [[0,0]]
* 输出：0
*
*
* 提示：
*
* 1 <= points.length <= 1000
* -106 <= xi, yi <= 106
* 所有点 (xi, yi) 两两不同。
*
* 来源：力扣（LeetCode）
* 链接：https://leetcode-cn.com/problems/min-cost-to-connect-all-points
* 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*
* -----------------------------------------------------
* 题解：最小生成树 Kruskal算法 (并查集)
* 将图的每两点间所有的边都找出来，然后排个序，再遍历这个边集，将每个边的两个点通过并查集连通，如果两个点不在一个连通集里
* 表明这两点间还没有通路，就可以将这条边输出到结果集里
*
 */

package main

import (
	"fmt"
	"sort"
)

func main() {
	// points := [][]int{{0, 0}, {2, 2}, {3, 10}, {5, 2}, {7, 0}}
	points := [][]int{{3, 12}, {-2, 5}, {-4, 1}}
	fmt.Println(minCostConnectPoints(points))
}

func minCostConnectPoints(points [][]int) int {
	fa := map[int]int{}
	for _, point := range points {
		id := point[0]*1000000 + point[1]
		fa[id] = id
	}

	find := func(node int) int {
		pa := node
		for fa[pa] != pa {
			pa = fa[pa]
		}
		if fa[node] != pa {
			fa[node] = pa
		}
		return pa
	}

	union := func(from, to int) bool {
		fFrom, fTo := find(from), find(to)
		if fFrom != fTo {
			if fFrom < fTo {
				fa[fTo] = fFrom
			} else {
				fa[fFrom] = fTo
			}
			return true
		}
		return false
	}

	type edge struct{ v, w, dis int }
	edges := []edge{}

	for i := range points {
		for j := range points {
			if i != j {
				vPoint, wPoint := points[i], points[j]
				v := vPoint[0]*1000000 + vPoint[1]
				w := wPoint[0]*1000000 + wPoint[1]
				dis := abs(vPoint[0]-wPoint[0]) + abs(vPoint[1]-wPoint[1])
				e := edge{v: v, w: w, dis: dis}
				edges = append(edges, e)
			}
		}
	}
	sort.Slice(edges, func(i, j int) bool { return edges[i].dis < edges[j].dis })

	ans := 0
	for _, edge := range edges {
		if union(edge.v, edge.w) {
			ans += edge.dis
		}
	}
	return ans
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}
