// 自由之路
// hard
/*
* 视频游戏“辐射4”中，任务“通向自由”要求玩家到达名为“Freedom Trail Ring”的金属表盘，并使用表盘拼写特定关键词才能开门。
*
* 给定一个字符串 ring，表示刻在外环上的编码；给定另一个字符串 key，表示需要拼写的关键词。您需要算出能够拼写关键词中所有字符的最少步数。
*
* 最初，ring 的第一个字符与12:00方向对齐。您需要顺时针或逆时针旋转 ring 以使 key 的一个字符在 12:00 方向对齐，然后按下中心按钮，以此逐个拼写完 key 中的所有字符。
*
* 旋转 ring 拼出 key 字符 key[i] 的阶段中：
*
* 您可以将 ring 顺时针或逆时针旋转一个位置，计为1步。旋转的最终目的是将字符串 ring 的一个字符与 12:00 方向对齐，并且这个字符必须等于字符 key[i] 。
* 如果字符 key[i] 已经对齐到12:00方向，您需要按下中心按钮进行拼写，这也将算作 1 步。按完之后，您可以开始拼写 key 的下一个字符（下一阶段）, 直至完成所有拼写。
*
*
* 输入: ring = "godding", key = "gd"
* 输出: 4
* 解释:
*  对于 key 的第一个字符 'g'，已经在正确的位置, 我们只需要1步来拼写这个字符。
*  对于 key 的第二个字符 'd'，我们需要逆时针旋转 ring "godding" 2步使它变成 "ddinggo"。
*  当然, 我们还需要1步进行拼写。
*  因此最终的输出是 4。
* 提示：
*
* ring 和 key 的字符串长度取值范围均为 1 至 100；
* 两个字符串中都只有小写字符，并且均可能存在重复字符；
* 字符串 key 一定可以由字符串 ring 旋转拼出。
*
* 来源：力扣（LeetCode）
* 链接：https://leetcode-cn.com/problems/freedom-trail
* 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*
* --------------------------------------------------------
* 题解：动态规划dp
* 设 dp[i][j] 为拼出 key 第i个字符，选择 ring 转到第j个字符时的最少步数。首先需要找出 ring 里有多少个 key 第i字符，
* 到时候好找，不用把整个 ring 遍历一遍，所以记个 pos，pos[key[i]] 记录 ring 的该字符的下标位置。
*
* 怎么转移状态，假设 i 字符之前已经选好了最少步数的转法，拟为 dp[i-1][k], 当前 ring 停在第k位上。
* 那么现在只需找出拼第 i 字符时，ring 从 k 转到某一个 j 位置的最少步数即可，最后招 dp[len(key) - 1] 列表中最小值即可
*
 */

package main

import (
	"fmt"
	"math"
)

func main() {
	res := findRotateSteps("edcba", "abcde")
	fmt.Println(res)
}

func findRotateSteps(ring string, key string) int {
	const inf = math.MaxInt32 / 2
	n, m := len(ring), len(key)
	pos := [26][]int{}
	for i, c := range ring {
		pos[c-'a'] = append(pos[c-'a'], i)
	}
	dp := make([][]int, m)
	for i := range dp {
		dp[i] = make([]int, n)
		for j := range dp[i] {
			dp[i][j] = inf
		}
	}

	for _, p := range pos[key[0]-'a'] {
		dp[0][p] = min(p, n-p) + 1
	}

	for i := 1; i < m; i++ {
		for _, j := range pos[key[i]-'a'] {
			for _, k := range pos[key[i-1]-'a'] {
				dp[i][j] = min(dp[i][j], dp[i-1][k]+min(abs(k-j), n-abs(k-j))+1)
			}
		}
	}
	fmt.Println(dp)
	return min(dp[m-1]...)
}

func min(list ...int) int {
	ret := list[0]
	for _, v := range list[1:] {
		if v < ret {
			ret = v
		}
	}
	return ret
}

func abs(v int) int {
	if v < 0 {
		return -v
	}
	return v
}
