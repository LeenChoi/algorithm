# 路径总和 II
# medium
'''
给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。

说明: 叶子节点是指没有子节点的节点。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:

[
   [5,4,11,2],
   [5,8,4,5]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/path-sum-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import copy
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if root == None:
            return []
        ans, path = [], []
        queue = [[root, 0]]
        path.append(root.val)
        _sum = root.val
        while len(queue) > 0:
            item = queue[-1]
            node = item[0]
            if node.left and item[1] & 1 == 0:
                item[1] |= 1
                queue.append([node.left, 0])
                _sum += node.left.val
                path.append(node.left.val)
            elif node.right and item[1] & 2 == 0:
                item[1] |= 2
                queue.append([node.right, 0])
                _sum += node.right.val
                path.append(node.right.val)
            else:
                if not node.left and not node.right and _sum == sum:
                    ans.append(copy.deepcopy(path))
                _sum -= node.val
                queue.pop()
                path.pop()
        return ans