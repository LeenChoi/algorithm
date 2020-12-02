# 拼接最大数
# hard
'''
给定长度分别为 m 和 n 的两个数组，其元素由 0-9 构成，表示两个自然数各位上的数字。现在从这两个数组中选出 k (k <= m + n) 个数字拼接成一个新的数，要求从同一个数组中取出的数字保持其在原数组中的相对顺序。

求满足该条件的最大数。结果返回一个表示该最大数的长度为 k 的数组。

说明: 请尽可能地优化你算法的时间和空间复杂度。

示例 1:

输入:
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
输出:
[9, 8, 6, 5, 3]
示例 2:

输入:
nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
输出:
[6, 7, 6, 0, 4]
示例 3:

输入:
nums1 = [3, 9]
nums2 = [8, 9]
k = 3
输出:
[9, 8, 9]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/create-maximum-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

-----------------------------------------
题解：贪心，单调栈
这题重点在找出两数组各自的最大子序列，然后俩最大子序列合并成尽可能大的数组，然后再在众多合并的数组中找出最大。
具体做法是，从一个数组中找出长度为 i 的最大子序列，另一个数组中找出长度为 k-i 的最大子序列，然后合并成大小为 k 的数组，
众多 k 数组中，最大的即是答案。

细节：这题有很多细节。
首先就是找指定长度的最大子序列的算法，算法很巧妙，用了单调栈，数组去实现。顺序遍历数组将数字入栈，如果下一个数字比栈顶大，
那么出栈，新的数字重新入栈，同时需要记一个remain字段，用来记录还可以出栈几个数字。比如长度 5 的数组中找长度 3 的最大子序列，
因为要保证结果的长度为 3，所以只能出栈 2 个数。2 次出栈用完，剩下的数字就只能怪怪入栈。
官方题解这个算法没有做出栈操作，用了一个top指针去记录该把哪个位置的数替换，替换后，后续的数顺序的从这位置往后一一替换原来的脏数，
其实就是入栈出栈的操作，理解了半天。

然后一个细节就是，俩子序列合并的时候，一开始我的做法是，俩子序列从头遍历，比较俩元素，谁大谁进队列。
但是有个特殊情况，比如 [6,7], [6,0,4] 俩数组合并，应该是 [6,7,6,0,4]。但是按我的做法谁大谁先进，小于等于的等候，
最终结果就成 [6,6,7,0,4]，原因就是第一个数组的 6 小于等于第二个数组的 6，所以第一个 6 等候，第二个 6 先进了，
然后第一个 6 和第二个 0 比较，6 再进，所以导致结果不正确。单纯的把大于判断改成大于等于不解决问题。
官方题解是做了个比较函数，传入俩数组和当前要比较的索引位，然后判断当前位的俩数字谁大，谁大谁进。如果相等，那么向后继续比较，
直到一个位比较能分出大小为止。如果某一个数组都遍历完了还没有分出大小，那么就返回没遍历完的那个。这样就解决问题了。

'''


class Solution:
    def maxNumber(self, nums1, nums2, k):
        maxSubsequence = []
        # for i in range(k + 1):
        #     if i > len(nums1) or k - i > len(nums2):
        #         continue
        #     seq1 = self.getMaxSubsequence(nums1, i)
        #     seq2 = self.getMaxSubsequence(nums2, k - i)
        #     curMaxSequence = self.mergeSubsequences(seq1, seq2)
        #     if self.compareSubsequences(curMaxSequence, maxSubsequence):
        #         maxSubsequence = curMaxSequence
        m, n = len(nums1), len(nums2)
        start, end = max(0, k - m), min(n, k)
        for i in range(start, end + 1):
            seq1 = self.getMaxSubsequence(nums1, k - i)
            seq2 = self.getMaxSubsequence(nums2, i)
            curMaxSequence = self.mergeSubsequences(seq1, seq2)
            if self.compareSubsequences(curMaxSequence, maxSubsequence):
                maxSubsequence = curMaxSequence
        return maxSubsequence 

    # 单调栈
    def getMaxSubsequence(self, nums, k):
        stack = [0] * k
        top = -1
        remain = len(nums) - k
        for num in nums:
            while top >= 0 and num > stack[top] and remain > 0:
                top -= 1
                remain -= 1
            if top < k - 1:
                top += 1
                stack[top] = num
            else:
                remain -= 1
        return stack

    def mergeSubsequences(self, seq1, seq2):
        seq = []
        i, j = 0, 0
        while i < len(seq1) and j < len(seq2):
            if self.compareBiggerSequence(seq1, i, seq2, j):
                seq.append(seq1[i])
                i += 1
            else:
                seq.append(seq2[j])
                j += 1
        while i < len(seq1):
            seq.append(seq1[i])
            i += 1
        while j < len(seq2):
            seq.append(seq2[j])
            j += 1
        return seq

    def compareSubsequences(self, seq1, seq2):
        m, n = len(seq1), len(seq2)
        if m != n:
            return m > n
        else:
            for i in range(m):
                if seq1[i] != seq2[i]:
                    return seq1[i] > seq2[i]
        return False

    def compareBiggerSequence(self, seq1, index1, seq2, index2):
        m, n = len(seq1), len(seq2)
        while index1 < m and index2 < n:
            if seq1[index1] > seq2[index2]:
                return True
            elif seq1[index1] < seq2[index2]:
                return False
            else:
                index1 += 1
                index2 += 1
        return index1 < m

# print(Solution().maxNumber([3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5))
# print(Solution().maxNumber([6,7], [6,0,4], 5))
print(Solution().maxNumber([2,5,6,4,4,0], [7,3,8,0,6,5,7,6,2], 15))