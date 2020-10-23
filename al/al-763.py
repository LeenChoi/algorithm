# 划分字母区间
# medium
'''
字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一个字母只会出现在其中的一个片段。返回一个表示每个字符串片段的长度的列表。 

示例 1：

输入：S = "ababcbacadefegdehijhklij"
输出：[9,7,8]
解释：
划分结果为 "ababcbaca", "defegde", "hijhklij"。
每个字母最多出现在一个片段中。
像 "ababcbacadefegde", "hijhklij" 的划分是错误的，因为划分的片段数较少。
 

提示：

S的长度在[1, 500]之间。
S只包含小写字母 'a' 到 'z' 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/partition-labels
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

--------------------------------------------------------
题解：

'''

# 朴素算法
class Solution:
    def partitionLabels(self, S: str):
        i, j, mid = 0, len(S) - 1, None
        ans = []
        while i < len(S):
            while mid == None or i < mid:
                if S[j] != S[i] and (mid == None or j > mid):
                    j -= 1
                else:
                    mid = j
                    i += 1
                    j = len(S) - 1
            
            if len(ans) == 0:
                ans.append(mid + 1)
            else:
                ans.append(mid - sum(ans) + 1)
            i = mid + 1
            j = len(S) - 1
            mid = None
        return ans


# 贪心
class Solution2:
    def partitionLabels(self, S: str):
        last = [0] * 26
        ans = []
        for i in range(len(S)):
            last[ord(S[i]) - ord('a')] = i
        start = end = 0
        for i in range(len(S)):
            end = max(end, last[ord(S[i]) - ord('a')])
            if i == end:
                ans.append(end - start + 1)
                start = end + 1
        return ans



print(Solution2().partitionLabels('ababcbacadefegdehijhklij'))
# print(Solution().partitionLabels('caedbdedda'))