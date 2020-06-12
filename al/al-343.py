# 整数拆分
# medium
'''
给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。

示例 1:

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1。
示例 2:

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
说明: 你可以假设 n 不小于 2 且不大于 58。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/integer-break
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

--------------------------------
题解：动态规划，贪心
    贪心：将数字尽量分成多个3，9[333]、8[332]、7[322]
    （为什么不是331，显然332乘积更大，所以 % 3 == 1 的数将 31 拆成 22 即 4）

    动态规划：i 从 3 开始遍历，找某一个 j 使 j * (i - j) 最大，但(i - j)直接参与计算不一定是最大的
    所以要和 dp[i - j] 比较下，所以转移方程为 dp[i] = j * max((i - j), dp[i - j])

'''


import math
class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 2:
            return 1
        if n == 3:
            return 2
        if n % 3 == 1:
            exp = n // 3 - 1
            return int(math.pow(3, exp) * 4)
        else:
            exp = n // 3
            return int(math.pow(3, exp) * (n % 3 or 1))

class SolutionV2:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(2, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], j * max((i - j), dp[i - j]))
        return dp[n]


print(SolutionV2().integerBreak(10))
