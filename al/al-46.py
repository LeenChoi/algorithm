# 全排列
# medium
'''
给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

-------------------------------------------
题解：回溯
全排列就是元素之间的交换，一个循环，将第一个元素和后面的每一个交换，交换后，剩下的[1:]数组继续递归，
当然也可以不交换进行下一步递归，不交换就是回溯

'''

import copy

class Solution:
    def permute(self, nums):
        ans = []
        def backtrack(cur):
            if cur == len(nums) - 1:
                tmp = copy.deepcopy(nums)
                ans.append(tmp)
                return
            for i in range(cur, len(nums)):
                nums[cur], nums[i] = nums[i], nums[cur]
                backtrack(cur + 1)
                nums[cur], nums[i] = nums[i], nums[cur]
        backtrack(0)
        return ans


print(Solution().permute([1,2,3]))