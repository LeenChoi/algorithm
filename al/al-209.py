# 长度最小的子数组
# medium
'''
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组，并返回其长度。如果不存在符合条件的连续子数组，返回 0。

示例: 
输入: s = 7, nums = [2,3,1,2,4,3]
输出: 2
解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。

进阶:
如果你已经完成了O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-size-subarray-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

------------------------------------
题解:
    滑动窗口 O(n)
    进阶说的 O(nlogn) 是前缀和+二分查找

'''


class Solution:
    def minSubArrayLen(self, s: int, nums) -> int:
        l, r = 0, -1
        _sum, length = 0, None
        while r < len(nums):
            if _sum < s:
                r += 1
                _sum += nums[r] if r < len(nums) else 0
            else:
                lens = r - l + 1
                length = lens if length == None else min(length, lens)
                _sum -= nums[l]
                l += 1
        return length or 0


# print(Solution().minSubArrayLen(7, [2,3,1,2,4,3]))
print(Solution().minSubArrayLen(3, [1,1]))