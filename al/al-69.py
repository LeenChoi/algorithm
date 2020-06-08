# x的平方根
'''
实现 int sqrt(int x) 函数。
计算并返回 x 的平方根，其中 x 是非负整数。
由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

输入: 4
输出: 2
示例 2:

输入: 8
输出: 2
说明: 8 的平方根是 2.82842..., 
     由于返回类型是整数，小数部分将被舍去。


'''
# 数学公式转换
# sqrt(x) =  x^(1/2) = e^(lnx)^(1/2) = e^(1/2*lnx)
import math

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        ans = int(math.exp(0.5 * math.log(x)))
        return ans + 1 if (ans + 1) ** 2 <= x else ans


# 二分法
class SolutionV2:
    def mySqrt(self, x: int) -> int:
        l, r, ans = 0, x, 0
        while l <= r:
            mid = (l + r) // 2
            if mid ** 2 <= x:
                l = mid + 1
                ans = mid
            else:
                r = mid - 1
            print(mid, l, r)
        return ans


# 牛顿迭代法 
'''
    y = x^2 - C, {x|y=0} 即是C的平方根
    我们可以知道二次函数上某一点的斜率，这一点的切线方程与y=0点相交的x点，与二次方程的y=0点越相近，那么此切线方程的{x|y=0}可以近似为解
    二次函数给一个初始点，然后通过这个点找切线方程一点点迭代逼近二次函数{x|y=0}点

    二次函数切线方程： 假设有 y = ax^2 + bx + c
    那么过二次函数的任一一点(xi, yi)的切线方程为： y - yi = k(x - xi), k为斜率，对二次函数这一点求导 f'(xi)
    所以最终切线方程为 y = f'(xi)(x - xi) + yi
    此方程的 {x|y=0} 点即是下一个逼近解的 x 点
    迭代到 x 和 xi 的差小于1e-7 几乎就可以看做是解了

    那么初始值 xi 给什么呢，可以直接给C值，为什么不给 -1 或 0 这种常规默认值，因为二次函数有两个0解
    要给个尽量大的初始值，不然很有可能会逼近另一个0值

'''

class SolutionV3:
    def mySqrt(self, x: int) -> int:
        c = x
        if c == 0:
            return 0

        xi = c
        while True:
            x0 = 0.5 * (xi + (c / xi))
            if (xi - x0) < 1e-7:
                return int(x0)
            xi = x0


solution = SolutionV3()
res = solution.mySqrt(1)
print(res)