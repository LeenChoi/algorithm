# 正则表达式匹配
# hard
'''
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。

说明:
s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。

示例 1:
输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。

示例 2:
输入:
s = "aa"
p = "a*"
输出: true
解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。

示例 3:
输入:
s = "ab"
p = ".*"
输出: true
解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。

示例 4:
输入:
s = "aab"
p = "c*a*b"
输出: true
解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。

示例 5:
输入:
s = "mississippi"
p = "mis*is*p*."
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/regular-expression-matching
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

------------------------------------------
题解：动态规划
设 dp[i][j] 为 s 到第 i 位，p 到第 j 位时是否匹配
当 p[j] != '*' 的时候，当 s[i] == p[j] (p[j]为字母或者'.'的时候), 那么 dp[i][j] = dp[i-1][j-1]，否则为 false
当 p[j] == '*' 时，需要判断下 p[j-1] 和 s[i], 这时分两种情况
1.如果 p[j-1] != s[i]，那么可以视为当前 '*' 将前面的 p[j-1] 重复了 0 次，这时 dp[i][j] 将继承 dp[i][j-2] 的状态
2.如果 p[j-1] == s[i], 又有以下两类场景
    视重复p[j-1] 0 次时，dp[i][j] = dp[i][j-2]
    为什么要假设重复0次？因为会有这种情况 s='mi[s]' p='mis[s]*', 此时虽然s[2],p[4]相等, 但如果按 p[j-1] 重复了一次算的话
    dp[i][j] 要按继承 dp[i-1][j-2] (下面的场景)来算，但 dp[i-1][j-2] 即 dp[1][2] 其实是 false，如果按重复 0 次算的话
    那么将继承dp[i][j-2] 即 dp[2][2]，其值是 true，将正确继承状态

    重复了 1 次时，dp[i][j] = dp[i-1][j-2] \    换个思路可以改写为 dp[i-1][j], 如果 s[i] 是重复了 s[i-1]
    重复了 2 次时，dp[i][j] = dp[i-2][j-2] -|=> 那么 dp[i][j] 可以直接继承 dp[i-1][j], 但如果 s[i] != s[i-1]，有两种情况
    重复了 3 次时，dp[i][j] = dp[i-3][j-2] /    可以当做 s[i] 是重复1次或重复0次，重复1次，还是此问题，重复0次，就退到了上个问题

                        p[j] != '*': / dp[i-1][j-1] (s[i] == p[j] 或 p[j] == '.')
整理后的公式为 dp[i][j] =              \ false
                        p[j] == '*': / dp[i-1][j] or dp[i][j-2] (s[i] == p[j-1] 或 p[j] == '.')
                                     \ dp[i][j-2]


'''


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        def match(i, j):
            if i < 0:
                return False # 传进来的 i < 0 表示s为空串，空串和任何字符都匹配不了
            return s[i] == p[j] or p[j] == '.'

        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for i in range(0, m + 1): # i == 0 为空串，空串有可能会被开头为 a* 的匹配串匹配到
            for j in range(1, n + 1):
                if p[j - 1] != '*':
                    dp[i][j] = dp[i - 1][j - 1] if match(i - 1, j - 1) else False
                else:
                    dp[i][j] = (dp[i][j - 2] or dp[i - 1][j]) if match(i - 1, j - 2) else dp[i][j - 2]
        return dp[m][n]


print(Solution().isMatch('aab', 'c*a*b'))

            
