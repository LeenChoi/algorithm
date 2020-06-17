# 最佳观光组合
# medium
'''
给定正整数数组 A，A[i] 表示第 i 个观光景点的评分，并且两个景点 i 和 j 之间的距离为 j - i。
一对景点（i < j）组成的观光组合的得分为（A[i] + A[j] + i - j）：景点的评分之和减去它们两者之间的距离。
返回一对观光景点能取得的最高分。 

示例：
输入：[8,1,5,2,6]
输出：11
解释：i = 0, j = 2, A[i] + A[j] + i - j = 8 + 5 + 0 - 2 = 11
 
提示：
2 <= A.length <= 50000
1 <= A[i] <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-sightseeing-pair
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

-----------------------------------------
题解：O(n)枚举
得分公式 A[i] + A[j] + i - j => (A[i] + i) + (A[j] - j)
A[i] + i 肯定是越大越好，从左遍历的时候，记录一个max值存最大的 A[i] + i, 初始 A[0]

之后从 1 位开始遍历比较 max + A[j] - j 是否是最大的 ans，并更新，
同时计算 A[j] + j 是否是当前位置最大的 max，并更新

'''


class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        _max, ans = A[0], 0
        for i in range(1, len(A)):
            _ans = _max + A[i] - i
            if _ans > ans:
                ans = _ans
            if A[i] + i > _max:
                _max = A[i] + i
        return ans
