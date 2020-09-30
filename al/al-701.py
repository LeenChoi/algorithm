# 二叉搜索树中的插入操作
# medium
'''
给定二叉搜索树（BST）的根节点和要插入树中的值，将值插入二叉搜索树。 返回插入后二叉搜索树的根节点。
输入数据保证，新值和原始二叉搜索树中的任意节点值都不同。
注意，可能存在多种有效的插入方式，只要树在插入后仍保持为二叉搜索树即可。 你可以返回任意有效的结果。

例如, 

给定二叉搜索树:

        4
       / \
      2   7
     / \
    1   3

和 插入的值: 5
你可以返回这个二叉搜索树:

         4
       /   \
      2     7
     / \   /
    1   3 5
或者这个树也是有效的:

         5
       /   \
      2     7
     / \   
    1   3
         \
          4
 

提示：

给定的树上的节点数介于 0 和 10^4 之间
每个节点都有一个唯一整数值，取值范围从 0 到 10^8
-10^8 <= val <= 10^8
新值和原始二叉搜索树中的任意节点值都不同


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/insert-into-a-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

--------------------------------------------------------
题解：模拟插入
模拟插入元素的步骤就可以，两种方法

一种是直接比较root，比root大就往右遍历，否则往左，遍历直至找到空缺的位置

另一种是，如果插入的元素在root的左右孩子之间，可以直接跟root交换，然后被换下来的root和原来的左右孩子比较，
决定向左还是向右遍历，然后反复此操作，直至没有可换的

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        pos = root
        while pos:
            if val <= pos.val:
                if pos.left:
                    pos = pos.left
                else:
                    pos.left = TreeNode(val)
                    pos = None
            else:
                if pos.right:
                    pos = pos.right
                else:
                    pos.right = TreeNode(val)
                    pos = None
        return root
