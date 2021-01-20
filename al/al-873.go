// 最长的斐波那契子序列的长度
// medium
/*
如果序列 X_1, X_2, ..., X_n 满足下列条件，就说它是 斐波那契式 的：

n >= 3
对于所有 i + 2 <= n，都有 X_i + X_{i+1} = X_{i+2}
给定一个严格递增的正整数数组形成序列，找到 A 中最长的斐波那契式的子序列的长度。如果一个不存在，返回  0 。

（回想一下，子序列是从原序列 A 中派生出来的，它从 A 中删掉任意数量的元素（也可以不删），而不改变其余元素的顺序。例如， [3, 5, 8] 是 [3, 4, 5, 6, 7, 8] 的一个子序列）



示例 1：

输入: [1,2,3,4,5,6,7,8]
输出: 5
解释:
最长的斐波那契式子序列为：[1,2,3,5,8] 。
示例 2：

输入: [1,3,7,11,12,14,18]
输出: 3
解释:
最长的斐波那契式子序列有：
[1,11,12]，[3,11,14] 以及 [7,11,18] 。


提示：

3 <= A.length <= 1000
1 <= A[0] < A[1] < ... < A[A.length - 1] <= 10^9
（对于以 Java，C，C++，以及 C# 的提交，时间限制被减少了 50%）

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/length-of-longest-fibonacci-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

----------------------------------------------------------
题解：动态规划dp
i, j 指针游标 i 先走，如果 (A[i] - A[j]) 在 A 里存在，有 A[k]，那么 k, i, j 这三个位置的数就可以构成斐波那契
对 A 做一个 val -> index 的索引表，然后按上述遍历指针即可。
再做一个复合键值的dp表，键为能构成斐波那契的两个数的索引位数组 [k, j] / [j, i] 等。代表这两个数结尾的斐波那契的最长长度
所以 dp 公式应该是 dp[j, i] = dp[k, j] + 1。需要注意的是如果构成斐波那契，dp值默认该是2


*/

package main

import "fmt"

func main() {
	arr := []int{1, 2, 3, 4, 5, 6, 7, 8}
	fmt.Println(lenLongestFibSubseq(arr))
}

func lenLongestFibSubseq(arr []int) int {
	indexes := map[int]int{}
	for i, num := range arr {
		indexes[num] = i
	}
	m := map[[2]int]int{}
	ans := 0
	for i := range arr {
		for j := 0; j <= i; j++ {
			key := arr[i] - arr[j]
			if k, has := indexes[key]; has && k < j {
				length := m[[2]int{k, j}]
				if length < 3 {
					length += 2
				}
				m[[2]int{j, i}] = length + 1
				ans = max(ans, m[[2]int{j, i}])
			}
		}
	}
	return ans
}

func max(x, y int) int {
	if x < y {
		return y
	}
	return x
}
