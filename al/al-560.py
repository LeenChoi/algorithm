# 和为K的子数组
'''
给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。

输入:nums = [1,1,1], k = 2
输出: 2 (注意，只输出个数), [1,1] 与 [1,1] 为两种不同的情况。

--------------------------------
题解：遍历数组，记录一个 [sum(0, i)->count] 的map，遍历到 i 的时候查找 [sum(0, i) - k] 在map里有没有，
    有的话将里面存的count累加上，map初始化的要给一个 [0->1] 值，因为还没遍历的时候 sum 为 0 是一种情况

'''

class Solution:
    def subarraySum(self, nums, k: int) -> int:
        m = {0: 1}
        sum = 0
        count = 0
        for i in range(0, len(nums)):
            if i == 0:
                sum = nums[i]
            else: 
                sum += nums[i]

            if m.get(sum - k) != None:
                count += m[sum - k]

            if m.get(sum) != None:
                m[sum] += 1
            else:
                m[sum] = 1

        return count

    
solution = Solution()
res = solution.subarraySum([1,2,3], 3)
print(res)

        


