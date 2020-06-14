# 转变数组后最接近目标值的数组和
# medium
'''
给你一个整数数组 arr 和一个目标值 target ，请你返回一个整数 value ，使得将数组中所有大于 value 的值变成 value 后，数组的和最接近  target （最接近表示两者之差的绝对值最小）。
如果有多种使得和最接近 target 的方案，请你返回这些整数中的最小值。
请注意，答案不一定是 arr 中的数字。

示例 1：、
输入：arr = [4,9,3], target = 10
输出：3
解释：当选择 value 为 3 时，数组会变成 [3, 3, 3]，和为 9 ，这是最接近 target 的方案。

示例 2：
输入：arr = [2,3,5], target = 10
输出：5

示例 3：
输入：arr = [60864,25176,27249,21296,20204], target = 56803
输出：11361
 
提示：
1 <= arr.length <= 10^4
1 <= arr[i], target <= 10^5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sum-of-mutated-array-closest-to-target
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

-----------------------------
题解：
先整体排个序，每次遍历计算前缀和，和target剩余和，剩余和除以剩余项得到平均值，
判断下一个元素是否大于这个平均值，并返回即可

'''


class Solution:
    def findBestValue(self, arr, target: int) -> int:
        arr.sort()
        length = len(arr)
        _sum, remain, count = 0, target, length
        base = remain // count
        for i in range(length):
            base = remain // count
            if arr[i] >= base:
                break
            count -= 1
            _sum += arr[i]
            remain = target - _sum
        a = abs((base + 1) * count + _sum - target)
        b = abs(base * count + _sum - target)
        ans = base + 1 if a < b else base
        return ans if ans <= arr[-1] else arr[-1]
        


print(Solution().findBestValue([4,9,3], 10))
print(Solution().findBestValue([2,3,4], 10))
print(Solution().findBestValue([60864,25176,27249,21296,20204], 56803))