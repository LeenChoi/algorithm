//  两两交换链表中的节点
//  medium
/*
* 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
*
* 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
*
*
*
* 示例:
*
* 给定 1->2->3->4, 你应该返回 2->1->4->3.
*
* 来源：力扣（LeetCode）
* 链接：https://leetcode-cn.com/problems/swap-nodes-in-pairs
* 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*
* --------------------------------------------------
* 题解：链表翻转
* 没啥难的，控制好指针就行，注意的是这里的head不是真正的头结点，而是第一个结点，所以定义一个hair结点当做真正的head就好做了
*
 */

//  Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

func swapPairs(head *ListNode) *ListNode {
	var h, p, q *ListNode
	hair := &ListNode{0, head}
	h = hair
	for h.Next != nil && h.Next.Next != nil {
		p = h.Next
		q = h.Next.Next
		p.Next = q.Next
		q.Next = p
		h.Next = q
		h = p
	}
	return hair.Next
}