class Queue:
    def __init__(self):
        self.items = []
        
    def enqueue(self, item):
        self.items.append(item)
        
    def dequeue(self):
        if not len(self.items) == 0:
            return self.items.pop(0)
        else:
            return None
        
queue = Queue()
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)

print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
        
