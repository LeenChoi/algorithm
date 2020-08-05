# 打家劫舍 III
# medium
'''
在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。

计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。

示例 1:

输入: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \ 
     3   1

输出: 7 
解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.
示例 2:

输入: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \ 
 1   3   1

输出: 9
解释: 小偷一晚能够盗取的最高金额 = 4 + 5 = 9.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/house-robber-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

---------------------------------------------
题解：dfs + dp
因为相邻父子节点不可以选，所以必须要跨一个或多个节点后才能再选，往后怎么选，取决于当前点的选和不选。所以 dp 的思路就有了，每个节点维护两个值
1. 选择当前节点时，当前节点往下的一棵树最大的值
2. 不选择当前节点时的最大值

设 f(n)、g(n) 为上两种情况得到的值，l、r 为当前节点的两个孩子
那么状态转移为:
f(n) = n.val + g(l) + g(r)
g(n) = max(f(l), g(l)) + max(f(r), g(r))

空间优化：
如果前序遍历，需要压栈，并且要维护一份 f,g 表，空间复杂度会很高
可以改成后续遍历，因为后续遍历最先遍历孩子，然后 dfs 函数返回该孩子的 f,g 结果，这样就省下了 f,g 表的空间

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root) -> int:
        def dfs(node):
            if not node:
                return (0, 0)
            l, r = dfs(node.left), dfs(node.right)
            selected = node.val + l[1] + r[1]
            nonSelected = max(l[0], l[1]) + max(r[0], r[1])
            return (selected, nonSelected)
        result = dfs(root)
        return max(result[0], result[1])

    

