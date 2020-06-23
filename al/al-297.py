# 二叉树的序列化与反序列化
# hard
'''
序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。
请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。

示例: 

你可以将以下二叉树：

    1
   / \
  2   3
     / \
    4   5

序列化为 "[1,2,3,null,null,4,5]"
提示: 这与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。

说明: 不要使用类的成员 / 全局 / 静态变量来存储状态，你的序列化和反序列化算法应该是无状态的。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import json

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        seq, str = [root], []
        while len(seq) > 0:
            node = seq.pop(0)
            if node:
                str.append(node.val)
                if node.left != None:
                    seq.append(node.left)
                else:
                    seq.append(None)
                if node.right != None:
                    seq.append(node.right)
                else:
                    seq.append(None)
            else:
                str.append(None)
        while len(str) > 0 and str[-1] == None:
            str.pop()
        return json.dumps(str)
        
        
    # TODO: leetcode 的输入二叉树序列转树结构
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        str = json.loads(data)
        if len(str) == 0:
            return None
        root = TreeNode(None)
        nodeList = [None] * len(str)
        if str[0] != None:
            root.val = str[0]
            nodeList[0] = root

        i, j = 0, 0
        while j < len(str):
            parent = nodeList[i]
            i += 1
            if parent == None:
                continue
            j += 1
            if j < len(str) and str[j] != None:
                left = TreeNode(str[j])
                nodeList[j] = left
                parent.left = left
            j += 1
            if j < len(str) and str[j] != None:
                right = TreeNode(str[j])
                nodeList[j] = right
                parent.right = right
        return root

        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))