# 另一个树的子树
'''
给定两个非空二叉树 s 和 t，检验 s 中是否包含和 t 具有相同结构和节点值的子树。s 的一个子树包括 s 的一个节点和这个节点的所有子孙。s 也可以看做它自身的一棵子树。

给定的树 s:
     3
    / \
   4   5
  / \
 1   2
给定的树 t：
   4 
  / \
 1   2
返回 true，因为 t 与 s 的一个子树拥有相同的结构和节点值。

给定的树 s：
     3
    / \
   4   5
  / \
 1   2
    /
   0
给定的树 t：
   4
  / \
 1   2
返回 false。

-------------------------------
题解：
1.暴力dfs
2.dfs序列串匹配
    如上面的第一个例子，s 前序遍历出来是 [3,4,1,2,5], t 是 [4,1,2], s 包含 t 数组，所以是子树。
    但第二个例子，s [3,4,1,2,0,5], t [4,1,2], 同样 s 包含 t，但却不是子树。遍历出来的的序列无法得知边界，那么就加个边界。
    将第二例的 s 树，叶子节点加上 null 子节点
            3
           / \
          4   5
         / \  | \
        1   2 n  n
       / \  |\
      n  n  0 n
           / \
          n   n      
    那么 s 序列化后就是 [3,4,1,n,n,2,0,n,n,n,5,n,n], 同样的 t 序列化后是 [4,1,n,n,2,n,n], 这回 s 就不包含 t 了。所以不是子树
    两个序列已经得出，接下来就是要判断是否是子串

    朴素暴力方法:
    双指针 i, j 。s 从i开始遍历j，如果s、t 第j位相同，继续j++，否则 j=0，i++

    kmp:
    kmp算法是优化上述暴力法的 j=0 这个步骤，比如 t 为 [1,2,3,6,5,1,2,3,4]
    假设 s 和 t 按位比较，j 走到 t 的最后 4 的元素，发现在这一位不相同，如果暴力法这时要 j=0，
    但是仔细看数组，最后 4 前面的 [1,2,3] 和数组头的 [1,2,3] 序列相同，其实 j 不需要跳回 0 的位置，跳到 6 的位置即可，
    因为 [1,2,3] 已经匹配过了，kmp算法就是解决这个事。

    算法的思路就是遍历 t ，生成一个 next 数组，next 记录 t 中该位置之前的子串中，最长相同头尾串的头串末尾指针。
    比如，上例 t [1,2,3,6,5,1,2,3,4]
                    i         j
    看 i，j 这个位置，相同，那么next数组需要在 next[j+1] 记录 i+1，
    这样通过这个next数组，在做j=0这个操作的时候直接读取 next[j+1] 跳到 i+1 那个位置
    比如模式串是 [1,2,3,6,5,1,2,3,8,9,0,4] 和匹配串 t 的最后一个位置发生冲突，这时取 next[k] 跳到对应 t 串对应的位置，继续比较即可
                                k

    上面是 i, j 所指元素相同的情况，如果不相同，如下面所标 i，j 的位置，当前 j 位置 [1,2,8,1,2] 是最长相同头尾串，
    i、j 元素不相同，那么 next[j+1] 要存什么，总不能存 -1 又回到最初位置吧。
    [1,2,8,1,2,5,6,1,2,8,1,2,8,3]
         k     i             j
    但是可以看到 j+1 这个位置之前有个相同头尾串 [1,2,8]，但怎么用代码去找呢？
    想想 next 数组的 i 这个位置存的是什么，是 k。那么比较下 k 和 j 的元素是否相同，如果相同那么 next[j+1] = k 是否就可以了
    如果不相同那就继续找 next[k] 所指位置的元素，和 j 的元素再比较，持续迭代，直至 next[x] 为 -1 没有相同头尾穿，再向后比较

    以上就是构建 next 数组的过程

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preOrder(self, node, array):
        array.append(node.val)
        if node.left == None:
            array.append(None)
        else:
            self.preOrder(node.left, array)

        if node.right == None:
            array.append(None)
        else:
            self.preOrder(node.right, array)
        
    def getNext(self, a):
        next = [-1] * len(a)
        i, j = -1, 0
        while j < len(a) - 1:
            if i == -1 or a[i] == a[j]:
                i += 1
                j += 1
                next[j] = i
            else:
                i = next[i]
        return next

    def kmp(self, sa, ta, next):
        si, ti = 0, 0
        while si < len(sa):
            if ti == -1 or sa[si] == ta[ti]:
                si += 1
                ti += 1
            else:
                ti = next[ti]
            if ti >= len(ta):
                return True
            if len(ta) - ti > len(sa) - si:
                break
        return False

    def isSubtree(self, s, t) -> bool:
        sa, ta = [], []
        self.preOrder(s, sa)
        self.preOrder(t, ta)
     
        print(sa)
        print(ta)
        next = self.getNext(ta)
        return self.kmp(sa, ta, next)





solution = Solution()
res = solution.isSubtree([3,4,5,1,2], [4,1,2])
print(res)