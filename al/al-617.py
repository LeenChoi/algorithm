# 合并二叉树
# easy
'''
给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。

你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则不为 NULL 的节点将直接作为新二叉树的节点。

示例 1:

输入: 
	Tree 1                     Tree 2                  
          1                         2                             
         / \                       / \                            
        3   2                     1   3                        
       /                           \   \                      
      5                             4   7                  
输出: 
合并后的树:
	     3
	    / \
	   4   5
	  / \   \ 
	 5   4   7
注意: 合并必须从两个树的根节点开始。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-two-binary-trees
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

--------------------------------------------------
题解：dfs
此题有个巧妙的做法是，如果 t1、t2 中某个为 null，那么直接将不为 null 的节点及它的子树直接挂到当前正在构造的树上即可
原来我是复制构造，但跟上面的方法比，做了些没必要的操作

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        root = None
        def dfs(node1, node2):
            if not node1 and not node2:
                return None
            nonlocal root
            cur = TreeNode(0)
            if not root:
                root = cur
            if node1 or node2:
                left1 = node1.left if node1 else None
                left2 = node2.left if node2 else None
                cur.left = dfs(left1, left2)

            if node1:
                cur.val += node1.val
            if node2:
                cur.val += node2.val

            if node1 or node2:
                right1 = node1.right if node1 else None
                right2 = node2.right if node2 else None
                cur.right = dfs(right1, right2)
            return cur
        dfs(t1, t2)
        return root

            
class Solution2:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        if not t2:
            return t1
        tar = TreeNode(t1.val + t2.val)
        tar.left = self.mergeTrees(t1.left, t2.left)
        tar.right = self.mergeTrees(t1.right, t2.right)
        return tar