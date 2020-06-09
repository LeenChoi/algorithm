# 把数字翻译成字符串
# medium
'''
给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

 

示例 1:

输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"

---------------------------------------------
题解：动态规划
    设 dp[i] 为数字从前数第 i 位时的最大翻译种数
    初始dp队列 0项，1项为 1，因为 0个数、1个数的输出种类只有一种
    当遍历到第 i 位时，判断和 i-1 为可否组成有效两位数

    如果可以，那么 dp[i + 1] = dp[i - 1] + dp[i]
    否则 dp[i + 1] = dp[i]

    解释：
    12258 当读取到 1225 时首先看当前为 5，和 5 能结合的前面 122 有 3 种 (1 2 2 | 5)(12 2 | 5)(1 22 | 5)
    再看 25，前面的 12 有 2种 (1 2 | 25)(12 | 25)，所以当前 1225 能组成的种类数即是将这两类统计的结果之和

'''


class Solution:
    def translateNum(self, num: int) -> int:
        numStr = str(num)
        ans = [1, 1]
        for i in range(1, len(numStr)):
            n = int(numStr[i - 1 : i + 1])
            if n >= 10 and n <= 25:
                ans.append(int(ans[i - 1]) + int(ans[i]))
            else:
                ans.append(int(ans[i]))
        return ans[len(numStr)]


print(Solution().translateNum(12258))
print(Solution().translateNum(25))
