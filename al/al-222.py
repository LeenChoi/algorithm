#  完全二叉树的节点个数
# medium
'''
给出一个完全二叉树，求出该树的节点个数。

说明：

完全二叉树的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层，则该层包含 1~ 2h 个节点。

示例:

输入: 
    1
   / \
  2   3
 / \  /
4  5 6

输出: 6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-complete-tree-nodes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

----------------------------------------------------------
题解：位运算 + 二分查找
完全二叉树特性，高度差最多差1，也就是说树的上层都是满的，查节点有多少个只需查最后一层叶子节点的个数就成。
最后一层编号从 2^h 到 2^(h+1)-1，只需在这范围里二分查找就可以了。

那么怎么精确遍历到这范围内指定的节点，比如示例里的5 怎么遍历到它，6 的二进制 110 就是遍历时指针的走向，
0 向左走，1 向右走，根节点算是 1，可以看做已经通过 1 向右走走到了根节点，110 剩下的 10 从根节点向右走再向左走，
就能遍历到 6 了。用此方法找某个节点手否存在并且缩短二分查找的范围就能找到最后一个节点，它的编号即是节点个数了。

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        def search(pos):
            node = root
            stack = []
            while pos != 0:
                key = pos & 1
                stack.append(key)
                pos >>= 1
            stack.pop()
            while len(stack) != 0:
                key = stack.pop()
                if key == 0:
                    node = node.left
                else:
                    node = node.right
            return node
        level = 0
        node = root
        while node.left:
            level += 1
            node = node.left
        start, end = pow(2, level), pow(2, level + 1) - 1
        while start < end:
            mid = (start + end) // 2
            if search(mid):
                start = mid + 1
            else:
                end = mid
        return start if search(start) else start - 1
