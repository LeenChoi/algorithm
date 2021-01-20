// 字母异位词分组
// medium
/*
* 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
*
* 示例:
*
* 输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
* 输出:
* [
*   ["ate","eat","tea"],
*   ["nat","tan"],
*   ["bat"]
* ]
* 说明：
*
* 所有输入均为小写字母。
* 不考虑答案输出的顺序。
*
* 来源：力扣（LeetCode）
* 链接：https://leetcode-cn.com/problems/group-anagrams
* 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*
* --------------------------------------------------
* 题解：哈希表
* 利用语言特性，python 和 go 都可以用数组当键。26个字母，做一个长度26的数组，记录每个单词中字符出现的次数，当做key，
* 将单词添加到这个 key 的数组里，最后扫一遍哈希表，将结果输出到数组里
 */

package main

import "fmt"

func main() {
	fmt.Println(groupAnagrams([]string{"eat", "tea", "tan", "ate", "nat", "bat"}))
}

func groupAnagrams(strs []string) [][]string {
	// !!! map key 为数组
	hm := map[[26]int][]string{}
	for _, str := range strs {
		key := [26]int{}
		for _, ch := range str {
			key[ch-'a'] += 1
		}
		hm[key] = append(hm[key], str)
	}
	ans := [][]string{}
	for _, arr := range hm {
		ans = append(ans, arr)
	}
	return ans
}

// python3
// class Solution:
//     def groupAnagrams(self, strs):
//         hm = collections.defaultdict(list)
//         for str in strs:
//             key = [0] * 26
//             for ch in str:
//                 offset = ord(ch) - ord('a')
//                 key[offset] += 1
//             hm[tuple(key)].append(str)
//         return list(hm.values())
