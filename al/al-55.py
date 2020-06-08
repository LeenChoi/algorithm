# 跳跃游戏
'''
给定一个非负整数数组，你最初位于数组的第一个位置。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
判断你是否能够到达最后一个位置。

输入: [2,3,1,1,4]
输出: true
解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。

-------------------------------
题解：直接从后遍历，判断前面的点能否到达现在的点，如果能就转到前面的点进行下一次迭代
    最终，如果能转到0点，那么就是个可到达的数组

'''

class Solution:
    def canJump(self, nums) -> bool:
        j = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= j:
                j = i
                
        return j == 0


solution = Solution()
res = solution.canJump([3,2,1,0,4])
print(res)
