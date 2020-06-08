# 最长回文子串
'''
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。

示例 2：
输入: "cbbd"
输出: "bb"
-------------------------------
题解：
    1. 动态规划 
    a[i][j] 代表 i处开头，j处结尾的字符串是否回文 存 true/false
    if a[i+1][j-1] & s[i] == s[j]: a[i][j] = true  没啥难度
    注意下边界条件，就是 j - i == 0 or j - i == 1 的情况
    不能 i,j 从0 遍历，要三指针法
        for l -> [0, max]
            for i -> [0, max]
                j = i + l
    实际都是从 l=1, l=2 开始状态慢慢传递的，状态的根儿在这俩地方

    2. 中心扩展法
    顺序遍历整个字符串，然后从中间向前后展开判断 s[i] == s[j],
    同样也注意下边界，即从 s[i-1]/s[i+1] 处展开，和 s[i]/s[i+1]处展开

    3. Manacher 算法
    以后再研究，复杂的一逼，不会当做面试题

'''


class Solution:
    def spread(self, s, l, r):
        while l - 1 >= 0 and r + 1 < len(s):
            if s[l - 1] == s[r + 1]:
                l -= 1
                r += 1
            else:
                break
        return (l, r)
        

    def longestPalindrome(self, s: str) -> str:
        i, l, r = 0, 0, 0
        ans = s[0] if len(s) > 0 else ''
        while i < len(s) - 1:
            if s[i] == s[i + 1]:
                (l, r) = self.spread(s, i, i + 1)
            if i - 1 >= 0 and s[i - 1] == s[i + 1]:
                (tl, tr) = self.spread(s, i - 1, i + 1)
                if tl < l or tr > r:
                    (l, r) = (tl, tr)
           
            i += 1   
            if len(s[l:r + 1]) > len(ans):
                ans = s[l:r + 1]
        return ans


solution = Solution()
res = solution.longestPalindrome('aaaa')
# res = solution.longestPalindrome("ababababa")
print(res)



            
