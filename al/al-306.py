# 累加数
# medium
'''
累加数是一个字符串，组成它的数字可以形成累加序列。

一个有效的累加序列必须至少包含 3 个数。除了最开始的两个数以外，字符串中的其他数都等于它之前两个数相加的和。

给定一个只包含数字 '0'-'9' 的字符串，编写一个算法来判断给定输入是否是累加数。

说明: 累加序列里的数不会以 0 开头，所以不会出现 1, 2, 03 或者 1, 02, 3 的情况。

示例 1:

输入: "112358"
输出: true 
解释: 累加序列为: 1, 1, 2, 3, 5, 8 。1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
示例 2:

输入: "199100199"
输出: true 
解释: 累加序列为: 1, 99, 100, 199。1 + 99 = 100, 99 + 100 = 199
进阶:
你如何处理一个溢出的过大的整数输入?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/additive-number

-------------------------------------------
题解：回溯
同 al-842

'''


class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        arr = []
        def backstrack(index):
            if index == len(num):
                return len(arr) >= 3
            cur = 0
            print(arr)
            for i in range(index, len(num)):
                if i > index and num[index] == '0':
                    return False
                cur = cur * 10 + int(num[i])
                # if cur > 2 ** 31 - 1:
                #     return False
                if len(arr) < 2 or arr[-2] + arr[-1] == cur:
                    arr.append(cur)
                    if backstrack(i + 1):
                        return True
                    arr.pop()
                elif arr[-2] + arr[-1] < cur:
                    return False
            return False
        return backstrack(0)
            

# print(Solution().isAdditiveNumber('112358'))
print(Solution().isAdditiveNumber("121474836472147483648"))
