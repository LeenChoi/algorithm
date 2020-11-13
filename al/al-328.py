# 奇偶链表
# medium
'''
给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。

请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。

示例 1:

输入: 1->2->3->4->5->NULL
输出: 1->3->5->2->4->NULL
示例 2:

输入: 2->1->3->5->6->4->7->NULL 
输出: 2->3->6->7->1->5->4->NULL
说明:

应当保持奇数节点和偶数节点的相对顺序。
链表的第一个节点视为奇数节点，第二个节点视为偶数节点，以此类推。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/odd-even-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

---------------------------------------------
题解：
链表分离后重合

'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        oddHead, evenHead = ListNode(), ListNode()
        p, q, node = oddHead, evenHead, head
        number = 1
        while node != None:
            if number % 2 == 1:
                p.next = node
                p = p.next
            else:
                q.next = node
                q = q.next
            node = node.next
            number += 1
        q.next = None # 这里注意，有可能链表是以奇数位结尾，所以 q 偶数链的末尾要指向 null
        p.next = evenHead.next
        return oddHead.next


