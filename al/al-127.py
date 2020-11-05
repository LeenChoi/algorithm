# 单词接龙
# medium
'''
给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord 的最短转换序列的长度。转换需遵循如下规则：

每次转换只能改变一个字母。
转换过程中的中间单词必须是字典中的单词。
说明:

如果不存在这样的转换序列，返回 0。
所有单词具有相同的长度。
所有单词只由小写字母组成。
字典中不存在重复的单词。
你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
示例 1:

输入:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

输出: 5

解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
     返回它的长度 5。
示例 2:

输入:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

输出: 0

解释: endWord "cog" 不在字典中，所以无法进行转换。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-ladder
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

---------------------------------------------------
题解：bfs，建图优化
首先将单词之间建立个连接，做成图。之后bfs，做个 cost 表记录每个 word 的最短变换次数，bfs时如果下一个 word 的 cost
大于当前 word 的 cost + 1，那么就更新那个 word 的 cost，否则放弃遍历那个 word，不再放进 bfs queue，最后记录下
endword 的 cost 即可。

建图的朴素想法是两两比较 word，如果可以转变，那么将两个 word 相连，但是效率很低，有个空间优化时间的方法。
比如 "hit" 可以转变为 "*it"，"h*t"，"hi*" 这三种 word，其他能转变为这三种里某一种的 word，它就一定能转变为 "hit"
所以做个 virtual word 表，将所有能转变成 virtual word 的所有 word 都记录起来，然后某一个 word 通过它的 virtual word 列表
就能找到它能转变的所有其他 word

'''


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        if not endWord in wordList:
            return 0
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

        queue = [ids[beginWord]]        
        cost = {}
        cost[ids[beginWord]] = 1
        ans = 0
        while len(queue) > 0:
            id = queue.pop()
            if id == ids[endWord]:
                if ans == 0 or cost[id] < ans:
                    ans = cost[id]
            else:
                if edgeMap.get(id) == None:
                    continue
                edges = edgeMap[id]
                for edge in edges:
                    if cost.get(edge) == None or cost[id] + 1 < cost[edge]:
                        cost[edge] = cost[id] + 1
                        queue.append(edge)
        return ans


class Solution2:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        if not endWord in wordList:
            return 0
        if not beginWord in wordList:
            wordList.insert(0, beginWord)

        def toVirtualWords(word):
            ret = []
            for i in range(len(word)):
                chList = list(word)
                chList[i] = '*'
                ret.append(''.join(chList))
            return ret

        ids = {}
        virtualEdgeMap = {}
        toVirtualMap = {}
        for i in range(len(wordList)):
            word = wordList[i]
            ids[word] = i
            virtualWords = toVirtualWords(word)
            toVirtualMap[i] = virtualWords
            for vw in virtualWords:
                if virtualEdgeMap.get(vw) == None:
                    virtualEdgeMap[vw] = []
                virtualEdgeMap[vw].append(i)

        queue = [ids[beginWord]]
        cost = {}
        cost[ids[beginWord]] = 1
        ans = 0
        while len(queue) > 0:
            id = queue.pop()
            if id == ids[endWord]:
                if ans == 0 or cost[id] < ans:
                    ans = cost[id]
            else:
                virtualWords = toVirtualMap[id]
                for vw in virtualWords:
                    edges = virtualEdgeMap[vw]
                    for edgeId in edges:
                        if edgeId != id:
                            if cost.get(edgeId) == None or cost[id] + 1 < cost[edgeId]:
                                cost[edgeId] = cost[id] + 1
                                queue.append(edgeId)

        return ans


print(Solution2().ladderLength('hit', 'cog', ["hot","dot","dog","lot","log","cog"]))
print(Solution2().ladderLength('hot', 'dog', ["hot", "dog"]))

        