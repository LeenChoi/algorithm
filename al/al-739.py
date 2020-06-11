# 每日温度
# medium
'''
根据每日 气温 列表，请重新生成一个列表，对应位置的输出是需要再等待多久温度才会升高超过该日的天数。如果之后都不会升高，请在该位置用 0 来代替。

例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。

提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/daily-temperatures
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

---------------------------------------------
题解：单调栈
    栈中存下标，遍历 i，比较 i 下标的数是否大于栈顶下标的数。如果大于，出栈，并计算下标差存入对应的ans数组，
    然后继续下一轮再比较栈顶，如果小于，则入栈


'''


class Solution:
    def dailyTemperatures(self, T):
        stack, ans = [0], [0] * len(T)
        for i in range(1, len(T)):
            while len(stack) > 0 and T[i] > T[stack[-1]]:
                index = stack.pop()
                ans[index] = i - index
            stack.append(i)
        return ans


print(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))