# 数组中的逆序对
'''
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组，求出这个数组中的逆序对的总数。

输入: [7,5,6,4]
输出: 5

-------------------------------------
题解： 归并排序, 算法的难点在于归并的[并]操作之间，比如以下是已经排好序准备并入的子数组
    L = [(8), 12, 16, 22, 100]   R = [(9), 26, 55, 64, 91] | T = []
    当判断 L[0] 小于 R[0], 这时 L[0] 要入临时队列T，且表明 L[0] 8 从位置上看，小于 R[0]以后的的任何一个元素，无法构成逆序对

    L = [8, (12), 16, 22, 100]   R = [(9), 26, 55, 64, 91] | T = [8]
    L的指针后移到 12 这个元素的位置，发现比 R[0] 大，R[0] 入T，同时表明 L[1] 和 R[0] 能组成一个逆序对，此时逆序对count可以 +1 (这其实是思路陷阱)
    9 入 T 后，R 到 R[1] 的位置，紧接着 L 入T 移到 L[2] 的位置，如下

    L = [8, 12, (16), 22, 100]   R = [9, (26), 55, 64, 91] | T = [8, 9, 12]
    此时16，与26比较，16要入T，但是16 即 L[2] 可与 R[0] 组成逆序对，但 R 的指针停留在 R[1]
    根据上面的 +1 操作是产生在 L 和 R 做比较 R 小的时候 +1，但当前指针是在26这个位置，比16大，没法做+1，也不能再向前遍历找到小的那个数再 +1

    这时有个骚操作，L的元素入T时，R 当前位置之前的所有元素其实都是小于 L 当前元素的，
    所以可以在 L 入T时，计算 R 指针的偏移量加到 count 里就可以了

'''

class Solution:
    def mergeSort(self, nums, tmp, l, r):
        count = 0
        mid = (l + r) // 2
        if r - l > 1:
            count = self.mergeSort(nums, tmp, l, mid) + self.mergeSort(nums, tmp, mid + 1, r)
        i, j = l, mid + 1
        k = l
        while i <= mid or j <= r:
            if i <= mid and (j > r or nums[i] <= nums[j]):
                tmp[k] = nums[i]
                i += 1
                k += 1
                count += (j - mid - 1)
                continue
            if j <= r and (i > mid or nums[i] > nums[j]):
                tmp[k] = nums[j]
                j += 1
                k += 1
        
        for h in range(l, r + 1):
            nums[h] = tmp[h]

        return count


    def reversePairs(self, nums) -> int:
        n = len(nums)
        t = [0] * n
        return self.mergeSort(nums, t, 0, n - 1)
      
    
solution = Solution()
res = solution.reversePairs([1,3,2,3,1])
print(res)