# 二叉树展开为链表
# medium
'''
给定一个二叉树，原地将它展开为一个单链表。

 

例如，给定二叉树

    1
   / \
  2   5
 / \   \
3   4   6
将其展开为：

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

------------------------------------------------------
题解：dfs
用一个栈缓存每个节点的右孩子(如果同时拥有左孩子)，然后 dfs 将左孩子链接到右孩子处，直到 dfs 到叶子节点，
随后从栈中取出原来的右孩子，嫁接到链表中

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        node = root
        stack = []
        while node:
            if node.left and node.right:
                stack.append(node.right)
                node.right = node.left
                node.left = None
            elif node.left:
                node.right = node.left
                node.left = None
            elif not node.right:
                if len(stack) > 0:
                    node.right = stack.pop()
                else:
                    node.right = None
            node = node.right
        
