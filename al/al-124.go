// 二叉树中的最大路径和
// hard
/*
* 给定一个非空二叉树，返回其最大路径和。
*
* 本题中，路径被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。
*
* 示例 1：
*
* 输入：[1,2,3]
*
*        1
*       / \
*      2   3
*
* 输出：6
*
* 示例 2：
*
* 输入：[-10,9,20,null,null,15,7]
*
*    -10
*    / \
*   9  20
*     /  \
*    15   7
*
* 输出：42
*
* 来源：力扣（LeetCode）
* 链接：https://leetcode-cn.com/problems/binary-tree-maximum-path-sum
* 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*
* ---------------------------------------------------
* 题解：
* 题意真是垃圾的一比，其实是要求从某个节点开始往下左右孩子的贡献值之和，但求孩子的贡献的时候只能是从此孩子开始往下的
* 单条遍历通道(题里指的路径)，而不是孩子的左右孩子子树的和，但求当前节点的最大路径和却要求左右孩子的路径之和
* dfs 记录每个节点的当前贡献值和当前最大和即可
*
 */

package main

import "math"

func main() {

}

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func maxPathSum(root *TreeNode) int {
	ans := math.MinInt32
	var dfs func(node *TreeNode) int
	dfs = func(node *TreeNode) int {
		if node == nil {
			return 0
		}
		var left, right, gain, _max int
		left = max(dfs(node.Left), 0)
		right = max(dfs(node.Right), 0)
		_max += node.Val + left + right
		if _max > ans {
			ans = _max
		}
		gain = node.Val + max(left, right)
		return gain
	}
	dfs(root)
	return ans
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
