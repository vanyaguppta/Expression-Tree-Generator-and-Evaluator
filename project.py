import networkx as nx
import matplotlib.pyplot as plt

# Node class
class Node:
    count = 0

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.id = Node.count
        Node.count += 1


# precedence for infix to postfix
def precedence(op):
    if op in "+-":
        return 1
    if op in "*/":
        return 2
    if op == "^":
        return 3
    return 0


# infix to postfix conversion
def infix_to_postfix(exp):
    stack = []
    output = ""

    for c in exp:
        if c.isalnum():
            output += c

        elif c == "(":
            stack.append(c)

        elif c == ")":
            while stack and stack[-1] != "(":
                output += stack.pop()
            stack.pop()

        else:
            while stack and precedence(stack[-1]) >= precedence(c):
                output += stack.pop()
            stack.append(c)

    while stack:
        output += stack.pop()

    return output


# building expression tree
def build_binarytree(postfix):
    stack = []

    for c in postfix:
        if c.isalnum():
            stack.append(Node(c))
        else:
            node = Node(c)
            node.right = stack.pop()
            node.left = stack.pop()
            stack.append(node)

    return stack.pop()


# converting tree to graph for visualization
def add_edges(graph, node):
    if node.left:
        graph.add_edge(node.id, node.left.id)
        add_edges(graph, node.left)

    if node.right:
        graph.add_edge(node.id, node.right.id)
        add_edges(graph, node.right)


# tree layout function
def get_tree_positions(root):
    pos = {}
    x = 0

    def inorder(node, depth):
        nonlocal x
        if node:
            inorder(node.left, depth + 1)

            pos[node.id] = (x, -depth)
            x += 1

            inorder(node.right, depth + 1)

    inorder(root, 0)
    return pos

# -------- MAIN PROGRAM --------

infix = input("Enter infix expression: ")

postfix = infix_to_postfix(infix)
print("Postfix:", postfix)

root = build_binarytree(postfix)

G = nx.DiGraph()

add_edges(G, root)

pos = get_tree_positions(root)

labels = {}
def get_labels(node):
    labels[node.id] = node.data
    if node.left:
        get_labels(node.left)
    if node.right:
        get_labels(node.right)

get_labels(root)

nx.draw(
    G,
    pos,
    labels=labels,
    with_labels=True,
    node_size=2500,
    node_color="skyblue",
    font_size=12,
    font_weight="bold",
    arrows=True
)

plt.show()



def evaluate(root, values):

    # if operand is a number
    if root.data.isdigit():
        return int(root.data)

    # if operand is a variable
    if root.data.isalpha():
        return values[root.data]

    # otherwise it is an operator
    left = evaluate(root.left, values)
    right = evaluate(root.right, values)

    if root.data == '+':
        return left + right
    elif root.data == '-':
        return left - right
    elif root.data == '*':
        return left * right
    elif root.data == '/':
        return left / right
    elif root.data == '^':
        return left ** right

values = {}

for ch in infix:
    if ch.isalpha() and ch not in values:
        values[ch] = int(input(f"Enter value of {ch}: "))
          
result = evaluate(root, values)

print("Result:", result)