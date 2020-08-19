# 最长回文子序列
# medium
'''
给定一个字符串 s ，找到其中最长的回文子序列，并返回该序列的长度。可以假设 s 的最大长度为 1000 。

示例 1:
输入:

"bbbab"
输出:

4
一个可能的最长回文子序列为 "bbbb"。

示例 2:
输入:

"cbbd"
输出:

2
一个可能的最长回文子序列为 "bb"。

提示：

1 <= s.length <= 1000
s 只包含小写英文字母

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

------------------------------------------------
题解：动态规划
设 f(i, j) 为字符串从 i 到 j 为止最长回文子序列的长度，那么：
如果 s[i] == s[j]， f(i, j) = f(i + 1, j - 1) + 2
如果不相等，f(i, j) = max(f(i + 1, j), f(i, j - 1))

还有一种思路，因为是回文，此题可以看做 s 和 reverse(s) 的最长公共子序列，al-1143

'''


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[1] * n for _ in range(n)]
        for i in range(n -1, -1, -1):
            for j in range(i + 1, n):
                    if s[i] == s[j]:
                        dp[i][j] = dp[i + 1][j - 1] + 2 if i + 1 <= j - 1 else 2
                    else:
                        dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][-1]


print(Solution().longestPalindromeSubseq('bbbabbba'))
                        

