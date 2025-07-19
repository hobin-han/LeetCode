class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Completion_Binary_Tree:
    def __init__(self):
        self.root = None
                    
    def breadth_first_search(self, nodes):
        if len(nodes) == 0:
            return

        new_nodes = []
        for n in nodes:
            print(n.value)
            if n.left:
                new_nodes.append(n.left)
            if n.right:
                new_nodes.append(n.right)
        
        self.breadth_first_search(new_nodes)

    def add(self, nodes, value):
        if self.root is None:
            self.root = Node(value)
            return

        if len(nodes) == 0:
            return

        new_nodes = []
        for n in nodes:
            if n.left is None:
                n.left = Node(value)
                return
            elif n.right is None:
                n.right = Node(value)
                return
            else:
                new_nodes.append(n.left)
                new_nodes.append(n.right)
        
        self.add(new_nodes, value)

cbt = Completion_Binary_Tree()
cbt.add([cbt.root], 10)
cbt.add([cbt.root], 5)
cbt.add([cbt.root], 3)
cbt.add([cbt.root], 1)
print("-> completion binary tree")
cbt.breadth_first_search([cbt.root])