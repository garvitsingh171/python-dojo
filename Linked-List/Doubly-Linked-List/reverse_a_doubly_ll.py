class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def reverse_dll(self):
        current = self.head
        while current is not None:
            current.prev, current.next = current.next, current.prev
            current = current.prev
        self.head, self.tail = self.tail, self.head

    def printll(self):
        current = self.head
        while current is not None:
            print(current.data, end=' -> ')
            current = current.next
        print(None)


linked_list = LinkedList()

n = int(input())

for i in range(n):
    item = int(input())
    linked_list.insert(item)

linked_list.reverse_dll()

linked_list.printll()
