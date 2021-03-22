// 将整数按权重排序
// medium
/*
* 我们将整数 x 的 权重 定义为按照下述规则将 x 变成 1 所需要的步数：
*
* 如果 x 是偶数，那么 x = x / 2
* 如果 x 是奇数，那么 x = 3 * x + 1
* 比方说，x=3 的权重为 7 。因为 3 需要 7 步变成 1 （3 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1）。
*
* 给你三个整数 lo， hi 和 k 。你的任务是将区间 [lo, hi] 之间的整数按照它们的权重 升序排序 ，如果大于等于 2 个整数有 相同 的权重，那么按照数字自身的数值 升序排序 。
*
* 请你返回区间 [lo, hi] 之间的整数按权重排序后的第 k 个数。
*
* 注意，题目保证对于任意整数 x （lo <= x <= hi） ，它变成 1 所需要的步数是一个 32 位有符号整数。
*
*
*
* 示例 1：
*
* 输入：lo = 12, hi = 15, k = 2
* 输出：13
* 解释：12 的权重为 9（12 --> 6 --> 3 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1）
* 13 的权重为 9
* 14 的权重为 17
* 15 的权重为 17
* 区间内的数按权重排序以后的结果为 [12,13,14,15] 。对于 k = 2 ，答案是第二个整数也就是 13 。
* 注意，12 和 13 有相同的权重，所以我们按照它们本身升序排序。14 和 15 同理。
* 示例 2：
*
* 输入：lo = 1, hi = 1, k = 1
* 输出：1
* 示例 3：
*
* 输入：lo = 7, hi = 11, k = 4
* 输出：7
* 解释：区间内整数 [7, 8, 9, 10, 11] 对应的权重为 [16, 3, 19, 6, 14] 。
* 按权重排序后得到的结果为 [8, 10, 11, 7, 9] 。
* 排序后数组中第 4 个数字为 7 。
* 示例 4：
*
* 输入：lo = 10, hi = 20, k = 5
* 输出：13
* 示例 5：
*
* 输入：lo = 1, hi = 1000, k = 777
* 输出：570
*
*
* 提示：
*
* 1 <= lo <= hi <= 1000
* 1 <= k <= hi - lo + 1
*
* 来源：力扣（LeetCode）
* 链接：https://leetcode-cn.com/problems/sort-integers-by-the-power-value
* 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*
* ---------------------------------------------------------
* 题解：递归 + 记忆法
* 写个递归算法，算出来每个数的权重，再做一个哈希表，记录算过的每个数的权重，这样下回再算其他数时遇到已经算过的数，
* 无需重复计算，直接取记录即可。
*
* 开始我用循环去解数的权重，但是循环算法只能知道当前数最终是多少权重，计算过程中的中间数无法得出权重，除非借助其他数据结构。
* 递归可以解决这个问题，因为本次往后的递归没有返回，此次递归也无法完成，所以一定会等到后面的结果，即中间数的权重。
*
 */

package main

import (
	"fmt"
	"sort"
)

func main() {
	lo := 12
	hi := 15
	k := 2
	fmt.Println(getKth(lo, hi, k))
}

func getKth(lo int, hi int, k int) int {
	weightMap := map[int]int{}
	weightMap[1] = 0
	weightList := [][2]int{}
	var getWeight func(num int) int
	getWeight = func(num int) int {
		if val, exists := weightMap[num]; exists {
			return val
		}
		if num%2 == 0 {
			weightMap[num] = getWeight(num/2) + 1
		} else {
			weightMap[num] = getWeight(num*3+1) + 1
		}
		return weightMap[num]
	}
	for v := lo; v <= hi; v++ {
		w := getWeight(v)
		weightList = append(weightList, [2]int{v, w})
	}
	sort.Slice(weightList, func(i, j int) bool {
		a, b := weightList[i], weightList[j]
		return a[1] < b[1] || a[1] == b[1] && a[0] < b[0]
	})
	return weightList[k-1][0]
}
