# 最大子序和
'''
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

进阶:
如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

------------------------------------
题解：
    1.贪心，遍历做和，两种思路，一是遍历找当前为止的最大和最小和做差，维护最大的差就是。二是遍历做和，当和小于0，重新做和，维护最大和
    2.动态规划，假设 f(i) 代表以 i 为结束的子数组的和，那么 f(i) = max(f(i-1) + xi, xi)
    3.分治法，线段树。找四种和，iSum 数组总和，lSum 以左边界的最大子数组和，rSum 以右边界的最大子数组和，mSum 中间不挨边的最大子数组和
        那么两个子数组 la, ra 合并为一个数组时，四个和更新为
        iSum = la.iSum + ra.iSum
        lSum = max(la.lSum, la.iSum + ra.lSum)
        rSum = max(ra.rSum, ra.iSum + la.rSum)
        mSum = max(la.mSum, ra.mSum, la.rSum + ra.lSum)
        最后 return mSum 即可

'''


# 遍历做和差
class Solution:
    def maxSubArray(self, nums) -> int:
        min, max, sum = 0, nums[0], 0
        for i in range(0, len(nums)):
            sum += nums[i]
            if sum - min > max:
                max = sum - min
            if sum < 0 and sum < min:
                min = sum
        return max


# 做和比较
class SolutionV1_5:
    def maxSubArray(self, nums) -> int:
        sum, _max = 0, nums[0]
        for num in nums:
            if sum > 0:
                sum += num
            else:
                sum = num
            _max = max(sum, _max)
        return _max



# 动态规划
class SolutionV2:
    def maxSubArray(self, nums) -> int:
        m = [0] * (len(nums) + 1)
        _max = None
        for i in range(0, len(nums)):
            m[i + 1] = max(m[i] + nums[i], nums[i])
            if _max == None or m[i + 1] > _max:
                _max = m[i + 1]
        return _max


# 分治法
class SolutionV3:

    def pushup(self, la, ra):
        iSum = la['iSum'] + ra['iSum']
        lSum = max(la['lSum'], la['iSum'] + ra['lSum'])
        rSum = max(ra['rSum'], ra['iSum'] + la['rSum'])
        mSum = max(la['mSum'], ra['mSum'], la['rSum'] + ra['lSum'])
        return {'iSum': iSum, 'lSum': lSum, 'rSum': rSum, 'mSum': mSum}

    def get(self, a, l, r):
        if l == r:
            return {'iSum': a[l], 'lSum': a[l], 'rSum': a[l], 'mSum': a[l]}

        m = (l + r) // 2
        la = self.get(a, l, m)
        ra = self.get(a, m + 1, r)
        return self.pushup(la, ra)


    def maxSubArray(self, nums) -> int:
        res = self.get(nums, 0, len(nums) - 1)
        return res['mSum']


solution = SolutionV1_5()
# res = solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
res = solution.maxSubArray([5,4,-3,4,-1,-2,1,-5,4])
print(res)
            