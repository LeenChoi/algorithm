# 课程表
# medium
'''
你这个学期必须选修 numCourse 门课程，记为 0 到 numCourse-1 。

在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们：[0,1]

给定课程总量以及它们的先决条件，请你判断是否可能完成所有课程的学习？

示例 1:

输入: 2, [[1,0]] 
输出: true
解释: 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以这是可能的。

示例 2:

输入: 2, [[1,0],[0,1]]
输出: false
解释: 总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0；并且学习课程 0 之前，你还应先完成课程 1。这是不可能的。
 

提示：

输入的先决条件是由 边缘列表 表示的图形，而不是 邻接矩阵 。详情请参见图的表示法。
你可以假定输入的先决条件中没有重复的边。
1 <= numCourses <= 10^5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/course-schedule
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

------------------------------------------------
题解：拓扑排序 dfs bfs

拓扑图为，所有有向通路(u,v)上的 u 点排在 v 点的前面，即拓扑图。有环图是典型不是拓扑图，因为有环，所以 v 点必将再通往 u 点。
拓扑图怎么拓扑排序，dfs 或 bfs

bfs：bfs 拓扑是正向排序，首先遍历一遍图，记录每个节点的入度，从入度 0 的节点开始遍历，遍历他的后继点时，将每个后继点的入度 -1
如果入度为 0 了，那么塞进 bfs 队列，参与后续的 bfs（注意：已遍历的节点避免重复遍历，此题我是将入度 -1 表示已遍历）
最后如果所有节点都遍历过，表明此图是拓扑图，可以拓扑排序

dfs: dfs 拓扑是反向排序，遍历图，依次对节点做 dfs，dfs 过程中当遍历到某个节点没有后继，那么将此节点压栈，接着回溯到父节点
继续判断父节点的后继情况，若都遍历过，没有可遍历的后继节点，那么压栈，以此类推
（注意：可能需要两种状态标记节点，一种是已遍历过，一种是已压栈，避免有环图无限 dfs）
最后如果所有节点都压栈了，说明是拓扑图，顺序出栈即是拓扑排序

'''


class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        queue, ans = [], []
        treeDict = {}
        indegree = [0] * numCourses
        for node in prerequisites:
            if treeDict.get(node[1]) == None:
                treeDict[node[1]] = [node[0]]
            else:
                treeDict[node[1]].append(node[0])
            indegree[node[0]] += 1
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        while len(queue) > 0:
            i = queue.pop(0)
            ans.append(i)
            indegree[i] -= 1
            if treeDict.get(i) != None:
                for ni in treeDict[i]:
                    if indegree[ni] > 0:
                        indegree[ni] -= 1
                        if indegree[ni] == 0:
                            queue.append(ni)
        return len(ans) == numCourses


print(Solution().canFinish(3, [[0,2],[1,2],[2,0]]))
                    