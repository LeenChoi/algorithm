# 验证回文串
# easy
'''
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true
示例 2:

输入: "race a car"
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-palindrome
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        S = ''
        for i in range(len(s)):
            asc = ord(s[i])
            if asc >= 48 and asc <= 57 or \
                asc >= 97 and asc <= 122 or \
                asc >= 65 and asc <= 90:
                if asc >= 65 and asc <= 90:
                    asc += 32
                S += chr(asc)
        i, j = 0, len(S) - 1
        while i < j:
            if S[i] != S[j]:
                return False
            i += 1
            j -= 1
        return True

class SolutionV2:
    def isPalindrome(self, s):
        i, j = 0, len(s) - 1
        while i < j:
            chri = validChr(s[i])
            if not chri:
                i += 1
                continue
            chrj = validChr(s[j])
            if not chrj:
                j -= 1
                continue
            if chri != chrj:
                return False
            i += 1
            j -= 1
        return True

def validChr(ch):
    asc = ord(ch)
    if asc >= 48 and asc <= 57 or \
        asc >= 97 and asc <= 122 or \
        asc >= 65 and asc <= 90:
        if asc >= 65 and asc <= 90:
            asc += 32
        return chr(asc)
    return None
    
print(SolutionV2().isPalindrome("A man, a plan, a canal: Panama"))