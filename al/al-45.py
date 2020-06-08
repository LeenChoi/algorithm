# 跳跃游戏II
'''
给定一个非负整数数组，你最初位于数组的第一个位置。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
你的目标是使用最少的跳跃次数到达数组的最后一个位置。

输入: [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。

---------------------------------
题解： 贪心
    要找出每一阶跳，能跳动的范围，比如上例,第一阶的跳动范围是 [2,(3,1),1,4]
    第二阶能跳动的范围是 [2,3,1,(1,4)], 至此结束，最少跳跃次数是2
    思路方向在于记录本次跳动的范围，然后遍历，找出下一阶能跳动的范围，迭代

'''

class Solution:
    def jump(self, nums) -> int:
        l, r, jump = 0, 0, 0
        length = len(nums)
        for i in range(0, length):
            if r >= length - 1:
                break
            if i >= l and i <= r:
                if i + nums[i] > r:
                    l = r + 1
                    r = min(i + nums[i], length - 1)
                    jump += 1
            elif i < l and i + nums[i] > r:
                r = max(min(i + nums[i], length - 1), r)
            
        return jump
            

class SolutionV2:
    def jump(self, nums) -> int:
        m, end, jump = 0, 0, 0
        l = len(nums)
        for i in range(0, l):
            if i >= l - 1:
                break
            m = max(i + nums[i], m)
            if m >= l - 1:
                jump += 1
                break
            if i >= end:
                end = m
                jump += 1
            
        return jump


solution = SolutionV2()
res = solution.jump([2,3,1,1,4])
print(res)