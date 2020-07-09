# 最佳买卖股票时机含冷冻期
# medium
'''
给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​

设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
示例:

输入: [1,2,3,0,2]
输出: 3 
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

--------------------------------
题解：动态规划 (两种)
1. 二维dp, dp[i][j] 表示第 i 天买入，到第 j 天时的最高收入情况，可能是第 j 天卖了，或者第 j 天之前卖了，一直空着手
    需要比较三种情况
    （1）第 j 天卖了，加上第 i - 2 天的最高收入情况，因为要在第 i 天买入，最迟也得在 i - 2 那天把手里的卖了
    （2）第 j 天之前卖了，加上第 i - 2 天的最高收入情况
    （3）可能第 i 天买入，不是最好的买入点，可能第 i 天之前的买入更加，需要看下第 i 天以前买入，到第 j 天的最高收入情况
    所以 dp 函数为
        第 i 天买入的比较：dpi = max(p[j] - p[i] + dp[i-2], dp[j-1])
        第 i 天以前的买入: max(dpi, dp[i])
        结合后: dp[j] = max(p[j] - p[i] + dp[i-2], dp[j-1], dp[i])

2. 一维dp，上面的思路是记录纯收益，此dp是要记录手里的当前值
    记录三个值，当天手里不持股，当天持股 和 当天卖出
    当天不持股 <= 昨天不持股 或者 昨天卖了
    当天持股 <= 昨天持股 或者 昨天买了
    当天卖出 <= 昨天持股
    转移这几个不同情况时，手里有多钱，然后取最大值就可以了

'''


class Solution:
    def maxProfit(self, prices) -> int:
        dp = [0] * len(prices)
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                earn = 0
                if i - 2 >= 0:
                    earn = dp[i - 2]
                dp[j] = max(prices[j] - prices[i] + earn, dp[j - 1], dp[j])
            print(dp)
        return dp[-1] if len(prices) > 0 else 0


class SolutionV2:
    def maxProfit(self, prices) -> int:
        dp = [[0] * 3 for _ in range(len(prices))] # 三个状态 0 当天不持股，1 当天持股(活买入)，2 当天卖出
        dp[0][1] = -prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][2])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
            dp[i][2] = dp[i - 1][1] + prices[i]
            print(dp[i])
        return max(dp[-1][0], dp[-1][2])


print(SolutionV2().maxProfit([1,2,3,0,2]))