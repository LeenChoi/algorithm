# 恢复空格
# medium
'''
哦，不！你不小心把一个长篇文章中的空格、标点都删掉了，并且大写也弄成了小写。
像句子"I reset the computer. It still didn’t boot!"已经变成了"iresetthecomputeritstilldidntboot"。
在处理标点符号和大小写之前，你得先把它断成词语。当然了，你有一本厚厚的词典dictionary，不过，有些词没在词典里。
假设文章用sentence表示，设计一个算法，把文章断开，要求未识别的字符最少，返回未识别的字符数。

注意：本题相对原题稍作改动，只需返回未识别的字符数

示例：

输入：
dictionary = ["looked","just","like","her","brother"]
sentence = "jesslookedjustliketimherbrother"
输出： 7
解释： 断句后为"jess looked just like tim her brother"，共7个未识别字符。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/re-space-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

--------------------------------------
题解：动态规划 + trie字典树，字典树 + 递归 + map
trie树生成，遍历字典将每个单词倒序存入trie树
动态规划过程，顺序遍历sentence，如果当前字母不匹配，则 dp[i] = dp[i-1] + 1
当遍历到某个词语的最后一个字母时，通过字典树往回找完整的单词，找到这个单词的开头位置 j，dp[i] = dp[j-1]

因为遍历trie树的一条链找词语的时候，一条链可能有几个单词，如果sentence找词语的时候能和 trie 树的这条链的每个单词都能匹配上
那么就要看看每个单词匹配后更新的 dp[i] 哪个更小，所以dp[i] = min(dp[i], dp[j-1])

上面的dp是反向更新，我最开始做dp是正向更新，trie树正向存每个单词，dp时遇到某个单词的开头就通过trie树找到这个开头字母可能的所有单词的结尾位置 j
然后将每个结尾 j 位置的 dp 值置为 dp[i-1]，感觉逻辑没错，但不知为啥就卡在一个用例上，结果死活不对

官方提示给的用递归做，通过trie树 找到从某个字母开头的可能的所有单词的结尾位置处，分别做同样的递归，递归结果返回本次递归统计的无效字符数
但有可能会产生很多重复的递归，而且是爆炸式的，所以需要个map记录每个递归后的结果，之后出现重复递归，直接读map表取数据即可
但是这个方法我失败了，失败代码删掉了。。。

'''

class SolutionV2:
    def respace(self, dictionary, sentence):
        trie = Trie()
        for word in dictionary:
            trie.add(word)
        dp = [None] * (len(sentence) + 1)
        dp[0] = 0
        for i in range(len(sentence)):
            ends = trie.search(sentence, i)
            if len(ends) > 0:
                for end in ends:
                    dp[i + 1] = dp[i] + 1 
                    dp[end + 1] = dp[i] if dp[end + 1] == None else min(dp[end + 1], dp[i])
            else:
                dp[i + 1] = dp[i] + 1 if dp[i + 1] == None else min(dp[i] + 1, dp[i + 1])
        print(dp)
        return dp[-1]


class SolutionV3:
    def respace(self, dictionary, sentence):
        trie = Trie2()
        for word in dictionary:
            trie.add(word)
        dp = [0] * (len(sentence) + 1)
        # dp[0] = 0
        for i in range(len(sentence)):
            dp[i + 1] = dp[i] + 1
            ends = trie.search(sentence, i)
            for j in ends:
                dp[i + 1] = min(dp[j], dp[i + 1])
        print(dp)
        return dp[-1]


class TrieNode:
    def __init__(self, val, isEnd = False):
        self.val = val
        self.children = []
        self.end = isEnd
    
    def addChild(self, node):
        self.children.append(node)

    def findChild(self, val):
        for node in self.children:
            if node.val == val:
                return node
        return None


class Trie:
    def __init__(self):
        self.root = TrieNode(None, False)
    
    def add(self, word):
        parent = self.root
        for i in range(len(word)):
            node = parent.findChild(word[i])
            if not node:
                node = TrieNode(word[i])
                parent.addChild(node)
            if i == len(word) - 1:
                node.end = True
            parent = node

    def search(self, str, i):
        parent = self.root
        ret = []
        while i < len(str):
            node = parent.findChild(str[i])
            if not node:
                break
            if node.end:
                ret.append(i)
            i += 1
            parent = node
        return ret
                

class Trie2:
    def __init__(self):
        self.root = TrieNode(None, False)
    
    def add(self, word):
        parent = self.root
        for i in range(len(word) -1, -1, -1):
            node = parent.findChild(word[i])
            if not node:
                node = TrieNode(word[i])
                parent.addChild(node)
            if i == 0:
                node.end = True
            parent = node

    def search(self, str, i):
        parent = self.root
        ret = []
        while i >= 0:
            node = parent.findChild(str[i])
            if not node:
                break
            if node.end:
                ret.append(i)
            i -= 1
            parent = node
        return ret

def printTrie(parent, n):
    ret = [n]
    for node in parent.children:
        ret.append([node.val, node.end])
        printTrie(node, n + 1)
    print(ret)

    

    

print(SolutionV3().respace(["looked","just","like","her","brother"], 'jesslookedjustliketimherbrother'))
# print(SolutionV2().respace(["ouf","uucuocucoouoffcpuuf","pf","o","fofopupoufuofffffocpocfccuofuupupcouocpocoooupcuu","cf","cffooccccuoocpfupuucufoocpocucpuouofffpoupu","opoffuoofpupcpfouoouufpcuocufo","fopuupco","upocfucuucfucofufu","ufoccopopuouccupooc","fffu","uuopuccfocopooupooucfoufop","occ","ppfcuu","o","fpp","o","oououpuccuppuococcpoucccffcpcucoffupcoppoc","ufc","coupo","ufuoufofopcpfoufoouppffofffuupfco","focfcfcfcfpuouoccupfccfpcooup","ffupfffccpffufuuo","cufoupupppocou","upopupopccffuofpcopouofpoffopcfcuooocppofofuuc","oo","pccc","oupupcccppuuucuuouocu","fuop","ppuocfuppff","focofooffpfcpcupupuuooufu","uofupoocpf","opufcuffopcpcfcufpcpufuupffpp","f","opffp","fpccopc"], "fofopupoufuofffffocpocfccuofuupupcouocpocoooupcuufffufffufpccopc"))
print(SolutionV3().respace(["ouf","uucuocucoouoffcpuuf","pf","o","fofopupoufuofffffocpocfccuofuupupcouocpocoooupcuu","cf","cffooccccuoocpfupuucufoocpocucpuouofffpoupu","opoffuoofpupcpfouoouufpcuocufo","fopuupco","upocfucuucfucofufu","ufoccopopuouccupooc","fffu","uuopuccfocopooupooucfoufop","occ","ppfcuu","o","fpp","o","oououpuccuppuococcpoucccffcpcucoffupcoppoc","ufc","coupo","ufuoufofopcpfoufoouppffofffuupfco","focfcfcfcfpuouoccupfccfpcooup","ffupfffccpffufuuo","cufoupupppocou","upopupopccffuofpcopouofpoffopcfcuooocppofofuuc","oo","pccc","oupupcccppuuucuuouocu","fuop","ppuocfuppff","focofooffpfcpcupupuuooufu","uofupoocpf","opufcuffopcpcfcufpcpufuupffpp","f","opffp","fpccopc"], "fofopupoufuofffffocpocfccuofuupupcouocpocoooupcuufffufffufpccopc"))
# print(SolutionV3().respace(["sssjjs","hschjf","hhh","fhjchfcfshhfjhs","sfh","jsf","cjschjfscscscsfjcjfcfcfh","hccccjjfchcffjjshccsjscsc","chcfjcsshjj","jh","h","f","s","jcshs","jfjssjhsscfc"], "sssjjssfshscfjjshsjjsjchffffs"))
# print(SolutionV3().respace(["tttttt","ttttttttttt","ttt","ttttttttttttttt","tttttttttttttttt","t","ttttttttttttttttttttttttttttttttttttttttttttttttttt","t","ttttttt","ttttttttt","ttttttttt","tttt","tttttttttt","tttt","ttttttttttttttttttttttttttttttttt","t"], "tttttttttttttttttttttttttttttttttttttttttttt"))
# print(SolutionV3().respace(["bt","vbtbvtvvbbvtbvvbbbvbtbbv","bvvbbbvvvbvttbtbvtvtvvbttbbbtvvvb","btttbvbbbtbbtbvvttbvbvtvbtbbttb","bt","vvbvbvbvtbvbvvvvtv","tbvvvtttvtbvbtttvvbtvvvvtvvbvvtvvbbvbbbvb","v","bvb","vvtbvtvbttbttvvbvttbt","btbtbtttvbbtbttbtvvttbvtbtvtbvvtbbbb","bttbvbbttvvbtvvvvb","bvvbvbvttbvtbvvtbttvvvvtvbtvbttbbvvtvtvv","vbtttt","btbvbbbvbtvtbvvv","b","tbtbtv","vbvbbvvbvbbvvb","vbvvtvbvbvbttvbvbtvbtbtvtbvbbtb","bvvbvvttttttbtvvvttvbvtvvbvtbtvtbvttvvtbt","bvtbttv","bbbt","vtt","ttvv","b","vbb","vtvvbtttvtbbvvbbtbb","vvv","vvvvbbbtbbbvbbbb","ttvvbtvv","v","btvbbvtbbvbvtvttvvbbbtbvvvtbtb","vv","btbttbtbbvbvvbvttbttvtbbtbvtttvbbtbbtvtvvvvbbttvtvvbbbv","ttvbbbbttbtbtb","tvvbvbvvb","vv","ttbttvtvbtbbbbv","bvvvtbbvvvbtvbvtvtvvvvbb","vtbvvbvvvvvttvbbttbbvtvt","tbvbbt","b","v","tvbbtvvtvvtbtbttvvvb","tbttbttbbbtbtvtvtvtbbbvvtbbbvbbvvvbbttvvt","bbvttvtvvtbvbbttvbbtbvvttbvbvbtbvvvbbbvbvbvbtvbtvvvtvvtbttbttbbvbbbttvvvbvvtb","vttvvbvv","tbttbvvttvbtvvtbbvvv","bvbbbbbbbb","vtbvvtbbvtt","bvttbvvbvb","tvttttbbvvvbbtttvvv"], "btbvtttttbvttbvvbbtvvbvbvvbtbtbtvbtttbvbbbtbbtbvvttbvbvtvbtbbttbvvbvbtttbvttbvvbbvvv"))
print(SolutionV3().respace(["axxpxakkxktpa","aappk","kddxxp","p","atxtdtpkt","ptxkatdakp","padpatxaptpaatkadaxka","xd","xa","kptkaxxpptpkxaxtx","t","atdxkttpppakkxkxpxdxxapakaadaxkakapxptdpkxkaadtx","kp","xa","pkkataxkakkxxktxxdptatkkxta","dxttapxpxkxttkktpkx","tat","txpdakdxpaa","axxkaxkxkkkdpkpttxdkpaaakkakdkkdxatd","paxaa"], "ppkaxpxddkpaatttxtpdtaxtadxaxatxtdtpktdxpppkaxpxddkpaatttxtpdtaxtadx"))


'ppkaxpxddkpaatttxtpdtaxtadxaxatxtdtpktdxpppkaxpxddkpaatttxtpdtaxtadx'