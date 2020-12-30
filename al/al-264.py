# 丑数 II
# medium
'''
编写一个程序，找出第 n 个丑数。

丑数就是质因数只包含 2, 3, 5 的正整数。

示例:

输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
说明:  

1 是丑数。
n 不超过1690。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ugly-number-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

--------------------------------------
题解：堆
从 1 开始乘以 2，3，5 将结果塞入堆，然后输出栈顶再乘以 2，3，5 继续塞入堆中，直到输出第 n 个栈顶，即是答案


'''

from heapq import heappush, heappop

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = []
        ans = []
        heappush(heap, 1)
        while len(ans) < n:
            cur = heappop(heap)
            ans.append(cur)
            for i in [2,3,5]:
                next = cur * i
                if next not in heap:
                    heappush(heap, next)
        return ans[n-1]
    
        
