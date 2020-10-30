# 岛屿的最大面积
# medium
'''
给定一个包含了一些 0 和 1 的非空二维数组 grid 。
一个 岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在水平或者竖直方向上相邻。你可以假设 grid 的四个边缘都被 0（代表水）包围着。
找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为 0 。)

示例 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
对于上面这个给定矩阵应返回 6。注意答案不应该是 11 ，因为岛屿只能包含水平或垂直的四个方向的 1 。

示例 2:

[[0,0,0,0,0,0,0,0]]
对于上面这个给定的矩阵, 返回 0。

 
注意: 给定的矩阵grid 的长度和宽度都不超过 50。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/max-area-of-island
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

------------------------------------------------------
题解: dfs

'''


class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        area = {}
        maxArea = 0
        def dfs(i, j, index):
            nonlocal maxArea
            grid[i][j] = index
            if area.get(index) == None:
                area[index] = 1
            else:
                area[index] += 1
            if area[index] > maxArea:
                maxArea = area[index]

            for (x, y) in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
                xx, yy = i + x, j + y
                if xx >= 0 and xx < m and yy >= 0 and yy < n and grid[xx][yy] == 1:
                    dfs(xx, yy, index)

        index = 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    index += 1
                    dfs(i, j, index)
        return maxArea

