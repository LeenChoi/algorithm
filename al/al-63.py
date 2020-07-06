# 不同路径 II
# medium
'''
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

网格中的障碍物和空位置分别用 1 和 0 来表示。

说明：m 和 n 的值均不超过 100。

示例 1:
输入:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
输出: 2

解释:
3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-paths-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

-----------------------------------
题解：动态规划

每个dp点需要从左侧和上侧获得状态，因为只能从左和从上走到这个点，所以每个dp点记录该点能走过来的路径数，
然后 dp[i][j] = dp[i-1][j] + dp[i][j-1] 就好，判断下该点是否有障碍物，有障碍物就不用计算，使该dp点为 0 即可

'''


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        if obstacleGrid[0][0] != 1:
            dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                if obstacleGrid[i][j] != 1:
                    up = dp[i - 1][j] if i - 1 >= 0 else 0
                    left = dp[i][j - 1] if j - 1 >= 0 else 0
                    dp[i][j] = up + left
        print(dp)
        return dp[m - 1][n - 1]


print(Solution().uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))
print(Solution().uniquePathsWithObstacles([[1]]))
