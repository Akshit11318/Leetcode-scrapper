## Parse Lisp Expression

**Problem Link:** https://leetcode.com/problems/parse-lisp-expression/description

**Problem Statement:**
- Input format: A string `expression` representing a valid Lisp expression.
- Constraints: The input expression is a valid Lisp expression.
- Expected output format: The value of the evaluated Lisp expression.
- Key requirements and edge cases to consider:
  - Handling nested parentheses.
  - Evaluating integers and operations (`+`, `-`, `*`, `/`).
  - Handling invalid expressions.
- Example test cases with explanations:
  - `evaluate("(add 1 2)" )` returns `3`.
  - `evaluate("(multiply 3 (add 2 3))" )` returns `15`.
  - `evaluate("(let x 2 (multiply x 5))" )` returns `10`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Start by parsing the input string to identify the operation and operands.
- Step-by-step breakdown of the solution:
  1. Parse the input string to extract the operation and operands.
  2. Use a stack to evaluate the expression.
  3. Handle nested parentheses by pushing and popping from the stack.
- Why this approach comes to mind first: It is a straightforward way to evaluate a Lisp expression by following the order of operations.

```cpp
class Solution {
public:
    int evaluate(string expression) {
        stack<int> s;
        int num = 0;
        char op = '+';
        
        for (int i = 0; i < expression.size(); i++) {
            if (isdigit(expression[i])) {
                num = num * 10 + expression[i] - '0';
            } else if (expression[i] == '(') {
                // Handle nested parentheses
                int j = i + 1;
                int count = 1;
                while (count != 0) {
                    if (expression[j] == '(') count++;
                    if (expression[j] == ')') count--;
                    j++;
                }
                string sub = expression.substr(i + 1, j - i - 2);
                num = evaluate(sub);
                i = j - 1;
            } else {
                if (op == '+') s.push(num);
                else if (op == '-') s.push(-num);
                else if (op == '*') s.push(s.top() * num), s.pop();
                else if (op == '/') s.push(s.top() / num), s.pop();
                op = expression[i];
                num = 0;
            }
        }
        
        if (op == '+') s.push(num);
        else if (op == '-') s.push(-num);
        else if (op == '*') s.push(s.top() * num), s.pop();
        else if (op == '/') s.push(s.top() / num), s.pop();
        
        int sum = 0;
        while (!s.empty()) {
            sum += s.top();
            s.pop();
        }
        
        return sum;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string. This is because we are parsing the input string once.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input string. This is because we are using a stack to evaluate the expression.
> - **Why these complexities occur:** These complexities occur because we are parsing the input string and using a stack to evaluate the expression.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a recursive approach to evaluate the Lisp expression.
- Detailed breakdown of the approach:
  1. Parse the input string to extract the operation and operands.
  2. Use a recursive function to evaluate the expression.
  3. Handle nested parentheses by recursively calling the function.
- Proof of optimality: This approach is optimal because it has a time complexity of $O(n)$ and a space complexity of $O(n)$, which is the best we can achieve for this problem.

```cpp
class Solution {
public:
    int evaluate(string expression) {
        int pos = 1;
        return parse(expression, pos);
    }
    
    int parse(string& expression, int& pos) {
        int result = 0;
        bool isNegative = false;
        
        if (expression[pos] == '-') {
            isNegative = true;
            pos++;
        }
        
        while (pos < expression.size()) {
            if (isdigit(expression[pos])) {
                int num = 0;
                while (pos < expression.size() && isdigit(expression[pos])) {
                    num = num * 10 + expression[pos] - '0';
                    pos++;
                }
                if (isNegative) result -= num;
                else result += num;
            } else if (expression[pos] == '(') {
                pos++;
                int num = parse(expression, pos);
                if (isNegative) result -= num;
                else result += num;
            } else if (expression[pos] == ')') {
                pos++;
                break;
            } else if (expression[pos] == '+') {
                pos++;
                isNegative = false;
            } else if (expression[pos] == '-') {
                pos++;
                isNegative = true;
            } else if (expression[pos] == '*') {
                pos++;
                int num = parse(expression, pos);
                result *= num;
            } else if (expression[pos] == '/') {
                pos++;
                int num = parse(expression, pos);
                result /= num;
            }
        }
        
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string. This is because we are parsing the input string once.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input string. This is because we are using a recursive function to evaluate the expression.
> - **Optimality proof:** This approach is optimal because it has a time complexity of $O(n)$ and a space complexity of $O(n)$, which is the best we can achieve for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Recursive parsing, stack-based evaluation, and recursive function calls.
- Problem-solving patterns identified: Handling nested parentheses, evaluating expressions, and using recursive functions.
- Optimization techniques learned: Using recursive functions to simplify the solution.
- Similar problems to practice: Evaluating postfix expressions, parsing JSON data, and implementing recursive descent parsers.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle nested parentheses, not checking for invalid input, and not using recursive functions correctly.
- Edge cases to watch for: Handling empty input strings, single-character input strings, and input strings with only whitespace characters.
- Performance pitfalls: Using inefficient algorithms, not optimizing the solution for large input strings, and not handling recursive function calls correctly.
- Testing considerations: Testing the solution with different input strings, including valid and invalid expressions, and checking for correct output and error handling.