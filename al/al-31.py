# 下一个排列
# medium
'''
实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须原地修改，只允许使用额外常数空间。

以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/next-permutation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

---------------------------------------------------
题解：模拟
以排列 [4,5,2,6,3,1] 为例，它的下一项是 [4,5,3,1,2,6], 以人的角度看当前项的 [4,5,2,...] 前缀的项已经排列完了，
2 后面已经是最大，降序了。该找比 2 大的一项继续排列，直接观察那么就是 [4,5,3,...] 从这个前缀开始排列，也就是说
2 首先要和比他稍微大一点的 3 做交换，那么原项交换后变成 [4,5,3,6,2,1], 之后需要将 3 后面的数字重新排列成最小，
因为原项 2 后面已经是降序，和 3 交换后依然是降序，只需将 3 后面的数字全翻转下就 ok 了。

所以算法的过程就是，从后向前遍历找到第一个小于后项的数字，这个数字就是要交换的数字(上面的2)，
然后再从后向前遍历到要替换数字的这个位置，找第一个比它大的数字(即上面3)，做交换，之后将后面的数字全翻转，
注意一些边界情况，比如 3,2,1 -> 1,2,3 这种

'''


class Solution:
    def nextPermutation(self, nums):
        smalleridx, biggeridx, idx = -1, -1, -1
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                smalleridx = i - 1
                idx = i
                break
        if idx != -1:
            for i in range(len(nums) - 1, idx - 1, -1):
                if nums[i] > nums[smalleridx]:
                    biggeridx = i
                    break
            if biggeridx == -1:
                biggeridx = len(nums) - 1
            nums[smalleridx], nums[biggeridx] = nums[biggeridx], nums[smalleridx]
        if idx == -1:
            idx = 0
        i, j = idx, len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        return nums

print(Solution().nextPermutation([2,3,1]))