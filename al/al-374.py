# 猜数字大小
# easy
'''
我们正在玩一个猜数字游戏。 游戏规则如下：
我从 1 到 n 选择一个数字。 你需要猜我选择了哪个数字。
每次你猜错了，我会告诉你这个数字是大了还是小了。
你调用一个预先定义好的接口 guess(int num)，它会返回 3 个可能的结果（-1，1 或 0）：

-1 : 我的数字比较小
 1 : 我的数字比较大
 0 : 恭喜！你猜对了！
 

示例 :

输入: n = 10, pick = 6
输出: 6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/guess-number-higher-or-lower
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

# 二分查找
class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n
        while l < r:
            mid = (l + r) // 2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:
                r = mid - 1
            else:
                l = mid + 1
        return l


# 三分查找
class Solution2:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n
        while l < r:
            mid1 = l + (r - l) // 3
            mid2 = l + 2 * (r - l) // 3
            if guess(mid1) == 0:
                return mid1
            if guess(mid2) == 0:
                return mid2
            if guess(mid1) == -1:
                r = mid1 - 1
            elif guess(mid2) == 1:
                l = mid2 + 1
            else:
                l = mid1 + 1
                r = mid2 - 1
        return l