# 岛屿的周长
# easy
'''
给定一个包含 0 和 1 的二维网格地图，其中 1 表示陆地 0 表示水域。

网格中的格子水平和垂直方向相连（对角线方向不相连）。整个网格被水完全包围，但其中恰好有一个岛屿（或者说，一个或多个表示陆地的格子相连组成的岛屿）。

岛屿中没有“湖”（“湖” 指水域在岛屿内部且不和岛屿周围的水相连）。格子是边长为 1 的正方形。网格为长方形，且宽度和高度均不超过 100 。计算这个岛屿的周长。

 
示例 :

输入:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

输出: 16


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/island-perimeter
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

----------------------------------------------------
题解: 迭代，dfs
循环遍历数组，满足条件就记个边
dfs，先找出一个为 1 的块，然后对它做dfs搜索记边

'''


class Solution:
    def islandPerimeter(self, grid) -> int:
        m, n = len(grid), len(grid[0])

        def calcArround(i, j):
            nonlocal m, n
            cnt = 0
            for (x, y) in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
                xx, yy = i + x, j + y
                if xx < 0 or xx >= m or yy < 0 or yy >= n or grid[xx][yy] == 0:
                    cnt += 1
            return cnt

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans += calcArround(i, j)
        return ans


class Solution2:
    def islandPerimeter(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0

        def find():
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        return i, j

        def dfs(x, y):
            grid[x][y] = 2
            for (i, j) in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
                xx, yy = i + x, j + y
                if xx < 0 or xx >= m or yy < 0 or yy >= n or grid[xx][yy] == 0:
                    nonlocal ans
                    ans += 1
                elif grid[xx][yy] == 1:
                    dfs(xx, yy)

        x, y = find()
        dfs(x, y)
        return ans






print(Solution2().islandPerimeter([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]))
