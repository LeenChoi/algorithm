# 有序链表转换二叉搜索树
# medium
'''
给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:

给定的有序链表： [-10, -3, 0, 5, 9],

一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

---------------------------------------
题解：分治 + 中序遍历
和 al-108 一样，可以先把链表先转成数组，然后和 108 解法相同，分治法+前序遍历构造 

还有无需转成数组，中序遍历构造的解法，升序链表其实就是二叉搜索树中序遍历后的结果，所以按中序遍历构造一个树的时候，
实际访问到节点的顺序就是遍历链表的顺序，可以直接一边遍历链表，一边中序遍历构造树。分治法从 mid 处构建 root 节点，
但只是生成节点，不赋值，在 dfs 中序访问到的时候再赋值

'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if head == None:
            return None
        nums = []
        node = head
        while node != None:
            nums.append(node.val)
            node = node.next
        def order(l, r):
            mid = (l + r + 1) // 2
            node = TreeNode(nums[mid])
            if mid > l:
                node.left = order(l, mid - 1)
            if mid < r:
                node.right = order(mid + 1, r)
            return node
        return order(0, len(nums) - 1)


class Solution2:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        length = 0
        node = head
        while node != None:
            length += 1
            node = node.next
        nnode = head
        def order(l, r):
            if l > r:
                return None
            mid = (l + r + 1) // 2
            root = TreeNode()
            root.left = order(l, mid - 1)
            nonlocal nnode
            root.val = nnode.val
            nnode = nnode.next
            root.right = order(mid + 1, r)
            return root
        return order(0, length - 1)