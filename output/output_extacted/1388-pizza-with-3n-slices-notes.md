## Pizza with 3n Slices
**Problem Link:** https://leetcode.com/problems/pizza-with-3n-slices/description

**Problem Statement:**
- Input format and constraints: The problem takes an array of integers `slices` as input, representing the number of slices for each pizza type, and an integer `n`, representing the total number of slices to choose. The input array is guaranteed to have a length of `3n`, where `n` is the number of slices to choose.
- Expected output format: The problem requires finding the maximum number of slices that can be chosen, given that no more than one slice of each type can be chosen.
- Key requirements and edge cases to consider: The key requirement is to choose `n` slices such that the total number of slices is maximized. Edge cases include handling empty input arrays, arrays with a single element, and arrays where `n` is greater than the length of the array.
- Example test cases with explanations:
  - For the input `slices = [1, 2, 3, 4, 5, 6]` and `n = 3`, the maximum number of slices that can be chosen is `10`, which is achieved by choosing slices with values `1`, `3`, and `6`.
  - For the input `slices = [8, 9, 8, 6, 1, 1]` and `n = 3`, the maximum number of slices that can be chosen is `16`, which is achieved by choosing slices with values `8`, `8`, and `0` (note that we cannot choose a slice with value `0` as it is not present in the input array, but we can choose slices with values `8`, `8`, and `0` if we consider the actual values of the slices).

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The initial thought process is to try all possible combinations of `n` slices and calculate the total number of slices for each combination.
- Step-by-step breakdown of the solution:
  1. Generate all possible combinations of `n` slices from the input array.
  2. For each combination, calculate the total number of slices.
  3. Keep track of the maximum total number of slices found so far.
- Why this approach comes to mind first: This approach comes to mind first because it is a straightforward and intuitive solution that tries all possible combinations of slices.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int maxSlices(vector<int>& slices, int n) {
    int maxSlices = 0;
    vector<bool> used(slices.size(), false);
    function<void(int, int, int)> backtrack = [&](int start, int count, int sum) {
        if (count == n) {
            maxSlices = max(maxSlices, sum);
            return;
        }
        for (int i = start; i < slices.size(); ++i) {
            if (!used[i]) {
                used[i] = true;
                backtrack(i + 1, count + 1, sum + slices[i]);
                used[i] = false;
            }
        }
    };
    backtrack(0, 0, 0);
    return maxSlices;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(3n \choose n)$, where ${3n \choose n}$ is the number of ways to choose `n` slices from `3n` slices. This is because we are trying all possible combinations of `n` slices.
> - **Space Complexity:** $O(3n)$, where `3n` is the size of the input array. This is because we need to store the input array and the `used` array.
> - **Why these complexities occur:** These complexities occur because we are trying all possible combinations of `n` slices, which results in an exponential time complexity. The space complexity is linear because we need to store the input array and the `used` array.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The key insight is to use dynamic programming to solve the problem. We can define a 2D array `dp` where `dp[i][j]` represents the maximum number of slices that can be chosen from the first `i` slices with `j` slices chosen.
- Detailed breakdown of the approach:
  1. Initialize a 2D array `dp` with size `(slices.size() + 1) x (n + 1)`.
  2. For each slice, consider two options: choose the slice or not choose the slice.
  3. If we choose the slice, we need to make sure that we do not choose the same slice again.
  4. If we do not choose the slice, we can move on to the next slice.
- Proof of optimality: The dynamic programming approach is optimal because it considers all possible combinations of slices and chooses the optimal combination.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int maxSlices(vector<int>& slices, int n) {
    int m = slices.size();
    vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
    for (int i = 1; i <= m; ++i) {
        for (int j = 1; j <= n; ++j) {
            dp[i][j] = dp[i - 1][j];
            if (j >= 1) {
                dp[i][j] = max(dp[i][j], dp[max(0, i - 2)][j - 1] + slices[i - 1]);
            }
        }
    }
    return dp[m][n];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(3n \cdot n)$, where `3n` is the size of the input array and `n` is the number of slices to choose. This is because we are using a 2D array to store the dynamic programming table.
> - **Space Complexity:** $O(3n \cdot n)$, where `3n` is the size of the input array and `n` is the number of slices to choose. This is because we need to store the dynamic programming table.
> - **Optimality proof:** The dynamic programming approach is optimal because it considers all possible combinations of slices and chooses the optimal combination. The time and space complexities are also optimal because we are using a 2D array to store the dynamic programming table, which has a size of `O(3n \cdot n)`.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, recursion, and memoization.
- Problem-solving patterns identified: The problem can be solved using a recursive approach with memoization, or using dynamic programming.
- Optimization techniques learned: The dynamic programming approach is an optimization technique that reduces the time complexity from exponential to polynomial.
- Similar problems to practice: Other problems that can be solved using dynamic programming, such as the knapsack problem, the Fibonacci sequence, and the longest common subsequence problem.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the dynamic programming table correctly, not considering the base cases correctly, and not using memoization correctly.
- Edge cases to watch for: Handling empty input arrays, arrays with a single element, and arrays where `n` is greater than the length of the array.
- Performance pitfalls: Using a recursive approach without memoization, which can result in exponential time complexity.
- Testing considerations: Testing the solution with different input arrays and values of `n`, and verifying that the solution produces the correct output.