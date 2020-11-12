# 按奇偶排序数组 II
# easy
'''
给定一个非负整数数组 A， A 中一半整数是奇数，一半整数是偶数。

对数组进行排序，以便当 A[i] 为奇数时，i 也是奇数；当 A[i] 为偶数时， i 也是偶数。

你可以返回任何满足上述条件的数组作为答案。

 

示例：

输入：[4,2,5,7]
输出：[4,5,2,7]
解释：[4,7,2,5]，[2,5,4,7]，[2,7,4,5] 也会被接受。
 

提示：

2 <= A.length <= 20000
A.length % 2 == 0
0 <= A[i] <= 1000


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-array-by-parity-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

--------------------------------------------------
题解：两次遍历，双指针
两次遍历，一次吧偶数放进 ans[0], ans[2], ans[4]... 再一次把奇数补缝
我是直接一次遍历把奇偶数放进俩队列，最后俩队列交替合并

双指针，i,j 指针分别找到偶数位为奇数的和奇数位为偶数的，直接交换

'''


class Solution:
    def sortArrayByParityII(self, A):
        even, odd = [], []
        for a in A:
            if a / 2 == a // 2:
                even.append(a)
            else:
                odd.append(a)

        ans = []
        for i in range(len(even)):
            ans.append(even[i])
            ans.append(odd[i])
        return ans


class Solution2:
    def sortArrayByParityII(self, A):
        i, j = 0, 1
        while i < len(A):
            if A[i] / 2 != A[i] // 2:
                while j < len(A):
                    if A[j] / 2 == A[j] // 2:
                        A[i], A[j] = A[j], A[i]
                        break
                    j += 2
            i += 2
        return A
                    


print(Solution2().sortArrayByParityII([4,2,5,7]))