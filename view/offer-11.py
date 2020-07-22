# 旋转数组的最小数字
# easy
# 同 al-154, 但 al-154 标的是 hard
'''
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  

示例 1：

输入：[3,4,5,1,2]
输出：1
示例 2：

输入：[2,2,2,0,1]
输出：0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

----------------------------------------
题解：二分查找
注意下 [2,2,2,2,0,1,2] 这种 l,r,mid 都相同的情况就行，官方题解是这种情况 r -= 1 再迭代，我是用递归把两段再迭代一遍取最小值做的

'''


class Solution:
    def minArray(self, numbers) -> int:
        def findMin(l, r):
            if l == r:
                return numbers[l]
            mid = (l + r) // 2
            if numbers[mid] < numbers[l]:
                r = mid
                return findMin(l, r)
            elif numbers[mid] > numbers[l]:
                if numbers[mid] <= numbers[r]:
                    r = mid
                    return findMin(l, r)
                else:
                    l = mid + 1
                    return findMin(l, r)
            else:
                if numbers[mid] < numbers[r]:
                    return numbers[mid]
                elif numbers[mid] > numbers[r]:
                    l = mid + 1
                    return findMin(l, r)
                else:
                    lmin = findMin(l, mid)
                    rmin = findMin(mid + 1, r)
                    return min(lmin, rmin)
        return findMin(0, len(numbers) - 1)


class Solution2:
    def findMin(self, nums) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < nums[r]:
                r = mid
            elif nums[mid] > nums[r]:
                l = mid + 1
            else:
                r -= 1
        return nums[l]



print(Solution().minArray([3,4,5,1,2]))
print(Solution().minArray([2,2,2,0,1]))
print(Solution2().findMin([2,2,0,1,2,2,2,2,2]))
print(Solution2().findMin([1,2,3,4,5]))