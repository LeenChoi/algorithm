// 冗余连接
// medium
/*
* 在本问题中, 树指的是一个连通且无环的无向图。
*
* 输入一个图，该图由一个有着N个节点 (节点值不重复1, 2, ..., N) 的树及一条附加的边构成。附加的边的两个顶点包含在1到N中间，这条附加的边不属于树中已存在的边。
*
* 结果图是一个以边组成的二维数组。每一个边的元素是一对[u, v] ，满足 u < v，表示连接顶点u 和v的无向图的边。
*
* 返回一条可以删去的边，使得结果图是一个有着N个节点的树。如果有多个答案，则返回二维数组中最后出现的边。答案边 [u, v] 应满足相同的格式 u < v。
*
* 示例 1：
*
* 输入: [[1,2], [1,3], [2,3]]
* 输出: [2,3]
* 解释: 给定的无向图为:
*   1
*  / \
* 2 - 3
* 示例 2：
*
* 输入: [[1,2], [2,3], [3,4], [1,4], [1,5]]
* 输出: [1,4]
* 解释: 给定的无向图为:
* 5 - 1 - 2
*     |   |
*     4 - 3
* 注意:
*
* 输入的二维数组大小在 3 到 1000。
* 二维数组中的整数在1到N之间，其中N是输入数组的大小。
*
* 来源：力扣（LeetCode）
* 链接：https://leetcode-cn.com/problems/redundant-connection
* 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*
* ----------------------------------------------------------
* 题解：并查集
* 利用并查集归并的时候，如果 from，to 的父节点不同，那么记录下这个边，直到遍历完返回这个记录的边即可
 */

package main

import "fmt"

func main() {
	edges := [][]int{{1, 2}, {1, 3}, {2, 3}}
	fmt.Println(findRedundantConnection(edges))
}

func findRedundantConnection(edges [][]int) []int {
	var ans []int
	fa := make([]int, len(edges)+1)
	for i := range fa {
		fa[i] = i
	}
	find := func(node int) int {
		f := node
		for fa[f] != f {
			f = fa[f]
		}
		if fa[node] != f {
			fa[node] = f
		}
		return f
	}
	merge := func(group []int) {
		from, to := group[0], group[1]
		fFrom, fTo := find(from), find(to)
		if fFrom != fTo {
			if fFrom < fTo {
				fa[fTo] = fFrom
			} else {
				fa[fFrom] = fTo
			}
		} else if from < to {
			ans = group
		}
	}
	for _, edge := range edges {
		merge(edge)
	}
	return ans
}
