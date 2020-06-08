# 有效的括号字符串
'''
给定一个只包含三种字符的字符串：（ ，） 和 *，写一个函数来检验这个字符串是否为有效字符串。有效字符串具有如下规则：

任何左括号 ( 必须有相应的右括号 )。
任何右括号 ) 必须有相应的左括号 ( 。
左括号 ( 必须在对应的右括号之前 )。
* 可以被视为单个右括号 ) ，或单个左括号 ( ，或一个空字符串。
一个空字符串也被视为有效字符串。

----------------------------------------
题解：双栈
    一个记录 '(' 的index， 一个记录 '*' 的index，碰到 ')' 优先出'('栈，如果没有就出 '*'栈，
    如果都没有那就不可能是有效字符串。另外需要记录一个 '('的游标，作用是记录与'*'的配对情况，
    起初游标指向  '('栈底，当 '*'入栈时，比较下该 '*'的 index 和 游标的 index，如果 '*'更大，说明能配对，游标上移，等下一个'*'/')'
    当碰到 ')' 的时候，如果和 '(' 配对，判断下出栈的元素是否是游标所指的（说明游标已经是栈顶了，到目前为止已遍历的字符串是有效的），如果是的话游标自然下移，
    如果和 '*' 配对，那么原来和 '(' 配对的 '*' 就减少了，所以游标下移(要判下游标是否在栈底)，最后判游标是否在栈顶，和 '(', '*' 的数量即可

'''


class Solution:
    def checkValidString(self, s: str) -> bool:
        a, b = [], []
        l = 0
        for i in range(0, len(s)):
            k = s[i]
            if k == '(':
                a.append(i)
            if k == ')':
                if len(a) > 0:
                    a.pop()
                    if l >= len(a):
                        l = len(a) - 1
                elif len(b) > 0:
                    b.pop()
                    if l > 0:
                        l -= 1
                else:
                    return False
            if k == '*':
                b.append(i)
                if len(a) > l + 1 and a[l] < i:
                    l += 1

        if len(b) >= len(a) and l >= len(a) - 1:
            return True
        else:
            return False


S = input()
solution = Solution()
res = solution.checkValidString(S)
print(res)
