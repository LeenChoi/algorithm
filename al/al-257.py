# 二叉树的所有路径
# easy
'''
给定一个二叉树，返回所有从根节点到叶子节点的路径。

说明: 叶子节点是指没有子节点的节点。

示例:

输入:

   1
 /   \
2     3
 \
  5

输出: ["1->2->5", "1->3"]

解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-paths
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''

import treeFunc

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode):
        if root == None:
            return []
        queue, ans = [[root, 0]], []
        while len(queue) > 0:
            item = queue[-1]
            node = item[0]
            if node.left and item[1] & 1 == 0 :
                item[1] |= 1
                queue.append([node.left, 0])
            elif node.right and item[1] & 2 == 0:
                item[1] |= 2
                queue.append([node.right, 0])
            else:
                if not node.left and not node.right:
                    ans.append(genStr(queue))
                queue.pop()
        return ans
            

def genStr(arr):
    _str = ''
    length = len(arr)
    for i in range(length):
        node = arr[i][0]
        _str += str(node.val)
        if i < length - 1:
            _str += '->'
    return _str


print(Solution().binaryTreePaths(treeFunc.deserialize([1,2,3,None,5])))