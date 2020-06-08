# 面试题56 - II. 数组中数字出现的次数 II
'''
在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。

输入：nums = [3,4,3,3]
输出：4

输入：nums = [9,1,7,9,7,9,7]
输出：1

-----------------------------
题解：尼玛？！ 数电，有限状态自动机
    三进制的思想
    5: 0 1 0 1
    9: 1 0 0 1
    7: 0 1 1 1
    ==========
       1 2 1 3

    每位数余3后得到的二进制就是那个要找的单数，但也无法按位遍历，太费，所以还是做位运算
    但一位只能表示两个状态，那就再加一位，用两位可以表达4个状态足够了

    0       1       2       3(进位)
    0 0     0 1     1 0     0 0

    定义 one，two 分别记录两个状态，对每一位n：
    1. 如果 two 等于1，那么 one 一定等于0，如果 n 等于1，那 [two,one] 等着进位，
        即，[1, 0] -> [0, 0]。 无论 n 是否等于1 (亦是否产生进位) one 始终等于0
        所以只要判 two 等于 1 ，将 one 直接置为 0 就行
    2. 如果 two 等于 0，说明状态还在前两种，这时判 n 是否等于 1，正常修改 one 即可。

    以上是修改 one， 修改 two 的逻辑同样屡一下其实也是上述过程。

    if two == 1:
        one = 0
    else:
        if n == 0:
            one = one
        else:
            one = ~one

    上述代码过程可以简写为 one = num & ~two ^ one (注意 & 的优先级比 ^ 高)

'''

class Solution:
    def singleNumber(self, nums) -> int:
        one, two = 0, 0
        for num in nums:
            one = num & ~two ^ one
            two = num & ~one ^ two
        return one


solution = Solution()
res = solution.singleNumber([3,4,3,3])
print(res)