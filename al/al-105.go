// 从前序与中序遍历序列构造二叉树
// medium
/*
* 根据一棵树的前序遍历与中序遍历构造二叉树。
*
* 注意:
* 你可以假设树中没有重复的元素。
*
* 例如，给出
*
* 前序遍历 preorder = [3,9,20,15,7]
* 中序遍历 inorder = [9,3,15,20,7]
* 返回如下的二叉树：
*
*     3
*    / \
*   9  20
*     /  \
*    15   7
*
* 来源：力扣（LeetCode）
* 链接：https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal
* 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*
* -----------------------------------------------------------------------
* 题解：dfs
* 利用前序和中序的性质即可。前序遍历先读根的性质，可以通过 preorder 取首元素得到根节点，再在 inorder 里查找这个根节点
* 所在的 index，将 inorder 一分为二，左面的为当前跟节点的左子树，右面为右子树。
* 利用 dfs 递归上述过程构造根节点即可。
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

func buildTree(preorder []int, inorder []int) *TreeNode {
	var dfs func(preorder, inorder []int) *TreeNode
	dfs = func(preorder, inorder []int) *TreeNode {
		if len(preorder) == 0 {
			return nil
		}
		rootVal := preorder[0]
		preorder = preorder[1:]
		root := &TreeNode{rootVal, nil, nil}

		mid := index(inorder, rootVal)
		leftorder := inorder[:mid]
		rightorder := inorder[mid+1:]
		root.Left = dfs(preorder[:len(leftorder)], leftorder)
		root.Right = dfs(preorder[len(leftorder):], rightorder)

		return root
	}
	return dfs(preorder, inorder)
}

func index(arr []int, num int) int {
	for i, v := range arr {
		if v == num {
			return i
		}
	}
	return -1
}
