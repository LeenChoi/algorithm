# 汉明距离
# easy
'''
两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。

给出两个整数 x 和 y，计算它们之间的汉明距离。

注意：
0 ≤ x, y < 231.

示例:

输入: x = 1, y = 4

输出: 2

解释:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

上面的箭头指出了对应二进制位不同的位置。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/hamming-distance
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

------------------------------------------------------------
题解：Brian Kernighan 算法
x & (x - 1)，首先两个数做 xor 操作，得出来的数二进制有多少个 1 就表示俩数的汉明距离
之后重复做上述算法运算，得出有多少个 1 即可


'''


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        ans = 0
        while xor > 0:
            xor = xor & (xor - 1)
            ans += 1
        return ans