// 买卖股票的最佳时机含手续费
// medium
/*
* 给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；非负整数 fee 代表了交易股票的手续费用。
*
* 你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。
*
* 返回获得利润的最大值。
*
* 注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。
*
* 示例 1:
*
* 输入: prices = [1, 3, 2, 8, 4, 9], fee = 2
* 输出: 8
* 解释: 能够达到的最大利润:
* 在此处买入 prices[0] = 1
* 在此处卖出 prices[3] = 8
* 在此处买入 prices[4] = 4
* 在此处卖出 prices[5] = 9
* 总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
* 注意:
*
* 0 < prices.length <= 50000.
* 0 < prices[i] < 50000.
* 0 <= fee < 50000.
*
* 来源：力扣（LeetCode）
* 链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee
* 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*
* -----------------------------------------------------------
* 题解：动态规划，贪心
* 动态规划：分两种情况转移状态，一是手里持有股票(当天买了，或者之前持有)，二是手里没有股票(当天卖了，或者之前没有)，
* 然后分别转移状态，手里持股是当天买完剩的钱和之前持有时手里的钱比较大值，手里没股是当天卖了后手里的钱和之前没有是手里剩的钱的比较大值。
* 当然转移的时候需要把手续费带上。
*
* 贪心：按位遍历，后面数减掉手续费后比当前数大就可以选择卖掉，和al-122的贪心解法差不多。但因为有手续费，不能单纯只判前后大小，
* 后面可能有更大的价格，卖掉后会赚更多，因为一次大交易收益大于两次小交易，因为会扣两次手续费。
* 这里有个小操作，我们可以把手续费在买入的时候就加上，卖掉的时候直接扣买入价就ok，然后第一次卖掉后刷新买入价的时候，可以不将手续费带上，
* 因为可能后面有更高的价格，给个反悔的机会，比如1元买入加上手续费2元后3元，5元时卖出，这时假定参与下一场交易的买入价为当前5元，但不带手续费，
* 后面如果没有比5元更低的价格(加上手续费后),遇到10元价格，直接卖掉，因为5元时没有加手续费，所以实际交易是1元价格加2元手续费3元买入，10元卖出，中途的5元卖出其实给反悔掉了。
*
 */

package main

import "fmt"

func main() {
	fmt.Println(maxProfit2([]int{1, 3, 2, 8, 4, 9}, 2))
}

func maxProfit(prices []int, fee int) int {
	dp := make([][2]int, len(prices))
	dp[0][1] = -prices[0]
	for i := 1; i < len(prices); i++ {
		dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i]-fee)
		dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])
	}
	fmt.Println(dp)
	return dp[len(prices)-1][0]
}

func maxProfit2(prices []int, fee int) int {
	ans := 0
	buy := prices[0] + fee
	for i := 1; i < len(prices); i++ {
		if prices[i]+fee < buy {
			buy = prices[i] + fee
		} else if prices[i] > buy {
			ans += prices[i] - buy
			buy = prices[i]
		}
	}
	return ans
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
