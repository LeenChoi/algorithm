# 最短回文串
# hard
'''
给定一个字符串 s，你可以通过在字符串前面添加字符将其转换为回文串。找到并返回可以用这种方式转换的最短回文串。

 

示例 1：

输入：s = "aacecaaa"
输出："aaacecaaa"
示例 2：

输入：s = "abcd"
输出："dcbabcd"
 

提示：

0 <= s.length <= 5 * 104
s 仅由小写英文字母组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shortest-palindrome
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

--------------------------------------------------
题解: kmp
字符串 s，可以看做回文串前缀 s1 + 后缀 s2，怎么去找 s1 的结尾。s 从头遍历，挨个字母向两侧展开判断回文可以找到，
但是效率比较低，是On2。怎么能在On复杂度完成？可以用 kmp 算法。

将 s 翻转成 s'，那么 s' 可以看做是 s2 + s1，将 s' 当做模式串，原串 s 当成匹配串，s' 匹配到末尾时 s 串当前所在的
指针位置即是回文串结束位置。官方题解中没有制造 s' 串，而是用双指针一个从头出发一个从尾部出发，效果是一样的。

'''


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        def getNext(s):
            next = [-1] * len(s)
            i, j = -1, 0
            while j < len(s) - 1:
                if i == -1 or s[i] == s[j]:
                    i += 1
                    j += 1
                    next[j] = i
                else:
                    i = next[i]
            return next

        next = getNext(s)
        i, j = 0, len(s) - 1
        while j >= 0:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                if i == 0:
                    j -= 1
                else:
                    i = next[i]
        return s[:i-1:-1] + s


# print(Solution().shortestPalindrome('aacecaaa'))
print(Solution().shortestPalindrome('abcd'))