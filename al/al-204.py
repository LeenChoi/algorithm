# 计数质数
# easy
'''
统计所有小于非负整数 n 的质数的数量。

示例 1：

输入：n = 10
输出：4
解释：小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
示例 2：

输入：n = 0
输出：0
示例 3：

输入：n = 1
输出：0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-primes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

-------------------------------------------
题解：枚举，埃氏筛，线性筛
我是用的线性遍历+剪枝做的，算是枚举，即满足 6*x-1, 6*x+1 的数里判断是否是素数，判断素数的方法依然是用 6*x-1, 6*x+1 的数取余。
但是效率慢，没有通过。

官方题解的埃氏筛和线性筛属于空间换时间的做法。
埃氏筛：做一个长度n的bool队列，代表 1 到 n 是否为素数，默认true。然后开始遍历数字，如果在bool队列里该数字是标为素数，那么ans+1
并且将该数的所有倍数对应的bool队列的值标为false，以此类推。

线性筛：比起上面的bool队列，多了个prime队列，用来记录素数。做法同样遍历数字，判断下bool队列里是否标记为素数，将素数塞进素数队列，
然后不将该数的倍数位置成false了，而是将该数与素数队列里的素数相乘得出的数，将他们的bool队列的值设置为false，并且如果当前数 x 能被
素数队列里的当前访问的素数 prime[i] 整除，那么就不继续相乘了，直接跳过，开始下一个数。因为 x * prime[i+1] 一定会在遍历到 x/prime[i] * prim[i+1]
这个数的时候，在他的后续相乘操作中bool队列会被访问到。举例：当前 4 开始与素数相乘，与 2 乘得 8，将 8 标记为false，与此同时 8 会被素数 2 整除，
那么乘到 8 之后不再后续相乘了，后面的 4*3 = 12 不会被置为 false，因为当遍历到 4/2 * 3 = 6 这个数的时候，6 与 2 相乘会改变 12 的标记

'''

import math

class Solution:
    # 此方法超时
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        if n <= 3:
            return 1
        if n <= 5:
            return 2
        ans = 2
        i = 1
        while 6 * i - 1 < n:
            for num in [6 * i - 1, 6 * i + 1]:
                if num < n:
                    isPrime = True
                    j = 1
                    while 6 * j - 1 <= math.sqrt(num):
                        for div in [6 * j - 1, 6 * j + 1]:
                            if num % div == 0:
                                isPrime = False
                                break
                        j += 1
                    if num % 3 == 0 or num % 2 == 0:
                        isPrime = False
                    if isPrime:
                        ans += 1
            i += 1
        return ans

    def countPrimes2(self, n: int) -> int:
        primes = []
        isPrime = [True] * (n + 1)
        for i in range(2, n):
            if isPrime[i]:
                primes.append(i)
            for p in primes:
                if i * p >= n:
                    break
                isPrime[i * p] = False
                if i % p == 0:
                    break
        return len(primes)





print(Solution().countPrimes2(15000))