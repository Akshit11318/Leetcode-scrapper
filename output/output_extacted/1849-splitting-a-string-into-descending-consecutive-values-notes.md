## Splitting a String into Descending Consecutive Values

**Problem Link:** https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/description

**Problem Statement:**
- Input: A string `s` consisting of digits.
- Output: A list of integers representing a valid split of `s` into descending consecutive values, or an empty list if no such split exists.
- Key requirements:
  - The integers in the list must be in descending order.
  - Each integer must be a substring of `s`.
  - The integers must be consecutive, meaning the difference between any two adjacent integers in the list is 1.
- Edge cases:
  - Input string can be empty.
  - Input string can contain leading zeros.
  - No valid split exists if the string cannot be divided into descending consecutive integers.

**Example Test Cases:**
- Input: `s = "050043"`
  - Output: `[5, 4, 3]`
  - Explanation: The integers 5, 4, and 3 are in descending order, are consecutive, and are substrings of `s`.
- Input: `s = "9887"`
  - Output: `[9, 8, 7]`
  - Explanation: The integers 9, 8, and 7 are in descending order, are consecutive, and are substrings of `s`.
- Input: `s = "10009998"`
  - Output: `[]`
  - Explanation: There is no valid split of `s` into descending consecutive integers.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking all possible splits of the string into substrings that could represent integers.
- We then check if these integers are in descending order and consecutive.

```cpp
#include <vector>
#include <string>

std::vector<int> splitIntoDescendingConsecutiveValues(std::string s) {
    std::vector<int> result;
    // Try all possible lengths for the first number
    for (int len1 = 1; len1 <= s.length(); ++len1) {
        // Extract the first number
        int num1 = std::stoi(s.substr(0, len1));
        std::string remaining = s.substr(len1);
        // Initialize the result with the first number
        std::vector<int> currentResult = {num1};
        // Try to extend the current result with consecutive numbers
        while (!remaining.empty()) {
            int nextNum = num1 - 1;
            std::string nextNumStr = std::to_string(nextNum);
            // Check if the next number is a prefix of the remaining string
            if (remaining.find(nextNumStr) == 0) {
                currentResult.push_back(nextNum);
                remaining = remaining.substr(nextNumStr.length());
                num1 = nextNum;
            } else {
                break;
            }
        }
        // If we've used up the entire string and the numbers are in descending order, update the result
        if (remaining.empty() && currentResult.size() > result.size()) {
            result = currentResult;
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the string, because in the worst case, we might try all possible splits of the string.
> - **Space Complexity:** $O(n)$, for storing the result and the current split being considered.
> - **Why these complexities occur:** The brute force approach involves trying all possible splits of the string, which leads to exponential time complexity. The space complexity is linear because we only need to store the current split and the result.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a backtracking approach to try all possible splits of the string into descending consecutive integers.
- We start with the first integer and try to extend it with consecutive integers.
- If we reach a point where we cannot extend the current split further, we backtrack and try a different split.

```cpp
#include <vector>
#include <string>

std::vector<int> splitIntoDescendingConsecutiveValues(std::string s) {
    std::vector<int> result;
    std::function<void(int, std::string, std::vector<int>)> backtrack =
        [&](int start, std::string remaining, std::vector<int> current) {
            if (remaining.empty()) {
                if (current.size() > result.size()) {
                    result = current;
                }
                return;
            }
            for (int len = 1; len <= remaining.length(); ++len) {
                std::string substr = remaining.substr(0, len);
                if (substr[0] == '0' && substr.length() > 1) {
                    continue;
                }
                int num = std::stoi(substr);
                if (current.empty() || num == current.back() - 1) {
                    current.push_back(num);
                    backtrack(start, remaining.substr(len), current);
                    current.pop_back();
                }
            }
        };
    backtrack(0, s, {});
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the string, because in the worst case, we might try all possible splits of the string.
> - **Space Complexity:** $O(n)$, for storing the result and the current split being considered.
> - **Optimality proof:** This approach is optimal because it tries all possible splits of the string into descending consecutive integers, and it uses backtracking to efficiently explore the search space.

---

### Final Notes

**Learning Points:**
- The problem requires a deep understanding of string manipulation and integer parsing.
- The optimal approach uses backtracking to efficiently explore the search space.
- The problem demonstrates the importance of considering all possible splits of the string.

**Mistakes to Avoid:**
- Not considering all possible lengths for the first integer.
- Not checking if the next integer is a prefix of the remaining string.
- Not using backtracking to efficiently explore the search space.
- Not handling edge cases, such as an empty input string or a string with leading zeros.