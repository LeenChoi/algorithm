# 被围绕的区域
# medium
'''
给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。

找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。

示例:

X X X X
X O O X
X X O X
X O X X
运行你的函数后，矩阵变为：

X X X X
X X X X
X X X X
X O X X
解释:

被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/surrounded-regions
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

------------------------------------------
题解: dfs, bfs, 并查集
dfs 和 bfs 简单，以四个边 O 为起点做遍历，将邻接的 O 做个记号，可以改写为 A，四个边都遍历过后，会只剩下被 X 包围的 O
再遍历一遍整个矩阵，将 O 改为 X, 将 A 改为 O 即可

并查集，此题并查集有点慢，因为dfs，bfs不需要遍历整个矩阵，但并查集需要，并的过程中最终每个节点的parent都会指到并集中的唯一点
做个 map，以这个集中点为 key，记录这个并集是否是邻边的集，最后再遍历一遍整个矩阵，每个 O 找到他的 root，通过 map 查看是否是临边集
不是的话将此 O 改为 X 即可



'''


class Solution:
    def solve(self, board) -> None:
        if len(board) == 0:
            return
        unionFindSet = UnionFindSet(board)
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    for k, l in [(i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)]:
                        unionFindSet.union((i, j), (k, l))
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    root = unionFindSet.find((i, j))
                    if not unionFindSet.edgeMap.get(root):
                        board[i][j] = 'X'

       
class UnionFindSet:
    def __init__(self, board):
        self.board = board
        m, n = len(board), len(board[0])
        self.m, self.n = m, n
        self.parents = [-1] * (m * n)
        self.edgeMap = {}
        for i in range(m):
            for j in range(n):
                key = i * n + j
                if board[i][j] == 'O':
                    self.parents[key] = key

    def find(self, node):
        key = node[0] * self.n + node[1]
        root = key
        while self.parents[root] != root:
            root = self.parents[root]
        pre = key
        while self.parents[pre] != root:
            pre = self.parents[pre]
            self.parents[pre] = root
        return root

    def union(self, node1, node2):
        root1 = self.find(node1)
        if self.isValid(node2):
            root2 = self.find(node2)
            if root1 != root2:
                self.parents[root2] = root1
            if self.isEdge(node1) or self.isEdge(node2):
                self.edgeMap[root1] = True
        elif self.isEdge(node1):
            self.edgeMap[root1] = True

    def isValid(self, node):
        if node[0] >= 0 and node[0] < self.m and \
            node[1] >= 0 and node[1] < self.n and \
            self.board[node[0]][node[1]] == 'O':
            return True
        else:
            return False

    def isEdge(self, node):
        key = node[0] * self.n + node[1]
        if self.edgeMap.get(key):
            return True
        if node[0] == 0 or node[0] == self.m - 1:
            self.edgeMap[key] = True
            return True
        if node[1] == 0 or node[1] == self.n - 1:
            self.edgeMap[key] = True
            return True    
        return False



# print(Solution().solve([['x','x','x','x'], ['x','o','o','x'], ['x','x','o','x'], ['x','o','x','x']]))
print(Solution().solve([["X","O","X","O","X","O"],["O","X","O","X","O","X"],["X","O","X","O","X","O"],["O","X","O","X","O","X"]]))