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

    def print_reverse(self):
        arr = []

        current = self.head
        while current is not None:
            arr.append(current.data)
            current = current.next

        for i in range(len(arr)-1, -1, -1):
            print(arr[i], end=' -> ')

        print(None)

    def printll(self):
        if self.head is None:
            print(None)
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
linked_list.print_reverse()
