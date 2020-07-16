# 不同的二叉搜索树 II
# medium
'''
给定一个整数 n，生成所有由 1 ... n 为节点所组成的 二叉搜索树 。

示例：

输入：3
输出：
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
解释：
以上的输出对应以下 5 种不同结构的二叉搜索树：

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
 

提示：

0 <= n <= 8

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-binary-search-trees-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

----------------------------------
题解：递归，和 95 题一个思路
95 题dp就可以输出个数，但此题需要递归去构造每个树

一开始我的想法是 gentree(n) n是节点数，去递归构造，但不行
官方题解是分治法的递归思路， gentree(start, end), 就好理解多了

要注意的是，需要左段和右端递归完后，for循环依次取左右节点时新构造一个当前node，组成新的树
如果先构造当前node再接左右节点，因为指针都是引用，其实始终都构造到一个树上了

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int):
        def genSubTree(start, end):
            if start > end:
                return [None]
            nodeList = []
            for i in range(start, end + 1):
                left = genSubTree(start, i - 1)
                right = genSubTree(i + 1, end)
                for lchild in left:
                    for rchild in right:
                        node = TreeNode(i)
                        node.left = lchild
                        node.right = rchild
                        nodeList.append(node)
            return nodeList
        return genSubTree(1, n) if n > 0 else []
        

