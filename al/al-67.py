# 二进制求和
# easy
'''
给你两个二进制字符串，返回它们的和（用二进制表示）。

输入为 非空 字符串且只包含数字 1 和 0。

 

示例 1:

输入: a = "11", b = "1"
输出: "100"
示例 2:

输入: a = "1010", b = "1011"
输出: "10101"
 

提示：

每个字符串仅由字符 '0' 或 '1' 组成。
1 <= a.length, b.length <= 10^4
字符串如果不是 "0" ，就都不含前导零。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-binary
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry, ans = 0, ''
        i, j = len(a) - 1, len(b) - 1
        while i >= 0 or j >= 0:
            A = a[i] if i >= 0 else 0
            B = b[j] if j >= 0 else 0
            result = int(A) + int(B) + carry
            carry = 1 if result // 2 else 0
            result %= 2
            ans = str(result) + ans
            i -= 1
            j -= 1
        if carry:
            ans = '1' + ans
        return ans

print(Solution().addBinary('11', '1'))
        
