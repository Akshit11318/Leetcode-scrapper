## Brace Expansion
**Problem Link:** https://leetcode.com/problems/brace-expansion/description

**Problem Statement:**
- Input format: A string `expression` containing `'{', '}', ','`, and lowercase English letters.
- Constraints: The input string is non-empty and contains only valid characters.
- Expected output format: A list of strings representing all possible expansions of the input string, sorted in lexicographical order.
- Key requirements and edge cases to consider: Handling nested brackets, duplicate characters, and empty strings.
- Example test cases with explanations:
  - Input: `"a{b,c}"` Output: `["ab", "ac"]`
  - Input: `"a{b,c,d}"` Output: `["ab", "ac", "ad"]`

---

### Brute Force Approach
**Explanation:**
- Initial thought process: The brute force approach involves generating all possible expansions by recursively exploring all branches of the input string.
- Step-by-step breakdown of the solution:
  1. Initialize an empty list to store the expanded strings.
  2. Define a recursive function to generate all possible expansions.
  3. In the recursive function, iterate over each character in the input string.
  4. If the character is a letter, append it to the current expansion.
  5. If the character is an opening bracket, recursively generate all expansions of the substring inside the brackets.
  6. If the character is a comma, start a new expansion by appending the current expansion to the result list and resetting the current expansion.
  7. If the character is a closing bracket, return the current expansion.
- Why this approach comes to mind first: The brute force approach is often the most straightforward solution, as it involves simply generating all possible expansions without considering any optimizations.

```cpp
#include <vector>
#include <string>

void expand(const std::string& expression, int start, std::string& current, std::vector<std::string>& result) {
    if (start == expression.size()) {
        result.push_back(current);
        return;
    }
    
    if (expression[start] == '{') {
        int end = start + 1;
        while (expression[end] != '}') {
            end++;
        }
        std::string options = expression.substr(start + 1, end - start - 1);
        size_t commaPos = options.find(',');
        while (commaPos != std::string::npos) {
            std::string option = options.substr(0, commaPos);
            expand(expression, end + 1, current + option, result);
            options = options.substr(commaPos + 1);
            commaPos = options.find(',');
        }
        expand(expression, end + 1, current + options, result);
    } else {
        current += expression[start];
        expand(expression, start + 1, current, result);
    }
}

std::vector<std::string> braceExpansionII(const std::string& expression) {
    std::vector<std::string> result;
    std::string current;
    expand(expression, 0, current, result);
    std::sort(result.begin(), result.end());
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n \cdot m \cdot \log(m))$, where $n$ is the length of the input string, $m$ is the maximum number of expansions of a single substring, and $\log(m)$ is due to sorting.
> - **Space Complexity:** $O(2^n \cdot n)$, as we store all possible expansions in the result list.
> - **Why these complexities occur:** The time complexity is due to the recursive generation of all possible expansions, and the space complexity is due to storing all expansions in the result list.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Using a stack to keep track of the current expansion and the options to be expanded.
- Detailed breakdown of the approach:
  1. Initialize an empty stack to store the current expansions and options.
  2. Iterate over each character in the input string.
  3. If the character is a letter, append it to the current expansion.
  4. If the character is an opening bracket, push the current expansion and the opening bracket onto the stack.
  5. If the character is a comma, push the current expansion onto the stack.
  6. If the character is a closing bracket, pop the stack until the opening bracket is found, and expand the current expansion with the options.
- Proof of optimality: The optimal approach has a time complexity of $O(2^n \cdot n \cdot m \cdot \log(m))$, which is the same as the brute force approach, but with improved space complexity.

```cpp
#include <vector>
#include <string>
#include <stack>

std::vector<std::string> braceExpansionII(const std::string& expression) {
    std::stack<std::vector<std::string>> stack;
    std::vector<std::string> result = {""};
    
    for (char c : expression) {
        if (c == '{') {
            stack.push(result);
            result = {""};
        } else if (c == ',') {
            std::vector<std::string> temp = result;
            result = stack.top();
            stack.pop();
            std::vector<std::string> newResult;
            for (const std::string& r : result) {
                for (const std::string& t : temp) {
                    newResult.push_back(r + t);
                }
            }
            result = newResult;
            stack.push(result);
            result = {""};
        } else if (c == '}') {
            std::vector<std::string> temp = result;
            result = stack.top();
            stack.pop();
            std::vector<std::string> newResult;
            for (const std::string& r : result) {
                for (const std::string& t : temp) {
                    newResult.push_back(r + t);
                }
            }
            result = newResult;
        } else {
            std::vector<std::string> newResult;
            for (const std::string& r : result) {
                newResult.push_back(r + c);
            }
            result = newResult;
        }
    }
    
    std::sort(result.begin(), result.end());
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n \cdot m \cdot \log(m))$, where $n$ is the length of the input string, $m$ is the maximum number of expansions of a single substring, and $\log(m)$ is due to sorting.
> - **Space Complexity:** $O(2^n \cdot n)$, as we store all possible expansions in the result list.
> - **Optimality proof:** The optimal approach has the same time complexity as the brute force approach, but with improved space complexity due to using a stack to keep track of the current expansion and options.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Recursion, stack operations, and sorting.
- Problem-solving patterns identified: Using a stack to keep track of the current expansion and options.
- Optimization techniques learned: Using a stack to improve space complexity.
- Similar problems to practice: Other string manipulation problems, such as substring searching and pattern matching.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly handling edge cases, such as empty strings or nested brackets.
- Edge cases to watch for: Handling duplicate characters and empty strings.
- Performance pitfalls: Using inefficient data structures or algorithms, such as using a list instead of a stack.
- Testing considerations: Thoroughly testing the implementation with various input cases, including edge cases.