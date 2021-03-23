# 移除盒子
# hard
'''
给出一些不同颜色的盒子，盒子的颜色由数字表示，即不同的数字表示不同的颜色。
你将经过若干轮操作去去掉盒子，直到所有的盒子都去掉为止。每一轮你可以移除具有相同颜色的连续 k 个盒子（k >= 1），这样一轮之后你将得到 k*k 个积分。
当你将所有盒子都去掉之后，求你能获得的最大积分和。

 

示例：

输入：boxes = [1,3,2,2,2,3,4,3,1]
输出：23
解释：
[1, 3, 2, 2, 2, 3, 4, 3, 1] 
----> [1, 3, 3, 4, 3, 1] (3*3=9 分) 
----> [1, 3, 3, 3, 1] (1*1=1 分) 
----> [1, 1] (3*3=9 分) 
----> [] (2*2=4 分)
 

提示：

1 <= boxes.length <= 100
1 <= boxes[i] <= 100


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-boxes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

--------------------------------------------------
题解：动态规划dp

设 f(l,r,k) 为删除 [l,r] 区间元素和它后面 k 个和 a[r] 相等的元素(离散的)的最大积分，假设后面不与 a[r] 相同的元素已经删除，
所以可以认为后面为连续 k 个 a[r] 相等元素。

那么删除策略可以分两类：
1.先删除后面连续 k+1 个相同元素, 再删除 [l, r-1] 里的元素，
    则 f(l,r,k) = f(l,r-1,0) + (k+1)^2
2.先删除区间里的某一段 [i+1,r-1] 若 a[i] == a[r]，再删除前面剩下的 [l,i] 和 后面剩下的连续 k+1 个元素，
    那么 f(l,r,k) = f(i+1,r-1,0) + f(l,i,k+1)
    找出符合 i 的所有情况，都算一遍取得最大积分

结合上述两种策略，f(l,r,k) = max{f(l,r-1,0) + (k+1)^2, max{i <= [l, r), a[i] == a[r] | f(i+1,r-1,0) + f(l,i,k+1)}}

最后，输出 f(0, n-1, 0) 即是答案。

'''


class Solution:
    def removeBoxes(self, boxes) -> int:
        dp = [[[0 for j in range(len(boxes))] for i in range(len(boxes))] for m in range(len(boxes))]
        def calcPoints(l, r, k):
            if l > r:
                return 0
            if dp[l][r][k] != 0:
                return dp[l][r][k]
            
            # 优化 r，如果 r 位置前面有一串相同的那么 r 前移，随之 k 会变长
            while r > l and boxes[r] == boxes[r - 1]:
                r -= 1
                k += 1
            # 策略1
            dp[l][r][k] = calcPoints(l, r - 1, 0) + (k + 1) * (k + 1)
            # 策略2
            for i in range(l, r):
                if boxes[i] == boxes[r]:
                    dp[l][r][k] = max(dp[l][r][k], calcPoints(l, i, k + 1) + calcPoints(i + 1, r - 1, 0))
            return dp[l][r][k]

        return calcPoints(0, len(boxes) - 1, 0)


print(Solution().removeBoxes([1,3,2,2,2,3,4,3,1]))
# print(Solution().removeBoxes([1,3,2]))