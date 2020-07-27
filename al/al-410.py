# 分割数组的最大值
# hard
'''
给定一个非负整数数组和一个整数 m，你需要将这个数组分成 m 个非空的连续子数组。设计一个算法使得这 m 个子数组各自和的最大值最小。

注意:
数组长度 n 满足以下条件:

1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)
示例:

输入:
nums = [7,2,5,10,8]
m = 2

输出:
18

解释:
一共有四种方法将nums分割为2个子数组。
其中最好的方式是将其分为[7,2,5] 和 [10,8]，
因为此时这两个子数组各自的和的最大值为18，在所有情况中最小。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/split-array-largest-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

--------------------------------------------
题解：动态规划，二分法+贪心

dp:
dp[i][j] 记录前 i 个数分成 j 段时的解。当想得到 dp[i][j]，他比前 i-1 多了一个 i，那么最直接的我可以先判下第 i 个数字本身
和前 i-1 个数分成 j-1 段的最大值，即 dp[i-1][j-1]，选出二中最大的。同理，我们可以遍历一个 k，使他大于 0，小于 i，
比较前 k 个数分成 j-1 段的最大值 dp[k][j-1]，和从 k 到 i 的和 sum(k,j) 即 dp[i][j] 的第 j 段，得到两者最大值，
并且遍历所有 k，获取里面的最小解，即是 dp[i][j] 的值。

另外，j = 0，或者 i < j 这种逻辑上不可能的情况，可能会需要参与到计算，因为 dp 值是找最小值，所以这种情况的值可以给个无穷大

二分法:
首先是贪心的思想，比如有某个阈值 x，遍历 nums 累加，如果当前累加值 > x，那么刨去当前这个值将前几项累加值分成一个段，并且count + 1
最终会得到一个总段数 count，当这个 count > m，说明 x 值找的有点小了，count < m 说明 x 有点大了，需要正好找到 count == m，
那就要二分查找了。取 l, r 为 nums 里的最大值，和 nums 总和。算出 mid 值做上述过程的分段，慢慢收敛范围，最终得出来的边界 l,r
即贪心过程中的 x，就是最终答案。

为什么 l 取 nums 最大值，因为如果遇到每个数是各自一段的时候，那么此题的解就是 nums 中最大的数。当二分法收敛范围的时候，通过上述
二分法 mid 会越来越趋近于 l，最终 l,r 重叠就在于 l 的这个点上，即 nums 的最大值。如果 l 取最小值，mid 会趋近于这个最小数，最终
l,r 收敛于其他位置，最终可能重叠在比最小数大，比最大数小的某一个位置上，结果是错误的

'''


class Solution:
    def splitArray(self, nums, m: int) -> int:
        n = len(nums)
        dp = [[float('inf')] * (m + 1) for _ in range(n +1)]
        dp[0][0] = 0
        sums = [0]
        for num in nums:
            sums.append(sums[-1] + num)
        for i in range(1, n + 1):
            for j in range(1, min(m, i) + 1):
                for k in range(i):
                    dp[i][j] = min(dp[i][j], max(dp[k][j - 1], sums[i] - sums[k]))
        return dp[-1][-1]

class Solution2:
    def splitArray(self, nums, m: int) -> int:
        def check(x):
            sums, count = 0, 1
            for n in nums:
                if sums + n > x:
                    count += 1
                    sums = n
                else:
                    sums += n
            return count <= m
        
        l, r = max(nums), sum(nums)
        while l < r:
            mid = (l + r) // 2
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return l


print(Solution().splitArray([7,2,5,10,8], 2))