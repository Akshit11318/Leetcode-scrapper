## Difference Between Maximum and Minimum Price Sum
**Problem Link:** https://leetcode.com/problems/difference-between-maximum-and-minimum-price-sum/description

**Problem Statement:**
- Input: An array of integers `prices` representing the prices of items and a target sum `k`.
- Output: Find the difference between the maximum and minimum price sums that can be obtained by selecting a subset of items such that their sum equals `k`.
- Key requirements:
  - The prices array may contain negative numbers.
  - The target sum `k` is always non-negative.
- Edge cases:
  - If no subset sums up to `k`, return -1.
- Example test cases:
  - `prices = [1, 3, 4], k = 5` should return `1`, as the maximum price sum is `4 + 1 = 5` and the minimum price sum is `3 + 1 + 1 = 5`, and their difference is `4 - 3 = 1`.
  - `prices = [1, 2, 3, 4], k = 10` should return `-1`, as no subset sums up to `10`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking all possible subsets of the `prices` array to find those that sum up to `k`.
- Step-by-step breakdown:
  1. Generate all possible subsets of the `prices` array.
  2. For each subset, calculate its sum.
  3. If the sum equals `k`, store it as a potential maximum or minimum price sum.
  4. After checking all subsets, find the maximum and minimum price sums stored, and return their difference.
- Why this approach comes to mind first: It's a straightforward, exhaustive search that guarantees finding all subsets that sum up to `k`, if any exist.

```cpp
#include <vector>
#include <algorithm>
#include <climits>

int maxAndMinPriceSum(std::vector<int>& prices, int k) {
    int minSum = INT_MAX, maxSum = INT_MIN;
    int n = prices.size();
    
    // Generate all possible subsets
    for (int mask = 0; mask < (1 << n); ++mask) {
        int subsetSum = 0;
        
        // Calculate the sum of the current subset
        for (int i = 0; i < n; ++i) {
            if ((mask & (1 << i))) {
                subsetSum += prices[i];
            }
        }
        
        // Check if the subset sum equals k
        if (subsetSum == k) {
            minSum = std::min(minSum, subsetSum);
            maxSum = std::max(maxSum, subsetSum);
        }
    }
    
    // If no subset sums up to k, return -1
    if (minSum == INT_MAX) {
        return -1;
    }
    
    return maxSum - minSum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the number of items in the `prices` array. This is because we generate all possible subsets (which is $2^n$) and for each subset, we calculate its sum (which takes $O(n)$ time).
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the minimum and maximum sums, and do not use any data structures that scale with the input size.
> - **Why these complexities occur:** The exponential time complexity comes from the brute-force generation of all subsets, and the linear factor within the exponential term comes from calculating the sum of each subset.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: The problem can be solved using dynamic programming, specifically by using a 2D array `dp` where `dp[i][j]` represents the minimum price sum that can be achieved using the first `i` items to reach a sum of `j`.
- Detailed breakdown:
  1. Initialize a 2D array `dp` of size `(n + 1) x (k + 1)` with all elements set to `INT_MAX`, except for `dp[0][0] = 0`.
  2. Iterate over each item `i` from 1 to `n`, and for each possible sum `j` from 1 to `k`, update `dp[i][j]` to be the minimum of its current value and the value of `dp[i-1][j]` (not including the current item) or `dp[i-1][j-prices[i-1]] + prices[i-1]` (including the current item), provided that `j - prices[i-1] >= 0`.
  3. After filling the `dp` array, the minimum price sum that reaches `k` is stored in `dp[n][k]`. To find the maximum price sum, we can similarly fill another 2D array `dpMax` but update its values to keep track of the maximum sum instead.
- Proof of optimality: This approach is optimal because it avoids the exponential time complexity of the brute-force approach by only considering each item and each possible sum once, resulting in a polynomial time complexity.

```cpp
#include <vector>
#include <algorithm>
#include <climits>

int maxAndMinPriceSum(std::vector<int>& prices, int k) {
    int n = prices.size();
    std::vector<std::vector<int>> dpMin(n + 1, std::vector<int>(k + 1, INT_MAX));
    std::vector<std::vector<int>> dpMax(n + 1, std::vector<int>(k + 1, INT_MIN));
    
    dpMin[0][0] = 0;
    dpMax[0][0] = 0;
    
    for (int i = 1; i <= n; ++i) {
        for (int j = 0; j <= k; ++j) {
            dpMin[i][j] = dpMin[i-1][j];
            dpMax[i][j] = dpMax[i-1][j];
            
            if (j - prices[i-1] >= 0) {
                dpMin[i][j] = std::min(dpMin[i][j], dpMin[i-1][j-prices[i-1]] + prices[i-1]);
                dpMax[i][j] = std::max(dpMax[i][j], dpMax[i-1][j-prices[i-1]] + prices[i-1]);
            }
        }
    }
    
    if (dpMin[n][k] == INT_MAX) {
        return -1;
    }
    
    return dpMax[n][k] - dpMin[n][k];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot k)$, where $n$ is the number of items and $k$ is the target sum. This is because we fill a 2D array of size $(n + 1) \times (k + 1)$.
> - **Space Complexity:** $O(n \cdot k)$, as we use two 2D arrays of size $(n + 1) \times (k + 1)$ to store the minimum and maximum price sums for each subproblem.
> - **Optimality proof:** This approach is optimal because it solves the problem in polynomial time, avoiding the exponential time complexity of the brute-force approach, and it uses dynamic programming to efficiently compute the solution by breaking the problem into smaller subproblems and solving each subproblem only once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: Dynamic programming, subset sum problem.
- Problem-solving patterns: Breaking down the problem into smaller subproblems and solving each subproblem only once.
- Optimization techniques: Using dynamic programming to avoid redundant computation and reduce time complexity.
- Similar problems to practice: Knapsack problem, subset sum problem, 0/1 knapsack problem.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the `dp` array correctly, not handling the base case properly.
- Edge cases to watch for: When the target sum `k` is 0, when the `prices` array is empty.
- Performance pitfalls: Using a brute-force approach for large inputs, not using dynamic programming to reduce time complexity.
- Testing considerations: Test the function with different inputs, including edge cases, to ensure it works correctly.