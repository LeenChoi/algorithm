# 模式匹配
# medium
'''
你有两个字符串，即pattern和value。 pattern字符串由字母"a"和"b"组成，用于描述字符串中的模式。例如，字符串"catcatgocatgo"匹配模式"aabab"（其中"cat"是"a"，"go"是"b"），该字符串也匹配像"a"、"ab"和"b"这样的模式。但需注意"a"和"b"不能同时表示相同的字符串。编写一个方法判断value字符串是否匹配pattern字符串。

示例 1：

输入： pattern = "abba", value = "dogcatcatdog"
输出： true
示例 2：

输入： pattern = "abba", value = "dogcatcatfish"
输出： false
示例 3：

输入： pattern = "aaaa", value = "dogcatcatdog"
输出： false
示例 4：

输入： pattern = "abba", value = "dogdogdogdog"
输出： true
解释： "a"="dogdog",b=""，反之也符合规则
提示：

0 <= len(pattern) <= 1000
0 <= len(value) <= 1000
你可以假设pattern只包含字母"a"和"b"，value仅包含小写字母。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/pattern-matching-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

-------------------------------------------
题解: 枚举
思路很惊奇，开始我起手就想 value 怎么拆分相同单词出来，但这题重点思路是通过 pattern 去匹配 value 的单词，
匹配的方法其实就是最笨的方法（有时又是最有效的方法），'abba' 假设 a 单词的长度是 [0,1,2,3,...]，那么去算 b 应该是长度为几的单词，然后去 value 上一个一个找去

那么整体的思路就是，先找出来 pattern 里 a 有多少个，然后假设 a 的长度是 la = [0,1,2,...,len(value)/counta]
然后求 b 应该的长度，lb = (len(value) - la * counta) / countb，剩下的就是在 value 里挨个匹配 a、b 串了

但这题恶心在有很多细节：
    1. pattern = '' 时，什么都匹配不了，除了 value 也等于 ''
    2. value = '' 时，pattern = '' 是可以匹配的，pattern 为任一个 a 时也可以匹配，因为 a 可以是空字符
        但 pattern a、b 同时存在时不可以匹配，因为 a、b 本身是不可以相同的
    3. 如果 a 的个数少于 b，那么 pattern 调个个儿，仅仅是为了逻辑上简洁，不然如果 a、b 某一个为 0 个的时候还得另外再判断
        a 为 0 个的时候，算法还要写成从枚举 b 开始，所以这一步比较重要，能避免饶进逻辑深坑


* 这题还有个解法，递归回溯，但担忧是否会超时，就没有去深挖。后来在题解里看到有人说可行，可以试试

'''


class Solution:
    def patternMatching(self, pattern: str, value: str) -> bool:
        counta = sum(1 for ch in pattern if ch == 'a')
        countb = len(pattern) - counta
        if counta < countb: # 如果b个数比a多，那就调个个儿，只是为了代码能简洁点
            counta, countb = countb, counta
            pattern = ''.join('b' if ch == 'a' else 'a' for ch in pattern)

        if pattern == '' and len(value) > 0: # patten为空，只要value也不为空，那就一定匹配不了
            return False
        if value == '': # value为空，看看b的个数是否是0就ok，因为patten = 'aaaaaa'的情况，a可以是空字符，是可以匹配的
            return countb == 0

        # 按a串的长度开始遍历，a可能的长度为[0, len(value) // counta]
        for i in range(0, (len(value) // counta) + 1):
            lengtha = i
            if countb == 0: # countb如果是0，无法除，a的长度那只能就是len(value) // counta
                if lengtha != len(value) // counta:
                    continue
            else:
                if (len(value) - lengtha * counta) % countb > 0: # a长度取完剩下的字符串可能除以countb得不到整数，那么这个一定匹配不了
                    continue
                lengthb = (len(value) - lengtha * counta) // countb

            pos = 0
            worda, wordb = None, None
            success = True
            # 遍历pattern顺序取a串，b串，每再次取到a串，b串时判断下和第一回取到的是否相同，不相同则匹配失败
            for ch in pattern:
                if ch == 'a':
                    word = value[pos:pos + lengtha]
                    if worda == None:
                        worda = word
                    elif worda != word:
                        success = False
                        break
                    pos = pos + lengtha
                else:
                    word = value[pos:pos + lengthb]
                    if wordb == None:
                        wordb = word
                    elif wordb != word:
                        success = False
                        break
                    pos = pos + lengthb
            if success and worda != wordb and pos >= len(value): # 注意判下a串b串可能会相同，还有判下有没有走到最后
                return True
        return False

print(Solution().patternMatching("bbbbbbbbbbbb", "xxxxxxy"))
# print(Solution().patternMatching('aaaa', 'catcatcatcat'))
# print(Solution().patternMatching('abba', 'dogcatcatfish'))

                    