## Valid Parentheses

**Problem Link:** https://leetcode.com/problems/valid-parentheses/description

**Problem Statement:**
- Input format and constraints: Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid. The brackets must close in the correct order, `"()"` and `"()[]{}"` are all valid but `"(]"` and `"([)]"` are not.
- Expected output format: Return `true` if the string is valid, and `false` otherwise.
- Key requirements and edge cases to consider: Handling different types of brackets, empty strings, and strings with only one type of bracket.
- Example test cases with explanations:
  - `s = "()"` returns `true` because the brackets are properly nested.
  - `s = "()[]{}"` returns `true` because all brackets are properly nested.
  - `s = "(]"` returns `false` because the brackets are not properly nested.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to manually check each character and try to match it with its corresponding closing bracket. This involves a lot of conditional checks and manual tracking of the brackets.
- Step-by-step breakdown of the solution:
  1. Start with an empty stack.
  2. Iterate over each character in the string.
  3. If the character is an opening bracket, push it onto the stack.
  4. If the character is a closing bracket, check if the stack is empty or if the top of the stack does not match the current closing bracket. If either condition is true, return `false`.
  5. After iterating over the entire string, if the stack is empty, return `true`. Otherwise, return `false`.

```cpp
#include <iostream>
#include <stack>
#include <string>
#include <unordered_map>

bool isValid(std::string s) {
    std::stack<char> stack;
    std::unordered_map<char, char> bracketMap = {
        {')', '('},
        {']', '['},
        {'}', '{'}
    };

    for (char c : s) {
        if (c == '(' || c == '[' || c == '{') {
            stack.push(c);
        } else if (c == ')' || c == ']' || c == '}') {
            if (stack.empty() || stack.top() != bracketMap[c]) {
                return false;
            }
            stack.pop();
        }
    }

    return stack.empty();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string. This is because we iterate over the string once.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input string. This is because in the worst-case scenario, we might have to push all characters onto the stack.
> - **Why these complexities occur:** The time complexity occurs because of the single pass through the input string, and the space complexity occurs because of the use of a stack to store the opening brackets.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution is actually the same as the brute force approach in this case, because we must check each character in the string at least once to determine if the brackets are properly nested.
- Detailed breakdown of the approach:
  1. Use a stack to keep track of the opening brackets.
  2. Iterate over the string, pushing opening brackets onto the stack and popping the corresponding opening bracket when a closing bracket is encountered.
  3. If a closing bracket is encountered when the stack is empty, or if the top of the stack does not match the current closing bracket, return `false`.
- Proof of optimality: This solution is optimal because it only requires a single pass through the input string, and it uses a stack to efficiently keep track of the opening brackets.

```cpp
#include <iostream>
#include <stack>
#include <string>
#include <unordered_map>

bool isValid(std::string s) {
    std::stack<char> stack;
    std::unordered_map<char, char> bracketMap = {
        {')', '('},
        {']', '['},
        {'}', '{'}
    };

    for (char c : s) {
        if (c == '(' || c == '[' || c == '{') {
            stack.push(c);
        } else if (c == ')' || c == ']' || c == '}') {
            if (stack.empty() || stack.top() != bracketMap[c]) {
                return false;
            }
            stack.pop();
        }
    }

    return stack.empty();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input string.
> - **Optimality proof:** This solution is optimal because it only requires a single pass through the input string, and it uses a stack to efficiently keep track of the opening brackets.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a stack to keep track of opening brackets, and iterating over the input string to check for properly nested brackets.
- Problem-solving patterns identified: The use of a stack to solve problems that involve nested or hierarchical structures.
- Optimization techniques learned: The importance of only iterating over the input string once, and using a stack to efficiently keep track of the opening brackets.
- Similar problems to practice: Other problems that involve using a stack to solve problems with nested or hierarchical structures, such as checking for balanced parentheses in a string.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to check if the stack is empty before popping an element, or not properly handling the case where a closing bracket is encountered when the stack is empty.
- Edge cases to watch for: Empty strings, strings with only one type of bracket, and strings with nested brackets.
- Performance pitfalls: Using a data structure that is not efficient for the problem, such as using a list instead of a stack to keep track of the opening brackets.
- Testing considerations: Testing the function with a variety of input strings, including empty strings, strings with only one type of bracket, and strings with nested brackets.