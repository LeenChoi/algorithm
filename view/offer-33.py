# 二叉搜索树的后序遍历序列
# medium
'''
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。

 

参考以下这颗二叉搜索树：

     5
    / \
   2   6
  / \
 1   3
示例 1：

输入: [1,6,3,2,5]
输出: false
示例 2：

输入: [1,3,2,6,5]
输出: true

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

------------------------------------------------------
题解：递归分治
二叉搜索树后续遍历的性质是，最后一位为root，从后向前遍历大于root的一段为右子树，小于root的一段为左子树。
所以从头遍历，先分出小于root的一段，再分出大于root的一段，最后如果游标等于root位置，那么这一整串是符合二叉搜索树的。
然后递归地将刚才分出来的左子树，右子树用同样的方法分，直到某一段只剩一个节点，那么返回true。
最后判断游标是否等于root位置，并且左子树，右子树的递归判断都返回true，那么这一整串就是符合二叉搜索树的。

'''


class Solution:
    def verifyPostorder(self, postorder) -> bool:
        def solve(i, j):
            if i == j:
                return True
            p = i
            while postorder[p] < postorder[j]:
                p += 1
            m = p
            while postorder[p] > postorder[j]:
                p += 1
            return p == j and solve(i, m - 1) and solve(m, j - 1)
        return solve(0, len(postorder) - 1)

        