class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def postOrder(root):
    # Left -> Right -> PRINT ROOT
    result = []
    stack = []
    currNode = root
    while stack or currNode is not None:
        if currNode is not None:
            stack.append(currNode)
            currNode = currNode.left
        else:
            s = stack.pop()
            if s.left is None and s.right is None:
                result.append(s.val)
            currNode = s.right
    return result

# 1, 4, 7, 6, 3, 13, 14, 10, 8


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

print(postOrder(t1))
