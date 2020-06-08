# Pow(x, n)
'''
输入: 2.00000, 10
输出: 1024.00000

输入: 2.10000, 3
输出: 9.26100

输入: 2.00000, -2
输出: 0.25000
解释: 2-2 = 1/22 = 1/4 = 0.25

说明:
-100.0 < x < 100.0
n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。

-------------------------------------------
题解：
    1.快速幂，递归(二分法)
    2.快速幂，迭代
    x^77: x^1 -> x^2 -> x^4 -> +x^9 -> +x^19 -> x^38 -> +x^77 （+号代表在此次迭代多乘了一个x）
    每一次迭代是一次翻倍，+x^9 的时候多乘了一个 x，这个 x 再之后参与了三轮迭代，贡献了 x^8
    同样 +x^19 里贡献了 x^4, 最后的 +x^77 贡献了 x^1，
    除去这些贡献，剩下的就是最初的 x 一直迭代，贡献 x^64

    所以，最后的式子可以为:
    x^77 = x * x^4 * x^8 * x^64
    指数 1，4，8，64 恰巧与 77的二进制 (1001101) 的1位相等

'''

# 归并法（错误的，实际是O-n）
class Solution:
    def subPow(self, x, n):
        if n <= 2:
            return x if n == 1 else x * x

        ln = n // 2
        lpow = self.subPow(x, ln)
        rpow = self.subPow(x, n - ln)
        print(ln)
        return lpow * rpow

    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n > 0:
            return self.subPow(x, n)
        return 1 / self.subPow(x, abs(n))


# 真正的分治法，二分法，递归
class SolutionV2:
    def subPow(self, x, n):
        if n <= 3:
            ans = x
            for i in range(1, n):
                ans *= x
            return ans
            
        m = n // 2
        res = self.subPow(x, m)
        ans = res * res
        if n % 2 == 1:
            ans = ans * x
        return ans
        

    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n > 0:
            return self.subPow(x, n)
        return 1 / self.subPow(x, abs(n))

# 迭代 
class SolutionV3:
    def subPow(self, x, n):
        ans = 1
        cursor = 1
        while cursor <= n:
            if n & cursor == cursor:
                ans *= x
            cursor = cursor << 1
            x *= x
        return ans

    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n > 0:
            return self.subPow(x, n)
        return 1 / self.subPow(x, abs(n))
        


    
solution = SolutionV3()
res = solution.myPow(2, 4)
print(res)