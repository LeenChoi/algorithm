# 数字范围按位与
# medium
'''
给定范围 [m, n]，其中 0 <= m <= n <= 2147483647，返回此范围内所有数字的按位与（包含 m, n 两端点）。

示例 1: 

输入: [5,7]
输出: 4
示例 2:

输入: [0,1]
输出: 0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/bitwise-and-of-numbers-range
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

----------------------------------------------
题解：
位右移，m、n 二进制开头几位如果一致那么[m, n]的所有按位与操作的结果就是开头那几个，所以将m、n右移，直到m、n相等
结果就是[m, n]的公共前缀

Brian Kernighan 算法
n & (n - 1)，反复这个操作是将数字二进制的最右一个 1 抹除，判断一个数二进制有多少个 1 就是用的这个方法
同样这道题也可以用此方法，其实目的和上面的方法一致，就是将右面不公共的 1 移除掉
反复此操作，直到 n < m 即可

'''


class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        ans = 0
        while True:
            ele = checkBit(m, n)
            if ele == 0:
                break
            else:
                ans += ele
                m = m - ele
                n = n - ele
        return ans

def checkBit(m, n):
    for i in range(1, 31):
        if m < 2 ** i:
            if n < 2 ** i:
                if i == 1:
                    return 0
                else:
                    return 2 ** (i - 1)
            else:
                return 0


class Solution2:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        shift = 0
        while m != n:
            m = m >> 1
            n = n >> 1
            shift += 1
        if m > 0:
            m = m << shift
        return m


class Solution3:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        while m < n:
            n = n & (n - 1)
        return n


print(Solution3().rangeBitwiseAnd(5, 7))