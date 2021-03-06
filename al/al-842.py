# 将数组拆分成斐波那契序列
# medium
'''
给定一个数字字符串 S，比如 S = "123456579"，我们可以将它分成斐波那契式的序列 [123, 456, 579]。

形式上，斐波那契式序列是一个非负整数列表 F，且满足：

0 <= F[i] <= 2^31 - 1，（也就是说，每个整数都符合 32 位有符号整数类型）；
F.length >= 3；
对于所有的0 <= i < F.length - 2，都有 F[i] + F[i+1] = F[i+2] 成立。
另外，请注意，将字符串拆分成小块时，每个块的数字一定不要以零开头，除非这个块是数字 0 本身。

返回从 S 拆分出来的任意一组斐波那契式的序列块，如果不能拆分则返回 []。

 

示例 1：

输入："123456579"
输出：[123,456,579]
示例 2：

输入: "11235813"
输出: [1,1,2,3,5,8,13]
示例 3：

输入: "112358130"
输出: []
解释: 这项任务无法完成。
示例 4：

输入："0123"
输出：[]
解释：每个块的数字不能以零开头，因此 "01"，"2"，"3" 不是有效答案。
示例 5：

输入: "1101111"
输出: [110, 1, 111]
解释: 输出 [11,0,11,11] 也同样被接受。
 

提示：

1 <= S.length <= 200
字符串 S 中只含有数字。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/split-array-into-fibonacci-sequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

----------------------------------------------------------
题解：回溯
回溯过程就是，遍历字符串转成数字进队列，开始时候是个位数进队列，队列长度小于2时，直接进队列，大于等于2时需要判断斐波那契规则，
满足则继续进队列，不满足则需要回溯，把原来的个位数增长至两位数(以此类推)加进队列继续。最终整个字符串遍历完，且满足斐波那契规则，
判断队列长度是否大于等于3，结束。

注意：需要判断每次字符串转数字的时候，'0'打头的多位数要直接跳过，因为不满足题意。再就是转成数字后判断下是否大于 2**31-1

'''


class Solution:
    def splitIntoFibonacci(self, S: str):
        ans = []
        def backstrack(index):
            if index == len(S):
                return len(ans) >= 3
            curNum = 0
            print(ans)
            for i in range(index, len(S)):
                if i > index and S[index] == '0':
                    return False
                curNum = curNum * 10 + int(S[i])
                if curNum > 2 ** 31 - 1:
                    return False
                if len(ans) < 2 or ans[-2] + ans[-1] == curNum:
                    ans.append(curNum)
                    if backstrack(i + 1):
                        return True
                    ans.pop()
                elif ans[-2] + ans[-1] < curNum:
                    return False
        backstrack(0)
        return ans


print(Solution().splitIntoFibonacci("123456579"))    
                    
                
                
            