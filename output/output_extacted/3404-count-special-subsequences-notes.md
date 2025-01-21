## Count Special Subsequences
**Problem Link:** https://leetcode.com/problems/count-special-subsequences/description

**Problem Statement:**
- Input format and constraints: The problem provides a binary string `s` and asks to count the number of special subsequences, where a special subsequence is a subsequence that starts with a `0` and ends with a `1`.
- Expected output format: The number of special subsequences.
- Key requirements and edge cases to consider: The input string `s` only contains `0`s and `1`s, and the length of `s` is less than or equal to $10^5$.
- Example test cases with explanations:
  - Example 1: Input `s = "1011"`, Output `2`. Explanation: The special subsequences are `01` and `011`.
  - Example 2: Input `s = "1111"`, Output `0`. Explanation: There are no special subsequences.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: The first approach that comes to mind is to generate all possible subsequences of the input string `s` and check if each subsequence is special.
- Step-by-step breakdown of the solution:
  1. Generate all possible subsequences of `s`.
  2. For each subsequence, check if it starts with a `0` and ends with a `1`.
  3. Count the number of special subsequences.
- Why this approach comes to mind first: It is a straightforward approach that involves generating all possible subsequences and checking each one.

```cpp
#include <iostream>
#include <vector>
#include <string>

int countSpecialSubsequences(const std::string& s) {
    int count = 0;
    int n = s.length();
    for (int mask = 1; mask < (1 << n); mask++) {
        std::string subsequence;
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) != 0) {
                subsequence += s[i];
            }
        }
        if (!subsequence.empty() && subsequence[0] == '0' && subsequence[subsequence.length() - 1] == '1') {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the input string `s`. This is because we generate all possible subsequences of `s`, and for each subsequence, we check if it is special.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input string `s`. This is because we need to store the subsequence.
> - **Why these complexities occur:** The time complexity occurs because we generate all possible subsequences, and the space complexity occurs because we need to store the subsequence.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We can use dynamic programming to solve this problem. We can maintain two arrays, `zero` and `one`, where `zero[i]` is the number of special subsequences ending at index `i` that start with a `0` and `one[i]` is the number of special subsequences ending at index `i` that end with a `1`.
- Detailed breakdown of the approach:
  1. Initialize the `zero` and `one` arrays.
  2. Iterate through the input string `s`. For each character, update the `zero` and `one` arrays.
  3. The final answer is the sum of all `one[i]` values.
- Proof of optimality: This approach is optimal because it has a time complexity of $O(n)$ and a space complexity of $O(n)$, which is the best possible time and space complexity for this problem.

```cpp
int countSpecialSubsequences(const std::string& s) {
    int n = s.length();
    int zero = 0, one = 0;
    for (int i = 0; i < n; i++) {
        if (s[i] == '0') {
            zero = (zero * 2) + 1;
        } else {
            one = (one * 2) + zero;
        }
    }
    return one;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string `s`. This is because we iterate through the input string `s` once.
> - **Space Complexity:** $O(1)$, where $n$ is the length of the input string `s`. This is because we only use a constant amount of space to store the `zero` and `one` variables.
> - **Optimality proof:** This approach is optimal because it has a time complexity of $O(n)$ and a space complexity of $O(1)$, which is the best possible time and space complexity for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, bit manipulation.
- Problem-solving patterns identified: Using dynamic programming to solve problems that have overlapping subproblems.
- Optimization techniques learned: Using bit manipulation to reduce the time complexity of the solution.
- Similar problems to practice: Other problems that involve counting special subsequences, such as counting the number of increasing subsequences in an array.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the `zero` and `one` arrays correctly, not updating the `zero` and `one` arrays correctly.
- Edge cases to watch for: The input string `s` is empty, the input string `s` contains only `0`s or only `1`s.
- Performance pitfalls: Using a brute force approach that has a high time complexity, not using dynamic programming to solve the problem.
- Testing considerations: Testing the solution with different input strings, testing the solution with edge cases.