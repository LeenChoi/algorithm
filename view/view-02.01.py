# 移除重复节点
# easy
'''
编写代码，移除未排序链表中的重复节点。保留最开始出现的节点。

示例1:

 输入：[1, 2, 3, 3, 2, 1]
 输出：[1, 2, 3]
示例2:

 输入：[1, 1, 1, 1, 2]
 输出：[1, 2]
提示：

链表长度在[0, 20000]范围内。
链表元素在[0, 20000]范围内。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicate-node-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

------------------------------------
题解：hashmap
    遍历链表，hashmap记录出现过的节点，遍历时如果该节点重复，
    将pre节直接连接到下一个节点上，绕过重复节点

'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        m = {}
        pre, node = None, head
        while node:
            if m.get(node.val) == None:
                m[node.val] = 1
                pre = node
                node = node.next
            else:
                pre.next = node.next
                node = node.next
        return head