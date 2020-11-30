# 最小区间
# hard
'''
你有 k 个 非递减排列 的整数列表。找到一个 最小 区间，使得 k 个列表中的每个列表至少有一个数包含在其中。

我们定义如果 b-a < d-c 或者在 b-a == d-c 时 a < c，则区间 [a,b] 比 [c,d] 小。

 

示例 1：

输入：nums = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
输出：[20,24]
解释： 
列表 1：[4, 10, 15, 24, 26]，24 在区间 [20,24] 中。
列表 2：[0, 9, 12, 20]，20 在区间 [20,24] 中。
列表 3：[5, 18, 22, 30]，22 在区间 [20,24] 中。
示例 2：

输入：nums = [[1,2,3],[1,2,3],[1,2,3]]
输出：[1,1]
示例 3：

输入：nums = [[10,10],[11,11]]
输出：[10,11]
示例 4：

输入：nums = [[10],[11]]
输出：[10,11]
示例 5：

输入：nums = [[1],[2],[3],[4],[5],[6],[7]]
输出：[1,7]
 

提示：

nums.length == k
1 <= k <= 3500
1 <= nums[i].length <= 50
-105 <= nums[i][j] <= 105
nums[i] 按非递减顺序排列

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/smallest-range-covering-elements-from-k-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

-------------------------------------------------
题解：哈希表 + 滑动窗口
题解类似 al-76, 给一个小字符串，从大字符串里找出涵盖小字符串所有字符的最小子串。
它的题解就是用的滑动窗口+哈希，滑动窗口在大字符串中从左开始移动并将窗口内的字符计数记录进哈希表，当计数满足小字符串的字符数量后，
窗口左侧向右收缩，窗口内的计数又不满足后窗口右侧再向右扩展，以此类推，找出最小的窗口就是答案。

此题的题解和上述类似，先将k个数组转成 num对应k个数组索引的映射表，即 [[1,2],[2,3]] -> {'1': [0], '2': [0, 1], '3': [1]}
找出整个nums里的最大最小值，然后滑动窗口在这个范围内在映射表上移动，窗口的大小应该保持在多少，即扩到什么范围窗口再收缩？
看示例5，k个数组都是相互不重叠的，这种极限情况这个窗口的大小就该是这些值的并集，即nums长度。所以需要一个计数，当这个计数等于len(nums)的时候窗口收缩。

其次我们还需要一个哈希表，用来记录上面的映射表中，每个索引位出现的次数。上面的映射表中，比如滑动窗口覆盖了 '1'，'2' 键，
那么值里面的 0 位出现了2次，1 位出现了1次。记录这个频次的时候判断下如果某个索引位计数从 0 到 1，表明这个索引位是新加入计数的，
那么滑动窗口的总计数 +1，当总计数等于len(nums)的时候，窗口就要从左收缩了，收缩时同样操作将哈希表中的频次 -1，当某个索引位的频次减到 0 时，总计数 -1，
当总计数不等于len(nums)了继续向右扩展窗口，以此类推，找到最小的窗口即是答案。

'''


class Solution:
    def smallestRange(self, nums):
        indices = {}
        _min, _max = None, None
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                num = nums[i][j]
                if indices.get(num) == None:
                    indices[num] = [i]
                else:
                    indices[num].append(i)
                if _min == None or num < _min:
                    _min = num
                if _max == None or num > _max:
                    _max = num
        
        l, r = _min, _min
        ansL, ansR = _min, _max
        freq = {}
        count = 0 # 用来记录所有子数组至少有一个数在范围内
        while r <= _max:
            if indices.get(r) != None:
                for pos in indices[r]:
                    if freq.get(pos) == None:
                        freq[pos] = 1
                    else:
                        freq[pos] += 1
                    if freq[pos] == 1:
                        count += 1
                while count == len(nums):
                    if indices.get(l) != None:
                        if r - l < ansR - ansL:
                            ansL, ansR = l, r
                        for pos in indices[l]:
                            freq[pos] -= 1
                            if freq[pos] == 0:
                                count -= 1
                    l += 1  
            r += 1
        return [ansL, ansR]


# print(Solution().smallestRange([[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]))
print(Solution().smallestRange([[1,3,5,7,9,10],[2,4,6,8,10]]))