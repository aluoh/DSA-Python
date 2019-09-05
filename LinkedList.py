class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setNext(self, new_next):
        self.next = new_next


class LinkedList(object):

    def __init__(self, head=None):
        self.head = Node(head)

    # Inserts after head
    def insert(self, data):
        self.head.setNext(Node(data))

    # Insert at head
    def insertAtHead(self, data):
        node = Node(data)
        node.setNext(self.head)
        self.head = node

    def search(self, data):
        currentNode = self.head
        found = False
        while currentNode is not None and not found:
            if currentNode.data == data:
                found = True
                return currentNode
            else:
                currentNode = currentNode.next

        if currentNode is None:
            raise ValueError("Invalid, node not found")
        return currentNode

    def delete(self, data):
        currentNode = None
        nodeToDelete = self.search(data)
        deleted = False
        if self.head is not None:
            currentNode = self.head
        if self.head == nodeToDelete:
            self.head = None
            deleted = True
        while currentNode is not None and not deleted:
            if currentNode.next == nodeToDelete:
                currentNode.next = currentNode.next.next
                deleted = True
            else:
                currentNode = currentNode.next


v = LinkedList(200)
v.delete(200)
print(v.head.data)
