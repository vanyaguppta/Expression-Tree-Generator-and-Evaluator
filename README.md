# Expression Tree Generator and Evaluator

A Python tool that takes any mathematical expression, converts it to postfix notation, builds a visual binary expression tree, and evaluates the result — including support for variable substitution.

<img width="640" height="480" alt="expressiontree output" src="https://github.com/user-attachments/assets/324071e1-1abe-435c-9d2f-cdac41632d91" />


---

## What it does

- Accepts any valid mathematical expression as input (e.g. `(a + b) * (c - 2)`)
- Converts the infix expression to **postfix notation** internally for easier tree construction
- Builds and visualizes a **binary expression tree** using `matplotlib` and `networkx`
- **Evaluates the expression**:
- If the expression contains only numbers → evaluates and returns the result directly
- If the expression contains variables (letters) → prompts the user to enter a value for each variable, then evaluates the final answer

---

## Demo

```
Enter an expression: (a + 3) * (b - 1)

Postfix: a 3 + b 1 - *

Enter value for a: 5
Enter value for b: 4

Result: (5 + 3) * (4 - 1) = 24
```

*(A visual tree window will also pop up showing the expression tree)*

---

## Tech Stack

- **Python 3**
- **NetworkX** — for building the tree graph structure
- **Matplotlib** — for rendering and visualizing the tree

---

## How to Run

### 1. Clone the repository
```bash
git clone https://github.com/vanyaguppta/Expression-Tree-Generator-and-Evaluator.git
cd Expression-Tree-Generator-and-Evaluator
```

### 2. Install dependencies
```bash
pip install matplotlib networkx
```

### 3. Run the program
```bash
python main.py
```

---

## How it works

1. **Infix → Postfix conversion** using the Shunting Yard algorithm (operator precedence + parentheses handled)
2. **Tree construction** by pushing operands as leaf nodes and operators as internal nodes onto a stack
3. **Tree traversal** to evaluate the expression (post-order traversal)
4. **Variable detection** — if any operand is a letter, the user is prompted to supply its value before evaluation

---

## Concepts Used

`Binary Trees` `Postfix Notation` `Stack` `Recursion` `Tree Traversal` `Expression Parsing` `Graph Visualization`

---

## Author

**Vanya Gupta** — B.Tech CSE, 2nd Year  
[GitHub](https://github.com/vanyaguppta)
