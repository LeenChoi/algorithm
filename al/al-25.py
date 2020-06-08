# K个一组翻转链表
'''
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
k 是一个正整数，它的值小于或等于链表的长度。
如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

示例：
给你这个链表：1->2->3->4->5
当 k = 2 时，应当返回: 2->1->4->3->5
当 k = 3 时，应当返回: 3->2->1->4->5

说明：
你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

---------------------------------------
题解：这题没啥算法，就是注意几个指针的移动，我把每k个分成一组做正常的翻转，
    然后记录下头尾指针，最后几个头尾指针相连即可。
    我在每组的翻转中是直接做翻转，最后如果发现长度不够k，再翻回来

    官方题解给的是每组先遍历一遍看看长度够不够，但这样的话时间复杂度其实是2n
    我的做法是 n+k

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverse(self, head, k, array, revert):
        # 这个是正常的链表翻转
        # p, q, y = head, head.next, None
        # # head.next = None
        # if q:
        #     y = q.next
        
        # while q:
        #     # q.next = p
        #     if p == head:
        #         q.next = None
        #     else:
        #         q.next = p
        #     p = q
        #     q = y
        #     if y:
        #         y = y.next
        # return p


        p, q, y = head, head.next, None
        if q:
            y = q.next

        count = 0
        while q and count < k:
            if p == head:
                q.next = None

            else:
                q.next = p
            p = q
            q = y
            if y:
                y = y.next
            count += 1

        tail = head.next
        head.next = p
        if count < k and not revert:
            return self.reverse(head, k, array, True)
        else:
            array.append((head, tail))
            newHead = ListNode(None)
            newHead.next = q    
            return newHead

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        array = []
        while head.next:
            head = self.reverse(head, k, array, False)

        for i in range(0, len(array) - 1):
            array[i][1].next = array[i + 1][0].next
        return array[0][0]
        




def makeChain(nums):
    head = ListNode(nums[0])
    prenode = head
    for i in range(0, len(nums)):
        node = ListNode(nums[i])
        prenode.next = node
        prenode = node
    return head

def printChain(head):
    node = head.next
    a = []
    while node:
        a.append(node.val)
        node = node.next
    print(a)




head = makeChain([1,2,3,4,5])

solution = Solution()
res = solution.reverseKGroup(head, 3)
printChain(res)