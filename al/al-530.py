# 二叉搜索树的最小绝对差
# easy
'''
给你一棵所有节点为非负值的二叉搜索树，请你计算树中任意两节点的差的绝对值的最小值。

示例：

输入：

   1
    \
     3
    /
   2

输出：
1

解释：
最小绝对差为 1，其中 2 和 1 的差的绝对值为 1（或者 2 和 3）。
 

提示：

树中至少有 2 个节点。
本题与 783 https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/ 相同

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

----------------------------------------------------------
题解：中序遍历
这种题就是利用二叉搜索树的特性，他的中序遍历是有序的，从有序列表里找出差值最小，那不就是遍历一遍，相邻俩数比较最小的就是么。
此类题我老犯不审题的错，利用题本身特性去解题很简单

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        pre, _min = None, None
        def dfs(node):
            nonlocal pre, _min
            if not node:
                return None
            dfs(node.left)
            if pre == None:
                pre = node.val
            else:
                _curMin = abs(node.val - pre)
                _min = _curMin if _min == None else min(_min, _curMin)
                pre = node.val
            dfs(node.right)
        dfs(root)
        return _min


