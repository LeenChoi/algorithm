# 数组中数字出现的次数
'''
一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。
要求时间复杂度是O(n)，空间复杂度是O(1)。

输入：nums = [4,1,4,6]
输出：[1,6] 或 [6,1]

输入：nums = [1,2,10,4,1,4,3,3]
输出：[2,10] 或 [10,2]

----------------------------------
题解：数组xor一遍得出 x，即是两个单数的xor结果，然后对 x 从0位开始按位遍历找到是1的那个位，
    xor结果为1代表两个数在这个位是不相等的，找出这个位偏移 offset，然后重新对数组遍历做 offset 位判断，是0的分一组，是1的分另一个组
    因为相等的放一组xor结果肯定是0，不影响结果要找的单数，这样最终会得到一个单数在一边的两个数组，对两个数组再做一遍xor即可
    优化方案： 只对一个分组做xor 得 a，另一个数通过 a ^ x 能算出

'''

class Solution:
    def singleNumbers(self, nums):
        a, b, x = 0, 0, 0
        for i in range(0, len(nums)):
            x ^= nums[i]
        
        offset = 1
        while offset <= x and x & offset == 0:
            offset = offset << 1

        for i in range(0, len(nums)):
            if nums[i] & offset == 0:
                a ^= nums[i]
            else:
                b ^= nums[i]
        return [a, b]


solution = Solution()
res = solution.singleNumbers([1,2,10,4,1,4,3,3])
print(res)