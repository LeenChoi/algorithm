# 根据身高重建队列
# medium
'''
假设有打乱顺序的一群人站成一个队列。 每个人由一个整数对(h, k)表示，其中h是这个人的身高，k是排在这个人前面且身高大于或等于h的人数。 编写一个算法来重建这个队列。

注意：
总人数少于1100人。

示例

输入:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

输出:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/queue-reconstruction-by-height
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

-----------------------------
题解：贪心
贪心在哪？ 贪心在，个高的不用在意他前面有几个个矮的，所以可先个高的排就完了。
people 按个儿降序，同个儿的按 k 位置升序排序，然后遍历排好序的 people，逐个按 k 的索引插入到队列即可

为什么插入 k 索引的位置？
比如 (6,2) 这个人，前面个儿 6 以上的已经入队了，(6,0) (6,1) 也入队了，此时队列的前两项肯定不矮于这个人，
所以直接插入到索引 2 的位置即可

solution1 也算能成功出解，但死慢，贪心理解错了

'''


class Solution:
    def reconstructQueue(self, people):
        length = len(people)
        i = 0
        while True:
            need = people[i][1]
            j, count = 0, 0
            while j < length:
                if i != j and people[j][0] >= people[i][0]:
                    count += 1
                if j < i:
                    if count > need:
                        people[i], people[j] = people[j], people[i]
                        i = min(i, j)
                        break
                else:
                    if count == need:
                        if i == j:
                            i += 1
                        else:
                            people[i], people[j] = people[j], people[i]
                            i = min(i, j)
                        break
                j += 1
            if i >= length:
                break
        return people


class Solution2:
    def reconstructQueue(self, people):
        ans = []
        people.sort(key = lambda x: (-x[0], x[1]))
        for p in people:
            ans.insert(p[1], p)
        return ans


print(Solution().reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]))