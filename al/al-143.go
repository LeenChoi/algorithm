// 143. 重排链表
// medium
/*
* 给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
* 将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…
*
* 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
*
* 示例 1:
*
* 给定链表 1->2->3->4, 重新排列为 1->4->2->3.
* 示例 2:
*
* 给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.
*
* 来源：力扣（LeetCode）
* 链接：https://leetcode-cn.com/problems/reorder-list
* 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*
* -------------------------------------------------
* 题解：线性表，找中点翻转合并
* 1.遍历链表记录到线性表(数组等)里，然后通过下标就能快速访问到对应的节点然后连接。
* 2.找中点，然后后段链表翻转，再两段链表合并。找中点我是先遍历一遍长度，然后长度/2，再重新遍历找到中点。
* 	其实链表题很多都会用到快慢指针，找中点就是其中一个场景，利用快慢指针遍历一遍就能找到中点。
*
 */

package main

func main() {

}

// Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

func reorderList(head *ListNode) {
	if head == nil {
		return
	}
	// 找中点
	count := 0
	hair := &ListNode{0, head}
	node := hair
	for node.Next != nil {
		node = node.Next
		count += 1
	}
	if count == 1 {
		return
	}
	headCount := count / 2

	node = hair
	count = 0
	for count < headCount {
		node = node.Next
		count += 1
	}
	tailHead := node.Next
	node.Next = nil

	// tail链翻转
	tailHair := &ListNode{0, tailHead}
	var p, q *ListNode
	p = tailHair.Next
	if p.Next != nil {
		q = p.Next
		tailHair.Next = q
		p.Next = nil
		for q.Next != nil {
			tailHair.Next = q.Next
			q.Next = p
			p = q
			q = tailHair.Next
		}
		q.Next = p
	}

	// 合并
	var p1, q1, p2, q2 *ListNode
	p1, p2 = head, tailHair.Next
	for p1.Next != nil {
		q1 = p1.Next
		q2 = p2.Next
		p1.Next = p2
		p2.Next = q1
		p1, p2 = q1, q2
	}
	p1.Next = p2
}

// 标准的链表翻转(这里的head是第一个节点)
func reverseList(head *ListNode) *ListNode {
	var pre, cur *ListNode = nil, head
	for cur != nil {
		next := cur.Next
		cur.Next = pre
		pre = cur
		cur = next
	}
	return pre
}

// 标准的找中点，快慢指针
func middleNode(head *ListNode) *ListNode {
	slow, fast := head, head
	for fast.Next != nil && fast.Next.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
	}
	return slow
}
