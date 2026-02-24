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

    def delete_kth(self, k):
        count = 0
        current = self.head
        while current:
            count += 1
            if count % k != 0:
                current = current.next
            else:
                current = current.next.next
        return self.head

    def printll(self):
        current = self.head
        if current is None:
            return None
        else:
            while current is not None:
                print(current.data, end=' -> ')
                current = current.next
            print(None)


linked_list = LinkedList()

n = int(input("Enter the length of the linked list: "))

for i in range(n):
    item = int(input(f"Enter the {i} element: "))
    linked_list.insert(item)

k = int(input("Enter the position which you want to delete: "))

linked_list.printll()

linked_list.delete_kth(k)

linked_list.printll()
