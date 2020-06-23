# 节点与其祖先之间的最大差值
# medium
'''
给定二叉树的根节点 root，找出存在于不同节点 A 和 B 之间的最大值 V，其中 V = |A.val - B.val|，且 A 是 B 的祖先。
（如果 A 的任何子节点之一为 B，或者 A 的任何子节点是 B 的祖先，那么我们认为 A 是 B 的祖先）
 
示例：
            8
           / \
          3   10
         / \    \
        1   6    14
           / \   /
          4   7 13

输入：[8,3,10,1,6,null,14,null,null,4,7,13]
输出：7

解释： 
我们有大量的节点与其祖先的差值，其中一些如下：
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
在所有可能的差值中，最大值 7 由 |8 - 1| = 7 得出。 

提示：
树中的节点数在 2 到 5000 之间。
每个节点的值介于 0 到 100000 之间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-difference-between-node-and-ancestor
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

--------------------------------------------
题解：dfs + 最大最小栈
    dfs 迭代法，做个最大栈和最小栈，遍历时记录当前路径的最大值最小值
    最后 dfs 迭代到某个节点的时候，将当前值与其父节点路径的最大值最小值做个差值取最大

'''


import treeFunc

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        maxValStack = [root.val]
        minValStack = [root.val]
        stack = [root]
        ans = 0
        while len(stack) > 0:
            node = stack[-1]
            if node.left and node.left.val != None:
                stack.append(node.left)
                _max = node.left.val if node.left.val > maxValStack[-1] else maxValStack[-1]
                maxValStack.append(_max)
                _min = node.left.val if node.left.val < minValStack[-1] else minValStack[-1]
                minValStack.append(_min)

            elif node.right and node.right.val != None:
                stack.append(node.right)
                _max = node.right.val if node.right.val > maxValStack[-1] else maxValStack[-1]
                maxValStack.append(_max)
                _min = node.right.val if node.right.val < minValStack[-1] else minValStack[-1]
                minValStack.append(_min)

            else:
                if node != root:
                    maxValStack.pop()
                    minValStack.pop()
                    ans = max(abs(maxValStack[-1] - node.val), abs(minValStack[-1] - node.val), ans)
                node.val = None
                stack.pop()
        return ans
        


print(Solution().maxAncestorDiff(treeFunc.deserialize([8,3,10,1,6,None,14,None,None,4,7,13])))