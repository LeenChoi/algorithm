// 二叉搜索树的最近公共祖先
// easy
/*
* 给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。
*
* 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
*
* 例如，给定如下二叉搜索树:  root = [6,2,8,0,4,7,9,null,null,3,5]
*			6
*		   / \
*		  2   8
* 		 /\   /\
*		0  4 7  9
*		  / \
*	     3   5
* 示例 1:
*
* 输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
* 输出: 6
* 解释: 节点 2 和节点 8 的最近公共祖先是 6。
* 示例 2:
*
* 输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
* 输出: 2
* 解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。
*
*
* 说明:
*
* 所有节点的值都是唯一的。
* p、q 为不同节点且均存在于给定的二叉搜索树中。
*
* 来源：力扣（LeetCode）
* 链接：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree
* 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*
* ------------------------------------------------------------
* 题解： 遍历，dfs
* 最开始我用 dfs 后序遍历递归遍历, 遍历回 root 节点时候判下自己的左右子树是否有匹配的节点（如果子树中某个节点匹配，
* 层层往上返回 true 就行），如果两个子树都返回 true，或者某一个返回 true 且 root 自身是匹配的，那么输出当前 root 即可。
*
* 但上面的方法有个缺点，不能简直，dfs一旦开始就要遍历完，不能在某个匹配点结束算法。
* 官方题解很巧妙，因为是二叉搜索树，是有顺序的，如果 p,q 都比当前小，那么看左子树就行，如果都大于，那么看右子树，
* 反复迭代遍历，碰到不满足上面判断的节点，直接 return 这个节点即可。
*
* 此方法有效的剪枝，而且很有效的往自己想要的方向遍历，有点贪心的思想
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

func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
	var ans *TreeNode
	var dfs func(node *TreeNode) bool
	dfs = func(node *TreeNode) bool {
		if node == nil {
			return false
		}
		left := dfs(node.Left)
		right := dfs(node.Right)
		if left && right {
			if ans == nil {
				ans = node
			}
			return true
		} else {
			flag := false
			if node.Val == p.Val || node.Val == q.Val {
				flag = true
			}
			if left || right {
				if flag {
					ans = node
				}
				flag = true
			}
			return flag
		}
	}
	dfs(root)
	return ans
}

func lowestCommonAncestor2(root, p, q *TreeNode) *TreeNode {
	node := root
	for {
		if p.Val < node.Val && q.Val < node.Val {
			node = node.Left
		} else if p.Val > node.Val && q.Val > node.Val {
			node = node.Right
		} else {
			return node
		}
	}
}