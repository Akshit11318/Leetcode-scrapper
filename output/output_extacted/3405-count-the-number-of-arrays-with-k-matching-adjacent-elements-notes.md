## Count the Number of Arrays with K Matching Adjacent Elements

**Problem Link:** https://leetcode.com/problems/count-the-number-of-arrays-with-k-matching-adjacent-elements/description

**Problem Statement:**
- Input: An integer `n` and an integer `k`.
- Expected output: The number of arrays of length `n` with exactly `k` pairs of adjacent elements that are the same.
- Key requirements and edge cases to consider: `1 <= n <= 1000`, `0 <= k <= n - 1`, and the possibility of `k` being 0.
- Example test cases with explanations:
  - For `n = 3` and `k = 1`, there are 6 arrays: `[1, 1, 2]`, `[1, 2, 1]`, `[2, 1, 1]`, `[2, 2, 1]`, `[1, 2, 2]`, and `[2, 1, 2]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible arrays of length `n` and count the number of arrays with exactly `k` pairs of adjacent elements that are the same.
- Step-by-step breakdown of the solution:
  1. Initialize a counter for the number of valid arrays.
  2. Generate all possible arrays of length `n`.
  3. For each array, count the number of pairs of adjacent elements that are the same.
  4. If the count is equal to `k`, increment the counter.
- Why this approach comes to mind first: It is a straightforward and intuitive solution that involves checking all possible arrays.

```cpp
#include <iostream>
#include <vector>

int countArrays(int n, int k) {
    int count = 0;
    // Generate all possible arrays of length n
    for (int i = 0; i < (1 << (n * 2)); i++) {
        std::vector<int> arr;
        for (int j = 0; j < n; j++) {
            arr.push_back((i >> (j * 2)) & 3);
        }
        int pairs = 0;
        // Count the number of pairs of adjacent elements that are the same
        for (int j = 0; j < n - 1; j++) {
            if (arr[j] == arr[j + 1]) {
                pairs++;
            }
        }
        // If the count is equal to k, increment the counter
        if (pairs == k) {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{2n} \cdot n)$, where $n$ is the length of the array. This is because we generate all possible arrays of length `n` and count the number of pairs of adjacent elements that are the same for each array.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the array. This is because we store the current array in memory.
> - **Why these complexities occur:** The time complexity is high because we generate all possible arrays of length `n`, which is an exponential operation. The space complexity is low because we only store the current array in memory.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use dynamic programming to store the number of arrays with a certain number of pairs of adjacent elements that are the same.
- Detailed breakdown of the approach:
  1. Initialize a 2D array `dp` where `dp[i][j]` represents the number of arrays of length `i` with exactly `j` pairs of adjacent elements that are the same.
  2. Fill the `dp` array using the following recurrence relation: `dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1] * (i - 1)`.
  3. The final answer is stored in `dp[n][k]`.
- Proof of optimality: This approach has a time complexity of $O(n^2)$, which is much better than the brute force approach.

```cpp
#include <iostream>
#include <vector>

int countArrays(int n, int k) {
    std::vector<std::vector<int>> dp(n + 1, std::vector<int>(k + 1, 0));
    dp[1][0] = 1;
    for (int i = 2; i <= n; i++) {
        for (int j = 0; j <= k; j++) {
            dp[i][j] = dp[i - 1][j] * 2;
            if (j > 0) {
                dp[i][j] += dp[i - 1][j - 1];
            }
        }
    }
    return dp[n][k];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the array. This is because we fill the `dp` array using a nested loop.
> - **Space Complexity:** $O(n^2)$, where $n$ is the length of the array. This is because we store the `dp` array in memory.
> - **Optimality proof:** This approach is optimal because it uses dynamic programming to store the number of arrays with a certain number of pairs of adjacent elements that are the same, which reduces the time complexity from exponential to quadratic.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, recurrence relations.
- Problem-solving patterns identified: Using dynamic programming to store the number of arrays with a certain number of pairs of adjacent elements that are the same.
- Optimization techniques learned: Reducing the time complexity from exponential to quadratic using dynamic programming.
- Similar problems to practice: Other problems that involve counting the number of arrays with certain properties.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the `dp` array correctly, not filling the `dp` array correctly.
- Edge cases to watch for: When `k` is 0, when `n` is 1.
- Performance pitfalls: Using the brute force approach, which has a high time complexity.
- Testing considerations: Testing the function with different values of `n` and `k`, testing the function with edge cases.