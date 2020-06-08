# 求1+2+…+n
# medium
'''
求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

示例 1：
输入: n = 3
输出: 6

示例 2：
输入: n = 9
输出: 45
 
限制：

1 <= n <= 10000

-------------------------------
题解：
    1.递归（秀我一脸）
    2.快速乘
    等差数列求和公式 n(n+1) / 2, 硬要说这题考察什么的话就是考察乘法的实现，先 n 和 n+1 相乘，最后结果 >>1
    和快速幂差不多的思路，A 乘 B，实际上是 A 加了 B次，B 转成二进制，从0位遍历碰到 1，就加 1 << n 个 A

    有了快速乘算法（下面的实现）就可以算出和了，但是快速乘里用到了while、if等，题目要求不允许用怎么办，
    官方题解操蛋的骚方法，把循环展开，因为 n <= 10000， 所以 n 最多也不超过 13位，所以执行 13 遍位操作(想砸键盘)
    
'''


class Solution:
    def sumNums(self, n: int) -> int:
        if n == 0:
            return 0
        else:
            return n + self.sumNums(n - 1)

class Multi:
    def multiple(self, a, b):
        ans, bit = 0, 1
        while bit < b:
            if bit & b > 0:
                ans += a
            a += a
            bit = bit << 1
        return ans


print(Multi().multiple(100,100))