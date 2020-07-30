# 匹配子序列的单词数
# medium
'''
给定字符串 S 和单词字典 words, 求 words[i] 中是 S 的子序列的单词个数。

示例:
输入: 
S = "abcde"
words = ["a", "bb", "acd", "ace"]
输出: 3
解释: 有三个是 S 的子序列的单词: "a", "acd", "ace"。
注意:

所有在words和 S 里的单词都只由小写字母组成。
S 的长度在 [1, 50000]。
words 的长度在 [1, 5000]。
words[i]的长度在[1, 50]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-matching-subsequences
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

-------------------------------------
题解：字典

遍历words，做个以 word 首字母为 key 的字典，如上例 dict: {'a': ['a', 'acd', 'ace'], 'b': ['bb']}
当遍历 S 的时候，根据当前字母更新 dict，如上面的 S 首字母 'a'，更新后的 dict 为 {'b': ['bb'], 'c': ['cd', 'ce']}
原 dict['a'] 中的单词 'a' 因为被削没了，此时 count+=1, 最终返回 count 即可

'''


class Solution:
    def numMatchingSubseq(self, S: str, words) -> int:
        dict = {}
        count = 0
        for word in words:
            key = word[0]
            if dict.get(key) == None:
                dict[key] = [word]
            else:
                dict[key].append(word)
        for ch in S:
            if dict.get(ch) != None:
                tmp = []
                while len(dict[ch]) > 0:
                    word = dict[ch].pop(0)
                    newWord = word[1:]
                    if not newWord:
                        count += 1
                    else:
                        key = newWord[0]
                        if key == ch:
                            tmp.append(newWord)
                        else:
                            if dict.get(key) == None:
                                dict[key] = [newWord]
                            else:
                                dict[key].append(newWord)
                if len(tmp) > 0:
                    dict[ch] = tmp
                else:
                    del dict[ch]
        return count
                        

print(Solution().numMatchingSubseq("abcde", ["a", "bb", "acd", "ace"]))