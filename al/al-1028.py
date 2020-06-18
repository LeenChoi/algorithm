# 从先序遍历还原二叉树
# hard
'''
我们从二叉树的根节点 root 开始进行深度优先搜索。
在遍历中的每个节点处，我们输出 D 条短划线（其中 D 是该节点的深度），然后输出该节点的值。（如果节点的深度为 D，则其直接子节点的深度为 D + 1。根节点的深度为 0）。
如果节点只有一个子节点，那么保证该子节点为左子节点。
给出遍历输出 S，还原树并返回其根节点 root。

示例1：
        1
       / \
     2    5
    / \  / \
   3  4  6  7
输入：”1-2--3--4-5--6--7”
输出：[1,2,5,3,4,6,7]

示例2：
        1
       / \
      2   5
     /   /
    3   6
   /   /
  4   7

输入：“1-2--3---4-5--6---7”
输出：[1,2,5,3,null,6,null,4,null,7]

示例3：
        1
       /
     401
     / \
   349  88
   /
  90
输入：“1-401--349---90--88”
输出：[1,401,null,349,88,90]

提示：
原始树中的节点数介于 1 和 1000 之间。
每个节点的值介于 1 和 10 ^ 9 之间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/recover-a-tree-from-preorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

------------------------------------------
题解：类似dfs迭代写法的思路
    用一个栈存放遍历到的元素
    记录下每个数字之前的"-"，计算他的deep，如果deep比上一个大说明是他的孩子，因为是先序，所以是左孩子，进栈
    如果当前deep小于上一个，表明是其他分支的了，将前面的元素一一出栈，直到某个元素的deep比当前小，表明是父节点
    此时当前元素为父节点的右孩子

    solution1 用的是递归dfs的思想，绕的一逼，时间还慢。
    后来用迭代思想改写 solution2，快很多，代码也简洁

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        i, number = 0, ''
        for i in range(len(S)):
            if S[i] == '-':
                break
            number += S[i]   
        root = TreeNode(int(number))
        order(S, root, 0, i - 1)
        return serialize(root)

def order(S, parent, level, index):
    deep = 0
    nindex = index + 1
    number = ''
    while nindex < len(S):
        if S[nindex] == '-':
            deep += 1
        else:
            if deep <= level:
                break
            elif deep == level + 1:
                number += S[nindex]
                if nindex + 1 == len(S) or S[nindex + 1] == '-':
                    child = TreeNode(int(number))
                    parent.left = child
                    order(S, child, deep, nindex)
                    break
            elif nindex + 1 == len(S) or S[nindex + 1] == '-':
                deep = 0
        nindex += 1
    
    deep = 0
    nindex = index + 1
    number = ''
    second = 0
    while nindex < len(S):
        if S[nindex] == '-':
            deep += 1
        else:
            if deep <= level:
                break
            elif deep == level + 1:
                number += S[nindex]
                if nindex + 1 == len(S) or S[nindex + 1] == '-':
                    if not second:
                        second = 1
                        number = ''
                        deep = 0
                    else:
                        child = TreeNode(int(number))
                        parent.right = child
                        order(S, child, deep, nindex)
                        break
            elif nindex + 1 == len(S) or S[nindex + 1] == '-':
                deep = 0
        nindex += 1


class SolutionV2:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        stack = []
        number = ''
        level, deep = 0, 0
        root = None
        for i in range(len(S)):
            if S[i] == '-':
                deep += 1
            else:
                number += S[i]
                if i + 1 == len(S) or S[i + 1] == '-':
                    node = TreeNode(int(number))
                    if not root:
                        root = node
                        stack.append(node)
                        level = deep
                    else:
                        if deep > level:
                            stack[-1].left = node
                            stack.append(node)
                            level = deep
                        else:
                            while level >= deep:
                                stack.pop()
                                level -= 1
                            stack[-1].right = node
                            stack.append(node)
                            level = deep
                    deep = 0
                    number = ''
        return serialize(root)        



def serialize(root):
    seq, arr = [root], []
    while len(seq) > 0:
        node = seq.pop(0)
        if node:
            arr.append(node.val)
            if node.left != None:
                seq.append(node.left)
            else:
                seq.append(None)
            if node.right != None:
                seq.append(node.right)
            else:
                seq.append(None)
        else:
            arr.append(None)
    while len(arr) > 0 and arr[-1] == None:
        arr.pop()
    return arr

print(SolutionV2().recoverFromPreorder('1-2--3--4-5--6--7'))
print(SolutionV2().recoverFromPreorder('1-401--349---90--88'))
print(SolutionV2().recoverFromPreorder('10-7--8'))
print(SolutionV2().recoverFromPreorder('7-6-2--5'))