# 最长有效括号
# hard
'''
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

示例 1:
输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"

示例 2:
输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-valid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

---------------------------------------
题解：动态规划

1. 动态规划思路
    s[i] == '('时候，dp[i] 记录它前面可行子串的起始位置，如果前面不是可行串，那么记录自己的位置
    s[i] == ')'时候，dp[i] 记录与之配套的'('的位置，
    细节：
    s[i] == '('
    如果前一个是'('，那么dp[i] = i
    如果前一个是')'，因为这个')'可能与前面的串形成有效串，所以此时dp[i]记录可行串的起始位置，即dp[i-1]，
    注意如果前一个')'无法形成有效串，此时'('应该为新的可行串的起始位置，此时dp[i] = i

    s[i] == ')'
    如果前一个是'('，可与之配套，所以 dp[i] 记录 dp[i-1]，因为 dp[i-1] 记录的是整个可行串的起始位置，
    所以此时 dp[i] 也记录了整个可行串的起始位置，此时记录下可行串长度
    如果前一个是')'，需要看下前一个')'参与的整个可行串的前一个字符是不是'('，如果是那么它和此时的')'又能配套
    所以 dp[i] 记录可行串前面的这个'('的位置，即 dp[i-1]-1，因为这个'('前面可能也是个可行串，
    所以要记录它前面可行串的起始位置，即dp[dp[i-1]-1]

'''


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        _max = 0
        dp = [-1] * (len(s) + 1)
        for i in range(len(s)):
            if s[i] == '(':
                if i - 1 >= 0 and s[i - 1] == ')':
                    dp[i + 1] = dp[i] if dp[i] != -1 else i
                else:
                    dp[i + 1] = i
            else:
                if i - 1 >= 0:
                    if s[i - 1] == '(':
                        dp[i + 1] = dp[i]
                        _max = max(_max, i - dp[i] + 1)
                    elif dp[i] - 1 >= 0 and s[dp[i] - 1] == '(':
                        dp[i + 1] = dp[dp[i]] # dp[dp[i] - 1 + 1]
                        _max = max(_max, i - dp[i + 1] + 1)
        return _max


print(Solution().longestValidParentheses(")()())"))
print(Solution().longestValidParentheses("(()"))
print(Solution().longestValidParentheses("(()())()()())"))
print(Solution().longestValidParentheses("()(())"))
        
