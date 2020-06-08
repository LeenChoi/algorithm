# 螺旋矩阵
# medium
'''
给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

示例 1:

输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出: [1,2,3,6,9,8,7,4,5]
示例 2:

输入:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
输出: [1,2,3,4,8,12,11,10,9,5,6,7]

'''

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []

        i, j, ans = 0, -1, []
        direction, count = 0, 0

        xlength = len(matrix[0])
        ylength = len(matrix)
        length = xlength * ylength
 
        while count < length:
            curi, curj = i, j
            if direction == 0:
                curj += 1
            elif direction == 1:
                curi += 1
            elif direction == 2:
                curj -= 1
            else:
                curi -= 1

            if curj >= xlength or curj < 0 or \
            curi >= ylength or curi < 0 or \
            matrix[curi][curj] == None:
                direction += 1
                direction %= 4
                continue
            i, j = curi, curj
            ans.append(matrix[i][j])
            matrix[i][j] = None
            count += 1
            if count >= length:
                break
        return ans


print(Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))