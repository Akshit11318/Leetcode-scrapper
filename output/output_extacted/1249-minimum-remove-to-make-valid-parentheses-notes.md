## Minimum Remove to Make Valid Parentheses

**Problem Link:** https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/description

**Problem Statement:**
- Input: A string containing parentheses, represented as a sequence of characters.
- Input format and constraints: The input string `s` is a string of length `n`, where `1 <= n <= 10^4`.
- Expected output format: The function should return the minimum number of parentheses that need to be removed to make the string valid.
- Key requirements and edge cases to consider: A string of parentheses is considered valid if every open parenthesis has a corresponding closing parenthesis, and vice versa. The function should return the modified string with the minimum number of parentheses removed to make it valid.
- Example test cases with explanations:
  - Example 1: Input: `s = "lee(t(c)o)de)"`, Output: `"lee(t(c)o)de"`. Explanation: We remove the last ')' to make the string valid.
  - Example 2: Input: `s = "a)b(c)"`, Output: `"ab(c)"`. Explanation: We remove the first ')' and the first '(' to make the string valid.
  - Example 3: Input: `s = "(a(b(c)d)"`, Output: `"a(b(c)d)"`. Explanation: We remove the first '(' to make the string valid.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves generating all possible combinations of removing parentheses from the string and checking if the resulting string is valid.
- Step-by-step breakdown of the solution:
  1. Generate all possible combinations of removing parentheses from the string.
  2. For each combination, check if the resulting string is valid by using a stack to keep track of the opening parentheses.
  3. If the string is valid, count the number of removed parentheses.
  4. Return the minimum count of removed parentheses among all valid combinations.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it is not efficient due to the large number of combinations.

```cpp
#include <iostream>
#include <string>
#include <vector>

std::string minRemoveToMakeValid(std::string s) {
    std::vector<std::string> validStrings;
    std::vector<std::string> combinations;
    combinations.push_back(s);

    // Generate all possible combinations of removing parentheses
    for (int i = 0; i < s.size(); i++) {
        if (s[i] == '(' || s[i] == ')') {
            std::vector<std::string> newCombinations;
            for (const auto& combination : combinations) {
                std::string newCombination = combination;
                newCombination.erase(i, 1);
                newCombinations.push_back(newCombination);
            }
            combinations.insert(combinations.end(), newCombinations.begin(), newCombinations.end());
        }
    }

    // Check if each combination is valid
    for (const auto& combination : combinations) {
        std::string validCombination = combination;
        bool isValid = true;
        std::vector<int> indicesToRemove;

        for (int i = 0; i < combination.size(); i++) {
            if (combination[i] == '(') {
                indicesToRemove.push_back(i);
            } else if (combination[i] == ')') {
                if (indicesToRemove.empty()) {
                    indicesToRemove.push_back(i);
                } else {
                    indicesToRemove.pop_back();
                }
            }
        }

        for (int i = indicesToRemove.size() - 1; i >= 0; i--) {
            validCombination.erase(indicesToRemove[i], 1);
        }

        if (indicesToRemove.empty()) {
            validStrings.push_back(validCombination);
        }
    }

    // Return the minimum valid string
    std::string minValidString = validStrings[0];
    for (const auto& validString : validStrings) {
        if (validString.size() < minValidString.size()) {
            minValidString = validString;
        }
    }

    return minValidString;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the input string. This is because we generate all possible combinations of removing parentheses, which is $2^n$, and then check if each combination is valid, which takes $O(n)$ time.
> - **Space Complexity:** $O(2^n \cdot n)$, as we store all possible combinations of removing parentheses.
> - **Why these complexities occur:** The brute force approach involves generating all possible combinations of removing parentheses, which results in exponential time and space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of generating all possible combinations of removing parentheses, we can use a stack to keep track of the indices of the parentheses that need to be removed.
- Detailed breakdown of the approach:
  1. Initialize an empty stack to store the indices of the opening parentheses.
  2. Iterate through the string and push the indices of the opening parentheses onto the stack.
  3. When we encounter a closing parenthesis, check if the stack is empty. If it is, mark the closing parenthesis for removal. If the stack is not empty, pop the index of the corresponding opening parenthesis from the stack.
  4. After iterating through the string, mark any remaining opening parentheses in the stack for removal.
  5. Create a new string by removing the marked parentheses.
- Proof of optimality: This approach is optimal because it only requires a single pass through the string and uses a stack to keep track of the indices of the parentheses that need to be removed.

```cpp
#include <iostream>
#include <string>
#include <stack>

std::string minRemoveToMakeValid(std::string s) {
    std::stack<int> indicesToRemove;
    std::vector<int> removeIndices;

    // Mark parentheses for removal
    for (int i = 0; i < s.size(); i++) {
        if (s[i] == '(') {
            indicesToRemove.push(i);
        } else if (s[i] == ')') {
            if (indicesToRemove.empty()) {
                removeIndices.push_back(i);
            } else {
                indicesToRemove.pop();
            }
        }
    }

    // Add remaining opening parentheses to removeIndices
    while (!indicesToRemove.empty()) {
        removeIndices.push_back(indicesToRemove.top());
        indicesToRemove.pop();
    }

    // Create a new string by removing the marked parentheses
    std::string result;
    for (int i = 0; i < s.size(); i++) {
        if (std::find(removeIndices.begin(), removeIndices.end(), i) == removeIndices.end()) {
            result += s[i];
        }
    }

    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string. This is because we only need to iterate through the string once to mark the parentheses for removal.
> - **Space Complexity:** $O(n)$, as we use a stack to store the indices of the opening parentheses and a vector to store the indices of the parentheses to remove.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the string and uses a stack to keep track of the indices of the parentheses that need to be removed, resulting in linear time and space complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a stack to keep track of indices of parentheses that need to be removed.
- Problem-solving patterns identified: Identifying the need to remove parentheses to make the string valid and using a stack to efficiently keep track of the indices.
- Optimization techniques learned: Avoiding the generation of all possible combinations of removing parentheses and instead using a stack to mark parentheses for removal.

**Mistakes to Avoid:**
- Common implementation errors: Not properly handling the case where the stack is empty when encountering a closing parenthesis.
- Edge cases to watch for: Handling the case where the input string is empty or contains only one parenthesis.
- Performance pitfalls: Using the brute force approach, which results in exponential time and space complexity.
- Testing considerations: Testing the function with different input strings, including edge cases, to ensure it produces the correct output.