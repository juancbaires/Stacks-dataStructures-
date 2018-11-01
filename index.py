class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


States = Stack()

States.push("new item")
States.push(5)
States.push(False)
print(States.items)
States.pop()
print(States.items)
States.peek()
print(States.items)
States.size()
print(States.size())
