import global_value as g

g.swap = 0
g.cmp = 0

def comp(a:int, b: int) -> int:
    g.cmp += 1
    if (a >= b):
        return (1)
    else:
        return (0)

class Node:
    def __init__(self, value):
        self.value = value 
        self.left = None 
        self.right = None 

class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

def insert(root: Node, node: Node) -> None:
    if (comp(root.value, node.value) == 1):
        if (root.left != None):
            insert(root.left, node)
        else:
            root.left = node
    elif (comp(root.value, node.value) == 0):
        g.cmp += 1
        if (root.right != None):
            insert(root.right, node)
        else:
            root.right = node

def make_tree(num: list[int]) -> BinaryTree:
    i = 0
    tree = BinaryTree(num[i])
    for j in range(1, len(num)):
        insert(tree.root, Node(num[j]))
    return (tree)

def print_tree(root: Node, num: list[int]) -> list[int]:
    if (root.left != None):
        print_tree(root.left, num)
    num.append(root.value)
    if (root.right != None):
        print_tree(root.right, num)
    return (num)

def binarytreesort(num: list[int]) -> list[int]:
    tree = make_tree(num)
    num = []
    ret = print_tree(tree.root, num)
    return (ret)