# 平衡二叉树
# easy
'''
给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

示例 1:

给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7
返回 true 。

示例 2:

给定二叉树 [1,2,2,3,3,null,null,4,4]

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
返回 false 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/balanced-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

--------------------------------------------------
题解：dfs
dfs 过程中记录每个节点的深度即可，然后每层节点都判下左右孩子的深度差时候大于1

'''

import treeFunc

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def order(node):
            left, right = 0, 0
            balance = True
            if node.left:
                leftResult = order(node.left)
                balance = balance and leftResult[0]
                left = leftResult[1]
            if node.right:
                rightResult = order(node.right)
                balance = balance and rightResult[0]
                right = rightResult[1]
            if abs(left - right) > 1:
                balance = balance and False
            return (balance, max(left, right) + 1)
        ans = order(root)
        return ans[0]
            

print(Solution().isBalanced(treeFunc.deserialize([1,2,2,3,3,None,None,4,4])))