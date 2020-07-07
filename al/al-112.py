# 路径总和
# easy
'''
给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。

说明: 叶子节点是指没有子节点的节点。

示例: 
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/path-sum
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
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root == None:
            return False
        queue = [[root, 0]]
        _sum = root.val
        while len(queue) > 0:
            item = queue[-1]
            node = item[0]
            if node.left and item[1] & 1 == 0 :
                item[1] |= 1
                queue.append([node.left, 0])
                _sum += node.left.val
            elif node.right and item[1] & 2 == 0:
                item[1] |= 2
                queue.append([node.right, 0])
                _sum += node.right.val
            else:
                if not node.left and not node.right and _sum == sum:
                    return True
                _sum -= node.val
                queue.pop()
        return False
            
                
print(Solution().hasPathSum(treeFunc.deserialize([5,4,8,11,None,13,4,7,2,None,None,None,1]), 22))


