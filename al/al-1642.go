// 可以到达的最远建筑
// medium
/*
* 给你一个整数数组 heights ，表示建筑物的高度。另有一些砖块 bricks 和梯子 ladders 。
*
* 你从建筑物 0 开始旅程，不断向后面的建筑物移动，期间可能会用到砖块或梯子。
*
* 当从建筑物 i 移动到建筑物 i+1（下标 从 0 开始 ）时：
*
* 如果当前建筑物的高度 大于或等于 下一建筑物的高度，则不需要梯子或砖块
* 如果当前建筑的高度 小于 下一个建筑的高度，您可以使用 一架梯子 或 (h[i+1] - h[i]) 个砖块
* 如果以最佳方式使用给定的梯子和砖块，返回你可以到达的最远建筑物的下标（下标 从 0 开始 ）。
*
*
* 示例 1：
*
*
* 输入：heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1
* 输出：4
* 解释：从建筑物 0 出发，你可以按此方案完成旅程：
* - 不使用砖块或梯子到达建筑物 1 ，因为 4 >= 2
* - 使用 5 个砖块到达建筑物 2 。你必须使用砖块或梯子，因为 2 < 7
* - 不使用砖块或梯子到达建筑物 3 ，因为 7 >= 6
* - 使用唯一的梯子到达建筑物 4 。你必须使用砖块或梯子，因为 6 < 9
* 无法越过建筑物 4 ，因为没有更多砖块或梯子。
* 示例 2：
*
* 输入：heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2
* 输出：7
* 示例 3：
*
* 输入：heights = [14,3,19,3], bricks = 17, ladders = 0
* 输出：3
*
*
* 提示：
*
* 1 <= heights.length <= 105
* 1 <= heights[i] <= 106
* 0 <= bricks <= 109
* 0 <= ladders <= heights.length
*
* 来源：力扣（LeetCode）
* 链接：https://leetcode-cn.com/problems/furthest-building-you-can-reach
* 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*
* ----------------------------------------------------------
* 题解：堆 二分法 贪心
* 最开始我用的二分法，判断边界就是，判断到 mid 为止的建筑可不可以到达，判断函数就是找出所有高度差，入堆，
* 然后比较小的高度差用砖头，剩下的用梯子，判断梯子是否够用。但效率较慢，因为每次二分查找的判断都要走一遍堆
*
* 其实可以不用二分法，直接贪心地入堆判断即可。做个小顶堆，堆大小控制在梯子的个数，当堆大于梯子数的时候，输出个栈顶，
* 判断砖头够不够用，当不够用的时候，即表示能到达的建筑位置。
 */

package main

import (
	"container/heap"
	"fmt"
)

// !!! go heap
type IntHeap []int

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
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

func main() {
	heights := []int{4, 2, 7, 6, 9, 14, 12}
	fmt.Println(furthestBuilding2(heights, 5, 1))

	heights = []int{4, 12, 2, 7, 3, 18, 20, 3, 19}
	fmt.Println(furthestBuilding2(heights, 10, 2))

	heights = []int{14, 3, 19, 3}
	fmt.Println(furthestBuilding2(heights, 17, 0))

	heights = []int{2, 7, 9, 12}
	fmt.Println(furthestBuilding2(heights, 5, 1))

}

// 二分法 + 堆
func furthestBuilding(heights []int, bricks int, ladders int) int {
	i, j := 0, len(heights)-1
	for i < j {
		mid := (i + j) / 2
		tempHeights := heights[:mid+1]
		if mayReach(tempHeights, bricks, ladders) {
			i = mid + 1
		} else {
			j = mid
		}
	}
	if mayReach(heights[:i+1], bricks, ladders) {
		return i
	}
	return i - 1
}

func mayReach(heights []int, bricks int, ladders int) bool {
	if len(heights) == 1 {
		return true
	}
	needBricks, needLadders := 0, 0

	steps := &IntHeap{}
	heap.Init(steps)
	for i := 1; i < len(heights); i++ {
		if heights[i] > heights[i-1] {
			heap.Push(steps, heights[i]-heights[i-1])
		}
	}
	for steps.Len() > 0 {
		step := heap.Pop(steps).(int)
		if step <= bricks-needBricks {
			needBricks += step
		} else {
			needLadders += 1
		}
	}
	return needLadders <= ladders
}

// 堆 + 贪心
func furthestBuilding2(heights []int, bricks int, ladders int) int {
	steps := &IntHeap{}
	remainBricks := bricks
	for i := 1; i < len(heights); i++ {
		if heights[i] > heights[i-1] {
			heap.Push(steps, heights[i]-heights[i-1])
		}
		if steps.Len() > ladders {
			step := heap.Pop(steps).(int)
			if remainBricks >= step {
				remainBricks -= step
			} else {
				return i - 1
			}
		}
	}
	return len(heights) - 1
}
