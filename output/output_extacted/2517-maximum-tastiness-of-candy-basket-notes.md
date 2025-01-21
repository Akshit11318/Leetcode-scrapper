## Maximum Tastiness of Candy Basket
**Problem Link:** https://leetcode.com/problems/maximum-tastiness-of-candy-basket/description

**Problem Statement:**
- Input format and constraints: Given an array `price` of size `n`, and an integer `k`, we need to find the maximum tastiness of a candy basket, where the tastiness of a candy basket is the sum of the absolute differences in prices of adjacent candies.
- Expected output format: The maximum tastiness of a candy basket.
- Key requirements and edge cases to consider: The candies must be selected in ascending order of their prices, and we can select at most `k` candies.
- Example test cases with explanations:
  - Example 1: `price = [1, 3, 1, 2, 4, 1], k = 3`, Output: `24`. We can select candies with prices `1, 2, 4`.
  - Example 2: `price = [9, 7, 6, 7, 6, 8, 5], k = 3`, Output: `25`. We can select candies with prices `5, 7, 9`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can generate all possible combinations of `k` candies and calculate the tastiness of each combination.
- Step-by-step breakdown of the solution:
  1. Generate all possible combinations of `k` candies.
  2. For each combination, calculate the tastiness by summing the absolute differences in prices of adjacent candies.
  3. Return the maximum tastiness found.
- Why this approach comes to mind first: It is a straightforward approach that considers all possible combinations of candies.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int maxTastiness(std::vector<int>& price, int k) {
    std::sort(price.begin(), price.end());
    int n = price.size();
    int maxTastiness = 0;

    // Generate all possible combinations of k candies
    for (int i = 0; i < (1 << n); i++) {
        std::vector<int> combination;
        for (int j = 0; j < n; j++) {
            if ((i & (1 << j)) != 0) {
                combination.push_back(price[j]);
            }
        }

        // Check if the combination has exactly k candies
        if (combination.size() == k) {
            int tastiness = 0;
            for (int j = 1; j < k; j++) {
                tastiness += std::abs(combination[j] - combination[j - 1]);
            }

            // Update the maximum tastiness
            maxTastiness = std::max(maxTastiness, tastiness);
        }
    }

    return maxTastiness;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot k)$, where $n$ is the number of candies and $k$ is the number of candies to select. This is because we generate all possible combinations of candies and calculate the tastiness of each combination.
> - **Space Complexity:** $O(n)$, where $n$ is the number of candies. This is because we need to store the prices of the candies and the current combination.
> - **Why these complexities occur:** The brute force approach has a high time complexity because it considers all possible combinations of candies, which grows exponentially with the number of candies.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a dynamic programming approach to store the maximum tastiness for each subproblem.
- Detailed breakdown of the approach:
  1. Sort the prices of the candies in ascending order.
  2. Create a 2D table `dp` where `dp[i][j]` represents the maximum tastiness that can be achieved by selecting `j` candies from the first `i` candies.
  3. Fill the `dp` table using the following recurrence relation: `dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + abs(price[i] - price[i-1]))`.
  4. Return the maximum tastiness stored in the `dp` table.
- Proof of optimality: The dynamic programming approach ensures that we consider all possible combinations of candies and calculate the maximum tastiness efficiently.

```cpp
int maxTastiness(std::vector<int>& price, int k) {
    std::sort(price.begin(), price.end());
    int n = price.size();
    std::vector<std::vector<int>> dp(n + 1, std::vector<int>(k + 1, 0));

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= k; j++) {
            dp[i][j] = dp[i - 1][j];
            if (j > 0) {
                for (int prev = 0; prev < i; prev++) {
                    dp[i][j] = std::max(dp[i][j], dp[prev][j - 1] + std::abs(price[i - 1] - price[prev - 1]));
                }
            }
        }
    }

    return dp[n][k];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot k)$, where $n$ is the number of candies and $k$ is the number of candies to select. This is because we fill the `dp` table using a nested loop.
> - **Space Complexity:** $O(n \cdot k)$, where $n$ is the number of candies and $k$ is the number of candies to select. This is because we need to store the `dp` table.
> - **Optimality proof:** The dynamic programming approach ensures that we consider all possible combinations of candies and calculate the maximum tastiness efficiently, resulting in an optimal solution.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, sorting, and iteration.
- Problem-solving patterns identified: Breaking down the problem into smaller subproblems and using a recursive approach.
- Optimization techniques learned: Using a dynamic programming approach to store the maximum tastiness for each subproblem.
- Similar problems to practice: Other dynamic programming problems, such as the knapsack problem or the longest common subsequence problem.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the `dp` table correctly or not considering all possible combinations of candies.
- Edge cases to watch for: Handling cases where the number of candies is less than or equal to the number of candies to select.
- Performance pitfalls: Using a brute force approach that has a high time complexity.
- Testing considerations: Testing the solution with different inputs and edge cases to ensure correctness.