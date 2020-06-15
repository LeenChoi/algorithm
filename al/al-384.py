# 打乱数组
# medium
'''
打乱一个没有重复元素的数组。

示例:
// 以数字集合 1, 2 和 3 初始化数组。
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// 打乱数组 [1,2,3] 并返回结果。任何 [1,2,3]的排列返回的概率应该相同。
solution.shuffle();

// 重设数组到它的初始状态[1,2,3]。
solution.reset();

// 随机返回数组[1,2,3]打乱后的结果。
solution.shuffle();

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shuffle-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

-------------------------------
题解: Fisher-Yates 洗牌算法 
    随机下标，交换元素

'''


import math
import random
class Solution:
    def __init__(self, nums: List[int]):
        self.origin = nums
        self.nums = list(nums)
        

    def reset(self) -> List[int]:
        self.nums = list(self.origin)
        return self.nums
        

    def shuffle(self) -> List[int]:
        length = len(self.nums)
        for i in range(0, length - 1):
            index = random.randrange(i, length)
            if index != i:
                self.nums[i], self.nums[index] = self.nums[index], self.nums[i]
        return self.nums
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()