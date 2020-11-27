# 四数相加 II
# medium
'''
给定四个包含整数的数组列表 A , B , C , D ,计算有多少个元组 (i, j, k, l) ，使得 A[i] + B[j] + C[k] + D[l] = 0。

为了使问题简单化，所有的 A, B, C, D 具有相同的长度 N，且 0 ≤ N ≤ 500 。所有整数的范围在 -228 到 228 - 1 之间，最终结果不会超过 231 - 1 。

例如:

输入:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

输出:
2

解释:
两个元组如下:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/4sum-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

-----------------------------------------------------------
题解：哈希表
A,B 数组组一队，计算每一个A[i]+B[j]的值，放到哈希表中，哈希表键为俩数的和，值为出现的次数
再 C,D 数组组一队，计算每个C[i]+D[j]的值，看和的相反值(因为总和为0)是否在哈希表的键值里有记录，有的话累加这个键的值

'''


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        hash = {}
        ans = 0
        for i in range(len(A)):
            for j in range(len(B)):
                sum = A[i] + B[j]
                if hash.get(sum) == None:
                    hash[sum] = 1
                else:
                    hash[sum] += 1
        for i in range(len(C)):
            for j in range(len(D)):
                sum = C[i] + D[j]
                if hash.get(-sum) != None:
                    ans += hash[-sum]
        return ans
