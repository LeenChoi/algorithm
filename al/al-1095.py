# 1095. 山脉数组中查找目标值
'''
（这是一个 交互式问题 ）
给你一个 山脉数组 mountainArr，请你返回能够使得 mountainArr.get(index) 等于 target 最小 的下标 index 值。
如果不存在这样的下标 index，就请返回 -1。
 
何为山脉数组？如果数组 A 是一个山脉数组的话，那它满足如下条件：

首先，A.length >= 3
其次，在 0 < i < A.length - 1 条件下，存在 i 使得：

A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]
 
你将 不能直接访问该山脉数组，必须通过 MountainArray 接口来获取数据：

MountainArray.get(k) - 会返回数组中索引为k 的元素（下标从 0 开始）
MountainArray.length() - 会返回该数组的长度
 
注意：
对 MountainArray.get 发起超过 100 次调用的提交将被视为错误答案。此外，任何试图规避判题系统的解决方案都将会导致比赛资格被取消。

-------------------------------------------
题解：
第一思路是二分法加递归，折半然后判断哪一边是平滑有序的，并且判断target是否落到这一区，另一区用递归形式迭代
但是get次数超过了限制。

第二思路是，直接三次二分，先二分找到top点，然后从top点分两个数组，再二分查找左数组，如果没有，再二分查找右数组。

第三思路是，对二分优化，因为二分法应该是这道题的理想答案了，但是还想再优化，那只能对二分再拆了，拆成三分查找。

'''

# 二分查找
class MountainArray:
    def __init__(self, array):
        self.array = array
        self.count = 0

    def get(self, index: int) -> int:
        self.count += 1
        return self.array[index]
       
    def length(self) -> int:
        return len(self.array)

    def getCount(self):
        return self.count
  

class Solution:
    def binarySearch(self, mountain_arr, target, start, end, desc):
        head, tail = start, end
        if target == mountain_arr.get(head):
            return head
        if target == mountain_arr.get(tail):
            return tail

        while head != tail:
            mid = (head + tail) // 2
            midNum = mountain_arr.get(mid)
            if target == midNum:
                return mid

            if target < midNum:
                if desc:
                    head = mid + 1
                    if target  == mountain_arr.get(head):
                        return head
                else:
                    tail = mid
                    if target  == mountain_arr.get(tail):
                        return tail
            else: 
                if desc:
                    tail = mid
                    if target  == mountain_arr.get(tail):
                        return tail
                else:
                    head = mid + 1
                    if target  == mountain_arr.get(head):
                        return head
        return -1


    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        start, end = 0, mountain_arr.length() - 1
        head, tail = start, end
        topIndex = -1
        while head != tail:
            mid = (head + tail) // 2
            midNum = mountain_arr.get(mid)
            preNum = mountain_arr.get(mid - 1)
            afterNum = mountain_arr.get(mid + 1)
            if midNum > preNum and midNum > afterNum:
                topIndex = mid
                break
            if afterNum > midNum:
                head = mid + 1
            else:
                tail = mid

        result = self.binarySearch(mountain_arr, target, start, topIndex, False)
        if result == -1:
            result = self.binarySearch(mountain_arr, target, topIndex + 1, end, True)
            
        return result


# 三分查找
class SolutionV3:
    def trisectionSearch(self, mountain_arr, target, head, tail, convert = lambda x: x):
        target = convert(target)
        while head < tail:
            step = (tail - head) // 3
            i, j = head + step, head + 2 * step
            numi, numj = convert(mountain_arr.get(i)), convert(mountain_arr.get(j))
            if target <= numi:
                tail = i
            elif target > numj:
                head = j + 1
            else:
                head, tail = i + 1, j

        if convert(mountain_arr.get(head)) == target:
            return  head
        else:
            return -1

    def findTop(self, mountain_arr):
        head, tail = 0, mountain_arr.length() - 1
        while head < tail:
            step = (tail - head) // 3
            # 两个游标指针
            i, j = head + step, head + 2 * step
            if i == j:
                # i == j 表明此子数组长度不足4，i 和 j 的指针永远等于 head，直接遍历取了，最多遍历4次
                while head <= tail:
                    print('11111111111111111', head, tail, mountain_arr.get(head), mountain_arr.get(head + 1))
                    if mountain_arr.get(head + 1) < mountain_arr.get(head):
                        return head
                    head += 1

            if mountain_arr.get(i + 1) < mountain_arr.get(i):
                tail = i
            elif mountain_arr.get(j - 1) < mountain_arr.get(j):
                head = j
            else:
                head = i + 1
                tail = j - 1

    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        topIndex = self.findTop(mountain_arr)
        print('topindex = ', topIndex)
        result = self.trisectionSearch(mountain_arr, target, 0, topIndex)
        if result == -1:
            result = self.trisectionSearch(mountain_arr, target, topIndex + 1, mountain_arr.length() - 1, lambda x: -x)
            
        return result


# array = MountainArray([3,5,3,2,0])
# array = MountainArray([1,5,2])
array = MountainArray([0,1,2,4,5,1])
# array = MountainArray([2,3,4,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,100,99,98,97,96,95,94,93,92,91,90,89,88,87,86,85,84,83,82,81,80,79,78,77,76,75,74,73,72,71,70,69,68,67,66,65,64,63,62,61,60,59,58,57,56,55,54,53,52,51,50,49,48,47,46,45,44,43,42,41,40,39,38,37,36,35,34,33,32,31,30,29,28,27,26,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1])
solution = SolutionV3()
res = solution.findInMountainArray(5, array)
print(res, array.getCount())