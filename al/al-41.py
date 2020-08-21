# 缺失的第一个正数
# hard
'''
给你一个未排序的整数数组，请你找出其中没有出现的最小的正整数。

示例 1:

输入: [1,2,0]
输出: 3

示例 2:

输入: [3,4,-1,1]
输出: 2

示例 3:

输入: [7,8,9,11,12]
输出: 1
 

提示：

你的算法的时间复杂度应为O(n)，并且只能使用常数级别的额外空间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/first-missing-positive
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

----------------------------------------------
题解：哈希表标记，置换
哈希：
哈希表正常思路是，遍历数组然后陆续入哈希表，然后从 1 开始递增去哈希表里读，如果读不到那就是解
但是要求常数空间，所以得还个方法，这里利用哈希表其实就是一个标记的作用，标记哪个数出现了
可以直接在原数组中标记，首先遍历数组把 <= 0 的数全部置为大于 n 的数 n + 1，这样数组里就没有负数了，
可以使用负数标记法，重新遍历数组，如果是 n 内的数，将对应位置的数换成负数，最后再遍历找到第一个正整数，
它对应的下标 + 1 即是答案

置换：
置换就是遍历数组，将数对号入座，[3,4,-1,1] --> [1,-1,3,4]，最后遍历一遍找到数和位置不一致的位置 + 1 即是答案

'''


class Solution:
    def firstMissingPositive(self, nums) -> int:
        i = 0
        while i < len(nums):
            if nums[i] <= 0:
                nums.pop(i)
            elif nums[i] > i + 1:
                if nums[i] > len(nums):
                    nums.pop(i)
                else:
                    if nums[i] == nums[nums[i] - 1]:
                        nums.pop(i)
                    else:
                        index = nums[i]
                        nums[i], nums[index - 1] = nums[index - 1], nums[i]
            elif nums[i] <= i:
                if nums[i] == nums[nums[i] - 1]:
                    nums.pop(i)
                else:
                    index = nums[i]
                    nums[i], nums[index - 1] = nums[index - 1], nums[i]
                    i = index
            else:
                i += 1
        ans = 1
        for num in nums:
            if num != ans:
                return ans
            ans += 1
        return ans


class Solution2:
    def firstMissingPositive(self, nums) -> int:
        i, n = 0, len(nums)
        while i < n:
            if  nums[i] >= 1 and nums[i] <= n and nums[i] != i + 1 and nums[i] != nums[nums[i] - 1]:
                j = nums[i] - 1
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        ans = 1
        for num in nums:
            if num != ans:
                return ans
            ans += 1
        return ans

class Solution3:
    def firstMissingPositive(self, nums) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1
        for i in range(n):
            num = abs(nums[i])
            if num > 0 and num <= n:
                nums[num - 1] = -abs(nums[num - 1])
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        return n + 1


    
# print(Solution2().firstMissingPositive([2,1]))
# print(Solution2().firstMissingPositive([3,4,-1,1]))
# print(Solution2().firstMissingPositive([7,8,9,11,12]))
# print(Solution3().firstMissingPositive([1,2,2,1,3,1,0,4,0]))
print(Solution3().firstMissingPositive([3,4,-1,1]))