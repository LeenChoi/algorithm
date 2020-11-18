# 移动零
# easy
'''
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/move-zeroes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

-----------------------------------------------
题解：双指针
i 从左遍历，如果碰到 0，j 从 i 向后遍历找到第一个非0点，与之交换，接着继续向后遍历 i
此时 i 一定是 0，j 继续像后找非0，再换，直到 j 超出长度退出

'''


class Solution:
    def moveZeroes(self, nums) -> None:
        i, j = 0, -1
        while i < len(nums):
            if nums[i] == 0:
                if j < i:
                    j = i
                while j < len(nums) and nums[j] == 0:
                    j += 1
                if j >= len(nums):
                    break
                nums[i], nums[j] = nums[j], nums[i]
            i += 1
