# 交错字符串
# hard
'''
给定三个字符串 s1, s2, s3, 验证 s3 是否是由 s1 和 s2 交错组成的。

示例 1:

输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
输出: true
示例 2:

输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/interleaving-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

--------------------------------------
题解：动态规划

如果 s1 的第 i 个字母和 s3 的第 i+j 字母相同，则 dp[i][j] = dp[i-1][j]
另外 s2 的第 j 个字母和 s3 的第 i+j 字母相同，则 dp[i][j] = dp[i][j-1]
最终，将这两种情况合并即可

'''


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if len(s3) != n1 + n2:
            return False
        dp = [False] * (n2 + 1)
        dp[0] = True
        for i in range(n1 + 1):
            for j in range(n2 + 1):
                f1, f2 = None, None
                if i - 1 >= 0:
                    f1 = dp[j] if s1[i - 1] == s3[i + j - 1] else False
                if j - 1 >= 0:
                    f2 = dp[j - 1] if s2[j - 1] == s3[i + j - 1] else False
                if f1 != None or f2 != None:
                    dp[j] = (f1 or False) or (f2 or False)
        return dp[-1]


# print(Solution().isInterleave('a', '', 'c'))
print(Solution().isInterleave("aabcc", "dbbca", "aadbbcbcac"))