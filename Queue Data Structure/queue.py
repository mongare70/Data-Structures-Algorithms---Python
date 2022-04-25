class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


if __name__ == "__main__":
    q = Queue()
    print(q.is_empty())
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q)
    print("The size of the queue is: ", q.size())
    q.dequeue()
    print(q)
    print("The size of the queue is: ", q.size())
