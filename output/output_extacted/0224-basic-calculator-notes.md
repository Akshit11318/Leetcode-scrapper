## Basic Calculator

**Problem Link:** https://leetcode.com/problems/basic-calculator/description

**Problem Statement:**
- Input format: a string `s` representing a basic arithmetic expression.
- Constraints: the string `s` consists of digits `0-9`, `+`, `-`, `*`, `/`, `(`, and `)`.
- Expected output format: the result of the arithmetic expression as an integer.
- Key requirements and edge cases to consider:
  - Handle parentheses correctly.
  - Follow the order of operations (PEMDAS/BODMAS).
  - Example test cases:
    - Input: `"1 + 1"`; Output: `2`.
    - Input: `" 2-1 + 2 "`; Output: `3`.
    - Input: `"(1+(4+5+2)-3)+(6+8)"`; Output: `23`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: directly evaluate the expression by iterating through the string and performing operations based on the encountered characters.
- Step-by-step breakdown of the solution:
  1. Initialize a stack to store intermediate results.
  2. Iterate through the string:
     - If a digit is encountered, push it onto the stack.
     - If an operator (`+`, `-`, `*`, `/`) is encountered, pop the top two elements from the stack, perform the operation, and push the result back onto the stack.
     - If an opening parenthesis is encountered, start a new stack to handle the subexpression inside the parentheses.
     - If a closing parenthesis is encountered, pop all elements from the current stack, perform operations, and push the final result onto the parent stack.
- Why this approach comes to mind first: it directly follows the order of operations and handles parentheses by using a stack.

```cpp
#include <iostream>
#include <stack>
#include <string>

int calculate(std::string s) {
    std::stack<int> stack;
    int currNum = 0;
    int result = 0;
    int sign = 1;
    for (int i = 0; i < s.size(); i++) {
        if (isdigit(s[i])) {
            currNum = currNum * 10 + (s[i] - '0');
        } else if (s[i] == '+' || s[i] == '-') {
            result += sign * currNum;
            currNum = 0;
            sign = (s[i] == '+') ? 1 : -1;
        } else if (s[i] == '(') {
            stack.push(result);
            stack.push(sign);
            sign = 1;
            result = 0;
        } else if (s[i] == ')') {
            result += sign * currNum;
            currNum = 0;
            result *= stack.top(); stack.pop();
            result += stack.top(); stack.pop();
        }
    }
    if (currNum != 0) result += sign * currNum;
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the length of the input string, as we iterate through the string once.
> - **Space Complexity:** $O(n)$ due to the use of the stack to handle parentheses.
> - **Why these complexities occur:** The iteration through the string and the use of a stack to handle nested parentheses lead to these complexities.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: instead of using a stack for every subexpression, we can simplify the problem by only considering the current number and the sign of the next operation.
- Detailed breakdown of the approach:
  1. Initialize variables to keep track of the current number, the result, and the sign of the next operation.
  2. Iterate through the string:
     - If a digit is encountered, update the current number.
     - If an operator is encountered, update the result based on the current number and the sign of the next operation, and reset the current number.
     - If an opening parenthesis is encountered, recursively call the function to handle the subexpression.
- Proof of optimality: this approach has the same time complexity as the brute force approach but simplifies the handling of parentheses and operations.

```cpp
int calculate(std::string s) {
    int stack = 0, sign = 1, res = 0;
    for (int i = 0; i < s.size(); i++) {
        if (isdigit(s[i])) {
            int num = 0;
            while (i < s.size() && isdigit(s[i])) {
                num = num * 10 + s[i++] - '0';
            }
            i--;
            res += sign * num;
        } else if (s[i] == '+') {
            sign = 1;
        } else if (s[i] == '-') {
            sign = -1;
        } else if (s[i] == '(') {
            int count = 0;
            int start = ++i;
            while (i < s.size()) {
                if (s[i] == '(') count++;
                else if (s[i] == ')') {
                    if (count == 0) break;
                    count--;
                }
                i++;
            }
            int tmp = calculate(s.substr(start, i - start));
            res += sign * tmp;
            i++;
        }
    }
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the length of the input string, as we iterate through the string once.
> - **Space Complexity:** $O(n)$ due to the recursive call stack for handling nested parentheses.
> - **Optimality proof:** This approach is optimal because it directly evaluates the expression without unnecessary operations, achieving the same time complexity as the brute force approach but with simplified logic.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: stack usage, recursive functions, and iteration through strings.
- Problem-solving patterns identified: handling parentheses and following the order of operations.
- Optimization techniques learned: simplifying the handling of subexpressions and using recursion.
- Similar problems to practice: more complex arithmetic expressions, parsing, and evaluating postfix or prefix expressions.

**Mistakes to Avoid:**
- Common implementation errors: incorrect handling of parentheses, misunderstanding the order of operations.
- Edge cases to watch for: empty strings, strings with only whitespace, and strings with invalid characters.
- Performance pitfalls: using unnecessary data structures or operations that increase time or space complexity.
- Testing considerations: thoroughly testing the function with various inputs, including edge cases and complex expressions.