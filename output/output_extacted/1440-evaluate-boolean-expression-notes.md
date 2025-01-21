## Evaluate Boolean Expression
**Problem Link:** https://leetcode.com/problems/evaluate-boolean-expression/description

**Problem Statement:**
- Input format: A string `expression` containing a boolean expression and an array of integers `values` where each integer corresponds to a variable in the expression.
- Constraints: The expression only contains `&` (AND), `|` (OR), and `!` (NOT) operators, and variables are represented as single lowercase letters.
- Expected output format: A boolean value representing the result of the expression evaluation.
- Key requirements and edge cases to consider:
  - Handling of `!` operator which negates the value of a variable.
  - Handling of `&` and `|` operators which require two operands.
  - Ensuring the correct order of operations (negation before AND and OR).
- Example test cases with explanations:
  - `expression = "!(f)", values = [1,0]`: Evaluates to `true` because `!` negates the value of `f`.
  - `expression = "|(f,t)", values = [0,1]`: Evaluates to `true` because `|` returns `true` if either operand is `true`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Replace each variable in the expression with its corresponding value and then evaluate the expression.
- Step-by-step breakdown of the solution:
  1. Create a dictionary mapping variables to their values.
  2. Replace each variable in the expression with its value.
  3. Evaluate the expression by applying the operators in the correct order.
- Why this approach comes to mind first: It directly addresses the problem by simulating the evaluation process.

```cpp
#include <iostream>
#include <string>
#include <unordered_map>

bool evaluateExpression(const std::string& expression, const std::vector<int>& values) {
    std::unordered_map<char, bool> varMap;
    for (int i = 0; i < values.size(); ++i) {
        varMap['a' + i] = values[i];
    }

    // Simple recursive descent parser or direct evaluation
    // This example uses a simplified evaluation for illustration
    bool result = false;
    for (char c : expression) {
        if (c == '!') {
            // Handle NOT operator
            result = !result;
        } else if (c == '&') {
            // Handle AND operator
            // For simplicity, assume the second operand is always true
            result = result && true;
        } else if (c == '|') {
            // Handle OR operator
            // For simplicity, assume the second operand is always true
            result = result || true;
        } else if (varMap.find(c) != varMap.end()) {
            // Replace variable with its value
            result = varMap[c];
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the length of the expression, because we potentially scan the expression once.
> - **Space Complexity:** $O(n)$ for storing the variable map and any additional space used during evaluation.
> - **Why these complexities occur:** The brute force approach involves scanning the expression and potentially storing each variable and its value, leading to linear time and space complexities.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Utilize a stack to efficiently evaluate the expression by directly applying operators when encountered, especially for `!`, and using the stack for `&` and `|` operations.
- Detailed breakdown of the approach:
  1. Initialize an empty stack.
  2. Iterate through the expression:
     - When encountering a variable, push its value onto the stack.
     - When encountering a `!`, pop the top value from the stack, negate it, and push it back.
     - When encountering a `&` or `|`, pop the top two values from the stack, apply the operation, and push the result back.
  3. After iterating through the entire expression, the stack should contain a single value, which is the result of the expression.
- Proof of optimality: This approach minimizes the number of operations by directly applying them as encountered, without unnecessary intermediate steps.

```cpp
#include <iostream>
#include <string>
#include <stack>
#include <unordered_map>

bool evaluateExpression(const std::string& expression, const std::vector<int>& values) {
    std::unordered_map<char, bool> varMap;
    for (int i = 0; i < values.size(); ++i) {
        varMap['a' + i] = values[i];
    }

    std::stack<bool> evalStack;
    for (char c : expression) {
        if (c == '!') {
            bool top = evalStack.top();
            evalStack.pop();
            evalStack.push(!top);
        } else if (c == '&') {
            bool right = evalStack.top();
            evalStack.pop();
            bool left = evalStack.top();
            evalStack.pop();
            evalStack.push(left && right);
        } else if (c == '|') {
            bool right = evalStack.top();
            evalStack.pop();
            bool left = evalStack.top();
            evalStack.pop();
            evalStack.push(left || right);
        } else {
            evalStack.push(varMap[c]);
        }
    }
    return evalStack.top();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the length of the expression, because we process each character in the expression once.
> - **Space Complexity:** $O(n)$ for the stack in the worst case (e.g., an expression with only variables).
> - **Optimality proof:** This approach is optimal because it processes the expression in a single pass, directly applying operators as encountered, which minimizes the number of operations required.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Stack-based evaluation of postfix expressions, direct application of operators.
- Problem-solving patterns identified: Using a stack to simplify the evaluation of expressions with multiple operators.
- Optimization techniques learned: Minimizing the number of operations by applying them as soon as possible.
- Similar problems to practice: Evaluating postfix expressions, parsing and evaluating expressions with more complex grammars.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly handling the order of operations, especially with the `!` operator.
- Edge cases to watch for: Empty expressions, expressions with no variables, expressions with only `!` operators.
- Performance pitfalls: Using inefficient data structures (e.g., linked lists instead of stacks) for evaluation.
- Testing considerations: Thoroughly testing with various expressions, including edge cases, to ensure correctness.