## Paint House II

**Problem Link:** https://leetcode.com/problems/paint-house-ii/description

**Problem Statement:**
- Input format and constraints: The problem takes as input a 2D vector `costs` where `costs[i][j]` is the cost of painting the `i-th` house with the `j-th` color. The number of houses is `n = costs.size()` and the number of colors is `k = costs[0].size()`. The constraints are `2 <= n <= 100`, `2 <= k <= 100`, and `1 <= costs[i][j] <= 100`.
- Expected output format: The function should return the minimum cost to paint all houses.
- Key requirements and edge cases to consider: The key requirement is that no two adjacent houses can have the same color.
- Example test cases with explanations:
  - Example 1: `costs = [[1,5,3],[2,9,4]]`, the output should be `5`. The minimum cost to paint the first house with color 0 (cost 1) and the second house with color 2 (cost 4) is 5.
  - Example 2: `costs = [[1,3,5],[2,4,6]]`, the output should be `4`. The minimum cost to paint the first house with color 0 (cost 1) and the second house with color 1 (cost 3) is 4.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves trying all possible color combinations for each house and calculating the total cost for each combination.
- Step-by-step breakdown of the solution:
  1. Initialize the minimum cost to infinity.
  2. Iterate over all possible color combinations for each house.
  3. For each combination, calculate the total cost.
  4. Update the minimum cost if the current cost is less than the minimum cost.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it has a high time complexity.

```cpp
class Solution {
public:
    int minCostII(vector<vector<int>>& costs) {
        int n = costs.size();
        if (n == 0) return 0;
        int k = costs[0].size();
        vector<vector<int>> dp(n, vector<int>(k, 0));
        for (int j = 0; j < k; j++) {
            dp[0][j] = costs[0][j];
        }
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < k; j++) {
                int minCost = INT_MAX;
                for (int m = 0; m < k; m++) {
                    if (m != j) {
                        minCost = min(minCost, dp[i-1][m]);
                    }
                }
                dp[i][j] = costs[i][j] + minCost;
            }
        }
        int minCost = INT_MAX;
        for (int j = 0; j < k; j++) {
            minCost = min(minCost, dp[n-1][j]);
        }
        return minCost;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot k^2)$, where $n$ is the number of houses and $k$ is the number of colors. This is because we have two nested loops over $n$ and $k$, and inside the inner loop, we have another loop over $k$.
> - **Space Complexity:** $O(n \cdot k)$, where $n$ is the number of houses and $k$ is the number of colors. This is because we need to store the minimum cost for each house and each color.
> - **Why these complexities occur:** The time complexity occurs because we have to try all possible color combinations for each house, and the space complexity occurs because we need to store the minimum cost for each house and each color.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The key insight is to use dynamic programming to store the minimum cost for each house and each color, and to update the minimum cost for each house based on the minimum cost of the previous house.
- Detailed breakdown of the approach:
  1. Initialize the minimum cost for the first house.
  2. Iterate over each house, starting from the second house.
  3. For each house, iterate over each color.
  4. For each color, calculate the minimum cost based on the minimum cost of the previous house.
  5. Update the minimum cost for the current house.
- Proof of optimality: The dynamic programming approach ensures that we consider all possible color combinations for each house, and we update the minimum cost for each house based on the minimum cost of the previous house. This ensures that we find the minimum cost to paint all houses.

```cpp
class Solution {
public:
    int minCostII(vector<vector<int>>& costs) {
        int n = costs.size();
        if (n == 0) return 0;
        int k = costs[0].size();
        vector<vector<int>> dp(n, vector<int>(k, 0));
        for (int j = 0; j < k; j++) {
            dp[0][j] = costs[0][j];
        }
        for (int i = 1; i < n; i++) {
            vector<int> minCosts(k, INT_MAX);
            for (int j = 0; j < k; j++) {
                for (int m = 0; m < k; m++) {
                    if (m != j) {
                        minCosts[j] = min(minCosts[j], dp[i-1][m]);
                    }
                }
            }
            for (int j = 0; j < k; j++) {
                dp[i][j] = costs[i][j] + minCosts[j];
            }
        }
        int minCost = INT_MAX;
        for (int j = 0; j < k; j++) {
            minCost = min(minCost, dp[n-1][j]);
        }
        return minCost;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot k^2)$, where $n$ is the number of houses and $k$ is the number of colors.
> - **Space Complexity:** $O(n \cdot k)$, where $n$ is the number of houses and $k$ is the number of colors.
> - **Optimality proof:** The dynamic programming approach ensures that we consider all possible color combinations for each house, and we update the minimum cost for each house based on the minimum cost of the previous house.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, optimization.
- Problem-solving patterns identified: Using dynamic programming to solve optimization problems.
- Optimization techniques learned: Using dynamic programming to reduce the time complexity of the solution.
- Similar problems to practice: Paint House, Paint Fence.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the minimum cost for the first house, not updating the minimum cost for each house based on the minimum cost of the previous house.
- Edge cases to watch for: Handling the case where the number of houses is 0, handling the case where the number of colors is 0.
- Performance pitfalls: Not using dynamic programming to reduce the time complexity of the solution.
- Testing considerations: Testing the solution with different inputs, testing the solution with edge cases.