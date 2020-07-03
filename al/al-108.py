# 将有序数组转换为二叉搜索树
# easy
'''
将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:
给定有序数组: [-10,-3,0,5,9],

一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

-----------------------------------
题解：dfs 
看题意，应该是每个节点的左孩子比自己小，右孩子比自己大，然后构成一个平衡树，
因为是有序数组，所以根据题意，直接对数组二分法，mid点就是父节点，分成的两段数组分别是左孩子和右孩子群,
然后分别递归就可以了

'''

import treeFunc

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums) -> TreeNode:
        def order(l, r):
            mid = (l + r + 1) // 2
            node = TreeNode(nums[mid])
            if mid > l:
                node.left = order(l, mid - 1)
            if mid < r:
                node.right = order(mid + 1, r)
            return node
        return order(0, len(nums) - 1)


    
print(treeFunc.serialize(Solution().sortedArrayToBST([-10,-3,0,5,9])))
    