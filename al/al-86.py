# 分隔链表
# medium
'''
给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。

你应当保留两个分区中每个节点的初始相对位置。

示例:

输入: head = 1->4->3->2->5->2, x = 3
输出: 1->2->2->4->3->5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/partition-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

-------------------------------------------
题解：
直接遍历链表，拔节点连接到各自的分链表上，然后连接俩分链表。注意要先把 node 从原链表摘掉再连接到分表，即 node.next = null 操作

'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        smaller = ListNode(0)
        bigger = ListNode(0)
        p, q = smaller, bigger
        node = head
        while node != None:
            tmp = node
            node = node.next
            tmp.next = None
            if tmp.val < x:
                p.next = tmp
                p = tmp
            else:
                q.next = tmp
                q = tmp
        p.next = bigger.next
        return smaller.next