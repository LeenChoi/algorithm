# 最长重复子数组
# medium
'''
给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。

示例 1:
输入:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
输出: 3

解释: 
长度最长的公共子数组是 [3, 2, 1]。
说明:

1 <= len(A), len(B) <= 1000
0 <= A[i], B[i] < 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

----------------------------------
题解：动态规划，滑动窗口，二分+哈希
1. dp: if a[i] == b[j] => dp[i][j] = dp[i-1][j-1] + 1
2. 滑动窗口, 滑动过程如下
         [3, 6, 1, 2, 4]     [3, 6, 1, 2, 4]       [3, 6, 1, 2, 4]
[7, 1, 2, 9]             =>     [7, 1, 2, 9]   =>              [7, 1, 2, 9]
                                    ↑ ↑

'''


class Solution:
    def findLength(self, A, B) -> int:
        dp = [0] * (len(B) + 1)
        _max = 0
        for i in range(1, len(A) + 1):
            for j in range(len(B), 0, -1):
                if A[i - 1] == B[j - 1]:
                    dp[j] = dp[j - 1] + 1
                    _max = max(_max, dp[j])
                else:
                    dp[j] = 0
        return _max


print(Solution().findLength([1,2,3,2,1], [3,2,1,4,7]))
print(Solution().findLength([1,0,0,0,1], [1,0,0,1,1]))