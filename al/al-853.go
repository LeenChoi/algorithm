// 车队
// medium
/*
* N  辆车沿着一条车道驶向位于 target 英里之外的共同目的地。
*
* 每辆车 i 以恒定的速度 speed[i] （英里/小时），从初始位置 position[i] （英里） 沿车道驶向目的地。
*
* 一辆车永远不会超过前面的另一辆车，但它可以追上去，并与前车以相同的速度紧接着行驶。
*
* 此时，我们会忽略这两辆车之间的距离，也就是说，它们被假定处于相同的位置。
*
* 车队 是一些由行驶在相同位置、具有相同速度的车组成的非空集合。注意，一辆车也可以是一个车队。
*
* 即便一辆车在目的地才赶上了一个车队，它们仍然会被视作是同一个车队。
*
* 会有多少车队到达目的地?
*
* 示例：
*
* 输入：target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
* 输出：3
* 解释：
* 从 10 和 8 开始的车会组成一个车队，它们在 12 处相遇。
* 从 0 处开始的车无法追上其它车，所以它自己就是一个车队。
* 从 5 和 3 开始的车会组成一个车队，它们在 6 处相遇。
* 请注意，在到达目的地之前没有其它车会遇到这些车队，所以答案是 3。
*
* 提示：
*
* 0 <= N <= 10 ^ 4
* 0 < target <= 10 ^ 6
* 0 < speed[i] <= 10 ^ 6
* 0 <= position[i] < target
* 所有车的初始位置各不相同。
*
* 来源：力扣（LeetCode）
* 链接：https://leetcode-cn.com/problems/car-fleet
* 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*
* ------------------------------------------------------------------
* 题解：排序
*
* 将 position 都转成剩余距离，然后从小到大排个序，再除以他们各自的速度，得出时间 costs 列表，
* 遍历 costs，如果后面的时间比前面的时间花的少，说明在终点线前能够赶上前一个，所以寻找 [i, j] 区间，
* 满足 costs[i] < costs[j] 的分成一个车队，最后统计出多少个这样的车队(区间)即可。
*
 */

package main

import (
	"fmt"
	"sort"
)

func main() {
	target := 10
	position := []int{8, 3, 7, 4, 6, 5}
	speed := []int{4, 4, 4, 4, 4, 4}
	fmt.Println(carFleet(target, position, speed))
}

func carFleet(target int, position []int, speed []int) int {
	if len(position) == 0 {
		return 0
	}
	groups := [][2]int{}
	for i := range position {
		tmp := [2]int{}
		tmp[0] = target - position[i]
		tmp[1] = speed[i]
		groups = append(groups, tmp)
	}
	sort.Slice(groups, func(i, j int) bool {
		a, b := groups[i], groups[j]
		return a[0] < b[0] || a[0] == b[0] && a[1] < b[1]
	})

	fmt.Println(groups)

	ans := 0
	slower := float32(0)
	costs := make([]float32, len(position))
	for i := range groups {
		tmp := groups[i]
		costs[i] = float32(tmp[0]) / float32(tmp[1])
		if costs[i] > slower {
			slower = costs[i]
			ans++
		}
	}
	fmt.Println(costs)
	return ans
}
