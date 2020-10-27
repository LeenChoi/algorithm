# 二叉树的前序遍历
# medium
'''
给定一个二叉树，返回它的 前序 遍历。

 示例:

输入: [1,null,2,3]  
   1
    \
     2
    /
   3 

输出: [1,2,3]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-preorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

-------------------------------------------
题解：迭代法，morris
迭代法一个迭代写法就能完成
morris遍历是常数空间复杂度的算法，递归和迭代都需要额外的空间记录，morris遍历是通过连接空闲指针让当前节点和它的前继节点相连接，
使之在遍历完当前节点后可以透明地直接遍历到后继节点，详细算法见 al-501

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode):
        node = root
        ans, stack = [], []
        while node != None:
            ans.append(node.val)
            if node.right != None:
                stack.append(node.right)
            node = node.left
            if node == None and len(stack) > 0:
                node = stack.pop()
        return ans
