# 摆动序列
# medium
'''
如果连续数字之间的差严格地在正数和负数之间交替，则数字序列称为摆动序列。第一个差（如果存在的话）可能是正数或负数。少于两个元素的序列也是摆动序列。

例如， [1,7,4,9,2,5] 是一个摆动序列，因为差值 (6,-3,5,-7,3) 是正负交替出现的。相反, [1,4,7,2,5] 和 [1,7,4,5,5] 不是摆动序列，第一个序列是因为它的前两个差值都是正数，第二个序列是因为它的最后一个差值为零。

给定一个整数序列，返回作为摆动序列的最长子序列的长度。 通过从原始序列中删除一些（也可以不删除）元素来获得子序列，剩下的元素保持其原始顺序。

示例 1:
输入: [1,7,4,9,2,5]
输出: 6 
解释: 整个序列均为摆动序列。

示例 2:
输入: [1,17,5,10,13,15,10,5,16,8]
输出: 7
解释: 这个序列包含几个长度为 7 摆动序列，其中一个可为[1,17,10,13,10,16,8]。

示例 3:
输入: [1,2,3,4,5,6,7,8,9]
输出: 2

进阶:
你能否用 O(n) 时间复杂度完成此题?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/wiggle-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

-------------------------------------
题解：贪心
遍历，逐个判断就行了，记一个flag，记录目前的坡向，然后向后逐个比较，直至找到能改变坡向的数，length + 1

还有动态规划的解法，但比贪心反锁。dp的思路就是维护一个 up,down数组，遍历比较，如果后一个数比前一个数大，那么 up[i] = down[i-1] + 1，down[i] = down[i-1]
反之 down[i] = up[i-1] + 1, up[i] = up[i-1]， 如果相同则 up，down 各自继承他们的前一个，最后输出 up,down 里最大的数

'''


class Solution:
    def wiggleMaxLength(self, nums) -> int:
        if len(nums) == 0:
            return 0
        flag, length = 0, 1
        for i in range(len(nums) - 1):
            diff = nums[i + 1] - nums[i]
            if flag == 0 and diff != 0:
                flag = diff
                length += 1
            elif diff < 0 and flag > 0 or diff > 0 and flag < 0:
                flag = -flag
                length += 1
        return length


print(Solution().wiggleMaxLength([1,7,4,9,2,5]))
print(Solution().wiggleMaxLength([1,17,5,10,13,15,10,5,16,8]))
print(Solution().wiggleMaxLength([1,2,3,4,5,6,7,8,9]))
print(Solution().wiggleMaxLength([3,3,3,2,5]))