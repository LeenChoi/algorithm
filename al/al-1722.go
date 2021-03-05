// 执行交换操作后的最小汉明距离
// medium
/*
* 给你两个整数数组 source 和 target ，长度都是 n 。还有一个数组 allowedSwaps ，其中每个 allowedSwaps[i] = [ai, bi] 表示你可以交换数组 source 中下标为 ai 和 bi（下标从 0 开始）的两个元素。注意，你可以按 任意 顺序 多次 交换一对特定下标指向的元素。
*
* 相同长度的两个数组 source 和 target 间的 汉明距离 是元素不同的下标数量。形式上，其值等于满足 source[i] != target[i] （下标从 0 开始）的下标 i（0 <= i <= n-1）的数量。
*
* 在对数组 source 执行 任意 数量的交换操作后，返回 source 和 target 间的 最小汉明距离 。
*
* 示例 1：
*
* 输入：source = [1,2,3,4], target = [2,1,4,5], allowedSwaps = [[0,1],[2,3]]
* 输出：1
* 解释：source 可以按下述方式转换：
* - 交换下标 0 和 1 指向的元素：source = [2,1,3,4]
* - 交换下标 2 和 3 指向的元素：source = [2,1,4,3]
* source 和 target 间的汉明距离是 1 ，二者有 1 处元素不同，在下标 3 。
* 示例 2：
*
* 输入：source = [1,2,3,4], target = [1,3,2,4], allowedSwaps = []
* 输出：2
* 解释：不能对 source 执行交换操作。
* source 和 target 间的汉明距离是 2 ，二者有 2 处元素不同，在下标 1 和下标 2 。
* 示例 3：
*
* 输入：source = [5,1,2,4,3], target = [1,5,4,2,3], allowedSwaps = [[0,4],[4,2],[1,3],[1,4]]
* 输出：0
*
*
* 提示：
*
* n == source.length == target.length
* 1 <= n <= 105
* 1 <= source[i], target[i] <= 105
* 0 <= allowedSwaps.length <= 105
* allowedSwaps[i].length == 2
* 0 <= ai, bi <= n - 1
* ai != bi
*
* 来源：力扣（LeetCode）
* 链接：https://leetcode-cn.com/problems/minimize-hamming-distance-after-swap-operations
* 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*
* ------------------------------------------------------------------
* 题解：并查集 + 哈希表
* 将 swap 表依次并查集合并，然后遍历 source 和 target，找 source 里有没有当前 target，如果有那么从并查集里找下
* 这两个数是否在一个集里，如果有，那就说明可以替换，如果没有，说明不能替换，汉明距离+1。
*
* 需要注意的是，source 或 target 可能会有重复的元素，可能会导致 source 里某个元素做重复替换，这是错误的，
* 所以记个哈希表，表里记录每个元素的下标，如果有多个重复元素，那么哈希表李记录了它出现的所有下标。
* 通过并查集判断可以替换的元素后，将此元素对应的下标从哈希表里删除，使之不在参与之后的替换判断。
*
 */

package main

import "fmt"

func main() {
	source := []int{1, 2, 3, 4}
	target := []int{2, 1, 4, 5}
	allowedSwaps := [][]int{[]int{0, 1}, []int{2, 3}}
	// allowedSwaps := [][]int{[]int{0, 2}, []int{1, 2}}
	fmt.Println(minimumHammingDistance(source, target, allowedSwaps))
}

func minimumHammingDistance(source []int, target []int, allowedSwaps [][]int) int {
	n := len(source)
	pa := make([]int, n)
	for i := range pa {
		pa[i] = i
	}

	find := func(node int) int {
		cur := node
		fa := pa[cur]
		for fa != cur {
			cur = fa
			fa = pa[cur]
		}
		if fa != node {
			pa[node] = fa
		}
		return fa
	}

	union := func(node1, node2 int) {
		fa1, fa2 := find(node1), find(node2)
		if fa1 != fa2 {
			if fa1 < fa2 {
				pa[fa2] = fa1
			} else {
				pa[fa1] = fa2
			}
		}
	}

	for _, swap := range allowedSwaps {
		union(swap[0], swap[1])
	}

	indexMap := map[int][]int{}
	for i, v := range source {
		if _, exists := indexMap[v]; !exists {
			indexMap[v] = []int{i}
		} else {
			indexMap[v] = append(indexMap[v], i)
		}
	}

	ans := 0
	for i := 0; i < n; i++ {
		indexes := indexMap[target[i]]
		faSrc := find(i)
		canSwap := false
		for j, index := range indexes {
			faTar := find(index)
			if faSrc == faTar {
				indexMap[target[i]] = append(indexes[:j], indexes[j+1:]...)
				canSwap = true
				break
			}
		}
		if !canSwap {
			ans++
		}
	}
	return ans
}
