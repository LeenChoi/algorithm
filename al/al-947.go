// 移除最多的同行或同列石头
// medium
/*
* n 块石头放置在二维平面中的一些整数坐标点上。每个坐标点上最多只能有一块石头。
*
* 如果一块石头的 同行或者同列 上有其他石头存在，那么就可以移除这块石头。
*
* 给你一个长度为 n 的数组 stones ，其中 stones[i] = [xi, yi] 表示第 i 块石头的位置，返回 可以移除的石子 的最大数量。
*
*
*
* 示例 1：
*
* 输入：stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
* 输出：5
* 解释：一种移除 5 块石头的方法如下所示：
* 1. 移除石头 [2,2] ，因为它和 [2,1] 同行。
* 2. 移除石头 [2,1] ，因为它和 [0,1] 同列。
* 3. 移除石头 [1,2] ，因为它和 [1,0] 同行。
* 4. 移除石头 [1,0] ，因为它和 [0,0] 同列。
* 5. 移除石头 [0,1] ，因为它和 [0,0] 同行。
* 石头 [0,0] 不能移除，因为它没有与另一块石头同行/列。
* 示例 2：
*
* 输入：stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
* 输出：3
* 解释：一种移除 3 块石头的方法如下所示：
* 1. 移除石头 [2,2] ，因为它和 [2,0] 同行。
* 2. 移除石头 [2,0] ，因为它和 [0,0] 同列。
* 3. 移除石头 [0,2] ，因为它和 [0,0] 同行。
* 石头 [0,0] 和 [1,1] 不能移除，因为它们没有与另一块石头同行/列。
* 示例 3：
*
* 输入：stones = [[0,0]]
* 输出：0
* 解释：[0,0] 是平面上唯一一块石头，所以不可以移除它。
*
*
* 提示：
*
* 1 <= stones.length <= 1000
* 0 <= xi, yi <= 104
* 不会有两块石头放在同一个坐标点上
*
* 来源：力扣（LeetCode）
* 链接：https://leetcode-cn.com/problems/most-stones-removed-with-same-row-or-column
* 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*
* -------------------------------------------------------------
* 题解：并查集
* 并查集将同行同列的石头都并到一个集上，题目的最终目标其实就是将每个集里的石头消减到只剩一个。
* 所以最后统计并集里相同祖先的个数即可，记得要减 1，因为要留一个石头。
* 再就是石头的坐标需要转换下，因为每个节点现在是坐标构成的，需要转成一个 id 代表一个节点。
*
* 注意：看好给出的提示条件，我tm因为坐标转id没有满足给出条件，找了半天bug
 */

package main

import "fmt"

func main() {
	// stones := [][]int{{0, 0}, {0, 1}, {1, 0}, {1, 2}, {2, 1}, {2, 2}}
	// stones := [][]int{{0, 0}, {0, 2}, {1, 1}, {2, 0}, {2, 2}}
	stones := [][]int{{3, 2}, {3, 1}, {4, 4}, {1, 1}, {0, 2}, {4, 0}}
	fmt.Println(removeStones(stones))
}

func removeStones(stones [][]int) int {
	if len(stones) <= 1 {
		return 0
	}
	fa := make(map[int]int)
	for _, pair := range stones {
		key := pair[0]*10000 + pair[1]
		fa[key] = key
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
	merge := func(from, to int) {
		fFrom, fTo := find(from), find(to)
		if fFrom != fTo {
			if fFrom < fTo {
				fa[fTo] = fFrom
			} else {
				fa[fFrom] = fTo
			}
		}
	}
	for _, pair1 := range stones {
		for _, pair2 := range stones {
			if pair1[0] == pair2[0] || pair1[1] == pair2[1] {
				stone1 := pair1[0]*10000 + pair1[1]
				stone2 := pair2[0]*10000 + pair2[1]
				merge(stone1, stone2)
			}
		}
	}

	counts := map[int]int{}
	for i := range fa {
		f := find(fa[i])
		counts[f]++
	}
	ans := 0
	for _, c := range counts {
		ans += (c - 1)
	}
	return ans
}
