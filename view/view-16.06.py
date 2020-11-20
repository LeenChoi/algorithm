# 最小差
# medium
'''
给定两个整数数组a和b，计算具有最小差绝对值的一对数值（每个数组中取一个值），并返回该对数值的差

示例：

输入：{1, 3, 15, 11, 2}, {23, 127, 235, 19, 8}
输出： 3，即数值对(11, 8)
提示：

1 <= a.length, b.length <= 100000
-2147483648 <= a[i], b[i] <= 2147483647
正确结果在区间[-2147483648, 2147483647]内

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/smallest-difference-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

--------------------------------------------------
题解：双指针，排序
首先将两数组排序，然后归并思想，两数组合并逻辑时算出各自元素的差值绝对值，找出最小值

'''


class Solution:
    def smallestDifference(self, a: List[int], b: List[int]) -> int:
        a.sort()
        b.sort()
        i, j = 0, 0
        min = 2147483647
        while i < len(a) and j < len(b):
            if abs(a[i] - b[j]) < min:
                min = abs(a[i] - b[j])
            if a[i] < b[j]:
                i += 1
            else:
                j += 1
        return min


