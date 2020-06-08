# 寻找重复数
# medium

'''
给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。

示例 1:
输入: [1,3,4,2,2]
输出: 2

示例 2:
输入: [3,1,3,4,2]
输出: 3

说明：
不能更改原数组（假设数组是只读的）。
只能使用额外的 O(1) 的空间。
时间复杂度小于 O(n2) 。
数组中只有一个重复的数字，但它可能不止重复出现一次。

--------------------------------------
题解：快慢指针 O(n)
将数组的 index 和他的值连通，就可以形成一个简单的有向图，如果数组有重复的元素，表明一定会有多个指针指向同一个元素
那么这个题就退化成了 寻找链表里的环。所以快慢指针就解决了问题。

但快慢指针只能找出一个链表是否有环，那怎么找到环的入口呢 (即本题的重复数字)，只需在快慢指针发生碰撞后，将满指针归零
然后两个指针相同步调向前走，那么一定会在入口处相遇，为什么？

假定从开始到环入口的距离为 a，快慢指针发生碰撞的地方距离环入口的距离为 b，从 b 绕一圈再到入口处的距离为 c，环一圈长度为 l
则： 2(a + b) = a + b + kl
=>  a + b = kl
=>  a = kl - b
=>  a = (k - 1)l + l - b

l - b 为 c，(k - 1)l 是转了好几圈，可以忽略，所以最终等式为 a = c
所以在快慢指针相遇处 B，只需将慢指针归0，然后两个指针步调一致，那么最终一定会再入口处相遇


'''

class Solution:
    def findDuplicate(self, nums) -> int:
        slow, fast = 0, 0
        find = False
        while True:
            if find and slow == fast:
                return fast

            slow = nums[slow]
            fast = nums[fast]
            if not find:
                fast = nums[fast]

            if not find and slow == fast:
                slow = 0
                find = True
            

    
print(Solution().findDuplicate([1,3,4,2,2]))
print(Solution().findDuplicate([3,1,3,4,2]))
print(Solution().findDuplicate([1,4,4,2,4]))