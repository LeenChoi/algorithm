# 岛屿数量
'''
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
此外，你可以假设该网格的四条边均被水包围。

输入:
11110
11010
11000
00000
输出: 1

-------------------------------------
题解：dfs遍历，遍历到1这个点了，先count+1，然后从这个点上下左右四条线展开dfs，
    如果是1继续向下dfs并且将1改为0(或者非1的数)表示已经遍历过了，以免外层遍历碰到1又 count + 1 了

    并查集：做一个祖先队列，记录每个1的祖先(相连的1之间，选出一个共同祖先)，初始化时都记录自己。
        顺序遍历地图，碰到1就上下左右四个方向判断，找同样是1的与之做并集。
        并：查两个点的祖先做关联的操作
        查：追溯自己的祖先，并且将遍历过的点直接指向祖先，以提升下次查的迭代过程
    在初始化祖先列表的时候，每有一个1，做count + 1，之后做并操作的时候 count - 1, 最后的count即是答案

'''

# dfs
class Solution:
    def dfs(self, grid, lr, lc, r, c):
        grid[r][c] = 0
        for i, j in [(r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)]:
            if i >= 0 and i < lr and j >= 0 and j < lc and grid[i][j] == 1:
                self.dfs(grid, lr, lc, i, j)                

    def numIslands(self, grid) -> int:
        lr = len(grid)
        if lr == 0:
            return 0
        lc = len(grid[0])
        count = 0
        for r in range(0, lr):
            for c in range(0, lc):
                if grid[r][c] == 1:
                    count += 1
                    self.dfs(grid, lr, lc, r, c)
        return count


# union-find
class UnionFindSet:
    def __init__(self, grid):
        lr, lc = len(grid), len(grid[0])
        self.parents = [-1] * (lr * lc)
        self.count = 0 # 记录岛屿个数
        for r in range(0, lr):
            for c in range(0, lc):
                if grid[r][c] == '1':
                    self.parents[r * lc + c] = r * lc + c
                    # 初始化时，每个为1的点的祖先都指向了自己，属于有N个孤立的岛，在union操作时合并祖先节点时count -1
                    self.count += 1

    def find(self, node):
        root = node
        while self.parents[root] != root:
            root = self.parents[root]
        
        node2 = node
        while self.parents[node2] != root:
            node2 = self.parents[node2]
            self.parents[node2] = root

        return root

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        if root1 != root2:
            self.parents[root2] = root1
            self.count -= 1
    
    def counts(self):
        return self.count
    

class SolutionV2:
    
    def numIslands(self, grid) -> int:
        lr = len(grid)
        if lr == 0:
            return 0
        lc = len(grid[0])
        unionFindSet = UnionFindSet(grid)

        for r in range(0, lr):
            for c in range(0, lc):
                if grid[r][c] == '1':
                    for i, j in [(r - 1, c), (r, c - 1), (r + 1, c), (r, c+ 1)]:
                        if i >= 0 and i < lr and j >= 0 and j < lc and grid[i][j] == '1':
                            unionFindSet.union(r * lc + c, i * lc + j)
            
        return unionFindSet.counts()




solution = Solution()
res = solution.numIslands([\
    [1,1,0,0,0],\
    [1,1,0,0,0],\
    [0,0,1,0,0],\
    [0,0,0,1,1]\
])
# res = solution.numIslands([])
print(res)
