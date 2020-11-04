# 插入区间
# hard
'''
给出一个无重叠的 ，按照区间起始端点排序的区间列表。

在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。

 

示例 1：

输入：intervals = [[1,3],[6,9]], newInterval = [2,5]
输出：[[1,5],[6,9]]
示例 2：

输入：intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
输出：[[1,2],[3,10],[12,16]]
解释：这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/insert-interval
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

----------------------------------------------------
题解:
如下图，不重叠部分可以直接输出，其实要处理的部分只有重叠的部分

--------  --------  ----   ------  -------  -----
                =========

--------  ---------------  ------  -------  -----

所以只要先把 ri < left 区间和 li > right 区间部分抛出去，剩下区间即重叠区间，将他们融合即可

官方题解很巧妙，当时我是将重叠区多种情况分别判断，很绕。其实只需要比较，得出重合区间最小值和最大值即可，
然后将融合后的整个区间插入到答案。注意有可能新的区间会覆盖到原数组的整个末尾，所以遍历完数组后需要再判下有没有融合完再插入

'''


class Solution:
    def insert(self, intervals, newInterval):
        ans = []
        start, end = -1, -1
        state = 0
        index = 0
        while index < len(intervals):
            interval = intervals[index]
            if state == 2:
                ans.append(interval)
                index += 1
            elif state == 0:
                if newInterval[1] < interval[0]:
                    ans.append(newInterval)
                    state = 2
                elif newInterval[0] >= interval[0] and newInterval[1] <= interval[1]:
                    state = 2
                elif newInterval[0] >= interval[0] and newInterval[0] <= interval[1]:
                    start = interval[0]
                    state = 1
                    index += 1
                elif newInterval[0] <= interval[0]:
                    if newInterval[1] >= interval[0] and newInterval[1] <= interval[1]:
                        start = newInterval[0]
                        end = interval[1]
                        ans.append([start, end])
                        state = 2
                        index += 1
                    else:
                        start = newInterval[0]
                        state = 1
                        index += 1
                else:
                    ans.append(interval)
                    index += 1
            else:
                if newInterval[1] < interval[0]:
                    end = newInterval[1]
                    ans.append([start, end])
                    state = 2
                elif newInterval[1] >= interval[0] and newInterval[1] <= interval[1]:
                    end = interval[1]
                    ans.append([start, end])
                    state = 2
                    index += 1
                else:
                    index += 1
        if state == 0:
            ans.append(newInterval)
        elif state == 1:
            end = newInterval[1]
            ans.append([start, end])

        return ans


class Solution2:
    def insert(self, intervals, newInterval):
        left, right = newInterval
        matched = False
        ans = []
        for li, ri in intervals:
            if ri < left:
                ans.append([li, ri])
            elif li > right:
                if not matched:
                    ans.append([left, right])
                    matched = True
                ans.append([li, ri])
            else:
                left = min(left, li)
                right = max(right, ri)
        if not matched:
            ans.append([left, right])
        return ans
            


print(Solution2().insert([[1,3], [6,9]], [2,5]))
print(Solution2().insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))
print(Solution2().insert([[1,5]], [0,3]))
print(Solution2().insert([[1,5]], [0,6]))