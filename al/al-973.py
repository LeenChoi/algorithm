# 最接近原点的 K 个点
# medium
'''
我们有一个由平面上的点组成的列表 points。需要从中找出 K 个距离原点 (0, 0) 最近的点。

（这里，平面上两点之间的距离是欧几里德距离。）

你可以按任何顺序返回答案。除了点坐标的顺序之外，答案确保是唯一的。

 

示例 1：

输入：points = [[1,3],[-2,2]], K = 1
输出：[[-2,2]]
解释： 
(1, 3) 和原点之间的距离为 sqrt(10)，
(-2, 2) 和原点之间的距离为 sqrt(8)，
由于 sqrt(8) < sqrt(10)，(-2, 2) 离原点更近。
我们只需要距离原点最近的 K = 1 个点，所以答案就是 [[-2,2]]。
示例 2：

输入：points = [[3,3],[5,-1],[-2,4]], K = 2
输出：[[3,3],[-2,4]]
（答案 [[-2,4],[3,3]] 也会被接受。）
 

提示：

1 <= K <= points.length <= 10000
-10000 < points[i][0] < 10000
-10000 < points[i][1] < 10000


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/k-closest-points-to-origin
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

------------------------------------------------
题解：top N
最小k个，做个大顶堆即可，最后输出堆的队列

'''


class Solution:
    def kClosest(self, points, K: int):
        heap = Heap(K)
        for point in points:
            heap.add(point)
        return heap.queue[1:]

# 要大顶堆
class Heap:
    def __init__(self, k):
        self.queue = [None]
        self.length = 0
        self.cap = k

    def add(self, point):
        if self.length < self.cap:
            self.queue.append(point)
            self.shiftUp()
            self.length += 1
        elif calcVal(point) < calcVal(self.queue[1]):
            self.queue[1] = point
            self.shiftDown()

    def shiftUp(self):
        i = len(self.queue) - 1
        while i > 1:
            if calcVal(self.queue[i]) > calcVal(self.queue[i // 2]):
                self.queue[i], self.queue[i // 2] = self.queue[i // 2], self.queue[i]
                i = i // 2
            else:
                break

    def shiftDown(self):
        i = 1
        while i <= self.length:
            t = i
            if i * 2 <= self.length and calcVal(self.queue[t]) < calcVal(self.queue[i * 2]):
                t = i * 2
            if i * 2 + 1 <= self.length and calcVal(self.queue[t]) < calcVal(self.queue[i * 2 + 1]):
                t = i * 2 + 1
            if t == i:
                break
            self.queue[i], self.queue[t] = self.queue[t], self.queue[i]
            i = t


def calcVal(point):
    return point[0] * point[0] + point[1] * point[1]


# print(Solution().kClosest([[3,3],[5,-1],[-2,4]], 2))
print(Solution().kClosest([[100,-16],[-31,45],[80,-47],[41,59],[-59,-34],[-34,-76],[-5,-77],[35,40],[58,-30],[31,-96],[40,14],[-25,50],[37,-38],[-54,-31]], 8))