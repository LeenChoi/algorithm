# 搜索旋转排序数组
'''
假设按照升序排序的数组在预先未知的某个点上进行了旋转。
( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
你可以假设数组中不存在重复的元素。
你的算法时间复杂度必须是 O(log n) 级别。

输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4

输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1

-------------------------------------
题解：二分法，启发点在于比较下首元素和中间元素的大小，如果首元素更大，说明旋转点在数组前半段，否则在后半段，
    然后判断 target 是否在平滑的那段数组里，如果是，那就和正常数组二分法一样，如果不是，说明在有旋转点的数组段里，
    那就继续迭代，下次迭代继续做和本次相同的事情


'''


class Solution:
    def search(self, nums, target: int) -> int:
        l = len(nums)
        if l == 0:
            return -1
        
        head, tail = 0, l - 1
        i = tail // 2

        while nums[i] != target:
            if head == tail:
                return -1
            if target == nums[head]:
                return head
            if target == nums[tail]:
                return tail

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
        return i



solution = Solution()
res = solution.search([5,6,7,0,1,2], 2)
print(res)