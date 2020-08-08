# 最长连续序列
# hard
'''
给定一个未排序的整数数组，找出最长连续序列的长度。

要求算法的时间复杂度为 O(n)。

示例:

输入: [100, 4, 200, 1, 3, 2]
输出: 4
解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-consecutive-sequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

--------------------------------------
题解：hashmap (并查集思想)
正常想法，每个数入 hashmap， 然后再遍历一遍数组，当前数 x 找 x+1, x+2,... x+n 是否在 map 里，如果存在那么长度 + 1，
但是会有重复查找的问题，如上例，遍历到 1 时做 x+i 查找，再遍历到后面的 3 和 2 时，做了重复查找，怎么避免重复，
我们只要找到连续序列的最小的那个值就可以，只用它做 x+i 查找，再连续段内的其他数全跳过，怎么找到最小的数，
判断 x-1 是否在 map 中即可，如果存在说明不是最小值，跳过

小说明：
为什么官方标签给了个并查集，此题不是完全意义的并查集，是它的思想。
遍历数组查 x-1 是否在 map 中这个操作，可以看成并查集里的查，因为并查集的查是找到当前节点连接的根节点，
这里的 x-1 操作目的是为了找到连续段的最小值，即根。和查做着相同的操作

硬要说并的话，那就是找连续段 x+i 这个操作了

'''


class Solution:
    def longestConsecutive(self, nums) -> int:
        numSet = set()
        curLength, maxLength = 0, 0
        for num in nums:
            numSet.add(num)
        for num in numSet:
            if not (num - 1) in numSet:
                curLength = 1
                i = 1
                while (num + i) in numSet:
                    curLength += 1
                    i += 1
                maxLength = max(curLength, maxLength)
        return maxLength


print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))
            
        