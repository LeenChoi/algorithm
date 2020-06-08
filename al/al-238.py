# 除自身以外数组的乘积
# medium
'''
给你一个长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。

示例:
输入: [1,2,3,4]
输出: [24,12,8,6]
 
提示：题目数据保证数组之中任意元素的全部前缀元素和后缀（甚至是整个数组）的乘积都在 32 位整数范围内。

说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。

进阶：
你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）

------------------------------------------------
题解：从左右分别遍历乘积，遍历到第i位，分别把遍历中得到的乘积(不算自己)相乘即可

'''


class Solution:
    def productExceptSelf(self, nums):
        length = len(nums)
        ans = [1] * length
        ascProduct, descProduct = 1, 1
        for i in range(0, length):
            j = length - 1 - i
            ans[i] *= ascProduct
            ans[j] *= descProduct
            ascProduct *= nums[i]
            descProduct *= nums[j]
        return ans


print(Solution().productExceptSelf([1,2,3,4,5]))