# Это пиздец

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def append(self, value):
        if self.root is None:
            self.root = Node(value)
            return value

        node = self.root

        while node:
            if node.left is None:
                node.left = Node(value)
                return value
            elif node.right is None:
                node.right = Node(value)
                return value
            else:
                #node = node.left




    def in_order(self, node):
        if node:
            self.in_order(node.left)
            print(node.value)
            self.in_order(node.right)

tree = Tree()
tree.append(6)
tree.append(2)
tree.append(5)
tree.append(1)
tree.append(2)
tree.append(7)
tree.in_order(tree.root)
