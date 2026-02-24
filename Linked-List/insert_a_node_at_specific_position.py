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

    def insert_at_position(self, k, m):
        new_node = Node(m)
        if k == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            count = 0
            current = self.head
            while count < k and current is not None:
                current = current.next
                count += 1
            new_node.next = current.next
            current.next = new_node

    def printll(self):
        current = self.head
        while current is not None:
            print(current.data, end=' -> ')
            current = current.next
        print(None)


linked_list = LinkedList()

n = int(input())

k = int(input())

m = int(input())

for _ in range(n):
    item = int(input())
    linked_list.insert(item)

linked_list.insert_at_position(k, m)

linked_list.printll()
