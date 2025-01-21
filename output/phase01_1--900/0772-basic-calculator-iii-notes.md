## Basic Calculator III
**Problem Link:** https://leetcode.com/problems/basic-calculator-iii/description

**Problem Statement:**
- Input format and constraints: The input is a string `s` representing a mathematical expression, containing digits, operators (`+`, `-`, `*`, `/`), and parentheses. The string does not contain any spaces or other characters. The input string is guaranteed to be a valid mathematical expression.
- Expected output format: The output should be an integer representing the result of the mathematical expression.
- Key requirements and edge cases to consider: The expression can contain nested parentheses and the operators can be used in any order. The division operator should perform integer division (i.e., round down to the nearest whole number).
- Example test cases with explanations:
  - Input: `s = "2*(5+5*2)-3*(4-6)"`
  - Output: `2*(5+5*2)-3*(4-6) = 2*(5+10)-3*(-2) = 2*15+3*2 = 30+6 = 36`
  - Explanation: Evaluate the expression inside the parentheses first, then perform the multiplication and division from left to right, and finally perform the addition and subtraction from left to right.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: One way to solve this problem is to use a recursive approach, where we recursively evaluate the expressions inside the parentheses.
- Step-by-step breakdown of the solution:
  1. Find the first opening parenthesis in the string.
  2. Find the corresponding closing parenthesis.
  3. Evaluate the expression inside the parentheses.
  4. Replace the expression with its result in the original string.
  5. Repeat steps 1-4 until there are no more parentheses in the string.
  6. Evaluate the final expression.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it can be inefficient for large inputs.

```cpp
int calculate(string s) {
    int pos = 0;
    return calculateHelper(s, pos);
}

int calculateHelper(string s, int& pos) {
    int result = 0;
    int sign = 1;
    int num = 0;
    while (pos < s.size()) {
        if (isdigit(s[pos])) {
            num = num * 10 + s[pos] - '0';
            pos++;
        } else if (s[pos] == '(') {
            pos++;
            num = calculateHelper(s, pos);
            pos++;
        } else if (s[pos] == '+' || s[pos] == '-') {
            result += sign * num;
            sign = (s[pos] == '+') ? 1 : -1;
            num = 0;
            pos++;
        } else if (s[pos] == '*' || s[pos] == '/') {
            int temp = num;
            pos++;
            num = calculateHelper(s, pos);
            pos++;
            if (s[pos - 2] == '*') {
                num *= temp;
            } else {
                num /= temp;
            }
        } else if (s[pos] == ')') {
            result += sign * num;
            return result;
        }
    }
    result += sign * num;
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the string. This is because in the worst case, we need to recursively evaluate the expressions inside the parentheses.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the string. This is because we need to store the recursive call stack.
> - **Why these complexities occur:** The recursive approach leads to a time complexity of $O(n^2)$ because we need to find the corresponding closing parenthesis for each opening parenthesis. The space complexity is $O(n)$ because we need to store the recursive call stack.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a stack-based approach to evaluate the expression. We can use two stacks, one for the numbers and one for the operators.
- Detailed breakdown of the approach:
  1. Initialize two stacks, one for the numbers and one for the operators.
  2. Iterate through the string. If we encounter a digit, we push it onto the number stack.
  3. If we encounter an operator, we push it onto the operator stack.
  4. If we encounter an opening parenthesis, we push it onto the operator stack.
  5. If we encounter a closing parenthesis, we pop operators and numbers from the stacks and evaluate the expression until we find the corresponding opening parenthesis.
  6. After iterating through the entire string, we pop any remaining operators and numbers from the stacks and evaluate the final expression.
- Proof of optimality: This approach has a time complexity of $O(n)$, where $n$ is the length of the string. This is because we only need to iterate through the string once.

```cpp
int calculate(string s) {
    stack<int> nums;
    stack<char> ops;
    int num = 0;
    for (int i = 0; i < s.size(); i++) {
        if (isdigit(s[i])) {
            num = num * 10 + s[i] - '0';
        } else if (s[i] != ' ') {
            if (s[i] == '(') {
                ops.push(s[i]);
            } else if (s[i] == ')') {
                while (ops.top() != '(') {
                    int b = nums.top();
                    nums.pop();
                    int a = nums.top();
                    nums.pop();
                    char op = ops.top();
                    ops.pop();
                    if (op == '+') {
                        nums.push(a + b);
                    } else if (op == '-') {
                        nums.push(a - b);
                    } else if (op == '*') {
                        nums.push(a * b);
                    } else if (op == '/') {
                        nums.push(a / b);
                    }
                }
                ops.pop();
            } else {
                while (!ops.empty() && ops.top() != '(' && precedence(ops.top()) >= precedence(s[i])) {
                    int b = nums.top();
                    nums.pop();
                    int a = nums.top();
                    nums.pop();
                    char op = ops.top();
                    ops.pop();
                    if (op == '+') {
                        nums.push(a + b);
                    } else if (op == '-') {
                        nums.push(a - b);
                    } else if (op == '*') {
                        nums.push(a * b);
                    } else if (op == '/') {
                        nums.push(a / b);
                    }
                }
                ops.push(s[i]);
            }
            num = 0;
        }
    }
    if (num != 0) {
        nums.push(num);
    }
    while (!ops.empty()) {
        int b = nums.top();
        nums.pop();
        int a = nums.top();
        nums.pop();
        char op = ops.top();
        ops.pop();
        if (op == '+') {
            nums.push(a + b);
        } else if (op == '-') {
            nums.push(a - b);
        } else if (op == '*') {
            nums.push(a * b);
        } else if (op == '/') {
            nums.push(a / b);
        }
    }
    return nums.top();
}

int precedence(char op) {
    if (op == '+' || op == '-') {
        return 1;
    } else if (op == '*' || op == '/') {
        return 2;
    }
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string. This is because we only need to iterate through the string once.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the string. This is because we need to store the numbers and operators in the stacks.
> - **Optimality proof:** This approach has a time complexity of $O(n)$, which is optimal because we need to at least read the input string once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Stack-based approach, precedence of operators.
- Problem-solving patterns identified: Using stacks to evaluate expressions, handling parentheses.
- Optimization techniques learned: Using a stack-based approach to reduce time complexity.
- Similar problems to practice: Evaluating postfix expressions, parsing arithmetic expressions.

**Mistakes to Avoid:**
- Common implementation errors: Not handling parentheses correctly, not considering operator precedence.
- Edge cases to watch for: Empty input string, invalid input string, division by zero.
- Performance pitfalls: Using recursive approach for large inputs, not using stacks to evaluate expressions.
- Testing considerations: Test with different input strings, including empty string, invalid string, and strings with parentheses.