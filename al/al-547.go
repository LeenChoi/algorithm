// 省份数量
// medium
/*
* 有 n 个城市，其中一些彼此相连，另一些没有相连。如果城市 a 与城市 b 直接相连，且城市 b 与城市 c 直接相连，那么城市 a 与城市 c 间接相连。
*
* 省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。
*
* 给你一个 n x n 的矩阵 isConnected ，其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，而 isConnected[i][j] = 0 表示二者不直接相连。
*
* 返回矩阵中 省份 的数量。
*
*
*
* 示例 1：
*
*
* 输入：isConnected = [[1,1,0],[1,1,0],[0,0,1]]
* 输出：2
* 示例 2：
*
*
* 输入：isConnected = [[1,0,0],[0,1,0],[0,0,1]]
* 输出：3
*
*
* 提示：
*
* 1 <= n <= 200
* n == isConnected.length
* n == isConnected[i].length
* isConnected[i][j] 为 1 或 0
* isConnected[i][i] == 1
* isConnected[i][j] == isConnected[j][i]
*
* 来源：力扣（LeetCode）
* 链接：https://leetcode-cn.com/problems/number-of-provinces
* 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*
* -----------------------------------------------------------------
* 题解：并查集
* 典型的并查集题，正常做并查集，将关联的节点都连接起来，最后再遍历一遍，做下find操作，更新每个节点的最终父节点，
* 然后找出整个数据集里有几个不同的父节点即可
*
 */

package main

import "fmt"

func main() {

	// con := [][]int{{1, 0, 0, 1}, {0, 1, 1, 0}, {0, 1, 1, 1}, {1, 0, 1, 1}}
	con := [][]int{{1, 0, 0, 0, 1, 0, 1, 0, 0, 0}, {0, 1, 0, 1, 0, 1, 0, 0, 0, 0}, {0, 0, 1, 0, 0, 1, 0, 0, 0, 0}, {0, 1, 0, 1, 0, 0, 0, 0, 0, 0}, {1, 0, 0, 0, 1, 0, 0, 0, 1, 0}, {0, 1, 1, 0, 0, 1, 1, 0, 0, 0}, {1, 0, 0, 0, 0, 1, 1, 0, 1, 0}, {0, 0, 0, 0, 0, 0, 0, 1, 0, 0}, {0, 0, 0, 0, 1, 0, 1, 0, 1, 0}, {0, 0, 0, 0, 0, 0, 0, 0, 0, 1}}
	fmt.Println(findCircleNum(con))
}

func findCircleNum(isConnected [][]int) int {
	fa := make([]int, len(isConnected))
	for i := range fa {
		fa[i] = i
	}

	find := func(node int) int {
		n := node
		for fa[n] != n {
			n = fa[n]
		}
		if fa[node] != n {
			fa[node] = n
		}
		return n
	}

	union := func(node1, node2 int) {
		if node1 == node2 {
			return
		}
		f1, f2 := find(node1), find(node2)
		if f1 < f2 {
			fa[f2] = f1
		} else if f2 < f1 {
			fa[f1] = f2
		}
	}

	for i := range isConnected {
		for j := range isConnected[i] {
			if isConnected[i][j] == 1 {
				union(i, j)
			}
		}
	}

	counts := 0
	records := make(map[int]struct{})
	for i := range isConnected {
		f := find(i)
		if _, has := records[f]; !has {
			records[f] = struct{}{}
			counts++
		}
	}
	return counts
}
