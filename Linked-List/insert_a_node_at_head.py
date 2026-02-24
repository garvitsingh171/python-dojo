class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            current = self.head
            while current.next is not None:
                current = current.next

            current.next = Node(data)

    def insert_at_head(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def printll(self):
        current = self.head
        while current is not None:
            print(current.data, end=' -> ')
            current = current.next


linked_list = LinkedList()

n = int(input())

k = int(input())

for _ in range(n):
    item = int(input())
    linked_list.insert(item)

linked_list.insert_at_head(k)
linked_list.printll()
