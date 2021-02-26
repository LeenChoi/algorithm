// 猜字谜
// hard
/*
* 外国友人仿照中国字谜设计了一个英文版猜字谜小游戏，请你来猜猜看吧。
*
* 字谜的迷面 puzzle 按字符串形式给出，如果一个单词 word 符合下面两个条件，那么它就可以算作谜底：
*
* 单词 word 中包含谜面 puzzle 的第一个字母。
* 单词 word 中的每一个字母都可以在谜面 puzzle 中找到。
* 例如，如果字谜的谜面是 "abcdefg"，那么可以作为谜底的单词有 "faced", "cabbage", 和 "baggage"；而 "beefed"（不含字母 "a"）以及 "based"（其中的 "s" 没有出现在谜面中）。
* 返回一个答案数组 answer，数组中的每个元素 answer[i] 是在给出的单词列表 words 中可以作为字谜迷面 puzzles[i] 所对应的谜底的单词数目。
*
*
*
* 示例：
*
* 输入：
* words = ["aaaa","asas","able","ability","actt","actor","access"],
* puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]
* 输出：[1,1,3,2,4,0]
* 解释：
* 1 个单词可以作为 "aboveyz" 的谜底 : "aaaa"
* 1 个单词可以作为 "abrodyz" 的谜底 : "aaaa"
* 3 个单词可以作为 "abslute" 的谜底 : "aaaa", "asas", "able"
* 2 个单词可以作为 "absoryz" 的谜底 : "aaaa", "asas"
* 4 个单词可以作为 "actresz" 的谜底 : "aaaa", "asas", "actt", "access"
* 没有单词可以作为 "gaswxyz" 的谜底，因为列表中的单词都不含字母 'g'。
*
*
* 提示：
*
* 1 <= words.length <= 10^5
* 4 <= words[i].length <= 50
* 1 <= puzzles.length <= 10^4
* puzzles[i].length == 7
* words[i][j], puzzles[i][j] 都是小写英文字母。
* 每个 puzzles[i] 所包含的字符都不重复。
*
* 来源：力扣（LeetCode）
* 链接：https://leetcode-cn.com/problems/number-of-valid-words-for-each-puzzle
* 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*
* --------------------------------------------------------------------
* 题解：位运算+哈希，字典树
* 做一个哈希表 wordCnt，key 是 word 按字母顺位转成的二进制数，value 是 count 值，因为可能不同 word 拥有相同的字母集
* 然后遍历 puzzles，将每个 puzzle 也转成二进制数，再得到它的所有子集，然后判断 wordCnt 里有没有这个 key，
* 如果有，那么就将对应 wordCnt 里的值累加。
*
* 这里 puzzle 的二进制转换，不用把所有字母都算进去，因为根据题意 puzzle 的第一个字母必须包含。
* 所以只从第二个字母开始转成二进制即可，然后比较的时候再将第一个字母的二进制位加进去比较。
* 那么现在的问题就是怎么找子集？有个非常巧妙方法，subset = (subset - 1) & oriMask，将当前子集与原始二进制做 & 操作
* 就能得到下一个子集，直到 subset == 0，能得到全部子集。这里需要注意的是 0 子集也需要比较，因为有第一个字母的存在。
*
 */

package main

import "fmt"

func main() {
	words := []string{"aaaa", "asas", "able", "ability", "actt", "actor", "access"}
	puzzles := []string{"aboveyz", "abrodyz", "abslute", "absoryz", "actresz", "gaswxyz"}
	fmt.Println(findNumOfValidWords(words, puzzles))
}

func findNumOfValidWords(words []string, puzzles []string) []int {
	wordCnt := map[int]int{}
	for _, word := range words {
		mask := 0
		for _, ch := range word {
			mask |= 1 << (ch - 'a')
		}
		wordCnt[mask]++
	}

	ans := make([]int, len(puzzles))
	for i, puzzle := range puzzles {
		mask := 0
		for i := 1; i < len(puzzle); i++ {
			mask |= 1 << (puzzle[i] - 'a')
		}
		sub := mask
		first := 1 << (puzzle[0] - 'a')
		for {
			if cnt, exists := wordCnt[sub|first]; exists {
				ans[i] += cnt
			}
			sub = (sub - 1) & mask
			if sub == mask {
				break
			}
		}
	}
	return ans
}
