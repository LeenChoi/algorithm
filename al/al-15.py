# 三数之和
'''
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。
注意：答案中不可以包含重复的三元组。

给定数组 nums = [-1, 0, 1, 2, -1, -4]，
满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

--------------------------------
题解：
    1. 两数相加算法的延伸(遍历数组，做[value->index]的map，同时先判断下[value-target]在map里有没有记录,有则输出index组合)，
        现在三个数可以遍历两遍将每两个数的和做成map，再遍历一遍按上个方法去找
    2. 双指针：快排的思路，一个基准指针k，两个游标i，j。先做个排序(O-logn), k从做遍历(最小)，判三数和是否大于0，如果大于0，表示j大了，j--
              如果三数和小于0，说明i小了，i++，如果等于0，可以记录组合了，但是要求去除重复，有可能 i的后一项或者j的前一项是与之相同的数，
              所以i，j都判下它的下一位数字，如果相等就直接进到下一位，最终输出最后的组合，然后i++,或者j-- 继续下一次迭代。
              注意，i、j 碰头后，下一轮k的进位迭代的时候要考虑 k 也要相同元素的跳越

'''

class Solution:
    def threeSum(self, nums):
        l = len(nums)
        if l < 3:
            return []

        results = []
        nums.sort()
        k, i, j = 0, 1, l - 1
        while True:
            sum = nums[k] + nums[i] + nums[j]
            if sum > 0:
                j -= 1
            elif sum < 0:
                i += 1
            else:
                if i + 1 < j and nums[i] == nums[i + 1]:
                    i += 1
                    continue
                if j - 1 > i and nums[j] == nums[j - 1]:
                    j -= 1
                    continue
                results.append([nums[k], nums[i], nums[j]])
                i += 1

            if i >= j:
                k += 1
                while nums[k - 1] == nums[k]:
                    if k >= j:
                        break
                    k += 1
                i, j = k + 1, l - 1
            if k >= l - 2:
                break

        return results


solution = Solution()
# res = solution.threeSum([-1, 0, 1, 2, -1, -4])
res = solution.threeSum([0, 0, 0])
print(res)
