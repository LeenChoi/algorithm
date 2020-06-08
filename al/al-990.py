# 等式方程的可满足性
# medium
'''
给定一个由表示变量之间关系的字符串方程组成的数组，每个字符串方程 equations[i] 的长度为 4，并采用两种不同的形式之一："a==b" 或 "a!=b"。在这里，a 和 b 是小写字母（不一定不同），表示单字母变量名。
只有当可以将整数分配给变量名，以便满足所有给定的方程时才返回 true，否则返回 false。 

示例 1：
输入：["a==b","b!=a"]
输出：false
解释：如果我们指定，a = 1 且 b = 1，那么可以满足第一个方程，但无法满足第二个方程。没有办法分配变量同时满足这两个方程。

示例 2：
输出：["b==a","a==b"]
输入：true
解释：我们可以指定 a = 1 且 b = 1 以满足满足这两个方程。

示例 3：
输入：["a==b","b==c","a==c"]
输出：true

示例 4：
输入：["a==b","b!=c","c==a"]
输出：false

示例 5：
输入：["c==c","b==d","x!=z"]
输出：true
 

提示：
1 <= equations.length <= 500
equations[i].length == 4
equations[i][0] 和 equations[i][3] 是小写字母
equations[i][1] 要么是 '='，要么是 '!'
equations[i][2] 是 '='

---------------------------------------------
题解：并查集
    首先将所有 '==' 的式子都关联起来，做成一个大的并集，然后再遍历一次判断所有 '!=' 的式子是否冲突。
    原来我的想法是，遍历一次，碰到 '==' 就并上，碰到 '!=' 就将两个分别独立。
    但会有问题，如果先碰到 'a!=b', 将两个分别独立，再碰到 'a==c', 'c==b'，a 和 b 还会并到一起，那就错了 

'''


class UnionFindSet:
    def __init__(self):
        self.parents = {}

    def find(self, node):
        if self.parents.get(node) == None:
            self.parents[node] = node
        
        root = node
        # 查找根
        while True:
            parent = self.parents[root]
            if parent == root:
                break
            root = parent
        
        # 快速指向根
        nextNode = node
        while True:
            parent = self.parents[nextNode]
            if parent != root:
                self.parents[nextNode] = root
                nextNode = parent
            else:
                break
        return self.parents[node]
        

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        if root1 != root2:
            self.parents[root2] = root1
        print(self.parents)


class Solution:
    def equationsPossible(self, equations) -> bool:
        unionFindSet = UnionFindSet()
        # 先处理 '==' 的式子，将并查集都关联上
        for str in equations:
            if str[0] == str[3]:
                if str[1] == '!':
                    return False
                else:
                    unionFindSet.find(str[0])
            else:
                if str[1] == '=':
                    unionFindSet.union(str[0], str[3])

        # 再处理 '!=' 的式子，判断冲突
        for str in equations:
            if str[1] == '!':
                root1 = unionFindSet.find(str[0])
                root2 = unionFindSet.find(str[3])
                print(str[0], str[3], root1, root2)
                if root1 == root2:
                    return False
        return True



# print(Solution().equationsPossible(["c==c","b==d","x!=z"]))
# print(Solution().equationsPossible(["a==b","b!=c","c==a"]))
# print(Solution().equationsPossible(["a==b","b!=a"]))
print(Solution().equationsPossible(["a==b","e==c","b==c","a!=e"]))