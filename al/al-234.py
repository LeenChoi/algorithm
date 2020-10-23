# 回文链表
# easy
'''
请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true
进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

------------------------------------------------
题解：双指针
快慢指针找到中点，中点往后的链表翻转，然后再两段链表遍历一遍看是否相等

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        # hair = ListNode(0, head)
        hair = ListNode(0)
        hair.next = head
        slow, fast = hair, hair
        count = 0
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            count += 1
        if count == 0:
            return True
        p, q = head, self.reverse(slow.next)
        for i in range(count):
            if p.val != q.val:
                return False
            p = p.next
            q = q.next
        return True

    def reverse(self, node) -> ListNode:
        p, q = node, None
        while p:
            tmp = p.next
            p.next = q
            q = p
            p = tmp
        return q


    