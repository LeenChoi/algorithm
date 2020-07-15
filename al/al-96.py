# 不同的二叉搜索树
# medium
'''
给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？

示例:

输入: 3
输出: 5
解释:
给定 n = 3, 一共有 5 种不同结构的二叉搜索树:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-binary-search-trees
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

-------------------------------------
题解：动态规划，数学：卡塔兰数

'''


class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        for i in range(2, n + 1):
            for j in range((i + 1) // 2):
                dp[i] += dp[j] * dp[i - j - 1]
            dp[i] *= 2
            if i % 2 == 1:
                dp[i] -= dp[i // 2] ** 2
 
            # for j in range(i):
                # dp[i] += dp[j] * dp[i - j - 1]
        print(dp)
        return dp[n]


class Solution2:
    def numTrees(self, n: int) -> int:
        c = 1
        for i in range(n):
            c = c * 2*(2*i+1) // (i+2) # 卡塔兰数通项公式
        return c
    
print(Solution2().numTrees(5))