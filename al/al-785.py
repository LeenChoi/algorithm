# 判断二分图
# medium
'''
给定一个无向图graph，当这个图为二分图时返回true。
如果我们能将一个图的节点集合分割成两个独立的子集A和B，并使图中的每一条边的两个节点一个来自A集合，一个来自B集合，我们就将这个图称为二分图。
graph将会以邻接表方式给出，graph[i]表示图中与节点i相连的所有节点。每个节点都是一个在0到graph.length-1之间的整数。这图中没有自环和平行边： graph[i] 中不存在i，并且graph[i]中没有重复的值。

示例 1:
输入: [[1,3], [0,2], [1,3], [0,2]]
输出: true

解释: 
无向图如下:
0----1
|    |
|    |
3----2
我们可以将节点分成两组: {0, 2} 和 {1, 3}。

示例 2:
输入: [[1,2,3], [0,2], [0,1,3], [0,2]]
输出: false

解释: 
无向图如下:
0----1
| \  |
|  \ |
3----2
我们不能将节点分割成两个独立的子集。

注意:
graph 的长度范围为 [1, 100]。
graph[i] 中的元素的范围为 [0, graph.length - 1]。
graph[i] 不会包含 i 或者有重复的值。
图是无向的: 如果j 在 graph[i]里边, 那么 i 也会在 graph[j]里边。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/is-graph-bipartite
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

---------------------------------------
题解：dfs，bfs + 标记染色
bfs 遍历，本次遍历标记 0，遍历他的邻接点时，给他们标记 1，再遍历他们的邻接点时再标记为 0，
如果遍历到某个节点时，发现已经被标记过，并且本次带的标记和记录的标记不相同，那么返回 False，
全部遍历完没有这样的点，那么就返回 True，说明是二分图

'''


class Solution:
    def isBipartite(self, graph) -> bool:
        record = {}
        queue = []
        for i in range(len(graph)):
            if record.get(i) == None:
                queue.append((i, 0))
                while len(queue) > 0:
                    spot = queue.pop()
                    if record.get(spot[0]) == None:
                        record[spot[0]] = spot[1]
                    else:
                        if record[spot[0]] != spot[1]:
                            return False
                    for i in graph[spot[0]]:
                        if record.get(i) == None:
                            queue.append((i, (spot[1] + 1) % 2))
        return True


# print(Solution().isBipartite([[1,3], [0,2], [1,3], [0,2]]))
# print(Solution().isBipartite([[1,2,3], [0,2], [0,1,3], [0,2]]))
# print(Solution().isBipartite([[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]))
# print(Solution().isBipartite([[2,4],[2,3,4],[0,1],[1],[0,1],[7],[9],[5],[],[6],[12,14],[],[10],[],[10],[19],[18],[],[16],[15],[23],[23],[],[20,21],[],[],[27],[26],[],[],[34],[33,34],[],[31],[30,31],[38,39],[37,38,39],[36],[35,36],[35,36],[43],[],[],[40],[],[49],[47,48,49],[46,48,49],[46,47,49],[45,46,47,48]]))
print(Solution().isBipartite([[4],[],[4],[4],[0,2,3]]))

