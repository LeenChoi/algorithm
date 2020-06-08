# 无重复字符的最长子串
# medium
'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:
输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。

请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

-------------------------------
题解：滑动窗口 (和 al-76 相似)
    hashmap存某个字符出现的位置，r 向右遍历的时候，查map如果之前出现过，
    那么将 l 设置为当前位置，最后比较找出 r-l 最大


'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, _max, m = -1, 0, 0, {}
        while r < len(s):
            i = m.get(s[r])
            if i != None and i > l:
                l = i
            m[s[r]] = r
            if r - l > _max:
                _max = r - l
            r += 1
            
        return _max



print(Solution().lengthOfLongestSubstring('abba'))