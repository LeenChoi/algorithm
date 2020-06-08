# LRU缓存机制
# medium
'''
运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。

获取数据 get(key) - 如果关键字 (key) 存在于缓存中，则获取关键字的值（总是正数），否则返回 -1。
写入数据 put(key, value) - 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字/值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。

进阶:

你是否可以在 O(1) 时间复杂度内完成这两种操作？


示例:

LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // 返回  1
cache.put(3, 3);    // 该操作会使得关键字 2 作废
cache.get(2);       // 返回 -1 (未找到)
cache.put(4, 4);    // 该操作会使得关键字 1 作废
cache.get(1);       // 返回 -1 (未找到)
cache.get(3);       // 返回  3
cache.get(4);       // 返回  4

'''
class LRUNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.pre = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.size = 0

        self.head = LRUNode(-1, None)
        self.tail = LRUNode(-2, None)
        self.head.next = self.tail
        self.tail.pre = self.head


    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.moveToHead(node)
            return node.value
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)
        else:
            self.setNewToHead(key, value)
        if self.size > self.capacity:
            self.removeTail()

    def setNewToHead(self, key, value):
        node = LRUNode(key, value)

        node.next = self.head.next
        node.next.pre = node

        self.head.next = node
        node.pre = self.head

        self.cache[key] = node
        self.size += 1

    def moveToHead(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre

        node.next = self.head.next
        node.next.pre = node

        self.head.next = node
        node.pre = self.head


    def removeTail(self):
        tailNode = self.tail.pre
        tailNode.pre.next = self.tail
        self.tail.pre = tailNode.pre
        
        tailNode.next = None
        tailNode.pre = None
        self.cache.pop(tailNode.key)
        self.size -= 1


cache = LRUCache(2)

cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))
cache.put(3, 3)
print(cache.get(2))
cache.put(4, 4)
print(cache.get(1))
print(cache.get(3))
print(cache.get(4))



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)