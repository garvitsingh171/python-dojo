class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while (current.next) is not None:
            current = current.next
        current.next = new_node

    def sortll(self):
        if self.head is None:
            return
        swapped = True
        while swapped:
            swapped = False
            current = self.head
            while (current.next) is not None:
                if current.data > current.next.data:
                    current.data, current.next.data = (
                        current.next.data, current.data)
                    swapped = True
                current = current.next

    def printll(self):
        current = self.head
        while current is not None:
            print(current.data, end=' ')
            current = current.next
        print()


linked_list = LinkedList()
n = int(input())
arr = list(map(int, input().split()))
for i in range(n):
    item = arr[i]
    linked_list.insert(item)
linked_list.sortll()
linked_list.printll()
