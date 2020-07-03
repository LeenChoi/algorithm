
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def deserialize(arr):
    if len(arr) == 0:
        return None
    root = TreeNode(None)
    nodeList = [None] * len(arr)
    if arr[0] != None:
        root.val = arr[0]
        nodeList[0] = root

    i, j = 0, 0
    while j < len(arr):
        parent = nodeList[i]
        i += 1
        if parent == None:
            continue
        j += 1
        if j < len(arr) and arr[j] != None:
            left = TreeNode(arr[j])
            nodeList[j] = left
            parent.left = left
        j += 1
        if j < len(arr) and arr[j] != None:
            right = TreeNode(arr[j])
            nodeList[j] = right
            parent.right = right
    return root 

def serialize(root):
    seq, arr = [root], []
    while len(seq) > 0:
        node = seq.pop(0)
        if node:
            arr.append(node.val)
            if node.left != None:
                seq.append(node.left)
            else:
                seq.append(None)
            if node.right != None:
                seq.append(node.right)
            else:
                seq.append(None)
        else:
            arr.append(None)
    while len(arr) > 0 and arr[-1] == None:
        arr.pop()
    return arr