## Design an Expression Tree with Evaluate Function

**Problem Link:** https://leetcode.com/problems/design-an-expression-tree-with-evaluate-function/description

**Problem Statement:**
- Input format and constraints: The input will be a string representing a valid mathematical expression with non-negative integers, `+`, `-`, `*`, `/`, and parentheses. The expression will be evaluated using the standard order of operations (PEMDAS/BODMAS).
- Expected output format: The output will be the result of the evaluated expression.
- Key requirements and edge cases to consider: The expression will not contain any whitespace, and division by zero will not occur. The input expression will be a string, and the output will be an integer.
- Example test cases with explanations: 
  - Input: `"2*3-4*5"` Output: `-14`
  - Input: `"1+2+3+4"` Output: `10`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach to solving this problem would be to create a recursive function that parses the expression and evaluates it based on the operator precedence. This would involve checking each character in the string to determine if it is a number or an operator and handling the parentheses accordingly.
- Step-by-step breakdown of the solution: 
  1. Parse the input string to identify numbers, operators, and parentheses.
  2. Use a recursive function to evaluate the expression based on the operator precedence.
  3. Handle parentheses by recursively evaluating the expressions within them first.
- Why this approach comes to mind first: This approach is straightforward and follows the standard order of operations. However, it may not be the most efficient solution.

```cpp
class Node {
public:
    string val;
    Node* left;
    Node* right;

    Node() {
        val = "";
        left = nullptr;
        right = nullptr;
    }

    Node(string val) {
        this->val = val;
        left = nullptr;
        right = nullptr;
    }

    Node(string val, Node* left, Node* right) {
        this->val = val;
        this->left = left;
        this->right = right;
    }
};

class Solution {
public:
    Node* expTree(string expression) {
        int pos = 0;
        return buildTree(expression, pos);
    }

    Node* buildTree(string& expression, int& pos) {
        if (pos >= expression.size()) return nullptr;

        if (isdigit(expression[pos])) {
            string num = "";
            while (pos < expression.size() && isdigit(expression[pos])) {
                num += expression[pos++];
            }
            return new Node(num);
        }

        if (expression[pos] == '(') {
            pos++;
            Node* left = buildTree(expression, pos);
            pos++; // Skip the operator
            Node* right = buildTree(expression, pos);
            pos++; // Skip the ')'
            return new Node(string(1, expression[pos - 2]), left, right);
        }

        return nullptr;
    }

    int evaluate(Node* root) {
        if (root == nullptr) return 0;

        if (isdigit(root->val[0])) {
            return stoi(root->val);
        }

        int leftVal = evaluate(root->left);
        int rightVal = evaluate(root->right);

        if (root->val == "+") {
            return leftVal + rightVal;
        } else if (root->val == "-") {
            return leftVal - rightVal;
        } else if (root->val == "*") {
            return leftVal * rightVal;
        } else if (root->val == "/") {
            return leftVal / rightVal;
        }

        return 0;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where n is the length of the input string, because we are parsing the string once to build the tree and then traversing the tree to evaluate the expression.
> - **Space Complexity:** $O(n)$ because in the worst case, we might need to store all characters in the tree.
> - **Why these complexities occur:** These complexities occur because we are using a recursive approach to build and evaluate the expression tree.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of using a recursive approach, we can use a stack-based approach to build and evaluate the expression tree. This will allow us to avoid the overhead of recursive function calls and make the solution more efficient.
- Detailed breakdown of the approach: 
  1. Use two stacks, one for numbers and one for operators, to build the expression tree.
  2. Iterate through the input string, pushing numbers onto the number stack and operators onto the operator stack.
  3. When encountering a parenthesis, push the current operator onto the operator stack and start a new subtree.
  4. When encountering a closing parenthesis, pop operators from the operator stack and numbers from the number stack to build the subtree.
- Proof of optimality: This approach is optimal because it has a linear time complexity and uses a constant amount of extra space to store the stacks.

```cpp
class Node {
public:
    string val;
    Node* left;
    Node* right;

    Node() {
        val = "";
        left = nullptr;
        right = nullptr;
    }

    Node(string val) {
        this->val = val;
        left = nullptr;
        right = nullptr;
    }

    Node(string val, Node* left, Node* right) {
        this->val = val;
        this->left = left;
        this->right = right;
    }
};

class Solution {
public:
    Node* expTree(string expression) {
        stack<Node*> numStack;
        stack<char> opStack;

        for (int i = 0; i < expression.size(); i++) {
            if (isdigit(expression[i])) {
                string num = "";
                while (i < expression.size() && isdigit(expression[i])) {
                    num += expression[i++];
                    i--;
                }
                numStack.push(new Node(num));
            } else if (expression[i] == '(') {
                opStack.push(expression[i]);
            } else if (expression[i] == ')') {
                while (opStack.top() != '(') {
                    Node* right = numStack.top();
                    numStack.pop();
                    Node* left = numStack.top();
                    numStack.pop();
                    char op = opStack.top();
                    opStack.pop();
                    numStack.push(new Node(string(1, op), left, right));
                }
                opStack.pop(); // Remove the '('
            } else {
                while (!opStack.empty() && precedence(opStack.top()) >= precedence(expression[i])) {
                    Node* right = numStack.top();
                    numStack.pop();
                    Node* left = numStack.top();
                    numStack.pop();
                    char op = opStack.top();
                    opStack.pop();
                    numStack.push(new Node(string(1, op), left, right));
                }
                opStack.push(expression[i]);
            }
        }

        while (!opStack.empty()) {
            Node* right = numStack.top();
            numStack.pop();
            Node* left = numStack.top();
            numStack.pop();
            char op = opStack.top();
            opStack.pop();
            numStack.push(new Node(string(1, op), left, right));
        }

        return numStack.top();
    }

    int evaluate(Node* root) {
        if (root == nullptr) return 0;

        if (isdigit(root->val[0])) {
            return stoi(root->val);
        }

        int leftVal = evaluate(root->left);
        int rightVal = evaluate(root->right);

        if (root->val == "+") {
            return leftVal + rightVal;
        } else if (root->val == "-") {
            return leftVal - rightVal;
        } else if (root->val == "*") {
            return leftVal * rightVal;
        } else if (root->val == "/") {
            return leftVal / rightVal;
        }

        return 0;
    }

    int precedence(char op) {
        if (op == '+' || op == '-') return 1;
        if (op == '*' || op == '/') return 2;
        return 0;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where n is the length of the input string, because we are parsing the string once to build the tree and then traversing the tree to evaluate the expression.
> - **Space Complexity:** $O(n)$ because in the worst case, we might need to store all characters in the tree.
> - **Optimality proof:** This approach is optimal because it has a linear time complexity and uses a constant amount of extra space to store the stacks.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a stack-based approach to build and evaluate an expression tree.
- Problem-solving patterns identified: Breaking down a complex problem into smaller sub-problems and solving them recursively or iteratively.
- Optimization techniques learned: Using a stack-based approach to avoid the overhead of recursive function calls.
- Similar problems to practice: Evaluating postfix expressions, parsing mathematical expressions, and building abstract syntax trees.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases such as division by zero or invalid input.
- Edge cases to watch for: Parentheses, operator precedence, and invalid input.
- Performance pitfalls: Using a recursive approach with a large input size.
- Testing considerations: Testing the solution with different input sizes and edge cases to ensure correctness and performance.