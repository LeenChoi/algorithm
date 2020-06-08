# 和可被 K 整除的子数组
# medium
'''
给定一个整数数组 A，返回其中元素之和可被 K 整除的（连续、非空）子数组的数目。

示例：
输入：A = [4,5,0,-2,-3,1], K = 5
输出：7

解释：
有 7 个子数组满足其元素之和可被 K = 5 整除：
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
 

提示：
1 <= A.length <= 30000
-10000 <= A[i] <= 10000
2 <= K <= 10000

------------------------------------
题解： 前缀和 + hash map， map里存的key是余数，同余数的值都会命中到同一个key，然后 value +1

'''


class Solution:
    def subarraysDivByK(self, A, K) -> int:
        remainder = {0: 1}
        sum, ans = 0, 0
        for num in A:
            sum += num
            remain = sum % K
            count = remainder.get(remain, 0)
            ans += count
            remainder[remain] = count + 1
        return ans


print(Solution().subarraysDivByK([4,5,0,-2,-3,1], 5))