## Clear Digits
**Problem Link:** https://leetcode.com/problems/clear-digits/description

**Problem Statement:**
- Input: A string `s` containing only digits.
- Output: The minimum number of operations required to clear all digits from the string.
- Key Requirements: 
  - The operation allowed is to remove a substring of digits if it starts with `0`.
  - The goal is to minimize the number of operations.
- Edge Cases: 
  - The string may be empty.
  - The string may contain no zeros.
  - The string may contain consecutive zeros.
- Example Test Cases:
  - Input: `s = "00110"`, Output: `2`
  - Input: `s = "000111000"`, Output: `2`

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Try all possible substrings that start with `0` and count the minimum number of operations to clear all digits.
- Step-by-step breakdown:
  1. Generate all possible substrings of `s`.
  2. Check if a substring starts with `0`.
  3. If it does, remove the substring and update the string `s`.
  4. Repeat steps 1-3 until no more substrings starting with `0` can be found.
- Why this approach comes to mind first: It directly follows from the problem statement, allowing for a straightforward implementation.

```cpp
#include <iostream>
#include <string>
using namespace std;

int minOperations(string s) {
    int operations = 0;
    while (true) {
        bool found = false;
        for (int i = 0; i < s.length(); i++) {
            if (s[i] == '0') {
                // Find the longest substring starting with '0'
                int j = i + 1;
                while (j < s.length() && s[j] != '0') {
                    j++;
                }
                // Remove the substring
                s.erase(i, j - i);
                operations++;
                found = true;
                break;
            }
        }
        if (!found) {
            break;
        }
    }
    return operations;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the string `s`, because in the worst case, we are removing one character at a time.
> - **Space Complexity:** $O(n)$, because we are modifying the string `s` in place.
> - **Why these complexities occur:** The nested loop structure leads to the quadratic time complexity, and the string modification leads to the linear space complexity.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight: Instead of trying all possible substrings, we can use a stack to keep track of the substrings starting with `0`.
- Detailed breakdown:
  1. Initialize an empty stack.
  2. Iterate through the string `s`. If we encounter a `0`, push it onto the stack.
  3. If we encounter a `1` and the stack is not empty, pop the stack until we find a `0` or the stack is empty.
  4. The number of operations is equal to the number of times we pushed `0` onto the stack.
- Proof of optimality: This approach is optimal because it only considers the substrings starting with `0` and removes them in a single operation, minimizing the number of operations.

```cpp
int minOperationsOptimal(string s) {
    int operations = 0;
    for (char c : s) {
        if (c == '0') {
            operations++;
        }
    }
    return operations;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string `s`, because we are iterating through the string once.
> - **Space Complexity:** $O(1)$, because we are only using a constant amount of space to store the operations count.
> - **Optimality proof:** This approach is optimal because it only counts the number of `0`s in the string, which is the minimum number of operations required to clear all digits.

---

### Final Notes
**Learning Points:**
- Key algorithmic concepts demonstrated: Greedy algorithm, stack data structure.
- Problem-solving patterns identified: Finding the minimum number of operations to solve a problem.
- Optimization techniques learned: Using a stack to keep track of substrings starting with `0`.
- Similar problems to practice: Other problems involving string manipulation and minimum number of operations.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as an empty string or a string with no zeros.
- Edge cases to watch for: Consecutive zeros, zeros at the beginning or end of the string.
- Performance pitfalls: Using a brute force approach that leads to quadratic time complexity.
- Testing considerations: Test the function with different inputs, including edge cases and large inputs.