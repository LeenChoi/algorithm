// 扁平化嵌套列表迭代器
// medium
/*
* 给你一个嵌套的整型列表。请你设计一个迭代器，使其能够遍历这个整型列表中的所有整数。
*
* 列表中的每一项或者为一个整数，或者是另一个列表。其中列表的元素也可能是整数或是其他列表。
*
* 示例 1:
*
* 输入: [[1,1],2,[1,1]]
* 输出: [1,1,2,1,1]
* 解释: 通过重复调用 next 直到 hasNext 返回 false，next 返回的元素的顺序应该是: [1,1,2,1,1]。
* 示例 2:
*
* 输入: [1,[4,[6]]]
* 输出: [1,4,6]
* 解释: 通过重复调用 next 直到 hasNext 返回 false，next 返回的元素的顺序应该是: [1,4,6]。
*
* 来源：力扣（LeetCode）
* 链接：https://leetcode-cn.com/problems/flatten-nested-list-iterator
* 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*
* ------------------------------------------------------------
* 题解：栈
* 做一个结构体，记录一个当前遍历到的某个list的指针，和这个list的游标。然后构建iterator的时候里面构建一个这个结构的栈。
* 遍历的时候如果当前碰到的不是int数，而是个list，那么将此list和它的游标一起入栈。
* 每次都优先遍历栈顶的list和游标即可，遍历完了就出栈，继续遍历栈顶。
 */

package main

func main() {

}

/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * type NestedInteger struct {
 * }
 *
 * // Return true if this NestedInteger holds a single integer, rather than a nested list.
 * func (this NestedInteger) IsInteger() bool {}
 *
 * // Return the single integer that this NestedInteger holds, if it holds a single integer
 * // The result is undefined if this NestedInteger holds a nested list
 * // So before calling this method, you should have a check
 * func (this NestedInteger) GetInteger() int {}
 *
 * // Set this NestedInteger to hold a single integer.
 * func (n *NestedInteger) SetInteger(value int) {}
 *
 * // Set this NestedInteger to hold a nested list and adds a nested integer to it.
 * func (this *NestedInteger) Add(elem NestedInteger) {}
 *
 * // Return the nested list that this NestedInteger holds, if it holds a nested list
 * // The list length is zero if this NestedInteger holds a single integer
 * // You can access NestedInteger's List element directly if you want to modify it
 * func (this NestedInteger) GetList() []*NestedInteger {}
 */

type iteratorPack struct {
	idx  int
	list []*NestedInteger
}

type NestedIterator struct {
	iter []*iteratorPack
}

func Constructor(nestedList []*NestedInteger) *NestedIterator {
	idx := -1
	list := nestedList
	iterPack := &iteratorPack{idx, list}
	iter := []*iteratorPack{iterPack}
	return &NestedIterator{iter}
}

func (this *NestedIterator) Next() int {
	iterPack := this.iter[len(this.iter)-1]
	return iterPack.list[iterPack.idx].GetInteger()

}

func (this *NestedIterator) HasNext() bool {
	for len(this.iter) > 0 {
		iterPack := this.iter[len(this.iter)-1]
		iterPack.idx++
		if iterPack.idx < len(iterPack.list) {
			if iterPack.list[iterPack.idx].IsInteger() {
				return true
			} else {
				list := iterPack.list[iterPack.idx].GetList()
				this.iter = append(this.iter, &iteratorPack{-1, list})
			}
		} else {
			this.iter = this.iter[:len(this.iter)-1]
		}
	}
	return false
}
