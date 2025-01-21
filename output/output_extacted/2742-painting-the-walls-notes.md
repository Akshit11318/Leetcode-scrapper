## Painting the Walls
**Problem Link:** https://leetcode.com/problems/painting-the-walls/description

**Problem Statement:**
- Input format and constraints: The problem requires painting `n` walls with `m` colors. Each wall can be painted with one of the `m` colors, and each color can be used to paint any number of walls. The input includes the number of walls `n`, the number of colors `m`, and the cost of painting each wall with each color `costs`.
- Expected output format: The function should return the minimum cost to paint all the walls.
- Key requirements and edge cases to consider: The cost of painting each wall with each color is given, and the goal is to minimize the total cost. Edge cases include when the number of walls or colors is 0, or when the cost matrix is empty.
- Example test cases with explanations:
    - For `n = 2`, `m = 2`, and `costs = [[1, 5], [2, 3]]`, the minimum cost is `4` (paint the first wall with the first color and the second wall with the second color).
    - For `n = 3`, `m = 3`, and `costs = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]`, the minimum cost is `3` (paint all walls with the first color).

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of painting each wall with each color and calculate the total cost for each combination.
- Step-by-step breakdown of the solution:
    1. Initialize the minimum cost to infinity.
    2. Iterate over all possible combinations of painting each wall with each color.
    3. For each combination, calculate the total cost.
    4. Update the minimum cost if the current total cost is less than the minimum cost.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it has an exponential time complexity due to the number of possible combinations.

```cpp
class Solution {
public:
    int minCost(vector<vector<int>>& costs) {
        if (costs.empty() || costs[0].empty()) {
            return 0;
        }
        
        int n = costs.size();
        int m = costs[0].size();
        
        vector<int> minCosts(n);
        
        // Base case: The minimum cost to paint the first wall is the minimum cost of each color.
        minCosts[0] = *min_element(costs[0].begin(), costs[0].end());
        
        for (int i = 1; i < n; i++) {
            int minCost = INT_MAX;
            for (int j = 0; j < m; j++) {
                int cost = INT_MAX;
                for (int k = 0; k < m; k++) {
                    if (j != k) {
                        cost = min(cost, minCosts[i - 1] + costs[i][j]);
                    }
                }
                minCost = min(minCost, cost);
            }
            minCosts[i] = minCost;
        }
        
        return minCosts[n - 1];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m^2)$, where $n$ is the number of walls and $m$ is the number of colors. This is because we iterate over all walls and for each wall, we iterate over all colors to find the minimum cost.
> - **Space Complexity:** $O(n)$, where $n$ is the number of walls. This is because we use a vector to store the minimum cost to paint each wall.
> - **Why these complexities occur:** The time complexity is high because we iterate over all colors for each wall, and the space complexity is moderate because we need to store the minimum cost to paint each wall.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use dynamic programming to store the minimum cost to paint each wall with each color and avoid redundant calculations.
- Detailed breakdown of the approach:
    1. Initialize a 2D vector `dp` to store the minimum cost to paint each wall with each color.
    2. Base case: The minimum cost to paint the first wall with each color is the cost of painting the first wall with that color.
    3. For each wall from the second wall to the last wall, iterate over all colors and calculate the minimum cost to paint the current wall with each color by considering the minimum cost to paint the previous wall with all other colors.
- Proof of optimality: This approach is optimal because it avoids redundant calculations by storing the minimum cost to paint each wall with each color and only considers the minimum cost to paint the previous wall with all other colors.

```cpp
class Solution {
public:
    int minCost(vector<vector<int>>& costs) {
        if (costs.empty() || costs[0].empty()) {
            return 0;
        }
        
        int n = costs.size();
        int m = costs[0].size();
        
        vector<vector<int>> dp(n, vector<int>(m, 0));
        
        // Base case: The minimum cost to paint the first wall with each color is the cost of painting the first wall with that color.
        for (int j = 0; j < m; j++) {
            dp[0][j] = costs[0][j];
        }
        
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < m; j++) {
                int minCost = INT_MAX;
                for (int k = 0; k < m; k++) {
                    if (j != k) {
                        minCost = min(minCost, dp[i - 1][k]);
                    }
                }
                dp[i][j] = minCost + costs[i][j];
            }
        }
        
        int minCost = INT_MAX;
        for (int j = 0; j < m; j++) {
            minCost = min(minCost, dp[n - 1][j]);
        }
        
        return minCost;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m^2)$, where $n$ is the number of walls and $m$ is the number of colors. This is because we iterate over all walls and for each wall, we iterate over all colors to find the minimum cost.
> - **Space Complexity:** $O(n \cdot m)$, where $n$ is the number of walls and $m$ is the number of colors. This is because we use a 2D vector to store the minimum cost to paint each wall with each color.
> - **Optimality proof:** This approach is optimal because it avoids redundant calculations by storing the minimum cost to paint each wall with each color and only considers the minimum cost to paint the previous wall with all other colors.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, memoization, and optimization.
- Problem-solving patterns identified: Using dynamic programming to avoid redundant calculations and optimizing the solution by considering the minimum cost to paint the previous wall with all other colors.
- Optimization techniques learned: Using a 2D vector to store the minimum cost to paint each wall with each color and iterating over all colors to find the minimum cost.
- Similar problems to practice: Other dynamic programming problems, such as the Fibonacci sequence, the knapsack problem, and the matrix chain multiplication problem.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the base case correctly, not considering all possible colors, and not updating the minimum cost correctly.
- Edge cases to watch for: When the number of walls or colors is 0, or when the cost matrix is empty.
- Performance pitfalls: Using a brute force approach that has an exponential time complexity, not using dynamic programming to avoid redundant calculations, and not optimizing the solution by considering the minimum cost to paint the previous wall with all other colors.
- Testing considerations: Testing the solution with different inputs, including edge cases, and verifying that the solution produces the correct output.