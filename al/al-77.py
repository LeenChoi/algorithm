# 组合
# medium
'''
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例:

输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combinations
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

------------------------------------------
题解：回溯
典型回溯题, +1-1 的做就行

'''

import copy

class Solution:
    def combine(self, n: int, k: int):
        ans, group = [], []
        def backtrack(num):
            if len(group) == k:
                tmp = copy.deepcopy(group)
                ans.append(tmp)
                return
            if num > n:
                return
            group.append(num)
            backtrack(num + 1)
            group.pop()
            backtrack(num + 1)
        
        backtrack(1)
        return ans
            

print(Solution().combine(4, 2))
        