// 删除排序链表中的重复元素 II
// medium
/*
* 存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除链表中所有存在数字重复情况的节点，只保留原始链表中 没有重复出现 的数字。
*
* 返回同样按升序排列的结果链表。
*
*
*
* 示例 1：
*
*
* 输入：head = [1,2,3,3,4,4,5]
* 输出：[1,2,5]
* 示例 2：
*
*
* 输入：head = [1,1,1,2,3]
* 输出：[2,3]
*
*
* 提示：
*
* 链表中节点数目在范围 [0, 300] 内
* -100 <= Node.val <= 100
* 题目数据保证链表已经按升序排列
*
* 来源：力扣（LeetCode）
* 链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii
* 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*
* --------------------------------------------------------------------
* 题解：
*
* 做三个指针 h，p，q 一次遍历，来回倒就完了。
* 记一个状态，表示当前操作是否要删除。当 p、q 相等时，状态置为 true，不相等时，状态置为 false。
* 然后根据这个状态，删除 p 即可。
*
 */

package main

func main() {

}

type ListNode struct {
	Val  int
	Next *ListNode
}

func deleteDuplicates(head *ListNode) *ListNode {
	if head == nil {
		return head
	}
	hair := &ListNode{0, head}
	del := false
	h, p, q := hair, head, head.Next
	for p != nil {
		if del {
			if q == nil || p.Val != q.Val {
				del = false
			}
			h.Next = q
			p.Next = nil
			p = q
			if p != nil {
				q = p.Next
			}
		} else {
			if q == nil || p.Val != q.Val {
				h = p
				p = q
				if p != nil {
					q = p.Next
				}
			} else {
				del = true
			}
		}
	}
	return hair.Next
}
