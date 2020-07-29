# 寻宝
# hard
'''
我们得到了一副藏宝图，藏宝图显示，在一个迷宫中存在着未被世人发现的宝藏。

迷宫是一个二维矩阵，用一个字符串数组表示。它标识了唯一的入口（用 'S' 表示），和唯一的宝藏地点（用 'T' 表示）。但是，宝藏被一些隐蔽的机关保护了起来。在地图上有若干个机关点（用 'M' 表示），只有所有机关均被触发，才可以拿到宝藏。

要保持机关的触发，需要把一个重石放在上面。迷宫中有若干个石堆（用 'O' 表示），每个石堆都有无限个足够触发机关的重石。但是由于石头太重，我们一次只能搬一个石头到指定地点。

迷宫中同样有一些墙壁（用 '#' 表示），我们不能走入墙壁。剩余的都是可随意通行的点（用 '.' 表示）。石堆、机关、起点和终点（无论是否能拿到宝藏）也是可以通行的。

我们每步可以选择向上/向下/向左/向右移动一格，并且不能移出迷宫。搬起石头和放下石头不算步数。那么，从起点开始，我们最少需要多少步才能最后拿到宝藏呢？如果无法拿到宝藏，返回 -1 。

示例 1：
输入： ["S#O", "M..", "M.T"]
输出：16
解释：最优路线为： S->O, cost = 4, 去搬石头 O->第二行的M, cost = 3, M机关触发 第二行的M->O, cost = 3, 我们需要继续回去 O 搬石头。 O->第三行的M, cost = 4, 此时所有机关均触发 第三行的M->T, cost = 2，去T点拿宝藏。 总步数为16。

示例 2：
输入： ["S#O", "M.#", "M.T"]
输出：-1
解释：我们无法搬到石头触发机关

示例 3：
输入： ["S#O", "M.T", "M.."]
输出：17
解释：注意终点也是可以通行的。

限制：

1 <= maze.length <= 100
1 <= maze[i].length <= 100
maze[i].length == maze[j].length
S 和 T 有且只有一个
0 <= M的数量 <= 16
0 <= O的数量 <= 40，题目保证当迷宫中存在 M 时，一定存在至少一个 O 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/xun-bao
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

------------------------------------
题解：bfs + dp + 状态压缩 + 记忆法

找到宝藏其实可以分解为三个步骤：
1. 从始发点 S 找到石头 O 再找到一个机关 M
2. 从当前机关 M 去找到石头 O 再到另一个机关 M', 重复此过程
3. 从最后一个 M 走到宝藏点 T

然后只需要找到路径最短的组合就可以。
点到点的距离可以 bfs 求出，然后预处理存起来 stepDict。
然后可以通过 stepDict 求出上述各阶段的最少步数。具体是，因为可能有多个 O，拿第一阶段来讲，遍历 Oi 找到某个 On，算出 S->On 距离加上 On->M 距离的最小值
最终会得到 S 到各 M 点的最短步数集合 s2m, 还有 Mi 到 Mj 的 m2m，M 到终点 T 的 m2t

动态规划过程：这里用到了状态压缩。
注：如果碰到一种题，如有 n 个 M 任务，完成任务 Mi, Mj 之间有个代价 c(Mi, Mj)，求完成所有任务的最小代价，这种的题，应该要想到状态压缩的动态规划
以本题为例，题中给的限制不是白给的，M 数量最多 16 个，可以用 16 位二进制数来表示状态（状态压缩），每一位的 1 代表此机关已经触发，0 代表还没触发
记 dp[mask][i] 为当触发状态为 mask 时，以第 i 个机关为最后触发的最少步数。
比如 mask (1 1 0 1)，   它的状态可以从 mask (1 1 0 0) 得到，我们可以从这个状态的第一个 M1 走到(耗费 m2m[M1][M4] 步数)下一个 mask 状态的 M4，
                |
                i 此机关第3个被触发
也可以从 M2 走到 M4(耗费 m2m[M2][M4])，取的两者的最小值即是当前 mask 下第 i 机关的 dp 值。

所以，状态转移方程为: dp[mask][i] = min{j | j!=i, 2^j & mask > 0}(dp[mask xor (1 << i)][j] + m2m[j][i])
最后得出来所有 dp 值后，遍历一遍最终状态 mask 的所有 dp 值，加上对应 Mi 出发到 T 的距离 m2t[i]，去最小值即是最终答案

'''


class Solution:
    def minimalSteps(self, maze) -> int:
        m, n = len(maze), len(maze[0])
        stepDict = [[None] * n for _ in range(m)]
        S, T = None, None
        O, M = [], []

        # 生成 step dict，记录 O, M, S, T 点
        for i in range(m):
            for j in range(n):
                if maze[i][j] != '#' and maze[i][j] != '.' and maze[i][j] != 'T':
                    stepDict[i][j] = bfs(i, j, maze)
                if maze[i][j] == 'M':
                    M.append((i, j))
                elif maze[i][j] == 'O':
                    O.append((i, j))
                elif maze[i][j] == 'S':
                    S = (i, j)
                elif maze[i][j] == 'T':
                    T = (i, j)

        # 如果没有 M，直接返回 S -> T 距离
        if len(M) == 0:
            sDict = stepDict[S[0]][S[1]]
            return sDict[T[0]][T[1]]

        # S -> O -> M 最短距离
        s2m = [-1] * len(M)
        for i in range(len(M)):
            _m = M[i]
            sDict = stepDict[S[0]][S[1]]
            for j in range(len(O)):
                _o = O[j]
                oDict = stepDict[_o[0]][_o[1]]
                step1 = sDict[_o[0]][_o[1]]
                step2 = oDict[_m[0]][_m[1]]
                if step1 != -1 and step2 != -1:
                    stepf = step1 + step2
                    s2m[i] = stepf if s2m[i] < 0 else min(s2m[i], stepf)
        
        # M -> T 距离
        m2t = [-1] * len(M)
        for i in range(len(M)):
            _m = M[i]
            mDict = stepDict[_m[0]][_m[1]]
            m2t[i] = mDict[T[0]][T[1]]

        # M -> O -> M' 最短距离
        m2m = [[-1] * len(M) for _ in range(len(M))]
        for i in range(len(M)):
            _m1 = M[i]
            mDict = stepDict[_m1[0]][_m1[1]]
            for j in range(len(M)):
                if i == j:
                    continue
                _m2 = M[j]
                for k in range(len(O)):
                    _o = O[k]
                    oDict = stepDict[_o[0]][_o[1]]
                    step1 = mDict[_o[0]][_o[1]]
                    step2 = oDict[_m2[0]][_m2[1]]
                    if step1 != -1 and step2 != -1:
                        stepf = step1 + step2
                        m2m[i][j] = stepf if m2m[i][j] < 0 else min(m2m[i][j], stepf)

        # dp
        lm = len(M)
        dp = [[-1] * lm for _ in range(1 << lm)]
        for i in range(lm):
            dp[1 << i][i] = s2m[i]
        
        for mask in range(1, 1 << lm):
            for i in range(lm):
                if mask & (1 << i) > 0:
                    pre = mask ^ (1 << i)
                    if pre == 0:
                        continue
                    for j in range(lm):
                        if i == j:
                            continue
                        if dp[pre][j] != -1 and m2m[j][i] != -1:
                            steps = dp[pre][j] + m2m[j][i]
                            if dp[mask][i] == -1 or steps < dp[mask][i]:
                                dp[mask][i] = steps

        ans = -1
        finMask = (1 << lm) - 1
        for i in range(lm):
            if dp[finMask][i] != -1 and m2t[i] != -1:
                steps = dp[finMask][i] + m2t[i]
                if ans == -1 or steps < ans:
                    ans = steps
        return ans


def bfs(x, y, maze):
    m, n = len(maze), len(maze[0])

    def arround(p):
        i, j = p[0], p[1]
        points = []
        if i - 1 >= 0 and maze[i - 1][j] != '#':
            points.append((i - 1, j))
        if j + 1 < n and maze[i][j + 1] != '#':
            points.append((i, j + 1))
        if i + 1 < m and maze[i + 1][j] != '#':
            points.append((i + 1, j))
        if j - 1 >= 0 and maze[i][j - 1] != '#':
            points.append((i, j - 1))
        return points

    queue = [(x, y)]
    steps = [[-1] * n for _ in range(m)]
    steps[x][y] = 0
    while len(queue) > 0:
        cp = queue.pop(0)
        for ap in arround(cp):
            ci, cj = cp[0], cp[1]
            i, j = ap[0], ap[1]
            if steps[i][j] == -1:
                steps[i][j] = steps[ci][cj] + 1
                queue.append(ap)
    return steps


print(Solution().minimalSteps(["S#O", "M..", "M.T"]))
print(Solution().minimalSteps(["S#O", "M.#", "M.T"]))
print(Solution().minimalSteps(["S#O", "M.T", "M.."]))
# print(Solution().minimalSteps(["MMMMM","MS#MM","MM#TO"]))
