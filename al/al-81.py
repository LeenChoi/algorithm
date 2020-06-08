# 搜索旋转排序数组 II
'''
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,0,1,2,2,5,6] 可能变为 [2,5,6,0,0,1,2] )。

编写一个函数来判断给定的目标值是否存在于数组中。若存在返回 true，否则返回 false。

示例 1:

输入: nums = [2,5,6,0,0,1,2], target = 0
输出: true
示例 2:

输入: nums = [2,5,6,0,0,1,2], target = 3
输出: false

----------------------------------------
题解： 和 al-33 一样二分法，只不过在二分法之前多了一层 head，i，tail 三个元素判断，比较下大小
    如果相同，那么就无法判断二分法该向哪个方向，所以要从 head 到 tail 遍历一遍

'''


class Solution:
    def search(self, nums, target: int) -> int:
        l = len(nums)
        if l == 0:
            return False
        
        head, tail = 0, l - 1
        i = tail // 2

        while nums[i] != target:
            if head == tail:
                return False
            if target == nums[head]:
                return True
            if target == nums[tail]:
                return True

            if nums[head] == nums[tail] and nums[head] == nums[i]:
                for i in range(head, tail + 1):
                    if nums[i] == target:
                        return True
                return False

            if nums[0] > nums[i]:
                if target < nums[0] and target >= nums[i]:
                    head = i + 1
                    i = (head + tail) // 2
                else:
                    tail = i
                    i = (head + tail) // 2
            else:
                if target < nums[i] and target >= nums[0]:
                    tail = i
                    i = (head + tail) // 2
                else:
                    head = i + 1
                    i = (head + tail) // 2
        return True



solution = Solution()
res = solution.search([1,3,1,1,1], 3)
print(res)