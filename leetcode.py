# 230
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def kthSmallest(root, k):
        # Inorder --> Left --> Root --> Right
    result = []
    currNode = root
    stack = []
    while currNode is not None or stack:
        if currNode is not None:
            stack.append(currNode)
            currNode = currNode.left
        else:
            currNode = stack.pop()
            result.append(currNode)
            currNode = currNode.right
    return result[k-1].val


t1 = TreeNode(8)
t2 = TreeNode(10)
t3 = TreeNode(3)
t4 = TreeNode(1)
t5 = TreeNode(6)
t6 = TreeNode(4)
t7 = TreeNode(14)
t1.right = t2
t1.left = t3
t3.left = t4
t3.right = t5
t5.left = t6
t5.right = TreeNode(7)
t2.right = t7
t7.left = TreeNode(13)

n = kthSmallest(t1, 5)
print(n)
