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

    def reverse_linked_list(self):
        if self.head is None:
            return None
        else:
            previous = None
            current = self.head
            while current is not None:
                nxt = current.next
                current.next = previous
                previous = current
                current = nxt
            self.head = previous
            return self.head

    def printll(self):
        if self.head is None:
            return None
        else:
            current = self.head
            while current is not None:
                print(current.data, end=' -> ')
                current = current.next
            print(None)


linked_list = LinkedList()

n = int(input())

for _ in range(n):
    item = int(input())
    linked_list.insert(item)

linked_list.printll()
linked_list.reverse_linked_list()
linked_list.printll()
