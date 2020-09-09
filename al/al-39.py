# 组合总和
# medium
'''
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 
示例 1：

输入：candidates = [2,3,6,7], target = 7,
所求解集为：
[
  [7],
  [2,2,3]
]
示例 2：

输入：candidates = [2,3,5], target = 8,
所求解集为：
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
 

提示：

1 <= candidates.length <= 30
1 <= candidates[i] <= 200
candidate 中的每个元素都是独一无二的。
1 <= target <= 500

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

-------------------------------------------------------
题解: 回溯
这种罗列的问题典型就是回溯，+1-1 递归操作，只不过这题可以反复选，所以 +1 后还递归当前本身，-1 才递归下一个

'''

import copy

class Solution:
    def combinationSum(self, candidates, target: int):
        ans, group = [], []
        _sum = 0
        def backstrap(index):
            if index >= len(candidates):
                return
            nonlocal _sum
            if _sum >= target:
                if _sum == target:
                    tmp = copy.deepcopy(group)
                    ans.append(tmp)
                return
            group.append(candidates[index])
            _sum += candidates[index]
            backstrap(index)
            group.pop()
            _sum -= candidates[index]
            backstrap(index + 1)
        backstrap(0)
        return ans


print(Solution().combinationSum([2,3,5], 8))