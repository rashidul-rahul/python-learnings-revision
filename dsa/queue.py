class Queue:
    def __init__(self, size_of_queue):
        self.max_size = size_of_queue
        self.data_list = [0] * size_of_queue
        self.size, self.head, self.tail = 0, 0, 0

    def enqueue(self, data):
        if self.is_full():
            print("queue is full")
            return
        print("inserting...")
        self.data_list[self.tail] = data
        self.tail = (self.tail + 1) % self.max_size
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            print("queue is empty")
            return
        self.size -= 1
        data = self.data_list[self.head]
        self.head = (self.head + 1) % self.max_size
        return data

    def is_full(self):
        print(self.tail)
        if self.size == self.max_size:
            return True
        return False

    def is_empty(self):
        print(self.head)
        if self.size == 0:
            return True
        return False


q = Queue(3)

q.enqueue(12)
q.enqueue(30)
q.enqueue(40)

print(q.data_list)
while not q.is_empty():
    print(q.dequeue())

