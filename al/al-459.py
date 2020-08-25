-# 重复的子字符串
# easy
'''
给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成。给定的字符串只含有小写英文字母，并且长度不超过10000。

示例 1:

输入: "abab"

输出: True

解释: 可由子字符串 "ab" 重复两次构成。

示例 2:

输入: "aba"

输出: False

示例 3:

输入: "abcabcabcabc"

输出: True

解释: 可由子字符串 "abc" 重复四次构成。 (或者子字符串 "abcabc" 重复两次构成。)

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/repeated-substring-pattern
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

-------------------------------------------
题解：
如果字符串满足，比如子串长度为 n' 那么一定存在 s[i] == s[i - n']，利用这个特性遍历盘一遍就可以，
子串一定不大于 n/2，所以遍历到 n/2 即可

还有一种方法，字符串满足的话 s+s 里除了前后本身s，一定包含其他 s 子串，所以将 s+s 掐头去尾一个字符后，
判断是否包含 s 子串即可，即变成了包含子串问题，上 kmp 伺候

上面的 kmp 还有优化的方法，其实不用做 s 的匹配过程，生成的 next 数组从中就能判断是否满足题意，
拿 "abcabcabcabc" 来说，他的 next 数组是 [-1, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8]，此串的长度为 12
他本身是满足题意的，这种串的 next 数组的特点是 next[i] = i - n'，比如上面的 next 最后一项 next[11] = 8，
而他的重复子串长度 n' = 3，所以只要判断 next[-1] 是否满足这个特性即可

注意：因为 next[i] 记录的是当 t[i-1] == t[j-1] 时的 j，当前 t[i] 可能不等于 t[j]，所以我给 t 后面多加了一个字符'*'
可以通过'*'这一位的 next 值，知道原串最后一个字符匹配的 i，j 是否相等，从而满足上述特性判断，得到解

'''


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(n // 2):
            if n % (i + 1) == 0:
                if all(s[j] == s[j - i - 1] for j in range(i + 1, n)):
                    return True
        return False

        # 方法2 如果 s 满足，那么 s + s 里除首位开始和 len(s) 处开始以外，一定会有 s 子串
        # return (s + s).find(s, 1) != len(s)


class Solution2:
    def repeatedSubstringPattern(self, s: str) -> bool:
        def kmp(s, t):
            i, j = -1, 0
            _next = [-1] * len(t)
            while j < len(t) - 1:
                if i == -1 or t[i] == t[j]:
                    i += 1
                    j += 1
                    _next[j] = i
                else:
                    i = _next[i]
            print(_next)

            # 如果 s 满足的话，s + s 掐头去尾后，还应该包含 s 子串，所以 si 从 1 开始，遍历到 -2 位置
            si, ti = 1, 0
            while si < len(s) - 1:
                # ti == -1 判断是因为 _next[0] 为 -1，并且表明连首字母都没匹配，得向后移一位继续判断
                if ti == -1 or s[si] == t[ti]:
                    si += 1
                    ti += 1
                else:
                    ti = _next[ti]
                if ti >= len(t):
                    return True
                if len(t) - ti > len(s) - si:
                    break
            return False

        return kmp(s + s, s)


class Solution3:
    def repeatedSubstringPattern(self, s: str) -> bool:
        def kmp(t):
            i, j = -1, 0
            n = len(t)
            t = t + '*'
            _next = [-1] * len(t)
            while j < len(t) - 1:
                if i == -1 or t[i] == t[j]:
                    i += 1
                    j += 1
                    _next[j] = i
                else:
                    i = _next[i]
            print(_next)
            nn = len(t)
            return _next[nn - 1] != 0 and n % (nn - 1 - _next[nn - 1]) == 0

        return kmp(s)

# print(Solution3().repeatedSubstringPattern('abcabcabcabc'))
print(Solution3().repeatedSubstringPattern('abab'))
print(Solution3().repeatedSubstringPattern('abac'))