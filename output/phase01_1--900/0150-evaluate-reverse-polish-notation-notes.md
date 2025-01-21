## Evaluate Reverse Polish Notation
**Problem Link:** https://leetcode.com/problems/evaluate-reverse-polish-notation/description

**Problem Statement:**
- Input format: An array of strings `tokens` representing a valid Reverse Polish notation expression.
- Constraints: `1 <= tokens.length <= 104`, `tokens[i]` is either an operator (`+`, `-`, `*`, `/`) or a number.
- Expected output format: The result of the evaluated Reverse Polish notation expression.
- Key requirements and edge cases to consider:
  - Handle operators and operands correctly.
  - Divide by zero is undefined, so avoid it or handle it according to the problem statement.
- Example test cases with explanations:
  - `["2","1","+","3","*"]` should return `9` because `(2 + 1) * 3 = 9`.
  - `["4","13","5","/","+" ]` should return `6` because `4 + (13 / 5) = 6`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Evaluate each token from left to right, applying operators as soon as they are encountered.
- Step-by-step breakdown of the solution:
  1. Parse each token in the input array.
  2. If the token is a number, store it.
  3. If the token is an operator, apply it to the last two numbers in the stored list.
  4. Repeat steps 1-3 until all tokens have been processed.
- Why this approach comes to mind first: It directly follows the definition of Reverse Polish notation, where operators follow their operands.

```cpp
#include <vector>
#include <string>
#include <stdexcept>

int evalRPN(std::vector<std::string>& tokens) {
    std::vector<int> stack;
    for (const auto& token : tokens) {
        if (token == "+" || token == "-" || token == "*" || token == "/") {
            if (stack.size() < 2) {
                throw std::invalid_argument("Invalid RPN expression");
            }
            int b = stack.back();
            stack.pop_back();
            int a = stack.back();
            stack.pop_back();
            if (token == "+") {
                stack.push_back(a + b);
            } else if (token == "-") {
                stack.push_back(a - b);
            } else if (token == "*") {
                stack.push_back(a * b);
            } else if (token == "/") {
                stack.push_back(a / b);
            }
        } else {
            stack.push_back(std::stoi(token));
        }
    }
    if (stack.size() != 1) {
        throw std::invalid_argument("Invalid RPN expression");
    }
    return stack[0];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of tokens, because each token is processed once.
> - **Space Complexity:** $O(n)$, because in the worst case, all tokens could be operands, and we store them in the stack.
> - **Why these complexities occur:** The algorithm iterates through each token once and uses a stack to store operands, leading to linear time and space complexities.

---

### Optimal Approach (Required)

The provided brute force approach is already optimal for this problem because it processes each token exactly once and uses a stack to efficiently handle operators and operands. Therefore, no further optimization is needed.

**Explanation:**
- Key insight that leads to optimal solution: Using a stack to store operands and apply operators as soon as they are encountered.
- Detailed breakdown of the approach: The same as the brute force approach, as it is already optimal.
- Proof of optimality: Any algorithm must at least read the input, so the time complexity cannot be less than $O(n)$. The space complexity is also optimal because we must store the operands somewhere.

```cpp
// Same code as the brute force approach, as it is already optimal
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$
> - **Space Complexity:** $O(n)$
> - **Optimality proof:** The algorithm has the minimum possible time complexity because it must read the input, and the space complexity is necessary to store the operands.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a stack to parse and evaluate postfix expressions.
- Problem-solving patterns identified: Processing tokens in a specific order and applying operators as soon as possible.
- Optimization techniques learned: Using data structures like stacks to efficiently handle temporary storage needs.
- Similar problems to practice: Other problems involving parsing expressions, such as prefix or infix notation.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly handling the order of operations or not validating the input.
- Edge cases to watch for: Divide by zero, invalid input, or expressions that are not valid Reverse Polish notation.
- Performance pitfalls: Using inefficient data structures or algorithms that have higher time or space complexities than necessary.
- Testing considerations: Thoroughly test with various inputs, including edge cases, to ensure the solution is robust.