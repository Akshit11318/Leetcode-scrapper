## Ternary Expression Parser
**Problem Link:** https://leetcode.com/problems/ternary-expression-parser/description

**Problem Statement:**
- Input format and constraints: Given a string `expression` consisting of ternary expressions and boolean values, parse the expression and return the result.
- Expected output format: A boolean value representing the result of the parsed expression.
- Key requirements and edge cases to consider: Handling nested ternary expressions, boolean values, and ensuring the expression is well-formed.
- Example test cases with explanations:
  - Input: "1 ? 1 : 0"
    Output: 1
    Explanation: Since the condition is true, the expression evaluates to 1.
  - Input: "0 ? 1 : 0"
    Output: 0
    Explanation: Since the condition is false, the expression evaluates to 0.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: The first approach that comes to mind is to recursively evaluate the expression by checking the condition and then evaluating the corresponding expression.
- Step-by-step breakdown of the solution:
  1. Check if the current character is a digit or a boolean value.
  2. If it is, return the corresponding boolean value.
  3. If not, it must be a ternary expression. Find the corresponding colon and question mark.
  4. Recursively evaluate the condition and the two possible expressions.
  5. Return the result based on the condition.
- Why this approach comes to mind first: It directly follows the structure of the ternary expression and is straightforward to implement.

```cpp
class Solution {
public:
    string parseTernary(string expression) {
        if (expression.size() == 1) {
            return expression;
        }
        int index = 0;
        char condition = expression[index];
        int count = 0;
        int colonIndex = -1;
        for (int i = 1; i < expression.size(); i++) {
            if (expression[i] == '?') {
                count++;
            } else if (expression[i] == ':') {
                count--;
            }
            if (count == 0) {
                colonIndex = i;
                break;
            }
        }
        string trueExpression = expression.substr(2, colonIndex - 2);
        string falseExpression = expression.substr(colonIndex + 1);
        if (condition == 'T') {
            return parseTernary(trueExpression);
        } else {
            return parseTernary(falseExpression);
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ where $n$ is the length of the expression. This is because we are recursively parsing the expression and in the worst case, we might have to traverse the entire expression for each recursive call.
> - **Space Complexity:** $O(n)$ due to the recursive call stack.
> - **Why these complexities occur:** The recursive nature of the solution and the need to traverse the expression multiple times lead to these complexities.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Instead of recursively parsing the expression, we can use a stack to store the expressions and conditions. This way, we only need to traverse the expression once.
- Detailed breakdown of the approach:
  1. Initialize an empty stack.
  2. Traverse the expression from right to left.
  3. When encountering a colon, pop the top two expressions from the stack and push the result of the ternary expression.
  4. When encountering a question mark, push the current expression onto the stack.
  5. When encountering a condition, push the condition onto the stack.
  6. At the end, the top of the stack will contain the result of the expression.
- Proof of optimality: This solution has a linear time complexity because we only need to traverse the expression once. The space complexity is also linear because in the worst case, we might need to store the entire expression on the stack.

```cpp
class Solution {
public:
    string parseTernary(string expression) {
        stack<string> s;
        for (int i = expression.size() - 1; i >= 0; i--) {
            if (expression[i] == ':') {
                continue;
            } else if (expression[i] == '?') {
                string b = s.top();
                s.pop();
                string a = s.top();
                s.pop();
                s.push(expression[i - 1] == 'T' ? b : a);
                i--;
            } else {
                s.push(string(1, expression[i]));
            }
        }
        return s.top();
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the length of the expression. This is because we only need to traverse the expression once.
> - **Space Complexity:** $O(n)$ due to the stack.
> - **Optimality proof:** This solution is optimal because it only requires a single pass through the expression and uses a stack to store the intermediate results, resulting in a linear time and space complexity.

---

### Final Notes
**Learning Points:**
- Key algorithmic concepts demonstrated: Using a stack to store intermediate results and parsing expressions from right to left.
- Problem-solving patterns identified: Breaking down complex expressions into smaller sub-expressions and using recursion or iteration to evaluate them.
- Optimization techniques learned: Using a stack to reduce the time complexity from $O(n^2)$ to $O(n)$.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases correctly, such as empty expressions or expressions with invalid syntax.
- Edge cases to watch for: Expressions with nested ternary expressions, boolean values, and invalid syntax.
- Performance pitfalls: Using recursive solutions that lead to high time complexities.
- Testing considerations: Thoroughly testing the solution with different input expressions, including edge cases and invalid syntax.