# 恢复二叉搜索树
# hard
'''
给你二叉搜索树的根节点 root ，该树中的两个节点被错误地交换。请在不改变其结构的情况下，恢复这棵树。

进阶：使用 O(n) 空间复杂度的解法很容易实现。你能想出一个只使用常数空间的解决方案吗？

示例 1：

   [1]                  [3]
   /                    /
 [3]         ==>      [1]
   \                    \
    2                    2

输入：root = [1,3,null,null,2]
输出：[3,1,null,null,2]
解释：3 不能是 1 左孩子，因为 3 > 1 。交换 1 和 3 使二叉搜索树有效。

示例 2：

    [3]                 [2]
    / \                 / \
   1   4      ==>      1   4
      /                   /
    [2]                 [3]

输入：root = [3,1,4,null,null,2]
输出：[2,1,4,null,null,3]
解释：2 不能在 3 的右子树中，因为 2 < 3 。交换 2 和 3 使二叉搜索树有效。
 

提示：

树上节点的数目在范围 [2, 1000] 内
-231 <= Node.val <= 231 - 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/recover-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

--------------------------------------------
题解：dfs
二叉搜索树的性质就是左小右大，中序遍历的队列是有序的，某两个节点值有交换，那么中序遍历后肯定有一对或两对数是反序的，
找到最开始反序的头一个数和最后反序的后一个数交换就可以了。

dfs遍历(用的迭代法，好跳出循环)，维护一个 pre 节点用来和当前节点判断，找出反序头一个节点和后一个节点，交换值

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        node = root
        stack = []
        pre, x, y = None, None, None
        while len(stack) != 0 or node != None:
            while node != None:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if pre != None and pre.val > node.val:
                y = node
                if x == None:
                    x = pre
                else:
                    break
            pre = node
            node = node.right
        x.val, y.val = y.val, x.val