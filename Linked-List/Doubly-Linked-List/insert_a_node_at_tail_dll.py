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

    def insert_at_tail(self, k):
        self.insert(k)

    def printll(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print(None)


linked_list = LinkedList()

n = int(input())

k = int(input())

for i in range(n):
    item = int(input())
    linked_list.insert(item)

linked_list.insert_at_tail(k)

linked_list.printll()
