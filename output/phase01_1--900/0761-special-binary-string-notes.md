## Special Binary String

**Problem Link:** https://leetcode.com/problems/special-binary-string/description

**Problem Statement:**
- Input: A string `s` consisting of only `1`s and `?`s.
- Output: A string of `1`s and `0`s, with no leading zeros, that matches the given pattern.
- Key Requirements:
  - Replace each `?` in `s` with either `1` or `0`.
  - Ensure the resulting string has no leading zeros.
- Edge Cases:
  - `s` can be empty.
  - `s` can contain only `1`s or only `?`s.

**Example Test Cases:**
- Input: `s = "1??0"`
  - Output: `"1100"`
- Input: `s = "0??"`
  - Output: `"000"`
- Input: `s = "1??1"`
  - Output: `"1111"`

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves trying all possible combinations of `1`s and `0`s in place of `?`s.
- For each combination, we check if the resulting string meets the criteria (no leading zeros).
- If it does, we have found a valid solution.

```cpp
#include <iostream>
#include <vector>
#include <string>

void backtrack(std::string& s, int index, std::string& current) {
    if (index == s.length()) {
        // Check if the current string has no leading zeros
        bool valid = true;
        for (int i = 0; i < current.length(); ++i) {
            if (current[i] == '0' && i == 0) {
                valid = false;
                break;
            }
        }
        if (valid) {
            std::cout << current << std::endl;
        }
        return;
    }

    if (s[index] == '?') {
        current += '0';
        backtrack(s, index + 1, current);
        current.pop_back();

        current += '1';
        backtrack(s, index + 1, current);
        current.pop_back();
    } else {
        current += s[index];
        backtrack(s, index + 1, current);
        current.pop_back();
    }
}

void bruteForce(std::string s) {
    std::string current;
    backtrack(s, 0, current);
}

int main() {
    std::string s = "1??0";
    bruteForce(s);
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, where $n$ is the number of `?`s in the string, because we try both `1` and `0` for each `?`.
> - **Space Complexity:** $O(n)$, due to the recursion stack and the storage of the current string.
> - **Why these complexities occur:** The brute force approach tries all possible combinations, leading to exponential time complexity. The space complexity is linear due to the recursion stack.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a stack-based approach to ensure that the resulting string has no leading zeros.
- We iterate through the string and push `1`s onto the stack.
- When we encounter a `?`, we check if the stack is empty. If it is, we push a `1` onto the stack (to avoid leading zeros). If the stack is not empty, we push a `0` onto the stack.
- Finally, we pop all elements from the stack and append them to the result string.

```cpp
#include <iostream>
#include <stack>
#include <string>

std::string optimalApproach(std::string s) {
    std::stack<char> stack;
    for (char c : s) {
        if (c == '1') {
            stack.push('1');
        } else if (c == '0') {
            if (!stack.empty()) {
                stack.pop();
            }
        } else {
            if (stack.empty()) {
                stack.push('1');
            } else {
                stack.push('0');
            }
        }
    }

    std::string result;
    while (!stack.empty()) {
        result = stack.top() + result;
        stack.pop();
    }
    return result;
}

int main() {
    std::string s = "1??0";
    std::cout << optimalApproach(s) << std::endl;
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string, because we iterate through the string once.
> - **Space Complexity:** $O(n)$, due to the storage of the stack.
> - **Optimality proof:** This approach is optimal because it avoids trying all possible combinations and instead uses a stack to efficiently construct the result string.

---

### Final Notes

**Learning Points:**
- The importance of using stacks to solve problems involving string manipulation and parsing.
- The need to consider edge cases, such as leading zeros, when solving string manipulation problems.
- The use of recursion and iteration to solve problems involving string manipulation.

**Mistakes to Avoid:**
- Trying all possible combinations of `1`s and `0`s, which can lead to exponential time complexity.
- Not considering edge cases, such as leading zeros, which can result in incorrect solutions.
- Not using efficient data structures, such as stacks, to solve problems involving string manipulation.