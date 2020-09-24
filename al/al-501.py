# 二叉搜索树中的众数
# easy
'''
给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。

假定 BST 有如下定义：

结点左子树中所含结点的值小于等于当前结点的值
结点右子树中所含结点的值大于等于当前结点的值
左子树和右子树都是二叉搜索树
例如：
给定 BST [1,null,2,2],

   1
    \
     2
    /
   2
返回[2].

提示：如果众数超过1个，不需考虑输出顺序

进阶：你可以不使用额外的空间吗？（假设由递归产生的隐式调用栈的开销不被计算在内）

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-mode-in-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

-----------------------------------------------
题解：Morris 中序遍历
朴素想法是，一次dfs，然后记个哈希表。
或者一次中序遍历得到序列，此时的序列是有序的，然后遍历此序列，记连续相同的个数，最后统计

但中序遍历后的序列还是需要一个 O(n) 的空间，怎么能 O(1) 的空间遍历呢，那就是 Morris 中序遍历

他的思想就是将当前节点挂到它的左子树里最右的节点下，因为中序遍历是 (左-当前-右) 的顺序，
当前节点的左子树的最右节点(前继节点)遍历完后才会遍历当前节点，所以如果把当前节点挂到那个最右节点的右孩子位置，
那么按中序遍历的顺序，下一个就是遍历当前节点了。

所以从当前节点左子树开始，不断的做 cur 节点挂到左子树最右节点.right 这个操作，反复迭代，如果某个节点没有左子树，
那么就遍历这个 cur 节点，然后向右子树迭代。

算法的一个核心判断是 pre.right != cur，cur 指针会在反复迭代后遍历到某个后挂上去的节点，重新指向那个节点，
然后 pre 指针也会遍历到那个节点的前继节点，最后会产生 pre.right == cur 的情况，表明那个cur节点的所有左子树都遍历完了，
该遍历自己，然后向右子树迭代了。

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findMode(self, root: TreeNode):
        base, count, maxCount, maxVal = None, 0, 0, []
        def update(val):
            nonlocal base, count, maxCount, maxVal
            if base == val:
                count += 1
            else:
                base = val
                count = 1
            if count == maxCount:
                maxVal.append(val)
            elif count > maxCount:
                maxCount = count
                maxVal = [val]
        cur = root
        while cur:
            if not cur.left:
                update(cur.val)
                cur = cur.right
                continue
            pre = cur.left
            while pre.right and pre.right != cur:
                pre = pre.right
            if not pre.right:
                pre.right = cur
                cur = cur.left
            else:
                pre.right = None
                update(cur.val)
                cur = cur.right
        return maxVal

