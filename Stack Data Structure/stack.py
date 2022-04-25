# Stack Class

class Stack:
    def __init__(self):
        self.items = []

    # check whether the stack is empty or not
    def is_empty(self):
        return len(self.items) == 0

    # push an item into the stack
    def push(self, item):
        self.items.append(item)

    # remove the last item from stack
    def pop(self):
        return self.items.pop()

    # return the last item in the stack
    def peek(self):
        return self.items[-1]

    # return the size of the stack
    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


if __name__ == "__main__":
    s = Stack()
    print(s)
    print(s.is_empty())
    s.push(4)
    print(s)
    s.push(5)
    s.push(6)
    print(s)
    s.pop()
    print(s)
    print(s.peek())
    print(s.size())