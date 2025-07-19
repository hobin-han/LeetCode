'''
FIFO = First-In, First-Out
'''

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
class Queue:
    def __init__(self):
        self.head = None
        self.last = None
        self._size = 0

    def enqueue(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            self.last = node
        else:
            self.last.next = node
            self.last = node

        self._size += 1

    def dequeue(self):
        if self.head is None:
            return None
        else:
            node = self.head
            self.head = self.head.next
            self._size -= 1
            return node.data

    def size(self):
        return self._size

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("queue:", queue.dequeue())
print("queue size:", queue.size())
print("queue:", queue.dequeue())
print("queue size:", queue.size())
print("queue:", queue.dequeue())
print("queue size:", queue.size())

# ------ Queue in Python

from queue import Queue

q = Queue()
q.put('a')
q.put('b')
q.put('c')
print(q.qsize())
for i in range(3):
    print(q.get())

print("-------------------------")
# ------ Create Queue only using Stack

class Queue_From_Stack:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, data):
        self.s1.append(data)


    def dequeue(self):
        if len(self.s2) == 0:
            if len(self.s1) == 0:
                return None
            else:
                while len(self.s1) > 0:
                    self.s2.append(self.s1.pop())
        return self.s2.pop()

q = Queue_From_Stack()
q.enqueue('a')
q.enqueue('b')
q.enqueue('c')
print(q.dequeue())
q.enqueue('d')
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())