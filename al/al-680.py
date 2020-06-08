# 验证回文字符串 Ⅱ
'''
给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。

示例 1:
输入: "aba"
输出: True

示例 2:
输入: "abca"
输出: True
解释: 你可以删除c字符。

注意:
字符串只包含从 a-z 的小写字母。字符串的最大长度是50000。

'''


class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        diff = 0
        ci, cj = 0, 0
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                if diff == 0:
                    ci = i
                    cj = j
                    j -= 1
                elif diff == 1:
                    i = ci + 1
                    j = cj
                else:
                    return False
                diff += 1
        return True


solution = Solution()
# res = solution.validPalindrome("ebcbbececabbacecbbcbe")
res = solution.validPalindrome("abc")
print(res)