# 地下城游戏
# hard
'''
一些恶魔抓住了公主（P）并将她关在了地下城的右下角。地下城是由 M x N 个房间组成的二维网格。我们英勇的骑士（K）最初被安置在左上角的房间里，他必须穿过地下城并通过对抗恶魔来拯救公主。
骑士的初始健康点数为一个正整数。如果他的健康点数在某一时刻降至 0 或以下，他会立即死亡。
有些房间由恶魔守卫，因此骑士在进入这些房间时会失去健康点数（若房间里的值为负整数，则表示骑士将损失健康点数）；其他房间要么是空的（房间里的值为 0），要么包含增加骑士健康点数的魔法球（若房间里的值为正整数，则表示骑士将增加健康点数）。
为了尽快到达公主，骑士决定每次只向右或向下移动一步。 

编写一个函数来计算确保骑士能够拯救到公主所需的最低初始健康点数。

例如，考虑到如下布局的地下城，如果骑士遵循最佳路径 右 -> 右 -> 下 -> 下，则骑士的初始健康点数至少为 7。

-2(K)| -3 |	3
-5   |-10 | 1
10   | 30 |-5 (P)
 
说明:
骑士的健康点数没有上限。
任何房间都可能对骑士的健康点数造成威胁，也可能增加骑士的健康点数，包括骑士进入的左上角房间以及公主被监禁的右下角房间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/dungeon-game
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

---------------------------------
题解：动态规划
反着动态规划，dp[i][j] 继承 dp[i+1][j]/dp[i][j+1]，
转移过程，dungeon[i][j] + dp[i+1][j]/dp[i][j+1]，表示目前点需要多少健康点才能顺利通过以后的点
直接做和，记录负值，如果大于0 表示不需要健康点就可以通过以后的点 还有剩余，那么置为0即可，因为不需要健康点
最后输出abs(dp[0][0]) + 1 即可，因为需要留 1 健康点，如果是大于0，直接返回 1

'''

class Solution:
    def calculateMinimumHP(self, dungeon) -> int:
        m, n = len(dungeon), len(dungeon[0])
        dp = [[float('-inf')] * (n + 1) for _ in range(m + 1)]
        dp[m][n - 1] = dp[m - 1][n] = 0
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                rightNeed = dungeon[i][j] + dp[i][j + 1] if dungeon[i][j] + dp[i][j + 1] < 0 else 0
                downNeed = dungeon[i][j] + dp[i + 1][j] if dungeon[i][j] + dp[i + 1][j] < 0 else 0
                dp[i][j] = max(rightNeed, downNeed)
        return abs(dp[0][0]) + 1 if dp[0][0] < 0 else 1


print(Solution().calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]]))
print(Solution().calculateMinimumHP([[1,-3,3],[0,-2,0],[-3,-3,-3]]))
print(Solution().calculateMinimumHP([[3,0,-3],[-3,-2,-2],[3,1,-3]]))
print(Solution().calculateMinimumHP([[0,0,0],[-1,0,0],[2,0,-2]]))
