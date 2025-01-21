## Basic Calculator II
**Problem Link:** [https://leetcode.com/problems/basic-calculator-ii/description](https://leetcode.com/problems/basic-calculator-ii/description)

**Problem Statement:**
- Input format and constraints: The input is a string `s` containing digits and operators (`+`, `-`, `*`, `/`). The string does not contain any whitespace characters.
- Expected output format: The output is the result of evaluating the expression in the input string.
- Key requirements and edge cases to consider: The expression may contain parentheses, and the operators have the usual precedence rules (`*` and `/` have higher precedence than `+` and `-`).
- Example test cases with explanations:
  - Input: `s = "3+2*2"`
    - Output: `7`
    - Explanation: First, multiply 2 and 2 to get 4, then add 3 and 4 to get 7.
  - Input: `s = " 3/2 `"
    - Output: `1`
    - Explanation: Divide 3 by 2 to get 1.5, but since the result should be an integer, it is truncated to 1.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to use a recursive approach to evaluate the expression. We can start by checking if the current character is a digit or an operator. If it is a digit, we can add it to the current number. If it is an operator, we can recursively evaluate the expression on the left and right sides of the operator.
- Step-by-step breakdown of the solution:
  1. Start by initializing an empty stack to store the intermediate results.
  2. Iterate over the input string from left to right.
  3. If the current character is a digit, add it to the current number.
  4. If the current character is an operator, recursively evaluate the expression on the left and right sides of the operator.
  5. Push the result of the recursive evaluation onto the stack.
  6. After iterating over the entire input string, the final result will be the only element left in the stack.

```cpp
int calculate(string s) {
    stack<int> st;
    int num = 0;
    char sign = '+';
    for (int i = 0; i < s.length(); i++) {
        if (isdigit(s[i])) {
            num = num * 10 + s[i] - '0';
        }
        if ((!isdigit(s[i]) && !isspace(s[i])) || i == s.length() - 1) {
            if (sign == '+') {
                st.push(num);
            } else if (sign == '-') {
                st.push(-num);
            } else if (sign == '*') {
                int prev = st.top();
                st.pop();
                st.push(prev * num);
            } else if (sign == '/') {
                int prev = st.top();
                st.pop();
                st.push(prev / num);
            }
            sign = s[i];
            num = 0;
        }
    }
    int res = 0;
    while (!st.empty()) {
        res += st.top();
        st.pop();
    }
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the length of the input string, because we iterate over the input string once.
> - **Space Complexity:** $O(n)$ because in the worst case, we may need to push all characters onto the stack.
> - **Why these complexities occur:** The time complexity occurs because we iterate over the input string once, and the space complexity occurs because we use a stack to store the intermediate results.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of using recursion, we can use a stack to evaluate the expression. We can iterate over the input string from left to right, and whenever we encounter an operator, we can push the current number and the operator onto the stack.
- Detailed breakdown of the approach:
  1. Initialize an empty stack to store the intermediate results.
  2. Initialize the current number to 0.
  3. Iterate over the input string from left to right.
  4. If the current character is a digit, add it to the current number.
  5. If the current character is an operator, push the current number and the operator onto the stack.
  6. If the current character is a `(`, push it onto the stack.
  7. If the current character is a `)`, pop elements from the stack until we encounter a `(`, and evaluate the expression inside the parentheses.
  8. After iterating over the entire input string, the final result will be the only element left in the stack.
- Proof of optimality: This solution has a time complexity of $O(n)$ and a space complexity of $O(n)$, which is optimal because we need to iterate over the input string at least once to evaluate the expression, and we need to use a stack to store the intermediate results.

```cpp
int calculate(string s) {
    stack<int> st;
    int num = 0;
    char sign = '+';
    for (int i = 0; i < s.length(); i++) {
        if (isdigit(s[i])) {
            num = num * 10 + s[i] - '0';
        }
        if ((!isdigit(s[i]) && !isspace(s[i])) || i == s.length() - 1) {
            if (sign == '+') {
                st.push(num);
            } else if (sign == '-') {
                st.push(-num);
            } else if (sign == '*') {
                int prev = st.top();
                st.pop();
                st.push(prev * num);
            } else if (sign == '/') {
                int prev = st.top();
                st.pop();
                st.push(prev / num);
            }
            sign = s[i];
            num = 0;
        }
    }
    int res = 0;
    while (!st.empty()) {
        res += st.top();
        st.pop();
    }
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the length of the input string, because we iterate over the input string once.
> - **Space Complexity:** $O(n)$ because in the worst case, we may need to push all characters onto the stack.
> - **Optimality proof:** This solution has a time complexity of $O(n)$ and a space complexity of $O(n)$, which is optimal because we need to iterate over the input string at least once to evaluate the expression, and we need to use a stack to store the intermediate results.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a stack to evaluate an expression, handling operators with different precedence levels.
- Problem-solving patterns identified: Breaking down a complex problem into smaller sub-problems, using a stack to store intermediate results.
- Optimization techniques learned: Using a stack to avoid recursion, handling operators with different precedence levels.
- Similar problems to practice: Evaluating expressions with parentheses, handling operators with different precedence levels.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle the case where the input string is empty, forgetting to handle the case where the input string contains only whitespace characters.
- Edge cases to watch for: Handling the case where the input string contains a `(` but no corresponding `)`, handling the case where the input string contains a `)` but no corresponding `(`.
- Performance pitfalls: Using recursion instead of a stack, not handling operators with different precedence levels correctly.
- Testing considerations: Testing the function with different input strings, testing the function with input strings that contain different operators and precedence levels.