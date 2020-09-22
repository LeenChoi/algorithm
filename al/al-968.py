# 监控二叉树
# hard
'''
给定一个二叉树，我们在树的节点上安装摄像头。

节点上的每个摄影头都可以监视其父对象、自身及其直接子对象。

计算监控树的所有节点所需的最小摄像头数量。

示例 1：

     0
    /
   回
  /  \
 0    0 

输入：[0,0,null,0,0]
输出：1
解释：如图所示，一台摄像头足以监控所有节点。

示例 2：

        0
       /
      回 
     /
    0
   /
  回
   \
    0

输入：[0,0,null,0,null,0,null,null,0]
输出：2
解释：需要至少两个摄像头来监视树的所有节点。 上图显示了摄像头放置的有效位置之一。

提示：

给定树的节点数的范围是 [1, 1000]。
每个节点的值都是 0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-cameras
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

-------------------------------------------
题解：dp + dfs
dp 三个状态：
    a：root放摄像头的情况下，覆盖整个树的最少摄像头数
    b：不论root放不放摄像头，覆盖整个树的最少摄像头数
    c：左右子树覆盖时的最少摄像头数，不论root放不放摄像头

a 的状态转移，因为 a 包括 root 的摄像头，能监视到 root 的左右孩子 l、r，所以只获取 l、r 各自的 c 就可以了，
最后再加上 root 的摄像头 +1，所以 a = lc + rc + 1

b 的状态转移，首先 b 的情况包括 a 情况，即 root 放摄像头的情况，不放摄像头的情况那么得借助俩孩子 l、r 上的某一个摄像头，
l、r 上只要有一个摄像头即可，所以要找 la + rb, lb + ra 中的较小值，最后再和 a 比较，取小值，
所以 b = min(a, min(la + rb, lb + ra))

c 的状态转移，因为只看左右孩子 l、r 的覆盖情况，不用考虑 root 有没有被监视覆盖，所以取 lb + rb 即可，
但 a 和 b 的情况也包含了 c，所以还有和 a、b 做比较取小值，但上面的 b 状态转移里已经和 a 比较过了，所以和 b 比较就可以了，
所以 c = min(b, lb + rb)

注意：对于某个节点，如果他的某个孩子节点为空，那么从此空节点返回的 a、b、c 中 a 需要返回一个大值，
因为不可能通过给一个空孩子节点放置摄像头来监视当前节点

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return (float('inf'), 0, 0)
            la, lb, lc = dfs(node.left)
            ra, rb, rc = dfs(node.right)
            a = lc + rc + 1
            b = min(a, min(la + rb, lb + ra))
            c = min(b, lb + rb)
            return (a, b, c)
        _, ans, _ = dfs(root)
        return ans
