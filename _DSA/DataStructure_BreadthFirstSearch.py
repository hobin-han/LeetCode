class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Binary_Tree:
    def __init__(self, root):
        self.root = root

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

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5

bin_tree = Binary_Tree(n1)
bin_tree.breadth_first_search([bin_tree.root])