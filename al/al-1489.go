// 找到最小生成树里的关键边和伪关键边
// hard
/*
* 给你一个 n 个点的带权无向连通图，节点编号为 0 到 n-1 ，同时还有一个数组 edges ，其中 edges[i] = [fromi, toi, weighti] 表示在 fromi 和 toi 节点之间有一条带权无向边。最小生成树 (MST) 是给定图中边的一个子集，它连接了所有节点且没有环，而且这些边的权值和最小。
*
* 请你找到给定图中最小生成树的所有关键边和伪关键边。如果从图中删去某条边，会导致最小生成树的权值和增加，那么我们就说它是一条关键边。伪关键边则是可能会出现在某些最小生成树中但不会出现在所有最小生成树中的边。
*
* 请注意，你可以分别以任意顺序返回关键边的下标和伪关键边的下标。
*
*
* 示例 1：
*
* 		2
*     /   \
* 	1 -	0 -	3
* 	  \	| /
* 		4
*
* 输入：n = 5, edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
* 输出：[[0,1],[2,3,4,5]]
* 解释：上图描述了给定图。
* 下图是所有的最小生成树。
*
* 注意到第 0 条边和第 1 条边出现在了所有最小生成树中，所以它们是关键边，我们将这两个下标作为输出的第一个列表。
* 边 2，3，4 和 5 是所有 MST 的剩余边，所以它们是伪关键边。我们将它们作为输出的第二个列表。
* 示例 2 ：
*
*
*
* 输入：n = 4, edges = [[0,1,1],[1,2,1],[2,3,1],[0,3,1]]
* 输出：[[],[0,1,2,3]]
* 解释：可以观察到 4 条边都有相同的权值，任选它们中的 3 条可以形成一棵 MST 。所以 4 条边都是伪关键边。
*
*
* 提示：
*
* 2 <= n <= 100
* 1 <= edges.length <= min(200, n * (n - 1) / 2)
* edges[i].length == 3
* 0 <= fromi < toi < n
* 1 <= weighti <= 1000
* 所有 (fromi, toi) 数对都是互不相同的。
*
* 来源：力扣（LeetCode）
* 链接：https://leetcode-cn.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree
* 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*
* ---------------------------------------------------------
* 题解：并查集，最小生成树(MST)
* 关键边是指无论哪个 MST，这条边是永远存在的，如果这条边删掉，那么这个 MST 可能不连通，或者最小权值和会变大。
* 伪关键边说的是不同的 MST 中这条边可能会被替代，也就是说可能最小权值和都相等的情况下，可能这条边或许可以被另一个相同权重的通路代替。
*
* 那么总体思路就清晰了，先生成一个 MST，然后得出最小权值和。再重新遍历 edges，每条边走一下上面的判断。
* 即，第一步，如果强行不让这条边并入 MST 生成，看看最终权值和是否增加了，或者不连通了。如果是，那么就是关键边
* 如果第一步不满足，那么判第二步，将这条边首先强行并入 MST 生成，看是否最终权值和没有改变，还是原来的权值和，那么就是伪关键边。
*
* edges 的每条边都做一遍上面的判断，最终就能得出哪些是关键边，哪些是伪关键边
*
 */

package main

import (
	"fmt"
	"math"
	"sort"
)

func main() {
	edges := [][]int{{0, 1, 1}, {1, 2, 1}, {2, 3, 2}, {0, 3, 2}, {0, 4, 3}, {3, 4, 3}, {1, 4, 6}}
	fmt.Println(findCriticalAndPseudoCriticalEdges(5, edges))
}

type unionFind struct {
	fa    []int
	count int
}

func newUf(n int) *unionFind {
	fa := make([]int, n)
	for i := 0; i < n; i++ {
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

func (uf *unionFind) union(from, to int) bool {
	fFrom, fTo := uf.find(from), uf.find(to)
	if fFrom == fTo {
		return false
	}
	if fFrom < fTo {
		uf.fa[fTo] = fFrom
	} else {
		uf.fa[fFrom] = fTo
	}
	uf.count--
	return true
}

func findCriticalAndPseudoCriticalEdges(n int, edges [][]int) [][]int {
	for i, e := range edges {
		edges[i] = append(e, i)
	}
	sort.Slice(edges, func(i, j int) bool { return edges[i][2] < edges[j][2] })
	calcMST := func(uf *unionFind, ignoreId int) (mstWeight int) {
		for i, e := range edges {
			if i != ignoreId && uf.union(e[0], e[1]) {
				mstWeight += e[2]
			}
		}
		if uf.count > 1 {
			return math.MaxInt64
		}
		return
	}

	keyEdges := []int{}
	fakeKeyEdges := []int{}
	mstWeight := calcMST(newUf(n), -1)
	for i, e := range edges {
		if calcMST(newUf(n), i) > mstWeight {
			keyEdges = append(keyEdges, e[3])
		} else {
			uf := newUf(n)
			uf.union(e[0], e[1])
			if e[2]+calcMST(uf, i) == mstWeight {
				fakeKeyEdges = append(fakeKeyEdges, e[3])
			}
		}
	}
	return [][]int{keyEdges, fakeKeyEdges}
}
