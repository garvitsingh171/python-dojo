class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def insert_at_head(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def printll(self):
        current = self.head
        while current is not None:
            print(current.data, end=' -> ')
            current = current.next
        print(None)


linked_list = LinkedList()

n = int(input())

k = int(input())

for i in range(n):
    item = int(input())
    linked_list.insert(item)

linked_list.insert_at_head(k)
linked_list.printll()
