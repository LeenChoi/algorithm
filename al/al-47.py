# 全排列 II
# medium
'''
给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:

输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

------------------------------------------------------
题解：回溯
和 al-40 的剪枝方法类似，先排个序，然后从原数组里摘数重新罗列的时候，判断如果当前数和它前一个数相同，那么跳过，直到遍历到不同的数为止，
因为罗列的时候一连串相同的数里面，第一个数已经罗列进去了，所以这么判断将会把后面一连串相同的数全跳过，让下一次递归去判断
要不要再选择这些相同的数，即 [1,1,2] 里面有相同的 1，每次递归里做的是要不要选 1 这个数字，而不是要不要选当前 1 那个元素

最开始我按 al-46 的思路，将原数组的元素递归交换，但此题因为有重复元素，按这个方法会得到重复的答案集，
官方题解的做法即上述的，从原数组摘数重新罗列，做一个 visit 数组记录哪个元素已经摘过，
然后罗列的时候，当前递归里判断当前要摘的元素是否已经被摘过，是否和它前一个元素是否相同，是否跳过

    i > 0 and not visit[i - 1] and nums[i - 1] == nums[i]:
这段判断是精髓，它表示如果前一个相同的数在上次递归已经被摘过，那么本次递归我要重新考虑是否要再选择这个相同的数，
而如果上次递归没有选择，那么表明这条递归链上，当前罗列的位置上我不想选择这个数，那么一连串这些相同元素都要跳过。

!!! 这个是这个算法题的核心递归判断，很难想到，需要巩固消化

'''

import copy

class Solution:
    def permuteUnique(self, nums):
        nums.sort()
        ans, group = [], []
        visit = [False] * len(nums)
        def backtrack(index):
            if index >= len(nums):
                ans.append(copy.deepcopy(group))
                return
            for i in range(len(nums)):
                if visit[i] or i > 0 and not visit[i - 1] and nums[i - 1] == nums[i]:
                    continue
                group.append(nums[i])
                visit[i] = True
                backtrack(index + 1)
                group.pop()
                visit[i] = False
        backtrack(0)
        return ans


print(Solution().permuteUnique([1,2,3]))
print(Solution().permuteUnique([2,2,1,1]))
