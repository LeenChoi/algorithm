// 账户合并
// medium
/*
* 给定一个列表 accounts，每个元素 accounts[i] 是一个字符串列表，其中第一个元素 accounts[i][0] 是 名称 (name)，其余元素是 emails 表示该账户的邮箱地址。
*
* 现在，我们想合并这些账户。如果两个账户都有一些共同的邮箱地址，则两个账户必定属于同一个人。请注意，即使两个账户具有相同的名称，它们也可能属于不同的人，因为人们可能具有相同的名称。一个人最初可以拥有任意数量的账户，但其所有账户都具有相同的名称。
*
* 合并账户后，按以下格式返回账户：每个账户的第一个元素是名称，其余元素是按顺序排列的邮箱地址。账户本身可以以任意顺序返回。
*
* 示例 1：
*
* 输入：
* accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
* 输出：
* [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
* 解释：
* 第一个和第三个 John 是同一个人，因为他们有共同的邮箱地址 "johnsmith@mail.com"。
* 第二个 John 和 Mary 是不同的人，因为他们的邮箱地址没有被其他帐户使用。
* 可以以任何顺序返回这些列表，例如答案 [['Mary'，'mary@mail.com']，['John'，'johnnybravo@mail.com']，
* ['John'，'john00@mail.com'，'john_newyork@mail.com'，'johnsmith@mail.com']] 也是正确的。
*
*
* 提示：
*
* accounts的长度将在[1，1000]的范围内。
* accounts[i]的长度将在[1，10]的范围内。
* accounts[i][j]的长度将在[1，30]的范围内。
*
* 来源：力扣（LeetCode）
* 链接：https://leetcode-cn.com/problems/accounts-merge
* 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*
* ------------------------------------------------------------------
* 题解：哈希 + 并查集
* 并查集记录每个集，然后哈希记录下每个mail对应的名字，为了最后答案的输出
*
 */

package main

import (
	"fmt"
	"sort"
)

func main() {
	accounts := [][]string{{"John", "johnsmith@mail.com", "john00@mail.com"}, {"John", "johnnybravo@mail.com"}, {"John", "johnsmith@mail.com", "john_newyork@mail.com"}, {"Mary", "mary@mail.com"}}
	fmt.Println(accountsMerge(accounts))
}

func accountsMerge(accounts [][]string) [][]string {
	fa := map[string]string{}
	names := map[string]string{}
	find := func(node string) string {
		if _, has := fa[node]; !has {
			fa[node] = node
		}
		pa := node
		for fa[pa] != pa {
			pa = fa[pa]
		}
		if fa[node] != pa {
			fa[node] = pa
		}
		return pa
	}

	union := func(from, to string) {
		fFrom, fTo := find(from), find(to)
		if fFrom != fTo {
			if fFrom < fTo {
				fa[fTo] = fFrom
			} else {
				fa[fFrom] = fTo
			}
		}
	}
	for _, account := range accounts {
		name := account[0]
		for i := 1; i < len(account); i++ {
			names[account[i]] = name
			union(account[1], account[i])
		}
	}
	group := map[string][]string{}
	for i := range fa {
		f := find(fa[i])
		group[f] = append(group[f], i)
	}
	ans := [][]string{}
	for i := range group {
		sort.Strings(group[i])
		tmp := []string{names[i]}
		tmp = append(tmp, group[i]...)
		ans = append(ans, tmp)
	}
	return ans
}
