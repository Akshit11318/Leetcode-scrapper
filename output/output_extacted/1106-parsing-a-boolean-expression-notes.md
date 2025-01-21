## Parsing a Boolean Expression
**Problem Link:** https://leetcode.com/problems/parsing-a-boolean-expression/description

**Problem Statement:**
- Input format and constraints: The input is a string representing a boolean expression containing `&` (and), `|` (or), `!` (not), `t` (true), and `f` (false).
- Expected output format: Return `1` if the expression evaluates to true and `0` otherwise.
- Key requirements and edge cases to consider: Handle parentheses to determine the order of operations, and be mindful of the `!` operator which negates the value of its operand.
- Example test cases with explanations:
  - `"!(f)"` should return `1` because `!f` is `true`.
  - `"&(t,f)"` should return `0` because `t&f` is `false`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Use a stack to keep track of the operators and operands. When encountering a `)`, pop operators and operands from the stack and evaluate the expression inside the parentheses.
- Step-by-step breakdown of the solution:
  1. Initialize a stack to store operators and operands.
  2. Iterate through the string. When encountering an operator or operand, push it onto the stack.
  3. When encountering a `)`, pop operators and operands from the stack, evaluate the expression inside the parentheses, and push the result back onto the stack.
  4. After iterating through the entire string, the stack should contain a single element, which is the result of the expression.
- Why this approach comes to mind first: It directly follows the order of operations defined by the parentheses and handles each operator and operand as it appears.

```cpp
#include <stack>
#include <string>

int parseBoolExpr(string expression) {
    stack<int> s;
    for (char c : expression) {
        if (c == ',') continue; // Ignore commas
        if (c == 't') s.push(1); // Push true
        else if (c == 'f') s.push(0); // Push false
        else if (c == ')') {
            int result = s.top(); s.pop();
            char op = s.top(); s.pop();
            if (op == '!') {
                result = !result;
            } else {
                while (s.top() != '(') {
                    int operand = s.top(); s.pop();
                    if (op == '&') result = result & operand;
                    else if (op == '|') result = result | operand;
                }
                s.pop(); // Remove the '('
            }
            s.push(result);
        } else {
            s.push(c); // Push operators and '('
        }
    }
    return s.top();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the expression, because we iterate through the string once.
> - **Space Complexity:** $O(n)$, because in the worst case, we might need to push every character onto the stack.
> - **Why these complexities occur:** The iteration through the string and the potential to store every character on the stack lead to these linear complexities.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Utilize a recursive approach to handle the nested parentheses, and directly evaluate expressions as they are parsed.
- Detailed breakdown of the approach:
  1. Define a recursive function that takes a substring of the expression and evaluates it.
  2. Handle the base cases where the expression is a single character (`t` or `f`).
  3. For expressions starting with `!`, recursively evaluate the substring inside the parentheses and negate the result.
  4. For expressions starting with `&` or `|`, recursively evaluate each operand and combine the results using the respective operator.
- Proof of optimality: This approach ensures that expressions are evaluated in the correct order as defined by the parentheses and operators, and it does so in a single pass through the string, leading to optimal time complexity.
- Why further optimization is impossible: Given the need to evaluate each character and the necessity of handling nested parentheses, any algorithm must at least read the input once, making $O(n)$ the best achievable time complexity.

```cpp
#include <string>

int parseBoolExpr(string expression) {
    int evaluate(string& expr, int& i) {
        if (expr[i] == 't') { i++; return 1; }
        if (expr[i] == 'f') { i++; return 0; }
        if (expr[i] == '!') {
            i++;
            int val = evaluate(expr, i);
            i++; // Skip ')'
            return !val;
        }
        char op = expr[i];
        i++; // Skip operator
        int result = evaluate(expr, i);
        i++; // Skip ','
        while (expr[i] != ')') {
            int val = evaluate(expr, i);
            i++; // Skip ','
            if (op == '&') result = result & val;
            else if (op == '|') result = result | val;
        }
        i++; // Skip ')'
        return result;
    }
    int i = 0;
    return evaluate(expression, i);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the expression, as we make a single pass through the string.
> - **Space Complexity:** $O(n)$, due to the recursive call stack in the worst case of deeply nested expressions.
> - **Optimality proof:** The recursive approach ensures expressions are evaluated according to the order of operations and parentheses, achieving the best possible time complexity for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Recursive approach for nested structures, direct evaluation of expressions.
- Problem-solving patterns identified: Handling operator precedence, using recursion for nested problems.
- Optimization techniques learned: Evaluating expressions directly as they are parsed, minimizing unnecessary operations.
- Similar problems to practice: Other parsing and expression evaluation problems, such as parsing arithmetic expressions.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect handling of parentheses, operator precedence, or recursive calls.
- Edge cases to watch for: Deeply nested expressions, expressions starting with `!`, and ensuring all characters are processed.
- Performance pitfalls: Inefficient recursion or unnecessary operations that could lead to higher than optimal time complexity.
- Testing considerations: Ensure to test with a variety of expressions, including those with different operators, nested parentheses, and edge cases like single-character expressions.