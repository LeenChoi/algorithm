
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