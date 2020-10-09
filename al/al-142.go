// 环形链表 II
// medium
/*
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
如果 pos 是 -1，则在该链表中没有环。

说明：不允许修改给定的链表。

示例如 al-141

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/linked-list-cycle-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

------------------------------------------
题解：Floyd 算法
首先快慢指针找到相遇的那个点，然后将一个指针重置回起点，一个在相遇点，然后同时两个指针都走一步，
最终俩指针再相遇，则相遇点即是入环点

证明，假设起点到入环点的距离为 t, 入环点到相遇点的距离为 a, 相遇回到入环点的距离为b，环的周长为l
2(t + a) = t + a + kl
t + a = kl
t = kl - a = (k-1)l + l - a
t = l - a = b

*/

//  Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

func detectCycle(head *ListNode) *ListNode {
	one, two := head, head
	for one != nil && two != nil {
		one = one.Next
		two = two.Next
		if two != nil {
			two = two.Next
			if one == two {
				break
			}
		}
	}
	if one == nil || two == nil {
		return nil
	}
	one = head
	for one != two {
		one = one.Next
		two = two.Next
	}
	return one
}