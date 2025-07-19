class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)

    def search(self, data):
        node = self.head
        while node:
            if node.data == data:
                return node
            node = node.next
        return None

    def remove(self, data):
        if self.head.data == data:
            self.head = self.head.next
            return
        
        node = self.head
        while node:
            if node.next.data == data:
                node.next = node.next.next
                return

    def reverse_list(self):
        previous = None
        current = self.head

        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next
            
        self.head = previous

# ------ Tips

# check having valid data
data = None
print(not data)         # True
print(data is None)     # True
data = 123
print(not data)         # False
print(data is None)     # False
