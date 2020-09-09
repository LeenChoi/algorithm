# 组合总和 II
# medium
'''
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

说明：

所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
示例 2:

输入: candidates = [2,5,2,1,2], target = 5,
所求解集为:
[
  [1,2,2],
  [5]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

----------------------------------------------------
题解: 回溯 + 剪枝
这题因为要去重，全罗列出来后判重复去重肯定是费时的，需要罗列的时候就利用手段剪枝，剪枝去重手段和 al-491 有点像
具体做法是：
    首先原数组先要排个序，这样相同元素能聚到一块去，方便判断去重，示例2 排序后 [1,2,2,2,5]
    当递归遍历到第一个 2 的时候，此时可以选或不选，就是常规回溯的 +1-1。
    但这里有个区别是，选 2 的话，是选择了 2 这个数字，而不是当前 2 这个元素，如果不选，那么应该后续的 2 全跳过，直接判断要不要选择 5。
    如果选了 2，那么这个 +1 操作的后续递归中将会面临剩下元素 [2,2,5] 中选不选 2。

代码需要递归和迭代结合，这个是难点之一，递归函数里面的迭代是为了迭代找出本次递归可满足条件的单个元素
+1-1 放到迭代里去做了，所以本次递归完成的的始终是对单个元素的筛选，迭代中判断前后元素，如果相同那么直接跳过，即去重

上面这个是大剪枝，还有个小剪枝，就是如果当前元素选了后，组合的和大于目标值，那么包括本次的递归以及后续递归都不需要了
已经不满足题意了，所以直接return即可，此为小剪枝

'''

import copy

class Solution:
    def combinationSum2(self, candidates, target: int):
        candidates.sort()
        ans, group = [], []
        n = len(candidates)
        _sum = 0
        def backstrap(index):
            nonlocal _sum
            if _sum >= target:
                if _sum == target:
                    tmp = copy.deepcopy(group)
                    ans.append(tmp)
                return
            for i in range(index, n):
                if _sum + candidates[index] > target:
                    break
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                group.append(candidates[i])
                _sum += candidates[i]
                backstrap(i + 1)
                group.pop()
                _sum -= candidates[i]
        backstrap(0)
        return ans
        
                
# print(Solution().combinationSum2([2,5,2,1,2], 5))
print(Solution().combinationSum2([10,1,2,7,6,1,5], 8))