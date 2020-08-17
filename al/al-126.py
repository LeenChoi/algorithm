# 单词接龙 II
# hard
'''
给定两个单词（beginWord 和 endWord）和一个字典 wordList，找出所有从 beginWord 到 endWord 的最短转换序列。转换需遵循如下规则：

每次转换只能改变一个字母。
转换后得到的单词必须是字典中的单词。
说明:

如果不存在这样的转换序列，返回一个空列表。
所有单词具有相同的长度。
所有单词只由小写字母组成。
字典中不存在重复的单词。
你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
示例 1:

输入:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

输出:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
示例 2:

输入:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

输出: []

解释: endWord "cog" 不在字典中，所以不存在符合要求的转换序列。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-ladder-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

---------------------------------------------------
题解：bfs
做个无向图将能转换的每两个词连接上，用一个 edge list map 维护，然后从 beginword 出发做 bfs，
bfs 过程中的 queue 中记录的节点信息包括 word 和从 beginword 到此 word 的路径。

这里有个巧妙的处理，因为要输出所有最短路径，所以一个节点可能会反复进 queue，一个节点可能会从多条路访问当前这个节点。
而 queue 中的节点信息中 path 记录的是当前遍历的路径，比如 A -> C, B -> C ，C 可以从 A、B 访问，
但 queue 中单个节点里的 path 是记录的某个 A -> C 或者 B -> C 的路径

每次遍历 queue 节点时判断其中的路径的最后一个 word，判断是否为 endword，如果是，那么将 path 输出进结果集即可
注意，如果一个节点某一次的访问 path 长度大于之前访问，那么此 path 不是最短路径，所以不该把此 path 塞进 queue
所以需要维护一个 cost 表，记录每个 word 能访问到的最短 cost，即词语的最少翻转次数。

官方题解中还做了个 word -> id 的映射表，使得 bfs 的时候需要记录的数据变得简洁，但对效率好像没多大提升，python依然超时

'''

import copy

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList):
        if not endWord in wordList:
            return []
        if not beginWord in wordList:
            wordList.insert(0, beginWord)
        edgeMap = {}
        ids = {}
        for i in range(len(wordList)):
            ids[wordList[i]] = i
        for word in wordList:
            for edge in wordList:
                if word != edge:
                    diffValue = 0
                    for i in range(len(word)):
                        if word[i] != edge[i]:
                            diffValue += 1                
                    if diffValue == 1:
                        if edgeMap.get(ids[word]) == None:
                            edgeMap[ids[word]] = set()
                        edgeMap[ids[word]].add(ids[edge])
                        if edgeMap.get(ids[edge]) == None:
                            edgeMap[ids[edge]] = set()
                        edgeMap[ids[edge]].add(ids[word])

        ans = []
        queue = [[ids[beginWord]]]
        cost = {}
        cost[ids[beginWord]] = 0
        while len(queue) > 0:
            path = queue.pop(0)
            last = path[-1]
            if last == ids[endWord]:
                tmp = []
                for index in path:
                    tmp.append(wordList[index])
                ans.append(tmp)
            else:
                if edgeMap.get(last) == None:
                    continue
                edges = edgeMap[last]
                for edge in edges:
                    if cost.get(edge) == None or cost[last] + 1 <= cost[edge]:
                        cost[edge] = cost[last] + 1
                        copyPath = copy.deepcopy(path)
                        copyPath.append(edge)
                        queue.append(copyPath)
        return ans


# print(Solution().findLadders('hit', 'cog', ["hot","dot","dog","lot","log","cog"]))
# print(Solution().findLadders('hot', 'dog', ['hot', 'dog']))
print(Solution().findLadders('red', 'tax', ["ted","tex","red","tax","tad","den","rex","pee"]))