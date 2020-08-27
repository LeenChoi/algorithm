// 重新安排行程
// medium
/*
* 给定一个机票的字符串二维数组 [from, to]，子数组中的两个成员分别表示飞机出发和降落的机场地点，对该行程进行重新规划排序。所有这些机票都属于一个从 JFK（肯尼迪国际机场）出发的先生，所以该行程必须从 JFK 开始。
*
* 说明:
*
* 如果存在多种有效的行程，你可以按字符自然排序返回最小的行程组合。例如，行程 ["JFK", "LGA"] 与 ["JFK", "LGB"] 相比就更小，排序更靠前
* 所有的机场都用三个大写字母表示（机场代码）。
* 假定所有机票至少存在一种合理的行程。
* 示例 1:
*
* 输入: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
* 输出: ["JFK", "MUC", "LHR", "SFO", "SJC"]
* 示例 2:
*
* 输入: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
* 输出: ["JFK","ATL","JFK","SFO","ATL","SFO"]
* 解释: 另一种有效的行程是 ["JFK","SFO","ATL","JFK","ATL","SFO"]。但是它自然排序更大更靠后。
*
* 来源：力扣（LeetCode）
* 链接：https://leetcode-cn.com/problems/reconstruct-itinerary
* 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

-----------------------------------------------------
* 题解：Hierholzer 算法
* Hierholzer 用于连通图中寻找欧拉路径，过程如下: (一笔画过程)
* 1.从起点出发，进行深度优先搜索。
* 2.每次沿着某条边从某个顶点移动到另外一个顶点的时候，都需要删除这条边。
* 3.如果没有下一个可移动的路径，则将所在节点加入到栈中，并返回。
* 4.栈中节点倒序输出，就是从起点的欧拉路径
* 
* 此题要按自然排序返回最小的行程组合，所以构造图的时候，给每个节点的孩子节点排个序就行，然后dfs的时候顺序取排头的遍历
* 根据上面的第三步，入度和出度相差 1 的节点（死胡同）将第一个入栈，因为出度入度相同的节点遍历出去后又会重新遍历到自己，
* 只要还能遍历回到自己，那么肯定不是第一个入栈，除非是欧拉图，此题是欧拉半图。
* 
* 根据 3 步，自己的出边全部遍历完了，把自己入栈，在这之前，通过遍历孩子反复访问到自己，其实已经入栈过很多次了

*/

package main

import (
	"fmt"
	"sort"
)

func main() {
	para := [][]string{}
	// para = append(para, []string{"MUC", "LHR"})
	// para = append(para, []string{"JFK", "MUC"})
	// para = append(para, []string{"SFO", "SJC"})
	// para = append(para, []string{"LHR", "SFO"})

	para = append(para, []string{"JFK", "SFO"})
	para = append(para, []string{"JFK", "ATL"})
	para = append(para, []string{"SFO", "ATL"})
	para = append(para, []string{"ATL", "JFK"})
	para = append(para, []string{"ATL", "SFO"})

	// para = append(para, []string{"JFK", "KUL"})
	// para = append(para, []string{"JFK", "NRT"})
	// para = append(para, []string{"NRT", "JFK"})

	res := findItinerary(para)
	fmt.Println(res)
}

func findItinerary(tickets [][]string) []string {
	ticketsMap := make(map[string][]string)
	for i := 0; i < len(tickets); i++ {
		cur := tickets[i][0]
		next := tickets[i][1]
		if _, exists := ticketsMap[cur]; !exists {
			ticketsMap[cur] = []string{next}
		} else {
			ticketsMap[cur] = append(ticketsMap[cur], next)
		}
	}
	for key := range ticketsMap {
		sort.Strings(ticketsMap[key])
	}

	ans := []string{}
	var dfs func(station string)
	dfs = func(station string) {
		if _, ok := ticketsMap[station]; ok {
			for len(ticketsMap[station]) > 0 {
				next := ticketsMap[station][0]
				ticketsMap[station] = ticketsMap[station][1:]
				dfs(next)
			}
		}
		ans = append(ans, station)
	}
	dfs("JFK")
	for i := 0; i < len(ans)/2; i++ {
		ans[i], ans[len(ans)-1-i] = ans[len(ans)-1-i], ans[i]
	}

	return ans
}
