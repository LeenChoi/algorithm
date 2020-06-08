# 硬币组合
'''
硬币。给定数量不限的硬币，币值为25分、10分、5分和1分，编写代码计算n分有几种表示法。(结果可能会很大，你需要将结果模上1000000007)

输入: n = 5
输出：2
解释: 有两种方式可以凑成总金额:
    5=5
    5=1+1+1+1+1

输入: n = 10
输出：4
解释: 有四种方式可以凑成总金额:
    10=10
    10=5+5
    10=5+1+1+1+1+1
    10=1+1+1+1+1+1+1+1+1+1

-----------------------------------------
题解：[25,10,5,1] 如果以 f(i, v) 表示前 i 种硬币构成总金额 v 的组合数，那么
    f(i, v) = f(i - 1, v) + f(i - 1, v - Ci) + ... + f(i - 1, v - k*Ci)  // Ci表示第 i 种面值硬币，k 应 <= floor(v / Ci)
    比如：i = 4 时，构成 80分的组合应为
        1. f(i - 1, v)
        2. 25 + f(i - 1, v - 25)
        3. 25 + 25 + f(i - 1, v - 25 - 25)
        4. 25 + 25 + 25 + f(i - 1, v - 25 - 25 - 25)
    这四种情况。

    考虑下，和 Ci = 25 有关的情况有后三种，如果把后三种情况的第一个25 (每个情况都有，共同性质) 提出去
        2. -25 | f(i - 1, (v - 25))
        3. -25 | 25 + f(i - 1, (v - 25) - 25)
        4. -25 | 25 + 25 + f(i - 1, (v - 25) - 25 - 25)
    
    整理后的式子根据上面的定义，是否等于 f(i, v - 25) 呢？ 即，f(i, v - Ci)
    所以最初的状态转移方程可以改写为：
        f(i, v) = f(i - 1, v) + f(i, v - Ci)

'''

class Solution:
    def waysToChange(self, n: int) -> int:
        if n == 0:
            return 0
        coin = [1, 5, 10, 25]


        loop = None
        for k in range(0, 4):
            if n <= coin[k]:
                loop = k
                break
        if loop == None:
            loop = 3
        elif loop == 0:
            return 1

        mod = 10 ** 9 + 7
        f = [1] * (n + 1)
        for i in range(1, loop + 1):
            for j in range(coin[i], n + 1):
                f[j] += f[j - coin[i]]
        
        return f[n] % mod

solution = Solution()
res = solution.waysToChange(10)
print(res)
