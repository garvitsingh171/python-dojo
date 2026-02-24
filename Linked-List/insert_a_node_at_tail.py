class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            current = self.head
            while current.next is not None:
                current = current.next

            current.next = Node(data)

    def print_ll(self):
        if self.head is None:
            return None
        else:
            current = self.head
            while current is not None:
                print(current.data, end=' -> ')
                current = current.next


n = int(input())

linkedlist = LinkedList()

for _ in range(n):
    item = int(input())
    linkedlist.insert(item)

print(linkedlist.print_ll())
