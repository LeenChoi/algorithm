# 24 点游戏
# hard
'''
你有 4 张写有 1 到 9 数字的牌。你需要判断是否能通过 *，/，+，-，(，) 的运算得到 24。

示例 1:

输入: [4, 1, 8, 7]
输出: True
解释: (8-4) * (7-1) = 24
示例 2:

输入: [1, 2, 1, 2]
输出: False
注意:

除法运算符 / 表示实数除法，而不是整数除法。例如 4 / (1 - 2/3) = 12 。
每个运算符对两个数进行运算。特别是我们不能用 - 作为一元运算符。例如，[1, 1, 1, 1] 作为输入时，表达式 -1 - 1 - 1 - 1 是不允许的。
你不能将数字连接在一起。例如，输入为 [1, 2, 1, 2] 时，不能写成 12 + 12 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/24-game
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

-----------------------------------------------------
题解：回溯
思路就是数组中选出2个，加减乘除某个运算得到结果后将结果塞入数组，此时数组剩余3个数，再从中选取2个数做运算将结果塞入数组，
最后数组中剩余2个数，最终计算得出结果并判断是否等于24即可。现只需通过回溯将各种组合都枚举一遍就可以了。

这里有几个细节：
1.因为是实数除法，程序里是浮点数计算，会有精度问题，所以判0需要做浮点判0，即小于1e-6就可以看做是0。
2.当0被选取做除数的时候，此时没有数学意义，这种情况应当直接跳过。
3.因为加法乘法满足交换律，A+B 组合枚举过后再遇到 B+A 就可以跳过了

'''


class Solution:
    def judgePoint24(self, nums) -> bool:
        ZERO = 1e-6
        ADD, MULTI, SUBSTRACT, DEVIDE = 1, 2, 3, 4
        def solve(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) < ZERO
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i == j:
                        continue
                    newNums = []
                    for k in range(len(nums)):
                        if k != i and k != j:
                            newNums.append(nums[k])
                    for op in range(1, 5):
                        if op <= 2 and j > i:
                            continue
                        if op == ADD:
                            newNums.append(nums[i] + nums[j])
                        elif op == MULTI:
                            newNums.append(nums[i] * nums[j])
                        elif op == SUBSTRACT:
                            newNums.append(nums[i] - nums[j])
                        elif op == DEVIDE:
                            if nums[j] < ZERO:
                                continue
                            newNums.append(nums[i] / nums[j])
                        if solve(newNums):
                            return True
                        newNums.pop()
            return False
        return solve(nums)


print(Solution().judgePoint24([4, 1, 8, 7]))
print(Solution().judgePoint24([1, 2, 1, 2]))
