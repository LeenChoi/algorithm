# 最接近的三数之和
# medium
'''
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

示例：
输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
 
提示：
* 3 <= nums.length <= 10^3
* -10^3 <= nums[i] <= 10^3
* -10^4 <= target <= 10^4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum-closest
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

--------------------------------------
题解：排序 + 双指针，和三数之和一个解法
    双指针遍历，记录最接近的和。小优化点，当三数之和等于target时，直接return就行

'''


class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        nums.sort()
        k, i, j = 0, 0, 0
        diff, ans = None, 0
        for k in range(0, len(nums) - 2):
            i = k + 1
            j = len(nums) - 1
            ttarget = target - nums[k]
            while i < j:
                tmp = abs(ttarget - nums[i] - nums[j])
                if diff == None or tmp < diff:
                    diff = tmp
                    ans = nums[k] + nums[i] + nums[j]
                if nums[i] + nums[j] > ttarget:
                    j -= 1
                elif nums[i] + nums[j] < ttarget:
                    i += 1
                else:
                    return ans
        return ans


# print(Solution().threeSumClosest([-1,2,1,-4], 1))
print(Solution().threeSumClosest([0,1,2], 3))