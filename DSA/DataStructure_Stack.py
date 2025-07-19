'''
LIFO = Last-In, First-Out
'''

# ------ Stack with Array

class Array_Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)
    
    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    
    def is_empty(self):
        return len(self.items) == 0
    
    def peek(self):
        return self.items[-1]

stack = Array_Stack()
stack.push(1)
stack.push(2)
stack.push(3)

for i in range(3):
    print("stack with array:", stack.pop())

# ------ Stack with Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_List_Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def pop(self):
        if self.head is None:
            return None
        node = self.head
        self.head = node.next
        return node.data

stack = Linked_List_Stack()
stack.push(1)
stack.push(2)
stack.push(3)

for i in range(3):
    print("stack with linked list:", stack.pop())

# ------ Stack in Python (Easiest Way 😍)

stack = []
stack.append(1)
stack.append(2)
stack.append(3)

for i in range(3):
    print("stack in python:", stack.pop())

# ------ Reverse String

string = "repus"

# Way 1) Use Stack structure

def reverse_string(string):
    stack = []
    for s in string:
        stack.append(s)

    string = ""
    while len(stack) > 0:
        string += stack.pop()
    return string

reversed = reverse_string(string)
print("reverse string 1:", reversed)

# Way 2) Use Python index

reversed = string[::-1]
print("reverse string 2:", reversed)

# Way 3) Use Python reversed

reversed = ''.join(reversed(my_string)) # occurs Error in Python1
print("reverse string 3:", reversed)

print("---------------------------------")

# ------ Tips

# char array to string
char_array = ['c', 'a', 't']
print("(char_array to string)", ''.join(char_array)) # cat
# append char to string
string = ""
string += 'a'
print("(append char to string)", string) # a
# string to char array
print(list("string"))