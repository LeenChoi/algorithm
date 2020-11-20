# 最长快乐字符串
# medium
'''
如果字符串中不含有任何 'aaa'，'bbb' 或 'ccc' 这样的字符串作为子串，那么该字符串就是一个「快乐字符串」。

给你三个整数 a，b ，c，请你返回 任意一个 满足下列全部条件的字符串 s：

s 是一个尽可能长的快乐字符串。
s 中 最多 有a 个字母 'a'、b 个字母 'b'、c 个字母 'c' 。
s 中只含有 'a'、'b' 、'c' 三种字母。
如果不存在这样的字符串 s ，请返回一个空字符串 ""。

 

示例 1：

输入：a = 1, b = 1, c = 7
输出："ccaccbcc"
解释："ccbccacc" 也是一种正确答案。
示例 2：

输入：a = 2, b = 2, c = 1
输出："aabbc"
示例 3：

输入：a = 7, b = 1, c = 0
输出："aabaa"
解释：这是该测试用例的唯一正确答案。
 

提示：

0 <= a, b, c <= 100
a + b + c > 0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-happy-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

-------------------------------------------------
题解：贪心
直接拼字符，优先选个数多的。所以写个选择函数，选择个数最多的，需要判下是否同字符三连，没有满足就返回空字符，表示结束

'''


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        def select(ex):
            nonlocal a, b, c
            ch = ''
            count = 0
            if a > count and ex != 'a':
                ch = 'a'
                count = a
            if b > count and ex != 'b':
                ch = 'b'
                count = b
            if c > count and ex != 'c':
                ch = 'c'
                count = c
            if ch == 'a':
                a -= 1
            elif ch == 'b':
                b -= 1
            elif ch == 'c':
                c -= 1
            return ch

        ans = ''
        pre = ''
        count = 0
        ch = select('')
        while ch != '':
            if pre == ch:
                count += 1
            else:
                pre = ch
                count = 0
            ans += ch
            ex = ''
            if count >= 1:
                ex = ch
            ch = select(ex)
        return ans


print(Solution().longestDiverseString(1,1,7))