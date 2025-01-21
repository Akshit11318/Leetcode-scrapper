## Lexicographically Minimum String After Removing Stars

**Problem Link:** https://leetcode.com/problems/lexicographically-minimum-string-after-removing-stars/description

**Problem Statement:**
- Input: A string `s` containing lowercase letters and stars (`*`).
- Constraints: The length of `s` is between 1 and 200,000.
- Expected Output: The lexicographically smallest string that can be obtained by removing the stars.
- Key Requirements: 
  - The removal of stars should result in a string where each character is the smallest possible lexicographically.
  - The order of characters after removal should maintain the original order as much as possible.
- Edge Cases:
  - Empty string.
  - String with only stars.
  - String with no stars.

Example Test Cases:
- Input: `"xy"*b""`
  Output: `"xb"`
- Input: `"a*b"`
  Output: `"ab"`
- Input: `"a*c"`
  Output: `"ac"`

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves iterating through the string and removing the stars one by one, considering all possible combinations of removals to find the lexicographically smallest string.
- Step-by-step breakdown:
  1. Generate all possible strings by removing stars.
  2. Compare each generated string lexicographically.
  3. Select the smallest one.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

void removeStarsUtil(std::string s, int index, std::string &current, std::vector<std::string> &results) {
    if (index == s.size()) {
        results.push_back(current);
        return;
    }

    if (s[index] == '*') {
        removeStarsUtil(s, index + 1, current, results);
    } else {
        current += s[index];
        removeStarsUtil(s, index + 1, current, results);
    }
}

std::string removeStarsBruteForce(std::string s) {
    std::vector<std::string> results;
    removeStarsUtil(s, 0, "", results);

    std::string minStr = results[0];
    for (const auto &str : results) {
        if (str < minStr) {
            minStr = str;
        }
    }

    return minStr;
}

int main() {
    std::string s = "xy*b";
    std::cout << removeStarsBruteForce(s) << std::endl;
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$ where $n$ is the number of stars in the string, due to considering all possible combinations of removing stars.
> - **Space Complexity:** $O(2^n)$ for storing all generated strings.
> - **Why these complexities occur:** The brute force approach generates all possible strings, leading to exponential time and space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Utilize a stack data structure to keep track of characters. When a star is encountered, pop the last character from the stack if it's not empty.
- Detailed breakdown:
  1. Initialize an empty stack.
  2. Iterate through the string. If the character is not a star, push it onto the stack. If it is a star, pop the top element from the stack if it's not empty.
  3. After iterating through the entire string, the stack contains the characters of the lexicographically smallest string.

```cpp
#include <iostream>
#include <stack>
#include <string>

std::string removeStarsOptimal(std::string s) {
    std::stack<char> stk;
    for (char c : s) {
        if (c == '*') {
            if (!stk.empty()) {
                stk.pop();
            }
        } else {
            stk.push(c);
        }
    }

    std::string result;
    while (!stk.empty()) {
        result.push_back(stk.top());
        stk.pop();
    }

    // Reverse the string to maintain the original order
    std::reverse(result.begin(), result.end());
    return result;
}

int main() {
    std::string s = "xy*b";
    std::cout << removeStarsOptimal(s) << std::endl;
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the length of the input string, as each character is processed once.
> - **Space Complexity:** $O(n)$ for the stack in the worst case (when no stars are present).
> - **Optimality proof:** This approach is optimal because it processes each character exactly once and uses a stack to efficiently remove characters when a star is encountered, resulting in a linear time complexity.

---

### Final Notes

**Learning Points:**
- Utilizing a stack to efficiently remove characters.
- The importance of considering the order of operations (e.g., pushing and popping from the stack).
- The trade-off between time and space complexity in different approaches.

**Mistakes to Avoid:**
- Not considering edge cases (e.g., empty string, string with only stars).
- Incorrectly handling the order of characters after removing stars.
- Not optimizing the solution for large input sizes.

By following the optimal approach, you can efficiently solve the problem of finding the lexicographically minimum string after removing stars, with a significant improvement in time and space complexity compared to the brute force method.