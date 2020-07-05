# 通配符匹配
# hard
'''
给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。

'?' 可以匹配任何单个字符。
'*' 可以匹配任意字符串（包括空字符串）。
两个字符串完全匹配才算匹配成功。

说明:
s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。

示例 1:
输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。

示例 2:
输入:
s = "aa"
p = "*"
输出: true
解释: '*' 可以匹配任意字符串。

示例 3:
输入:
s = "cb"
p = "?a"
输出: false
解释: '?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。

示例 4:
输入:
s = "adceb"
p = "*a*b"
输出: true
解释: 第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".

示例 5:
输入:
s = "acdcb"
p = "a*c?b"
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/wildcard-matching
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

--------------------------------
题解：动态规划

如果当前 p 不是 '*' 那么好办，判断下 s 和 p 是否相等，或者 p 等于 '?'，直接 dp[i][j] = dp[i-1][j-1] 继承就好
如果当前 p 是 '*', 因为'*'是可以匹配空字符，所以比较下 dp[i][j-1]，看看 '*' 前面的字符是否能和 s 当前的匹配上，如果能匹配，那么当前 '*' 也能匹配
    再就是比较下 dp[i-1][j]，因为 '*' 可以匹配任一个字符，所以看下 s 的前一个字符状态能否和 '*' 匹配上
    (有可能 '*' 之前的串就已经匹配不上)，如果能，那么当前 '*' 也能匹配
    
之前我还判断了 dp[i-1][j-1], 但其实有点多余，因为生成 dp[i-1][j] 的状态的时候已经将它的前一个状态(dp[i][j-1]) 即 dp[i-1][j-1] 继承过来了
而 dp[i-1][j] 又是本次需要的状态转移，所以已经涵盖了 dp[i-1][j-1]


'''


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = True
        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j - 1] != '*':
                    if i - 1 >= 0 and (p[j - 1] == '?' or p[j - 1] == s[i - 1]):
                        dp[i][j] = dp[i - 1][j - 1]
                else:
                    if i - 1 >= 0:
                        dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
                    else:
                        dp[i][j] = dp[i][j - 1]
        return dp[m][n]


print(Solution().isMatch('adceb', '*a*b'))
print(Solution().isMatch('acdcb', 'a*c?b'))
print(Solution().isMatch('aa', '*'))
print(Solution().isMatch('', 'a'))
print(Solution().isMatch('', '?'))
print(Solution().isMatch('a', 'a*'))
