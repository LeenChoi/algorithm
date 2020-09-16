# 复原IP地址
# medium
'''
给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

有效的 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。

例如："0.1.2.201" 和 "192.168.1.1" 是 有效的 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效的 IP 地址。

 

示例 1：

输入：s = "25525511135"
输出：["255.255.11.135","255.255.111.35"]
示例 2：

输入：s = "0000"
输出：["0.0.0.0"]
示例 3：

输入：s = "1111"
输出：["1.1.1.1"]
示例 4：

输入：s = "010010"
输出：["0.10.0.10","0.100.1.0"]
示例 5：

输入：s = "101023"
输出：["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
 

提示：

0 <= s.length <= 3000
s 仅由数字组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/restore-ip-addresses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

------------------------------------------------------
题解：回溯
此题的回溯 +1-1 的选择是，加'.'还是不加，加'.'有条件，就是隔开的数字长度不能大于 3 并且数字不能大于255，
'.'后第一个数字如果是 0，那么必须 0 后加'.'

'''


class Solution:
    def restoreIpAddresses(self, s: str):
        ans, group = [], []
        n = len(s)
        def dfs(start, end):
            if len(group) == 4:
                if start < n or end < n:
                    return
                else:
                    ans.append('.'.join(group))
                    return
            if end >= n:
                return
            
            tmp = s[start : end + 1]
            if int(tmp) <= 255:
                group.append(tmp)
                dfs(end + 1, end + 1)
                group.pop()
            if tmp != '0' and end - start < 2:
                dfs(start, end + 1)
        dfs(0, 0)
        return ans


print(Solution().restoreIpAddresses('25525511135'))
print(Solution().restoreIpAddresses('101023'))

