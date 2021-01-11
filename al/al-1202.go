// 交换字符串中的元素
// medium
/*
* 给你一个字符串 s，以及该字符串中的一些「索引对」数组 pairs，其中 pairs[i] = [a, b] 表示字符串中的两个索引（编号从 0 开始）。
*
* 你可以 任意多次交换 在 pairs 中任意一对索引处的字符。
*
* 返回在经过若干次交换后，s 可以变成的按字典序最小的字符串。
*
*
*
* 示例 1:
*
* 输入：s = "dcab", pairs = [[0,3],[1,2]]
* 输出："bacd"
* 解释：
* 交换 s[0] 和 s[3], s = "bcad"
* 交换 s[1] 和 s[2], s = "bacd"
* 示例 2：
*
* 输入：s = "dcab", pairs = [[0,3],[1,2],[0,2]]
* 输出："abcd"
* 解释：
* 交换 s[0] 和 s[3], s = "bcad"
* 交换 s[0] 和 s[2], s = "acbd"
* 交换 s[1] 和 s[2], s = "abcd"
* 示例 3：
*
* 输入：s = "cba", pairs = [[0,1],[1,2]]
* 输出："abc"
* 解释：
* 交换 s[0] 和 s[1], s = "bca"
* 交换 s[1] 和 s[2], s = "bac"
* 交换 s[0] 和 s[1], s = "abc"
*
*
* 提示：
*
* 1 <= s.length <= 10^5
* 0 <= pairs.length <= 10^5
* 0 <= pairs[i][0], pairs[i][1] < s.length
* s 中只含有小写英文字母
*
* 来源：力扣（LeetCode）
* 链接：https://leetcode-cn.com/problems/smallest-string-with-swaps
* 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*
* --------------------------------------------------------
* 题解：并查集
* 并查集找连通的字母，连通的字母之间可以随意互换，所以这些字母排个序，然后在他们的索引集里对号入座即可
 */

package main

import (
	"fmt"
	"sort"
)

func main() {
	s := "dcab"
	pairs := [][]int{{0, 3}, {1, 2}}
	fmt.Println(smallestStringWithSwaps(s, pairs))
}

func smallestStringWithSwaps(s string, pairs [][]int) string {

	fa := make([]int, len(s))
	for i := range fa {
		fa[i] = i
	}
	find := func(node int) int {
		n := node
		for fa[n] != n {
			n = fa[n]
		}
		if fa[node] != n {
			fa[node] = n
		}
		return n
	}
	merge := func(from, to int) {
		fFrom, fTo := find(from), find(to)
		if fFrom != fTo {
			if fFrom < fTo {
				fa[fTo] = fFrom
			} else {
				fa[fFrom] = fTo
			}
		}
	}

	for _, pair := range pairs {
		merge(pair[0], pair[1])
	}

	groups := map[int][]int{}
	for i := 0; i < len(s); i++ {
		f := find(i)
		groups[f] = append(groups[f], i)
	}
	ans := make([]byte, len(s))
	for _, arr := range groups {
		bytes := make([]byte, len(arr))
		for i := 0; i < len(arr); i++ {
			index := arr[i]
			bytes[i] = s[index]
		}
		// !!! sort by less function
		sort.Slice(bytes, func(i, j int) bool { return bytes[i] < bytes[j] })
		for i := 0; i < len(arr); i++ {
			index := arr[i]
			ans[index] = bytes[i]
		}
	}
	return string(ans)
}
