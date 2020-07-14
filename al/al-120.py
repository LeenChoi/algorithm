# 三角形最小路径和
# medium
'''
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。

例如，给定三角形：

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/triangle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''


class Solution:
    def minimumTotal(self, triangle) -> int:
        if len(triangle) == 0:
            return 0
        dp = [0] * len(triangle)
        dp[0] = triangle[0][0]
        ans = None
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i]) - 1, -1, -1):
                left = dp[j - 1] if j - 1 >= 0 else float('inf')
                up = dp[j] if j < len(triangle[i - 1]) else float('inf')
                dp[j] = min(left, up) + triangle[i][j]
                if i == len(triangle) - 1:
                    ans = min(ans, dp[j]) if ans != None else dp[j]
        return ans if ans != None else triangle[0][0]


# print(Solution().minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))
print(Solution().minimumTotal([[-1],[2,3],[1,-1,-1]]))