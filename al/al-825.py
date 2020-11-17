# 适龄的朋友
# medium
'''
人们会互相发送好友请求，现在给定一个包含有他们年龄的数组，ages[i] 表示第 i 个人的年龄。

当满足以下任一条件时，A 不能给 B（A、B不为同一人）发送好友请求：

age[B] <= 0.5 * age[A] + 7
age[B] > age[A]
age[B] > 100 && age[A] < 100
否则，A 可以给 B 发送好友请求。

注意如果 A 向 B 发出了请求，不等于 B 也一定会向 A 发出请求。而且，人们不会给自己发送好友请求。 

求总共会发出多少份好友请求?

 

示例 1：

输入：[16,16]
输出：2
解释：二人可以互发好友申请。
示例 2：

输入：[16,17,18]
输出：2
解释：好友请求可产生于 17 -> 16, 18 -> 17.
示例 3：

输入：[20,30,100,110,120]
输出：3
解释：好友请求可产生于 110 -> 100, 120 -> 110, 120 -> 100.
 

提示：

1 <= ages.length <= 20000.
1 <= ages[i] <= 120.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/friends-of-appropriate-ages
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

----------------------------------------------------
题解：
记一个数组记录每个age有多少个，然后遍历这个age数组，计算每两对age能产生多少个请求
当 age a、age b 不同时，能产生age[a] * age[b] 个请求，如果相同，因为自己不能请求自己所以 age[a] * (age[a] - 1)

'''


class Solution:
    def numFriendRequests(self, ages) -> int:
        ans = 0
        age = [0] * 121
        for a in ages:
            age[a] += 1
        for a in range(1, len(age)):
            if age[a] == 0:
                continue
            for b in range(1, len(age)):
                if age[b] == 0:
                    continue
                if b <= a and b > a / 2 + 7:
                    if a == b:
                        ans += age[a] * (age[a] - 1)
                    else:
                        ans += age[a] * age[b]
        return ans


print(Solution().numFriendRequests([20,30,100,110,120]))
