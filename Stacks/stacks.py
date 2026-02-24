class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if self.isEmpty():
            return None
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            return None
        return self.items[-1]

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


stack = Stack()

n = int(input())

for i in range(n):
    action = input().strip()
    parts = action.split()
    cmd = parts[0].lower()

    if cmd == 'push':
        stack.push(int(parts[1]))
    elif cmd == 'pop':
        print(stack.pop())
    else:
        print(stack.peek())
