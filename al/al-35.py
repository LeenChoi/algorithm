# 搜索插入位置
# easy
'''
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。

示例 1:

输入: [1,3,5,6], 5
输出: 2
示例 2:

输入: [1,3,5,6], 2
输出: 1
示例 3:

输入: [1,3,5,6], 7
输出: 4
示例 4:

输入: [1,3,5,6], 0
输出: 0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-insert-position
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

----------------------------------
题解：二分查找
二分法，没什么难点。要注意的是，像 [1,2,4,5] t=7 这种，因为 7 要插入到最后面，而二分查找只能最大返回数组长度-1的位置，
所以这种情况需要在返回值 + 1


'''


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if target <= nums[mid]:
                r = mid
            else:
                l = mid + 1
        
        return l + 1 if target > nums[l] else l