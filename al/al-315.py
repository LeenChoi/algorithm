# 计算右侧小于当前元素的个数
# hard
'''
给定一个整数数组 nums，按要求返回一个新数组 counts。数组 counts 有该性质： counts[i] 的值是  nums[i] 右侧小于 nums[i] 的元素的数量。

示例:

输入: [5,2,6,1]
输出: [2,1,1,0] 
解释:
5 的右侧有 2 个更小的元素 (2 和 1).
2 的右侧仅有 1 个更小的元素 (1).
6 的右侧有 1 个更小的元素 (1).
1 的右侧有 0 个更小的元素.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

---------------------------
题解: 归并排序 + 记录map
归并排序每次合并的时候，右段先入队时(表明右面的比左面的小，符合题意) count+1，
左段入队时map里找该数索引值 + count，最后按照数组顺序将map里的记录输出即可

'''


class Solution:
    def countSmaller(self, nums):
        if len(nums) == 0:
            return []
        counts = {}
        inums = [(nums[i], i) for i in range(len(nums))]
        def mergeSort(nums, l, r):
            if l == r:
                return [nums[l]]
            mid = (l + r) // 2
            lnums = mergeSort(nums, l, mid)
            rnums = mergeSort(nums, mid + 1, r)

            i, j = 0, 0
            tmp = []
            count = 0
            while i < len(lnums) and j < len(rnums):
                if rnums[j][0] < lnums[i][0]:
                    count += 1
                    tmp.append(rnums[j])
                    j += 1
                else:
                    if counts.get(lnums[i][1]) == None:
                        counts[lnums[i][1]] = count
                    else:
                        counts[lnums[i][1]] += count

                    tmp.append(lnums[i])
                    i += 1
            while i < len(lnums):
                if counts.get(lnums[i][1]) == None:
                    counts[lnums[i][1]] = count
                else:
                    counts[lnums[i][1]] += count
                tmp.append(lnums[i])
                i += 1
            while j < len(rnums):
                tmp.append(rnums[j])
                j += 1
            return tmp
        mergeSort(inums, 0, len(inums) - 1)
        ans = [counts.get(n) or 0 for n in range(len(inums))]
        return ans



# print(Solution().countSmaller([5,2,6,1]))
print(Solution().countSmaller([26,78,27,100,33,67,90,23,66,5,38,7,35,23,52,22,83,51,98,69,81,32,78,28,94,13,2,97,3,76,99,51,9,21,84,66,65,36,100,41]))