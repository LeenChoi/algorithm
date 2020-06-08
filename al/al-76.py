#  最小覆盖子串
'''
给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字符的最小子串。

示例：
输入: S = "ADOBECODEBANC", T = "ABC"
输出: "BANC"

说明：
如果 S 中不存这样的子串，则返回空字符串 ""。
如果 S 中存在这样的子串，我们保证它是唯一的答案。

--------------------------------------
题解：滑动窗口
l,r 指针，r 先移动，碰到 T 里的元素就记录下状态，如果 S[l, r] 满足条件，那就先暂存这个答案与之后的比较,
然后 l 向右收敛，找到最短的那个

xxxxabc 的这种情况找abc 其实 l 不需要从 0 位开始一步步收敛，我的做法是做一个数组 a，
r 向右遍历的时候，如果碰到 T 中元素，那么将这个元素的下标存放到 a 中，那么 l 只需在 a 中遍历即可。

最初我是做了两个map，一个 m 记录当前 [l, r] 之间的 T 元素个数情况，另一个是 need 记录上限，
用来判断 m 满不满足条件，但是慢的一逼

官方题解是，用一个 map (初始 T 中各元素的个数，上述的need) 和一个 length (初始 T 的长度)

r 向右遍历的时候，碰到一个 T 中元素，map[t] -1，map[t] 可以是负数，因为某个 t 会过多，
不过等 l 收敛的时候，会将这些多出的 t 过滤掉。当 map[t] > 0 时 length -1

当length == 0时，表明 T 中的所有元素均被遍历过，此时 [l,r]就是一个解，此时比较下最小解，然后 l 向右收敛，

l 向右遍历的时候，碰到一个 T 中元素，map[t] +1, 当 map[t] 又大于 0时，length +1，表明 [l, r]中又缺某个 t 了

最终 r 遍历到 len(S), 并且 length > 0 退出遍历


'''     


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        r, i = 0, 0
        need, a = {}, []
        count = len(t)
        ans = (0, 0)

        for c in t:
            if need.get(c) == None:
                need[c] = 1
            else:
                need[c] += 1

        while True:
            if count > 0:
                if r < len(s) and s[r] in t:
                    if need[s[r]] > 0:
                        count -= 1
                    need[s[r]] -= 1    
                    a.append(r)
                r += 1
            else:
                l = a[i]
                if ans[1] - ans[0] == 0 or r - l < ans[1] -ans[0]:
                    ans = (l, r)
                if need[s[l]] == 0:
                    count += 1
                need[s[l]] += 1
                i += 1
            
            if r >= len(s) and count > 0:
                break
        return s[ans[0]:ans[1]]


print(Solution().minWindow('ADOBECODEBANC', 'ABC'))
print(Solution().minWindow('bba', 'ab'))