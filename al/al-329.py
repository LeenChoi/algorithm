# 矩阵中的最长递增路径
# hard
'''
给定一个整数矩阵，找出最长递增路径的长度。

对于每个单元格，你可以往上，下，左，右四个方向移动。 你不能在对角线方向上移动或移动到边界外（即不允许环绕）。

示例 1:

输入: nums = 
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
] 
输出: 4 
解释: 最长递增路径为 [1, 2, 6, 9]。

示例 2:
输入: nums = 
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
] 
输出: 4 
解释: 最长递增路径是 [3, 4, 5, 6]。注意不允许在对角线方向上移动。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-increasing-path-in-a-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

-------------------------------------------
题解：dfs + dp（记忆法）

dfs遍历比自己大的点，出点应该有三个或三个以内（除去边界），因为入点肯定比当前点小，所以不用再遍历，这也是代替了图遍历中标记已遍历点防止重复遍历
遍历时，从三个出点遍历出去后回来的结果中选取最长路径的点，记录下，如果接下来的某个点的遍历中，又遍历到了该点，那么可以直接从记录中获取，无需再次遍历。

这个记录值，也算是 dp 的转移过程，设 dp[i][j] 记录为从该点出发的最长距离，那么他的相邻点如果能遍历到该点，那么那个相邻点的最长距离为 dp[i][j] + 1

所以这个算法的完整过程就是，对没给点做dfs遍历，同时更新dp，说白了就是暴力dfs中加入个记忆点，防止爆炸式遍历，合理剪枝

'''


class Solution:
    def longestIncreasingPath(self, matrix) -> int:
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        def order(pi, pj, i, j):
            points = []
            if i - 1 >= 0 and (i - 1 != pi or j != pj):
                if matrix[i - 1][j] > matrix[i][j]:
                    points.append((i - 1, j))
            if j + 1 < n and (i != pi or j + 1 != pj):
                if matrix[i][j + 1] > matrix[i][j]:
                    points.append((i, j + 1))
            if i + 1 < m and (i + 1 != pi or j != pj):
                if matrix[i + 1][j] > matrix[i][j]:
                    points.append((i + 1, j))
            if j - 1 >= 0 and (i != pi or j - 1 != pj):
                if matrix[i][j - 1] > matrix[i][j]:
                    points.append((i, j - 1))
            maxStep = 0
            for point in points:
                if dp[point[0]][point[1]] > 0:
                    maxStep = max(maxStep, dp[point[0]][point[1]])
                else:
                    maxStep = max(maxStep, order(i, j, point[0], point[1]))
            dp[i][j] = 1 + maxStep
            return dp[i][j]

        maxLength = 0
        for i in range(m):
            for j in range(n):
                order(i, j, i, j)
                maxLength = max(maxLength, dp[i][j])
        return maxLength
        
        
print(Solution().longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]))
print(Solution().longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]]))
