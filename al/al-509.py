# 斐波那契数列
# easy

class Solution:
    def fib(self, N: int) -> int:
        if N <= 2:
            return 1

        seed = (1, 1, 0, 0)
        unit = (1, 1, 1, 0)

        for i in range(0, N - 2):
            seed = matrixCalc(seed, unit)
        return seed[0]

class SolutionV2:
    def fib(self, N: int) -> int:
        if N <= 2:
            return 1
        
        bit, n, ans = 1, N - 2, None
        base = (1, 1, 1, 0)
        while bit <= n:
            if n & bit == bit:
                if ans == None:
                    ans = base
                else:
                    ans = matrixCalc(ans, base)
            
            base = matrixCalc(base, base)
            bit = bit << 1
        
        return ans[0] + ans[2]



def matrixCalc(ori, des):
    return (
        ori[0] * des[0] + ori[1] * des[2],
        ori[0] * des[1] + ori[1] * des[3],
        ori[2] * des[0] + ori[3] * des[2],
        ori[2] * des[1] + ori[3] * des[3]
    )

print(SolutionV2().fib(10))

