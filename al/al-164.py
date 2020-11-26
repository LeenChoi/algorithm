# 最大间距
# hard
'''
给定一个无序的数组，找出数组在排序之后，相邻元素之间最大的差值。

如果数组元素个数小于 2，则返回 0。

示例 1:

输入: [3,6,9,1]
输出: 3
解释: 排序后的数组是 [1,3,6,9], 其中相邻元素 (3,6) 和 (6,9) 之间都存在最大差值 3。
示例 2:

输入: [10]
输出: 0
解释: 数组元素个数小于 2，因此返回 0。
说明:

你可以假设数组中所有元素都是非负整数，且数值在 32 位有符号整数范围内。
请尝试在线性时间复杂度和空间复杂度的条件下解决此问题。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-gap
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

----------------------------------------------
题解：桶计算
最理想是，有一些有序桶，桶的下标就是数字本身，然后将数字一一入桶，遍历一遍桶，计算找出最大间隔。这样两次遍历，只需O(n)复杂度。
数组结构可以当做这种桶，但是如果有非常大的数，那么这个数组的长度也会特别大，会浪费不必要的空间。

所以我们做一个桶，从数组找出最大最小值，算出他们的差值，这个差值除以数组长度-1，就是每个数字间的平均间隔，
知道平均间隔了就知道要做几个桶了，即上面的差值除以平均间隔再+1，+1是因为上面的取平均间隔的除法是向下取整，会丢长度

有了桶之后，就需要将数一一入桶了，但数字间大小参差不齐，可能一个桶内会入几个数。
但是我们要求的是最大间隔，桶的长度是恒定的，所以最大间隔肯定不能出现在一个桶内的两个数之间。因为如果最大间隔出现在一个桶内，
比平均间隔还小，这样矛盾。所以最大间隔一定是产生在不同的桶之间，所以一个桶内的数无需计算间隔，只需记录桶内的最大值和最小值即可。
然后只需计算当前桶的最小值和前一个桶的最大值的差值，找出最大值，即是最大间隔

'''


class Solution:
    def maximumGap(self, nums) -> int:
        if len(nums) <= 1:
            return 0
        _min, _max = None, None
        for num in nums:
            if _min == None or num < _min:
                _min = num
            if _max == None or num > _max:
                _max = num
        step = (_max - _min) // (len(nums) - 1) or 1
        bucket = [[] for i in range((_max - _min) // step + 1)]
        for num in nums:
            pos = (num - _min) // step
            if pos > len(nums) - 1:
                pos = len(nums) - 1
            if len(bucket[pos]) == 0:
                bucket[pos].append(num)
            elif len(bucket[pos]) == 1:
                if bucket[pos][0] < num:
                    bucket[pos].append(num)
                else:
                    bucket[pos].insert(0, num)
            else:
                bucket[pos][0] = min(bucket[pos][0], num)
                bucket[pos][1] = max(bucket[pos][1], num)
        maxDiff = 0
        preMax = None
        for ele in bucket:
            if len(ele) == 0:
                continue
            if preMax != None:
                if ele[0] - preMax > maxDiff:
                    maxDiff = ele[0] - preMax
            preMax = ele[-1]
        return maxDiff


print(Solution().maximumGap([3,6,9,1]))
# print(Solution().maximumGap([1,1,1,1,1,5,5,5,5,5]))
