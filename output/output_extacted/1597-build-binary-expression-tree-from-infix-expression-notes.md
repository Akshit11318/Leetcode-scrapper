## Build Binary Expression Tree from Infix Expression

**Problem Link:** https://leetcode.com/problems/build-binary-expression-tree-from-infix-expression/description

**Problem Statement:**
- Input: An infix expression as a string, where operands are single characters (a-z) and operators are one of '+', '-', or '*'.
- Expected Output: The root of the binary expression tree representing the given infix expression.
- Key Requirements:
  - Each node in the binary tree should have a `val`, `left`, and `right` attribute.
  - The tree should represent the expression in a way that operators are internal nodes, and operands are leaf nodes.
- Edge Cases:
  - The input expression is guaranteed to be valid.
  - The expression will not contain any parentheses.
  - The expression will not contain any spaces.
- Example Test Cases:
  - Input: "3+4*5"
    - Explanation: The expression can be represented as a binary tree where the root is the operator '+', the left child is the operand '3', and the right child is another binary tree with the operator '*' as its root, '4' as its left child, and '5' as its right child.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves parsing the infix expression character by character and deciding whether to create a new node or use an existing one based on the operator precedence.
- However, without proper handling of operator precedence, this approach quickly becomes cumbersome and prone to errors.
- A more structured approach involves using a stack to keep track of operators and operands.

```cpp
struct Node {
    string val;
    Node* left;
    Node* right;
    Node(string val) : val(val), left(nullptr), right(nullptr) {}
};

Node* expTree(string expression) {
    stack<Node*> nodes;
    stack<char> ops;
    for (char c : expression) {
        if (isdigit(c) || isalpha(c)) {
            Node* newNode = new Node(string(1, c));
            nodes.push(newNode);
        } else if (c == '+' || c == '-' || c == '*') {
            while (!ops.empty() && precedence(c) <= precedence(ops.top())) {
                Node* right = nodes.top(); nodes.pop();
                Node* left = nodes.top(); nodes.pop();
                Node* opNode = new Node(string(1, ops.top()));
                ops.pop();
                opNode->left = left;
                opNode->right = right;
                nodes.push(opNode);
            }
            ops.push(c);
        }
    }
    while (!ops.empty()) {
        Node* right = nodes.top(); nodes.pop();
        Node* left = nodes.top(); nodes.pop();
        Node* opNode = new Node(string(1, ops.top()));
        ops.pop();
        opNode->left = left;
        opNode->right = right;
        nodes.push(opNode);
    }
    return nodes.top();
}

int precedence(char op) {
    if (op == '+' || op == '-') return 1;
    if (op == '*') return 2;
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input expression, because each character is processed exactly once.
> - **Space Complexity:** $O(n)$, due to the use of stacks for operators and nodes.
> - **Why these complexities occur:** The algorithm iterates through the input string once, and in the worst case, it might need to store all characters in the stacks.

---

### Optimal Approach (Required)

The optimal approach is essentially the same as the brute force approach provided above, with minor optimizations in handling the stacks and precedence rules. The key insight is recognizing that using two stacks (one for operators and one for operands/nodes) allows for an efficient construction of the binary expression tree by respecting operator precedence rules.

```cpp
Node* expTree(string expression) {
    stack<Node*> nodes;
    stack<char> ops;
    for (char c : expression) {
        if (isalpha(c)) { // Assuming only letters as operands
            Node* newNode = new Node(string(1, c));
            nodes.push(newNode);
        } else if (c == '+' || c == '-' || c == '*') {
            while (!ops.empty() && precedence(ops.top()) >= precedence(c)) {
                createNode(nodes, ops);
            }
            ops.push(c);
        }
    }
    while (!ops.empty()) {
        createNode(nodes, ops);
    }
    return nodes.top();
}

void createNode(stack<Node*>& nodes, stack<char>& ops) {
    Node* right = nodes.top(); nodes.pop();
    Node* left = nodes.top(); nodes.pop();
    Node* newNode = new Node(string(1, ops.top()));
    ops.pop();
    newNode->left = left;
    newNode->right = right;
    nodes.push(newNode);
}

int precedence(char op) {
    if (op == '+' || op == '-') return 1;
    if (op == '*') return 2;
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input expression, as each character is processed once.
> - **Space Complexity:** $O(n)$, due to the potential need to store all characters in the stacks in the worst case.
> - **Optimality proof:** This approach is optimal because it processes the input string in a single pass and uses a minimal amount of extra space to store the operators and nodes, respecting the precedence rules without unnecessary operations.

---

### Final Notes

**Learning Points:**
- Understanding operator precedence and how to implement it using stacks.
- Recognizing the importance of a structured approach in parsing expressions.
- Practicing the use of stacks in parsing and constructing trees.

**Mistakes to Avoid:**
- Incorrect handling of operator precedence.
- Failing to properly validate input.
- Not considering edge cases, such as an empty input string or a string with only one operand.
- Inefficient use of stacks or other data structures.