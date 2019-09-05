class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def inorderTraversal(root):
    result = []
    stack = []
    done = False
    while not done:
        if root is not None:
            stack.append(root)
            root = root.left
        else:
            if len(stack) > 0:
                root = stack.pop()
                result.append(root.val)
                root = root.right
            else:
                done = True
    return result


a = TreeNode(5)  # root
b = TreeNode(1)
f = TreeNode(0)
c = TreeNode(10)
g = TreeNode(7)
d = TreeNode(3)
e = TreeNode(15)

a.left = b
a.right = c
b.right = d
b.left = f
c.left = g
c.right = e

print(inorderTraversal(a))
