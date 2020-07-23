# 构建回文串检测
# medium
'''
给你一个字符串 s，请你对 s 的子串进行检测。

每次检测，待检子串都可以表示为 queries[i] = [left, right, k]。我们可以 重新排列 子串 s[left], ..., s[right]，并从中选择 最多 k 项替换成任何小写英文字母。 

如果在上述检测过程中，子串可以变成回文形式的字符串，那么检测结果为 true，否则结果为 false。

返回答案数组 answer[]，其中 answer[i] 是第 i 个待检子串 queries[i] 的检测结果。

注意：在替换时，子串中的每个字母都必须作为 独立的 项进行计数，也就是说，如果 s[left..right] = "aaa" 且 k = 2，我们只能替换其中的两个字母。（另外，任何检测都不会修改原始字符串 s，可以认为每次检测都是独立的）

 

示例：

输入：s = "abcda", queries = [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]
输出：[true,false,false,true,true]
解释：
queries[0] : 子串 = "d"，回文。
queries[1] : 子串 = "bc"，不是回文。
queries[2] : 子串 = "abcd"，只替换 1 个字符是变不成回文串的。
queries[3] : 子串 = "abcd"，可以变成回文的 "abba"。 也可以变成 "baab"，先重新排序变成 "bacd"，然后把 "cd" 替换为 "ab"。
queries[4] : 子串 = "abcda"，可以变成回文的 "abcba"。
 

提示：

1 <= s.length, queries.length <= 10^5
0 <= queries[i][0] <= queries[i][1] < s.length
0 <= queries[i][2] <= s.length
s 中只有小写英文字母

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/can-make-palindrome-from-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

-----------------------------------------------
题解：
这题很巧妙，因为每个子串可以重新排列，看似是脱离大体，针对每个子串做处理就完了，但是！！！ 超时！！！
优化时间有几个出发点：
1. 长度 1 的子串，一定是可以回文的
2. 因为子串可以替换字母，所以如果可替换的数 >= 子串长度 / 2，那么一定是可以回文的
3. 再考虑英文字母总共26个，极端情况这个字串就是单个26个字母组成的，那么如果可替换数 >= 13，就一定能回文
4. 如果上面都不满足，那么需要遍历子串看看有几个奇数个的字母，再比较可替换数

前三个都是边缘优化的小优化项，其实 4 主体判断才是最大需要优化的，因为每个子串我都需要遍历一遍查看有几个奇数个字母，很费
如果我拿到这个子串的时候就能知道有多少奇数字母，那就省了一个大环节。为什么不是直接给一堆字符串，而是给了一个大串，和一些子串？

这就是优化点的方向，利用前缀和的思想，我们遍历大串的每个字母时，可以记录每个字母该位置为止，有多少个字母，
然后如果碰到[i, j]子串，只需从记录中取出两个前缀和做差就能得到这个子串有多少个字母，而此题其实只需要知道有奇数个或偶数个字母，
所以用掩码标记法利用异或运算记录26位标记数即可，然后[i, j]子串，取到i，j位置的两个掩码，再做异或操作，
得出结果判断二进制里有多少个 1，即表示这段子串里有多少奇数个字母，然后和可替换数做比较即可。

'''


class Solution:
    def canMakePaliQueries(self, s: str, queries):
        ans = [True] * len(queries)
        base = 0
        records = [0] * (len(s) + 1)
        for i in range(len(s)):
            base = base ^ (1 << (ord(s[i]) - 97))
            records[i + 1] = base

        for i in range(len(queries)):
            q = queries[i]
            if q[1] - q[0] != 0 or q[2] < (q[1] - q[0] + 1) // 2 or q[2] < 13:
                diff = records[q[1] + 1] ^ records[q[0]]
                count = 0
                while diff != 0:
                    diff = diff & (diff - 1)
                    count += 1
                if q[2] < count // 2:
                    ans[i] = False
        return ans



# print(Solution().canMakePaliQueries("abcda", [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]))
print(Solution().canMakePaliQueries("lyb", [[0,1,0],[2,2,1]]))