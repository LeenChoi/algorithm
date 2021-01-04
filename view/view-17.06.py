# 2出现的次数
# hard
'''
编写一个方法，计算从 0 到 n (含 n) 中数字 2 出现的次数。

示例:

输入: 25
输出: 9
解释: (2, 12, 20, 21, 22, 23, 24, 25)(注意 22 应该算作两次)
提示：

n <= 10^9


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-2s-in-range-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

-------------------------------------------------------
题解：
12345 以这个数为例，我想查百位数为 2 的一共有多少个

   200 -    299   100个
 1 200 -  1 299   100个
 2 200 -  2 299   100个
...
12 200 - 12 299   100个

一共 (12 + 1) * 100，这是百位数大于 2 的时候，
当百位数小于 2 比如 12145，那么就是 12 * 100 个
当百位数等于 2 比如 12245，那么就是 12 * 100 个，加上 12 200 - 12 245 的 45+1 个

了解这个规则后，只需将数字 N 按位遍历，算出每个位的总个数，然后累加即可

'''


class Solution:
    def numberOf2sInRange(self, n: int) -> int:
        dp = [0] * (n + 1)
        count = 0
        for i in range(n + 1):
            digit = 1
            while i // digit >= 10:
                digit *= 10
            high = i // digit
            remain = i % digit
            if high == 2:
                dp[i] = dp[remain] + 1
            else:
                dp[i] = dp[remain]
            count += dp[i]
        return count

    def numberOf2sInRange2(self, n: int) -> int:
        s = str(n)
        count = 0
        for i in range(len(s)):
            high = 0 if len(s[:i]) == 0 else int(s[:i])
            low = 0 if len(s[i+1:]) == 0 else int(s[i+1:])
            cur = int(s[i])
            if cur < 2:
                count += high * (10 ** len(s[i+1:]))
            elif cur > 2:
                count += (high + 1) * (10 ** len(s[i+1:]))
            else:
                count += high * (10 ** len(s[i+1:])) + low + 1
        return count

print(Solution().numberOf2sInRange2(559366752))