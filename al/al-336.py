# 回文对
# hard
'''
可拼接成回文串。

示例 1:

输入: ["abcd","dcba","lls","s","sssll"]
输出: [[0,1],[1,0],[3,2],[2,4]] 
解释: 可拼接成的回文串为 ["dcbaabcd","abcddcba","slls","llssssll"]

示例 2:

输入: ["bat","tab","cat"]
输出: [[0,1],[1,0]] 
解释: 可拼接成的回文串为 ["battab","tabbat"]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-pairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

----------------------------------------
题解：字典树 + 回文串判断(可以马拉车)
其实没啥太难的，就是复杂麻烦，做个字典树，把每个 word 倒着存进去，然后再遍历一遍 words，找到能够配对的 word 组合
然后对比，组合有三类：
1. 正好和 word 匹配
2. 和 word 的前缀匹配，需要把 word 剩下的后缀再判一遍是否回文
3. word 和字典树里找到的那些 words 的前缀匹配，需要把 words 里的每个剩下的后缀判一遍是否回文，当然字典树是倒叙放进去的，
    所以判这些 words 的前缀是否回文即可

这里的 2，3 部分我用了个哈希map存储子串是否回文的结果，避免之后的数据中会有重复计算回文的情况


官方题解还有一办法是，枚举所有 word，找出它的所有前缀回文，和后缀回文，判断把回文串截掉后剩下的字符串，如果在 words 里，
那么就可以构成回文对，然后可以把所有 words 放进一个哈希表或者字典树里

还有个优化版，就是利用拉马车算法线性找回文，然后剩下的字符串在字典树里找，需要建两个字典树，正向和反向，用来对 word 的前缀和后缀的查找


'''


class Solution:
    def palindromePairs(self, words):
        trie = Trie()
        dict = {}
        ans = []
        for i in range(len(words)):
            word = words[i]
            trie.addWord(word, i)
            if len(word) > 0:
                dict[word] = [None] * len(word)
                dict[word][0] = True
                dict[word][-1] = isPalindrome(word, 0, len(word) - 1)
        
        for i in range(len(words)):
            word = words[i]
            result = trie.search(word, i)
            if result[0] != None:
                ans.append([i, result[0]])
            for j in result[1]:
                index = len(words[j])
                if index == 0:
                    if dict[word][-1]:
                        ans.append([i, j])
                else:
                    if isPalindrome(word, len(words[j]), len(word) - 1):
                        ans.append([i, j])
            node = result[2]
            if node:
                remains = trie.getRemainStr(node)
                for remain in remains:
                    Str = remain[0]
                    index = remain[1]
                    flag = dict[words[index]][len(Str) - 1]
                    if flag == None:
                        flag = isPalindrome(words[index], 0, len(Str) - 1)
                        dict[words[index]][len(Str) - 1] = flag
                    if flag:
                        ans.append([i, index])
        return ans
                

class TrieNode:
    def __init__(self, val, index = None):
        self.val = val
        self.children = []
        self.endIndex = index

    def addChild(self, node):
        self.children.append(node)

    def findChild(self, val):
        for node in self.children:
            if node.val == val:
                return node
        return None
    
    def setEnd(self, index):
        self.endIndex = index


class Trie:
    def __init__(self):
        self.root = TrieNode('*', None)

    def addWord(self, word, index):
        parent = self.root
        for i in range(len(word) - 1, -1, -1):
            node = parent.findChild(word[i])
            if not node:
                node = TrieNode(word[i])
                parent.addChild(node)
            parent = node
        parent.setEnd(index)        

    def search(self, word, index):
        matchedIndex = None
        finishedIndex = []
        parent = self.root
        if parent.endIndex != None and index != parent.endIndex:
            finishedIndex.append(parent.endIndex)
        for i in range(len(word)):
            node = parent.findChild(word[i])
            if node:
                if node.endIndex != None and index != node.endIndex:
                    if i == len(word) - 1:
                        matchedIndex = node.endIndex
                    else:
                        finishedIndex.append(node.endIndex)
                parent = node
            else:
                parent = None
                break
        return (matchedIndex, finishedIndex, parent)

    def getRemainStr(self, parent):
        arr = []
        def dfs(node, Str):
            nStr = Str + (node.val or '')
            if node.endIndex != None:
                remain = nStr[1:]
                if remain:
                    arr.append((remain, node.endIndex))
            for child in node.children:
                dfs(child, nStr)
        dfs(parent, '')
        return arr


def isPalindrome(word, l, r):
    while l < r:
        if word[l] != word[r]:
            return False
        l += 1
        r -= 1
    return True


print(Solution().palindromePairs(["abcd","dcba","lls","s","sssll"]))
print(Solution().palindromePairs(["bat","tab","cat"]))
print(Solution().palindromePairs(['a', '']))