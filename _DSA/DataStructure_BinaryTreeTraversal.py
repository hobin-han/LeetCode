class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5

class Binary_Tree:
    def __init__(self, root):
        self.root = root
    
    def traversal_inorder(self, root):
        if root is None:
            return

        if root.left is None and root.right is None:
            print(root.val)
            return

        self.traversal_inorder(root.left)
        print(root.val)
        self.traversal_inorder(root.right)

    def traversal_preorder(self, root):
        print(root.val)

        if root.left:
            self.traversal_preorder(root.left)

        if root.right:
            self.traversal_preorder(root.right)

    def traversal_postorder(self, root):
        if root.left:
            self.traversal_postorder(root.left)

        if root.right:
            self.traversal_postorder(root.right)
        
        print(root.val)

tree = Binary_Tree(node1)
print("-> inorder")
tree.traversal_inorder(tree.root)
print("-> preorder")
tree.traversal_preorder(tree.root)
print("-> postorder")
tree.traversal_postorder(tree.root)

print("--------------------")
# ------ Tips

print([] == True)
print([1, 2])