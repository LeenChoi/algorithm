// 完全二叉树插入器
// medium
/*
* 完全二叉树是每一层（除最后一层外）都是完全填充（即，节点数达到最大）的，并且所有的节点都尽可能地集中在左侧。
*
* 设计一个用完全二叉树初始化的数据结构 CBTInserter，它支持以下几种操作：
*
* CBTInserter(TreeNode root) 使用头节点为 root 的给定树初始化该数据结构；
* CBTInserter.insert(int v)  向树中插入一个新节点，节点类型为 TreeNode，值为 v 。使树保持完全二叉树的状态，并返回插入的新节点的父节点的值；
* CBTInserter.get_root() 将返回树的头节点。
*
*
* 示例 1：
*
* 输入：inputs = ["CBTInserter","insert","get_root"], inputs = [[[1]],[2],[]]
* 输出：[null,1,[1,2]]
* 示例 2：
*
* 输入：inputs = ["CBTInserter","insert","insert","get_root"], inputs = [[[1,2,3,4,5,6]],[7],[8],[]]
* 输出：[null,3,4,[1,2,3,4,5,6,7,8]]
*
*
* 提示：
*
* 最初给定的树是完全二叉树，且包含 1 到 1000 个节点。
* 每个测试用例最多调用 CBTInserter.insert  操作 10000 次。
* 给定节点或插入节点的每个值都在 0 到 5000 之间。
*
* 来源：力扣（LeetCode）
* 链接：https://leetcode-cn.com/problems/complete-binary-tree-inserter
* 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*
* ---------------------------------------------------------------
* 题解：队列
* 插入过程其实就是树的最后一层从左往右找空位置插入，所以需要一个队列能够记录目前有哪些节点左右孩子不饱和。
* 插入新节点的时候，将此节点加到队列末尾，然后将它的父节点指到队首的节点上，因为队列里记录的节点都是左右孩子不饱和的，
* 所以直接取队首节点即可。之后看队首节点左右还是是否饱和，饱和就从队列里移除。
*
* 队列的初始化过程，直接root节点开始bfs即可，判断如果一个节点，它的孩子不饱和，直接入队
*
 */

package main

func main() {

}

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

type CBTInserter struct {
	root  *TreeNode
	deque []*TreeNode
}

func Constructor(root *TreeNode) CBTInserter {
	q := []*TreeNode{root}
	deque := []*TreeNode{}
	for len(q) > 0 {
		node := q[0]
		q = q[1:]
		if node.Left == nil || node.Right == nil {
			deque = append(deque, node)
		}
		if node.Left != nil {
			q = append(q, node.Left)
		}
		if node.Right != nil {
			q = append(q, node.Right)
		}
	}
	return CBTInserter{root, deque}
}

func (this *CBTInserter) Insert(v int) int {
	node := TreeNode{v, nil, nil}
	this.deque = append(this.deque, &node)
	pa := this.deque[0]
	if pa.Left == nil {
		pa.Left = &node
	} else {
		pa.Right = &node
		this.deque = this.deque[1:]
	}
	return pa.Val
}

func (this *CBTInserter) Get_root() *TreeNode {
	return this.root
}

/**
 * Your CBTInserter object will be instantiated and called as such:
 * obj := Constructor(root);
 * param_1 := obj.Insert(v);
 * param_2 := obj.Get_root();
 */
