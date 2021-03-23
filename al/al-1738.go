// 找出第 K 大的异或坐标值
// medium
/*
* 给你一个二维矩阵 matrix 和一个整数 k ，矩阵大小为 m x n 由非负整数组成。
*
* 矩阵中坐标 (a, b) 的 值 可由对所有满足 0 <= i <= a < m 且 0 <= j <= b < n 的元素 matrix[i][j]（下标从 0 开始计数）执行异或运算得到。
*
* 请你找出 matrix 的所有坐标中第 k 大的值（k 的值从 1 开始计数）。
*
* 示例 1：
*
* 输入：matrix = [[5,2],[1,6]], k = 1
* 输出：7
* 解释：坐标 (0,1) 的值是 5 XOR 2 = 7 ，为最大的值。
* 示例 2：
*
* 输入：matrix = [[5,2],[1,6]], k = 2
* 输出：5
* 解释：坐标 (0,0) 的值是 5 = 5 ，为第 2 大的值。
* 示例 3：
*
* 输入：matrix = [[5,2],[1,6]], k = 3
* 输出：4
* 解释：坐标 (1,0) 的值是 5 XOR 1 = 4 ，为第 3 大的值。
* 示例 4：
*
* 输入：matrix = [[5,2],[1,6]], k = 4
* 输出：0
* 解释：坐标 (1,1) 的值是 5 XOR 2 XOR 1 XOR 6 = 0 ，为第 4 大的值。
*
*
* 提示：
*
* m == matrix.length
* n == matrix[i].length
* 1 <= m, n <= 1000
* 0 <= matrix[i][j] <= 106
* 1 <= k <= m * n
*
* 来源：力扣（LeetCode）
* 链接：https://leetcode-cn.com/problems/find-kth-largest-xor-coordinate-value
* 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
* 
* ---------------------------------------------------------------
* 题解：前缀和 + 排序/优先队列
* 每一项都算好它的二维前缀和，然后得出来的前缀和结果，可以给它排序后输出第 K 大的元素，
* 或者是在算前缀和的同时维护一个长度 K 大小的最小堆，这样最后输出堆顶即是第 K 大的值。
* 
*/

package main

import (
	"container/heap"
	"fmt"
	"sort"
)

func main() {
	matrix := [][]int{[]int{5, 2}, []int{1, 6}}
	k := 1
	fmt.Println(kthLargestValue2(matrix, k))
}

// 利用排序
func kthLargestValue(matrix [][]int, k int) int {
	m, n := len(matrix), len(matrix[0])
	preSum := make([]int, m*n)
	for i := range matrix {
		xor := 0
		for j := range matrix[i] {
			xor = xor ^ matrix[i][j]
			preSum[i*n+j] = xor
			if i > 0 {
				preSum[i*n+j] ^= preSum[(i-1)*n+j]
			}
		}
	}
	sort.Slice(preSum, func(i, j int) bool {
		return preSum[i] > preSum[j]
	})

	return preSum[k-1]
}

// 利用堆-优先队列
type IntHeap []int

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h IntHeap) Top() int           { return h[0] }
func (h *IntHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}
func (h *IntHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func kthLargestValue2(matrix [][]int, k int) int {
	m, n := len(matrix), len(matrix[0])
	preSum := make([][]int, m)
	for i := range preSum {
		preSum[i] = make([]int, n)
	}

	queue := &IntHeap{}
	heap.Init(queue)

	for i := range matrix {
		xor := 0
		for j := range matrix[i] {
			xor = xor ^ matrix[i][j]
			preSum[i][j] = xor
			if i > 0 {
				preSum[i][j] ^= preSum[i-1][j]
			}
			if queue.Len() < k || preSum[i][j] > queue.Top() {
				heap.Push(queue, preSum[i][j])
			}
			if queue.Len() > k {
				heap.Pop(queue)
			}
		}
	}

	return queue.Top()
}
