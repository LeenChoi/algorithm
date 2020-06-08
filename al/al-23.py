# 合并K个排序链表
'''
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6

-----------------------------
题解：每个链表取头指针放到一个优先队列里(最小堆实现)，元素进入优先队列里时，已经把最小的放到了队列头
    所以直接遍历优先队列取队列头就可以，头元素出队列后将该链表的指针向后移，并且做堆平衡，直至把队列取空

    具体实现是，首先将所有链表的头指针入堆(siftup操作)，随即开始遍历取堆首(siftdown操作平衡堆)，
    之后堆首的链表指针后移，以便下一次迭代时候可以siftdown，直至将某一个链表取空，堆首返回None，
    此时堆首堆尾交换，再去尾， 堆排的思想

'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Heap:
    def __init__(self):
        self.queue = [0]

    def isEmpty(self):
        return len(self.queue) <= 1

    def push(self, node):
        self.queue.append(node)
        tail = len(self.queue) - 1
        self.siftup(tail)

    def shift(self):
        self.siftdown(1)

        node = None
        if not self.isEmpty():
            node = self.queue[1]
            self.queue[1] = self.queue[1].next
            if self.queue[1] == None:
                tail = len(self.queue) - 1
                self.queue[1], self.queue[tail] = self.queue[tail], self.queue[1]
                self.queue.pop(tail)
        
        return node

    def siftup(self, i):
        while i > 1:
            if self.queue[i // 2].val > self.queue[i].val:
                self.queue[i // 2], self.queue[i] = self.queue[i], self.queue[i // 2]
                i = i // 2
            else:
                break
        
    def siftdown(self, i):
        l = len(self.queue)
        if l <= 2:
            return

        tail = l - 1
        while i <= tail // 2:
            t = None
            if self.queue[i].val > self.queue[i * 2].val:
                t = i * 2
            else:
                t = i

            if i * 2 + 1 <= tail and self.queue[t].val > self.queue[i * 2 + 1].val:
                t = i * 2 + 1
            if t == i:
                break
            else:
                self.queue[i], self.queue[t] = self.queue[t], self.queue[i]
                i = t

    def output(self, str):
        array = []
        for i in range(1, len(self.queue)):
            array.append(self.queue[i].val)
        print(str, array)

class Solution:
    def mergeKLists(self, lists):
        heap = Heap()
        head, p = None, None
        for i in range(0, len(lists)):
            if lists[i]:
                heap.push(lists[i])

        while not heap.isEmpty():
            if p == None:
                p = heap.shift()
                head = p
            else:
                p.next = heap.shift()
                p = p.next
        
        return head


def init(nodelist):
    res = []
    for h in range(0, len(nodelist)):
        head, p = None, None
        array = nodelist[h]
        for i in range(0, len(array)):
            node = ListNode(array[i])
            if p == None:
                p = node
                head = p
            else:
                p.next = node
                p = p.next
        res.append(head)
    return res


inputs = init([[-9,-7,-7],[-6,-4,-1,1],[-6,-5,-2,0,0,1,2],[-9,-8,-6,-5,-4,1,2,4],[-10],[-5,2,3]])

def output(node):
    array = []
    p = node
    while p != None:
        array.append(p.val)
        p = p.next

    print(array)


solution = Solution()
res = solution.mergeKLists(inputs)
output(res)