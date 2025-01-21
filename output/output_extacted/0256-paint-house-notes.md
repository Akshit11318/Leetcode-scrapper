## Paint House
**Problem Link:** https://leetcode.com/problems/paint-house/description

**Problem Statement:**
- Input format: A 2D array `costs` where `costs[i][j]` is the cost of painting the `i-th` house with the `j-th` color.
- Constraints: `1 <= costs.length <= 100`, `costs[i].length == 3`, `1 <= costs[i][j] <= 10^5`.
- Expected output format: The minimum cost to paint all houses.
- Key requirements and edge cases to consider: The first house can be painted with any color, and each subsequent house must be painted with a different color than the previous one.
- Example test cases with explanations:
  - `costs = [[17,2,17],[16,16,5],[14,3,19]]`, the minimum cost is `10`.
  - `costs = [[7,9,5],[2,4,3],[8,5,3]]`, the minimum cost is `8`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible color combinations for each house and calculate the total cost.
- Step-by-step breakdown of the solution:
  1. Define a recursive function that takes the current house index and the previous house's color.
  2. For each possible color of the current house, recursively call the function for the next house with a different color.
  3. Calculate the total cost by summing up the costs of painting each house with the chosen colors.
- Why this approach comes to mind first: It's a straightforward way to explore all possible solutions.

```cpp
class Solution {
public:
    int minCost(vector<vector<int>>& costs) {
        if (costs.empty()) return 0;
        int n = costs.size();
        vector<vector<int>> memo(n, vector<int>(3, -1));
        return dfs(0, -1, costs, memo);
    }
    
    int dfs(int i, int prevColor, vector<vector<int>>& costs, vector<vector<int>>& memo) {
        if (i == costs.size()) return 0;
        if (memo[i][prevColor + 1] != -1) return memo[i][prevColor + 1];
        int minCost = INT_MAX;
        for (int color = 0; color < 3; color++) {
            if (color != prevColor) {
                minCost = min(minCost, costs[i][color] + dfs(i + 1, color, costs, memo));
            }
        }
        memo[i][prevColor + 1] = minCost;
        return minCost;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot 3)$, where $n$ is the number of houses, since we have a recursive function that tries all 3 colors for each house.
> - **Space Complexity:** $O(n \cdot 3)$, since we use a memoization table to store the results of subproblems.
> - **Why these complexities occur:** The recursive function has a branching factor of 3 (one for each color), and we use memoization to avoid redundant calculations.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use dynamic programming to store the minimum cost of painting each house with each color.
- Detailed breakdown of the approach:
  1. Create a `dp` table where `dp[i][j]` represents the minimum cost of painting the first `i` houses with the `i-th` house painted with color `j`.
  2. Initialize the `dp` table with the costs of painting the first house with each color.
  3. For each subsequent house, calculate the minimum cost of painting it with each color by considering the minimum cost of painting the previous house with a different color.
- Proof of optimality: This approach considers all possible color combinations and chooses the one with the minimum cost.

```cpp
class Solution {
public:
    int minCost(vector<vector<int>>& costs) {
        if (costs.empty()) return 0;
        int n = costs.size();
        vector<vector<int>> dp(n, vector<int>(3, 0));
        dp[0] = costs[0];
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < 3; j++) {
                dp[i][j] = costs[i][j] + min(dp[i - 1][(j + 1) % 3], dp[i - 1][(j + 2) % 3]);
            }
        }
        return *min_element(dp[n - 1].begin(), dp[n - 1].end());
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot 3)$, where $n$ is the number of houses, since we have a nested loop that iterates over each house and each color.
> - **Space Complexity:** $O(n \cdot 3)$, since we use a dynamic programming table to store the minimum costs.
> - **Optimality proof:** This approach considers all possible color combinations and chooses the one with the minimum cost, resulting in an optimal solution.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, memoization, and recursion.
- Problem-solving patterns identified: Using a recursive function to explore all possible solutions and then optimizing it with dynamic programming.
- Optimization techniques learned: Memoization and dynamic programming.
- Similar problems to practice: Paint House II, House Robber, and Coin Change.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as an empty input array.
- Edge cases to watch for: When the input array is empty or has only one element.
- Performance pitfalls: Using a naive recursive approach without memoization or dynamic programming.
- Testing considerations: Testing the function with different input arrays and edge cases to ensure correctness and performance.