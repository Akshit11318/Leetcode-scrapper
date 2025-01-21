## Minimum Length of String After Operations
**Problem Link:** https://leetcode.com/problems/minimum-length-of-string-after-operations/description

**Problem Statement:**
- Input format and constraints: The problem takes a string `s` as input, which consists of lowercase English letters.
- Expected output format: The expected output is the minimum length of the string after performing a series of operations, where each operation involves removing a pair of adjacent characters that are the same.
- Key requirements and edge cases to consider:
  - The input string only contains lowercase English letters.
  - The string can be empty.
  - The operations should be performed until no more pairs of adjacent characters are the same.
- Example test cases with explanations:
  - Input: "aabaa" - Output: 0 - Explanation: Remove 'a' from the start and end of the string, then remove the remaining 'a's.
  - Input: "letsgodigital" - Output: 2 - Explanation: No pairs of adjacent characters are the same, so the string remains the same.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to iterate through the string, checking for pairs of adjacent characters that are the same, and removing them.
- Step-by-step breakdown of the solution:
  1. Initialize an empty stack to store the characters.
  2. Iterate through each character in the string.
  3. If the stack is not empty and the current character is the same as the top of the stack, pop the top of the stack.
  4. Otherwise, push the current character onto the stack.
  5. After iterating through the entire string, the size of the stack represents the minimum length of the string after operations.

```cpp
#include <iostream>
#include <stack>
#include <string>

int min_length(const std::string& s) {
    std::stack<char> stack;
    for (char c : s) {
        if (!stack.empty() && stack.top() == c) {
            stack.pop();
        } else {
            stack.push(c);
        }
    }
    return stack.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string. This is because we iterate through each character in the string once.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the string. This is because in the worst-case scenario, we might need to store all characters in the stack.
> - **Why these complexities occur:** The time complexity occurs because we iterate through each character in the string once. The space complexity occurs because we use a stack to store the characters.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution is the same as the brute force approach, as it already has a time complexity of $O(n)$ and a space complexity of $O(n)$.
- Detailed breakdown of the approach:
  1. Initialize an empty stack to store the characters.
  2. Iterate through each character in the string.
  3. If the stack is not empty and the current character is the same as the top of the stack, pop the top of the stack.
  4. Otherwise, push the current character onto the stack.
  5. After iterating through the entire string, the size of the stack represents the minimum length of the string after operations.
- Proof of optimality: The optimal solution is the same as the brute force approach because it already has a time complexity of $O(n)$ and a space complexity of $O(n)$. This is the best possible time and space complexity for this problem, as we must at least read the input string once.

```cpp
#include <iostream>
#include <stack>
#include <string>

int min_length(const std::string& s) {
    std::stack<char> stack;
    for (char c : s) {
        if (!stack.empty() && stack.top() == c) {
            stack.pop();
        } else {
            stack.push(c);
        }
    }
    return stack.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string. This is because we iterate through each character in the string once.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the string. This is because in the worst-case scenario, we might need to store all characters in the stack.
> - **Optimality proof:** The optimal solution is the same as the brute force approach because it already has a time complexity of $O(n)$ and a space complexity of $O(n)$. This is the best possible time and space complexity for this problem, as we must at least read the input string once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the use of a stack to solve a problem that involves removing pairs of adjacent characters that are the same.
- Problem-solving patterns identified: The problem requires identifying a pattern in the input string and using a stack to remove pairs of adjacent characters that are the same.
- Optimization techniques learned: The problem does not require any optimization techniques beyond using a stack to solve the problem efficiently.
- Similar problems to practice: Similar problems to practice include problems that involve using a stack to solve a problem, such as evaluating the validity of parentheses in a string.

**Mistakes to Avoid:**
- Common implementation errors: A common implementation error is to forget to check if the stack is empty before popping the top of the stack.
- Edge cases to watch for: An edge case to watch for is an empty input string, which should return 0.
- Performance pitfalls: A performance pitfall is to use a naive approach that involves iterating through the string multiple times, which can result in a time complexity of $O(n^2)$.
- Testing considerations: Testing considerations include testing the function with different input strings, including an empty string, and verifying that the function returns the correct result.