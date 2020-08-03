# 字符串相乘
# medium
'''
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

示例 1:

输入: num1 = "2", num2 = "3"
输出: "6"
示例 2:

输入: num1 = "123", num2 = "456"
输出: "56088"
说明：

num1 和 num2 的长度小于110。
num1 和 num2 只包含数字 0-9。
num1 和 num2 均不以零开头，除非是数字 0 本身。
不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/multiply-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

-------------------------------------
题解：
竖向相加，长度 m 与长度 n 的数相乘，结果长度最长为 m+n，所以维护一个 m+n 长度的数组
 
        1 2 3
      *   4 5
    -----------
          1 5
        1 0
      0 5 

        1 2
      0 8
    0 4
   -----------
    0 5 5 3 5

遍历每个数字，相乘后将得到的两位数对号入座加到 m+n 数组的结果即可

'''


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ans = [0] * (len(num1) + len(num2))

        def addUnit(index, num):
            carry, added = 0, False
            while carry == 1 or added == False:
                target = ans[index]
                if not added:
                    tmp = target + num + carry
                    added = True
                else:
                    tmp = target + carry
                carry = 1 if tmp >= 10 else 0
                ans[index] = tmp % 10
                index -= 1

        m, n = len(num1), len(num2)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                a, b = int(num1[i]), int(num2[j])
                result = a * b
                low, high = result % 10, result // 10
                addUnit(i + j + 1, low)
                addUnit(i + j, high)
        
        while ans[0] == 0 and len(ans) > 1:
            ans.pop(0)
        return ''.join(str(i) for i in ans)
                

print(Solution().multiply('123', '456'))
print(Solution().multiply('0', '0'))