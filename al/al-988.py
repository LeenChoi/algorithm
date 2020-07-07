# 从叶结点开始的最小字符串
# medium
'''
给定一颗根结点为 root 的二叉树，树中的每一个结点都有一个从 0 到 25 的值，分别代表字母 'a' 到 'z'：值 0 代表 'a'，值 1 代表 'b'，依此类推。

找出按字典序最小的字符串，该字符串从这棵树的一个叶结点开始，到根结点结束。

（小贴士：字符串中任何较短的前缀在字典序上都是较小的：例如，在字典序上 "ab" 比 "aba" 要小。叶结点是指没有子结点的结点。）

示例 1：
        a
       / \
      b   c
     / \  / \
    d  e  d  e
输入：[0,1,2,3,4,3,4]
输出："dba"

示例 2：
        z
       / \
      b   d
     / \  / \
    b  d  a  c
输入：[25,1,3,1,3,0,2]
输出："adz"

示例 3：
        c
       / \
      c   b
      \   /
       b a  
     /
    a
输入：[2,2,1,null,1,0,null,0]
输出："abc"
 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/smallest-string-starting-from-leaf
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''

import treeFunc

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        if root == None:
            return ''
        queue, ans = [[root, 0]], None
        while len(queue) > 0:
            item = queue[-1]
            node = item[0]
            if node.left and item[1] & 1 == 0 :
                item[1] |= 1
                queue.append([node.left, 0])
            elif node.right and item[1] & 2 == 0:
                item[1] |= 2
                queue.append([node.right, 0])
            else:
                if not node.left and not node.right:
                    ans = compare(ans, queue)
                queue.pop()
        return transform(ans)


def compare(ans, treeArr):
    queue = []
    for i in range(len(treeArr) - 1, -1, -1):
        queue.append(treeArr[i][0].val)
    if ans == None:
        return queue
    length = min(len(ans), len(queue))
    for i in range(length):
        if ans[i] < queue[i]:
            return ans
        if queue[i] < ans[i]:
            return queue
    return ans if len(ans) <= len(queue) else queue
    
def transform(ans):
    _str = ''
    for num in ans:
        _str += chr(97 + num)
    return _str


print(Solution().smallestFromLeaf(treeFunc.deserialize([2,2,1,None,1,0,None,0])))
print(Solution().smallestFromLeaf(treeFunc.deserialize([25,1,3,1,3,0,2])))