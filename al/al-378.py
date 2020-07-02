# 有序矩阵中第K小的元素
# medium
'''
给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。
请注意，它是排序后的第 k 小元素，而不是第 k 个不同的元素。

示例：
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

返回 13。
 
提示：
你可以假设 k 的值永远是有效的，1 ≤ k ≤ n2 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

-----------------------------------------
题解：堆，二分法
    小顶堆，遍历就完了
    二维二分法，因为此矩阵的特性是每行每列有序，matrix[0][0]为最小，matrix[-1][-1]为最大，所以利用这个特点，做二分查找
    找一个mid数，从矩阵左下角为入口，当前点如果小于mid，指针右移，如果大于mid，指针上移，最终指针会从上边界或右边界移出
    一次二分迭代的过程中，将会在矩阵上产生一个分界线，分界线左面的都小于等于mid，可以算出有多少个小于mid的数，
    如果大于k个，表明第k小的数在分界线左面，如果小于k个，表明在分界线右面，对对应区域再次迭代即可，直到左边界和右边界相等

'''


class Solution:
    def kthSmallest(self, matrix, k: int) -> int:
        heap = Heap(k)
        n = len(matrix)
        for i in range(n):
            if heap.length == heap.cap and matrix[i][i] > heap.queue[1]:
                break
            heap.add(matrix[i][i])
            for j in range(i + 1, n):
                if j < n:
                    heap.add(matrix[i][j])
                    heap.add(matrix[j][i])
        print(heap.queue)
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
        elif value <= self.queue[1]:
            self.queue[1] = value
            self.shiftDown()

    def shiftUp(self):
        i = len(self.queue) - 1
        while i > 1:
            if i // 2 >= 1 and self.queue[i // 2] < self.queue[i]:
                self.queue[i // 2], self.queue[i] = self.queue[i], self.queue[i // 2]
                i = i // 2
            else:
                break

    def shiftDown(self):
        i = 1
        while i <= self.length:
            t = i
            if i * 2 <= self.length and self.queue[i * 2] > self.queue[i]:
                t = i * 2
            if  i * 2 + 1 <= self.length and self.queue[i * 2 + 1] > self.queue[t]:
                t = i * 2 + 1
            if t == i:
                break
            self.queue[i], self.queue[t] = self.queue[t], self.queue[i]
            i = t



class SolutionV2:
    def kthSmallest(self, matrix, k: int) -> int:
        n = len(matrix)
        l, r = matrix[0][0], matrix[-1][-1]
        def checkCount(mid):
            i, j = n - 1, 0
            count, ans = 0, None
            while i >= 0 and j < n:
                if matrix[i][j] <= mid:
                    ans = matrix[i][j] if ans == None else max(ans, matrix[i][j])
                    count += i + 1
                    j += 1
                else:
                    i -= 1
            return (count, ans)
        
        while l < r:
            mid = (l + r) // 2
            result = checkCount(mid)
            if result[0] == k:
                return result[1]
            if result[0] > k:
                r = mid
            else:
                l = mid + 1
        return l



print(SolutionV2().kthSmallest([[ 1,  5,  9],[10, 11, 13],[12, 13, 15]], 8))
print(SolutionV2().kthSmallest([[ 1,  5,  9],[10, 11, 12],[11, 12, 15]], 8))
print(SolutionV2().kthSmallest([[ 1,  5,  9],[10, 11, 12],[11, 13, 15]], 8))
print(SolutionV2().kthSmallest([[1,3,5],[6,7,12],[11,14,14]], 5))
print(SolutionV2().kthSmallest([[1,2],[1,3]], 4))
print(SolutionV2().kthSmallest([[1,2],[1,3]], 1))
print(SolutionV2().kthSmallest([[-5]], 1))