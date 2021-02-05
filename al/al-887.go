// 鸡蛋掉落
// hard
/*
* 你将获得 K 个鸡蛋，并可以使用一栋从 1 到 N  共有 N 层楼的建筑。
*
* 每个蛋的功能都是一样的，如果一个蛋碎了，你就不能再把它掉下去。
*
* 你知道存在楼层 F ，满足 0 <= F <= N 任何从高于 F 的楼层落下的鸡蛋都会碎，从 F 楼层或比它低的楼层落下的鸡蛋都不会破。
*
* 每次移动，你可以取一个鸡蛋（如果你有完整的鸡蛋）并把它从任一楼层 X 扔下（满足 1 <= X <= N）。
*
* 你的目标是确切地知道 F 的值是多少。
*
* 无论 F 的初始值如何，你确定 F 的值的最小移动次数是多少？
*
*
* 示例 1：
*
* 输入：K = 1, N = 2
* 输出：2
* 解释：
* 鸡蛋从 1 楼掉落。如果它碎了，我们肯定知道 F = 0 。
* 否则，鸡蛋从 2 楼掉落。如果它碎了，我们肯定知道 F = 1 。
* 如果它没碎，那么我们肯定知道 F = 2 。
* 因此，在最坏的情况下我们需要移动 2 次以确定 F 是多少。
* 示例 2：
*
* 输入：K = 2, N = 6
* 输出：3
* 示例 3：
*
* 输入：K = 3, N = 14
* 输出：4
*
*
* 提示：
*
* 1 <= K <= 100
* 1 <= N <= 10000
*
* 来源：力扣（LeetCode）
* 链接：https://leetcode-cn.com/problems/super-egg-drop
* 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*
* ------------------------------------------------------
* 题解：二分法 + 动态规划
* 朴素想法，直接上二分法，取中间楼层，如果碎了应该在低层，如果没碎应该在高层。
* 但是二分法需要一个判断选边界的条件，此题虽知道鸡蛋会在某个楼层碎掉，但是没有一个判断工具，能够得知当前楼层会不会碎掉。
*
* 所以这里需要上动态规划来转移鸡蛋与楼层的状态。设 T(K, N) 表示 K 个鸡蛋，N 楼层时的最小移动次数，他应该是 1 ~ N 楼层间的
* 某个楼层 X, 以 X 分界的高层段和低层段的两个最小移动次数中较大值 + 1，即 T(K, N) = 1 + max(T(K-1, X-1), T(K, N-X))。
* 因为要求最小移动次数，但需要把最坏的情况算上，我们要求的就是将最坏情况最小化。
* T(K-1, X-1) 表示鸡蛋在 X 这层碎了，那么 F 层应该在 X 以下的层，且已经用掉一个鸡蛋，所以剩 K-1 个鸡蛋。
* T(K, N-X) 表示 X 层没碎，那么需要向高层移动，T() 函数关心的是考虑多少个层，而不是第几层，所以这里直接用 N-X
*
* 那么现需要找到这个 X 层，使的让 X 上段和下段的 T()函数得到的值尽量小，那么就需要 X = [1...N] 去扫，但挨个扫肯定慢，
* 所以这里还需要二分法去找 X，问题又回到了最初，那么二分法的用来选边界的判断条件是什么？ 上述的 dp 过程就是判断条件。
*
* 比如，从 1 ~ N 取个中间层 M，取 T1 = T(K-1, M-1), T2= T(K, N-M)，如果 T1 < T2，说明 T2 需要的次数更多，
* 此时的 M 层不是最优的楼层，那么下边界就需要向上移，下次再从 M ~ N (转换后是 1 ~ N-M) 层中取出下一个中间层 M'，
* 再做同样的操作，直至找到最优的 M 层
*
* 最后为了求 M，收敛得到的 l,h 俩边界，分别对这俩层求 T，取两者中较小值 +1 即是本次 dp 转移的 dp值。最终输出 T(K, N) 即是答案。
*
 */

package main

import (
	"fmt"
	"math"
)

func main() {
	K, N := 2, 2
	fmt.Println(superEggDrop(K, N))
}

func superEggDrop(K int, N int) int {
	dp := map[[2]int]int{}
	var transfer func(k, n int) int
	transfer = func(k, n int) int {
		key := [2]int{k, n}
		if _, exist := dp[key]; !exist {
			ret := math.MaxInt64
			if n == 0 {
				ret = 0
			} else if k == 1 {
				ret = n
			} else {
				l, h := 1, n
				for l+1 < h { // 为啥是 l+1，因为必须求出来个 mid 是与 l,h 不重叠的，不然 mid == l 可能会死循环
					mid := (l + h) / 2
					fmt.Println(l, h, mid, k, n)
					t1 := transfer(k-1, mid-1)
					t2 := transfer(k, n-mid)
					fmt.Println("tttttt", t1, t2)
					if t1 < t2 {
						l = mid
					} else if t1 > t2 {
						h = mid
					} else {
						l = mid
						h = mid
					}
				}
				for _, x := range []int{l, h} {
					ret = min(ret, max(transfer(k-1, x-1), transfer(k, n-x)))
				}
				ret++
			}
			dp[key] = ret
		}
		return dp[key]
	}
	ans := transfer(K, N)
	fmt.Println(dp)
	return ans
}

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func max(x, y int) int {
	if x < y {
		return y
	}
	return x
}
