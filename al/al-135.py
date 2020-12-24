# 分发糖果
# hard
'''
老师想给孩子们分发糖果，有 N 个孩子站成了一条直线，老师会根据每个孩子的表现，预先给他们评分。

你需要按照以下要求，帮助老师给这些孩子分发糖果：

每个孩子至少分配到 1 个糖果。
相邻的孩子中，评分高的孩子必须获得更多的糖果。
那么这样下来，老师至少需要准备多少颗糖果呢？

示例 1:

输入: [1,0,2]
输出: 5
解释: 你可以分别给这三个孩子分发 2、1、2 颗糖果。
示例 2:

输入: [1,2,2]
输出: 4
解释: 你可以分别给这三个孩子分发 1、2、1 颗糖果。
     第三个孩子只得到 1 颗糖果，这已满足上述两个条件。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/candy
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

-----------------------------------------------------------
题解: 贪心
做个糖果list，初始都是1，然后正序遍历一遍评分，贪心的将比较大的后一个数的糖果 +1，这里不是单纯在现有糖果list上的数 +1，
而是前一个糖果数 +1。然后再反序遍历一遍，做同样操作，但需要额外的判断是，前一个比较大的数的糖果是否已经大于后一个

'''


class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        print(candies)
        for j in range(len(ratings) - 2, -1, -1):
            if ratings[j] > ratings[j + 1] and candies[j] <= candies[j + 1]:
                candies[j] = candies[j + 1] + 1
        print(candies)
        return sum(candies)    
        