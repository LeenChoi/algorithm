# 对称二叉树
# easy
'''
给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
 
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3

进阶：
你可以运用递归和迭代两种方法解决这个问题吗？

-------------------------
题解：
    递归和迭代都可以，root的左右子树分别遍历左面的正常前序遍历，右面的反向前序遍历，最后比较俩数组相等即可

    迭代的话就是借助一个队列，node入队，然后左右节点分别入队(root右子树的话是右左顺序入队)，
    然后遍历队列，依次对元素的子节点入队，最后比较两个队列是否想的即可

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def order(self, node, opposite, arr):
        if node:
            arr.append(node.val)
        else:
            arr.append(None)
            return

        if opposite:
            self.order(node.right, opposite, arr)
            self.order(node.left, opposite, arr)
        else:
            self.order(node.left, opposite, arr)
            self.order(node.right, opposite, arr)

    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        larr, rarr = [], []
        self.order(root.left, False, larr)
        self.order(root.right, True, rarr)
        return larr == rarr