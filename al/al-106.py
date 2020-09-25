# 从中序与后序遍历序列构造二叉树
# medium
'''
根据一棵树的中序遍历与后序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

中序遍历 inorder = [9,3,15,20,7]
后序遍历 postorder = [9,15,7,20,3]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

---------------------------------------------------------
题解：dfs
后续遍历有个特点，就是序列的最后一项肯定是某个子树(包括整个树)的根，然后就可以通过这个数，找中序遍历里面的索引位置，
以它为左的子数组为根的左子树，右子数组为右子树。
然后同样用这个索引，在后续遍历里面它以左是左子树，从它(包括)往右到最后第二项为右子树，因为最后一项为根

这样就又分出来了左右各自的前序遍历和后续遍历，反复递归，就能构建这棵树

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder, postorder) -> TreeNode:
        def dfs(inarr, portarr):
            if len(portarr) == 0:
                return None
            rootVal = portarr[-1]
            root = TreeNode(rootVal)
            cursor = inarr.index(rootVal)
            leftIn, rightIn = inarr[: cursor], inarr[cursor + 1 :]
            leftPost, rightPost = portarr[: cursor], portarr[cursor : -1]
            root.left = dfs(leftIn, leftPost)
            root.right = dfs(rightIn, rightPost)
            return root
        return dfs(inorder, postorder)