# 递增子序列
# medium
'''
给定一个整型数组, 你的任务是找到所有该数组的递增子序列，递增子序列的长度至少是2。

示例:

输入: [4, 6, 7, 7]
输出: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
说明:

给定数组的长度不会超过15。
数组中的整数范围是 [-100,100]。
给定数组中可能包含重复数字，相等的数字应该被视为递增的一种情况。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/increasing-subsequences
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

-------------------------------------------
题解：dfs，回溯
顺序遍历每个数，对每个数dfs，dfs 对当前数之后的满足 >= 条件的数进行输出（需要判重），再对这个数再dfs，比较暴力

回溯优化，此题可以回溯法做，和 al-22 类似
一个枚举子序列的通用模板
temp, ans = [], []
def dfs(cur, nums):
    if cur == len(nums):
        if isValid() and notVisited():
            ans.append(temp)
        return
    // 第一步，选择当前元素之后的 dfs
    temp.append(nums[cur])
    dfs(cur + 1, nums)
    temp.pop() // 回溯
    // 第二步，不选择当前元素之后的 dfs
    dfs(cur + 1, nums)

第一步 dfs 比较简单，此题里因为需要递增，所以判下当前元素是否大于上次选择的元素，如果满足那么就执行第一步，不然第二步
第二步，因为需要有去重，所以这里需要判下当前元素和上次选择的元素是否相等，如果不相等那么执行第二步
    如果有连续两个数相同的时候，有4中选择：
    1. 两个都选择
    2. 前面的选，后面的不选
    3. 前面的不选，后面的选
    4. 两个都不选
    其实 2，3 的结果是一样的，上面的第二步的判法是将 2 的情况舍弃了，就不继续 dfs，保留了 3 的情况，从而达到去重

'''

import copy

class Solution:
    def findSubsequences(self, nums):
        ans = []
        def dfs(index, arr):
            for i in range(index + 1, len(nums)):
                if nums[i] >= nums[index]:
                    narr = copy.deepcopy(arr)
                    narr.append(nums[i])
                    if not narr in ans:
                        ans.append(narr)
                    dfs(i, narr)
        for i in range(len(nums) - 1):
            dfs(i, [nums[i]])
        return ans


class Solution2:
    def findSubsequences(self, nums):
        temp = []
        ans = []
        minInt = -10 ** 9
        def dfs(index, last):
            if index == len(nums):
                if len(temp) >= 2:
                    ans.append(copy.deepcopy(temp))
                return
            if nums[index] >= last:
                temp.append(nums[index])
                dfs(index + 1, nums[index])
                temp.pop()
            if nums[index] != last:
                dfs(index + 1, last)
        dfs(0, minInt)
        return ans



print(Solution2().findSubsequences([4, 6, 7, 7]))
