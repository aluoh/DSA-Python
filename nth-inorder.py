class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


first = Node(7)
second = Node(2)
third = Node(3)
fourth = Node(8)
fifth = Node(5)

first.left = second
first.right = third
third.left = fourth
third.right = fifth


result = []

inorder = []


def inOrder(root, nth):
    counter = 1
    stack = [root]
    answer = 0

    while stack:
        if root.left is not None:
            root = root.left
            stack.append(root)
        else:
            currNode = stack.pop()
            inorder.append(currNode.val)
            if counter == nth:
                answer = currNode.val
            counter += 1
            if currNode.right is not None:
                root = currNode.right
                stack.append(root)
    return answer


c1 = Node(10)
c2 = Node(20)
c3 = Node(30)
c4 = Node(40)
c5 = Node(50)

c1.left = c2
c1.right = c3
c2.left = c4
c2.right = c5


print("Expected Output: 8")
print("Actual: " + str(inOrder(first, 3)))
print(inorder)

inorder.clear()
print("Expected Output: 10")
print("Actual: " + str(inOrder(c1, 4)))
print(inorder)
