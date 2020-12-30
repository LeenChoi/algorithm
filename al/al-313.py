# 超级丑数
# medium
'''
编写一段程序来查找第 n 个超级丑数。

超级丑数是指其所有质因数都是长度为 k 的质数列表 primes 中的正整数。

示例:

输入: n = 12, primes = [2,7,13,19]
输出: 32 
解释: 给定长度为 4 的质数列表 primes = [2,7,13,19]，前 12 个超级丑数序列为：[1,2,4,7,8,13,14,16,19,26,28,32] 。
说明:

1 是任何给定 primes 的超级丑数。
 给定 primes 中的数字以升序排列。
0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000 。
第 n 个超级丑数确保在 32 位有符整数范围内。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/super-ugly-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

---------------------------------------------------
题解：堆
和 al-264 解法一样，但是完全按 264 的写法 n = 100000 的用例会超时，最后猜测可能入堆的时候判断 not in 导致超时，
所以就不判重了，直接入堆，即使相同的数在堆中，再连续取栈顶的时候取到的都会是相同的，所以在取出与上一个相同数的时候
直接跳过就可以了。

'''

from heapq import heappush, heappop

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        heap, ans = [], []
        heappush(heap, 1)
        while len(ans) < n:
            cur = heappop(heap)
            if len(ans) != 0 and cur == ans[-1]:
                continue
            ans.append(cur)
            for i in primes:
                next = cur * i
                heappush(heap, next)
        return ans[n-1]