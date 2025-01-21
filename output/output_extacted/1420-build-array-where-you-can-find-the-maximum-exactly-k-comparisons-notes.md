## Build Array Where You Can Find The Maximum Exactly K Comparisons

**Problem Link:** https://leetcode.com/problems/build-array-where-you-can-find-the-maximum-exactly-k-comparisons/description

**Problem Statement:**
- Given an integer `n` and an integer `k`, return the length of the longest array that can be built such that the maximum value in the array appears exactly `k` times.
- Input format: `n` and `k` are integers.
- Expected output format: The length of the longest array.
- Key requirements and edge cases to consider: `1 <= n <= 4`, `1 <= k <= 25`.
- Example test cases with explanations:
  - Input: `n = 3`, `k = 1`
    - Output: `3`
    - Explanation: The array `[1, 2, 3]` has a maximum value of `3`, which appears exactly once.
  - Input: `n = 3`, `k = 2`
    - Output: `3`
    - Explanation: The array `[1, 3, 3]` has a maximum value of `3`, which appears exactly twice.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can start by generating all possible arrays of length up to `n` and then check each array to see if the maximum value appears exactly `k` times.
- Step-by-step breakdown of the solution:
  1. Generate all possible arrays of length up to `n`.
  2. For each array, find the maximum value and count the number of times it appears.
  3. If the maximum value appears exactly `k` times, update the length of the longest array.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it has a high time complexity due to the generation of all possible arrays.

```cpp
#include <vector>
#include <algorithm>
#include <iostream>

int longestArray(int n, int k) {
    int maxLength = 0;
    for (int len = 1; len <= n; len++) {
        for (int i = 0; i < (1 << len); i++) {
            std::vector<int> arr;
            for (int j = 0; j < len; j++) {
                if (i & (1 << j)) {
                    arr.push_back(n);
                } else {
                    arr.push_back(j + 1);
                }
            }
            int maxVal = *std::max_element(arr.begin(), arr.end());
            int count = std::count(arr.begin(), arr.end(), maxVal);
            if (count == k) {
                maxLength = std::max(maxLength, len);
            }
        }
    }
    return maxLength;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the input integer.
> - **Space Complexity:** $O(n)$, where $n$ is the input integer.
> - **Why these complexities occur:** The time complexity is high due to the generation of all possible arrays, and the space complexity is moderate due to the storage of each array.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a dynamic programming approach to build up the longest array.
- Detailed breakdown of the approach:
  1. Initialize a 2D array `dp` of size `(n + 1) x (k + 1)` to store the length of the longest array for each subproblem.
  2. For each `i` from `1` to `n`, for each `j` from `1` to `k`, calculate the length of the longest array by considering two cases: including the maximum value or not including it.
  3. Update the `dp` array with the maximum length found.
- Proof of optimality: This approach is optimal because it uses a dynamic programming approach to build up the solution, avoiding redundant calculations.

```cpp
#include <vector>
#include <algorithm>
#include <iostream>

int longestArray(int n, int k) {
    std::vector<std::vector<int>> dp(n + 1, std::vector<int>(k + 1, 0));
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= k; j++) {
            if (j == 1) {
                dp[i][j] = i;
            } else {
                dp[i][j] = std::max(dp[i - 1][j], dp[i - 1][j - 1] + 1);
            }
        }
    }
    return dp[n][k];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot k)$, where $n$ is the input integer and $k$ is the number of comparisons.
> - **Space Complexity:** $O(n \cdot k)$, where $n$ is the input integer and $k$ is the number of comparisons.
> - **Optimality proof:** This approach is optimal because it uses a dynamic programming approach to build up the solution, avoiding redundant calculations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming.
- Problem-solving patterns identified: Building up a solution using a dynamic programming approach.
- Optimization techniques learned: Avoiding redundant calculations using dynamic programming.
- Similar problems to practice: Other dynamic programming problems.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the `dp` array correctly.
- Edge cases to watch for: Handling the case where `k` is `1`.
- Performance pitfalls: Not using dynamic programming to avoid redundant calculations.
- Testing considerations: Testing the function with different inputs to ensure correctness.