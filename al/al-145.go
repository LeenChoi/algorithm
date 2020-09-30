// 二叉树的后序遍历
// medium
/*
* 给定一个二叉树，返回它的 后序 遍历。
*
* 示例:
*
* 输入: [1,null,2,3]
*    1
*     \
*      2
*     /
*    3
*
* 输出: [3,2,1]
* 进阶: 递归算法很简单，你可以通过迭代算法完成吗？
*
* 来源：力扣（LeetCode）
* 链接：https://leetcode-cn.com/problems/binary-tree-postorder-traversal
* 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*
* ----------------------------------------------------
* 题解：后序遍历，迭代
* 和迭代法中序遍历一个思路，但是有个要注意的地方，中序是循环一直遍历到最左的节点，然后直接就可以遍历root节点，然后再把指针
* 扔给right就可以了，交个下个迭代。
* 但后序遍历要缓一下root节点，需要判断right是否存在，存在则指针扔给right，走下次迭代，否则访问该节点，并且需要记录pre，
* pre是用来记下一个要遍历的节点它的right有没有遍历过，因为有right判断，如果不记pre，会一直在right循环下去
*
 */

package main

func main() {

}

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func postorderTraversal(root *TreeNode) []int {
	if root == nil {
		return nil
	}
	var pre *TreeNode
	stack := []*TreeNode{}
	ans := []int{}
	node := root
	for node != nil || len(stack) > 0 {
		for node != nil {
			stack = append(stack, node)
			node = node.Left
		}
		node = stack[len(stack)-1]
		if node.Right == nil || node.Right == pre {
			stack = stack[:len(stack)-1]
			ans = append(ans, node.Val)
			pre = node
			node = nil
		} else {
			node = node.Right
		}
	}
	return ans
}
