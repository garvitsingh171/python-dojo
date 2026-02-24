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

    def delete_node(self, k):
        current = self.head
        if k == 0:
            self.head = current.next
        else:
            count = 0
            while current.next is not None and count < k:
                current = current.next
                count += 1
            if current.next is not None:
                current.next = current.next.next

    def printll(self):
        current = self.head
        while current is not None:
            print(current.data, end=' -> ')
        print(None)


linked_list = LinkedList

n = int(input())

k = int(input())

linked_list.delete_node(k)

linked_list.printll()
