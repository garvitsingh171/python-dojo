class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        if self.isEmpty:
            return None
        return self.items.pop(0)

    def front(self):
        if self.isEmpty:
            return None
        return self.items[0]

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


queue = Queue()

n = int(input())

for i in range(n):
    items = input().strip()
    parts = items.split()
    cmd = parts[0].lower()

    if cmd == 'enqueue':
        queue.enqueue(int(parts[1]))
    elif cmd == 'dequeue':
        queue.dequeue()
    elif cmd == 'front':
        queue.front()
