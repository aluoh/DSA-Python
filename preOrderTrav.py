# Print --> Left --> Right


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def preOrder(root):
    currNode = root
    stack = []
    result = []
    while currNode is not None or stack:
        if currNode is not None:
            result.append(currNode.val)
            stack.append(currNode)
            currNode = currNode.left
        else:
            prevNode = stack.pop()
            currNode = prevNode.right
    return result


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

print(preOrder(t1))
