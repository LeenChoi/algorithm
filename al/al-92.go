// 反转链表 II
// medium
/*
* 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
*
* 说明:
* 1 ≤ m ≤ n ≤ 链表长度。
*
* 示例:
*
* 输入: 1->2->3->4->5->NULL, m = 2, n = 4
* 输出: 1->4->3->2->5->NULL
*
* 来源：力扣（LeetCode）
* 链接：https://leetcode-cn.com/problems/reverse-linked-list-ii
* 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*
* ---------------------------------------------------------
* 题解：
* 和整个链表翻转没区别，记好 p、q、t 仨指针的转移过程就好。
* 因为是部分翻转，所以需要一个头指针记录下起点，剩下的就是链表翻转了。注意判好起点终点完事。
*
 */

package main

func main() {

}

type ListNode struct {
	Val  int
	Next *ListNode
}

func reverseBetween(head *ListNode, left int, right int) *ListNode {
	if right-left == 0 {
		return head
	}
	hair := &ListNode{0, head}
	hair2 := hair
	cnt := 1
	var p, q, t *ListNode
	for cnt < left {
		hair2 = head
		head = head.Next
		cnt++
	}
	p = head
	q = p.Next
	if q != nil {
		t = q.Next
	}
	head.Next = nil

	for cnt < right {
		q.Next = p
		p = q
		q = t
		if t != nil {
			t = t.Next
		}
		cnt++
	}
	hair2.Next = p
	head.Next = q

	return hair.Next
}
