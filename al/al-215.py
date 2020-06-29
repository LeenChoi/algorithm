# 数组中的第K个最大元素
# medium
'''
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:
输入: [3,2,1,5,6,4] 和 k = 2
输出: 5

示例 2:
输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4

说明:
你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kth-largest-element-in-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

--------------------------------
题解：堆排 top N，快排剪枝
1.典型的 top N 问题，做个大小 k 的小顶堆，遍历数组往里插值，最后输出堆顶即可
2.快排，以某个数为基准点分完两段子数组后，只对包含 k 的那一段再次拆分，另一端不用管，迭代最终某个基准点是 k 的时候返回即可

'''


class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        heap = Heap(k)
        for num in nums:
            heap.add(num)
        return heap.queue[1]


class Heap:
    def __init__(self, k):
        self.queue = [0]
        self.length = 0
        self.cap = k

    def add(self, value):
        if self.length < self.cap:
            self.queue.append(value)
            self.length += 1
            self.shiftUp()
        elif value >= self.queue[1]:
            self.queue[1] = value
            self.shiftDown()

    def shiftUp(self):
        i = len(self.queue) - 1
        while i > 1:
            if i // 2 >= 1 and self.queue[i // 2] > self.queue[i]:
                self.queue[i // 2], self.queue[i] = self.queue[i], self.queue[i // 2]
                i = i // 2
            else:
                break

    def shiftDown(self):
        i = 1
        while i <= self.length:
            t = i
            if i * 2 <= self.length and self.queue[i * 2] < self.queue[i]:
                t = i * 2
            if  i * 2 + 1 <= self.length and self.queue[i * 2 + 1] < self.queue[t]:
                t = i * 2 + 1
            if t == i:
                break
            self.queue[i], self.queue[t] = self.queue[t], self.queue[i]
            i = t
        

# print(Solution().findKthLargest([3,2,3,1,2,4,5,5,6], 4))
# print(Solution().findKthLargest([3,2,1,5,6,4], 2))
print(Solution().findKthLargest([7,6,5,4,3,2,1], 5))