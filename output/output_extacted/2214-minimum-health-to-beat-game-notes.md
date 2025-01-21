## Minimum Health to Beat Game
**Problem Link:** https://leetcode.com/problems/minimum-health-to-beat-game/description

**Problem Statement:**
- Input format: A 2D array `dungeon` representing the game map, where each cell is an integer.
- Constraints: The input array is not empty, and each row in the array is not empty.
- Expected output format: The minimum initial health required to reach the bottom-right corner of the dungeon.
- Key requirements: The player starts at the top-left corner, and the goal is to reach the bottom-right corner with the minimum initial health.
- Edge cases to consider: The player's health cannot be negative at any point.

### Brute Force Approach
**Explanation:**
- Initial thought process: Try all possible paths from the top-left to the bottom-right corner and calculate the minimum health required for each path.
- Step-by-step breakdown of the solution:
  1. Initialize a 2D array `dp` to store the minimum health required to reach each cell.
  2. Iterate over each cell in the dungeon, starting from the top-left corner.
  3. For each cell, calculate the minimum health required to reach it by considering all possible paths from the top-left corner.
  4. Update the `dp` array with the minimum health required to reach each cell.
- Why this approach comes to mind first: It is a straightforward approach that tries all possible solutions.

```cpp
class Solution {
public:
    int calculateMinimumHP(vector<vector<int>>& dungeon) {
        int m = dungeon.size();
        int n = dungeon[0].size();
        vector<vector<int>> dp(m, vector<int>(n, INT_MAX));
        
        for (int i = m - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                if (i == m - 1 && j == n - 1) {
                    dp[i][j] = max(1, 1 - dungeon[i][j]);
                } else if (i == m - 1) {
                    dp[i][j] = max(1, dp[i][j + 1] - dungeon[i][j]);
                } else if (j == n - 1) {
                    dp[i][j] = max(1, dp[i + 1][j] - dungeon[i][j]);
                } else {
                    dp[i][j] = max(1, min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j]);
                }
            }
        }
        
        return dp[0][0];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ and $n$ are the number of rows and columns in the dungeon, respectively. This is because we iterate over each cell in the dungeon once.
> - **Space Complexity:** $O(m \cdot n)$, where $m$ and $n$ are the number of rows and columns in the dungeon, respectively. This is because we use a 2D array `dp` to store the minimum health required to reach each cell.
> - **Why these complexities occur:** The time complexity occurs because we iterate over each cell in the dungeon once, and the space complexity occurs because we use a 2D array `dp` to store the minimum health required to reach each cell.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We can use dynamic programming to calculate the minimum health required to reach each cell.
- Detailed breakdown of the approach:
  1. Initialize a 2D array `dp` to store the minimum health required to reach each cell.
  2. Iterate over each cell in the dungeon, starting from the bottom-right corner.
  3. For each cell, calculate the minimum health required to reach it by considering the minimum health required to reach the cell below it or to its right.
  4. Update the `dp` array with the minimum health required to reach each cell.
- Proof of optimality: This approach is optimal because it uses dynamic programming to calculate the minimum health required to reach each cell, which reduces the time complexity from exponential to quadratic.

```cpp
class Solution {
public:
    int calculateMinimumHP(vector<vector<int>>& dungeon) {
        int m = dungeon.size();
        int n = dungeon[0].size();
        vector<vector<int>> dp(m, vector<int>(n, 0));
        
        dp[m - 1][n - 1] = max(1, 1 - dungeon[m - 1][n - 1]);
        
        for (int i = m - 2; i >= 0; i--) {
            dp[i][n - 1] = max(1, dp[i + 1][n - 1] - dungeon[i][n - 1]);
        }
        
        for (int j = n - 2; j >= 0; j--) {
            dp[m - 1][j] = max(1, dp[m - 1][j + 1] - dungeon[m - 1][j]);
        }
        
        for (int i = m - 2; i >= 0; i--) {
            for (int j = n - 2; j >= 0; j--) {
                dp[i][j] = max(1, min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j]);
            }
        }
        
        return dp[0][0];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ and $n$ are the number of rows and columns in the dungeon, respectively. This is because we iterate over each cell in the dungeon once.
> - **Space Complexity:** $O(m \cdot n)$, where $m$ and $n$ are the number of rows and columns in the dungeon, respectively. This is because we use a 2D array `dp` to store the minimum health required to reach each cell.
> - **Optimality proof:** This approach is optimal because it uses dynamic programming to calculate the minimum health required to reach each cell, which reduces the time complexity from exponential to quadratic.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, memoization, and optimization techniques.
- Problem-solving patterns identified: Using dynamic programming to solve problems that have overlapping subproblems.
- Optimization techniques learned: Reducing the time complexity from exponential to quadratic using dynamic programming.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the `dp` array correctly, not considering the base cases correctly, and not updating the `dp` array correctly.
- Edge cases to watch for: The player's health cannot be negative at any point, and the input array is not empty.
- Performance pitfalls: Not using dynamic programming to solve problems that have overlapping subproblems, which can lead to exponential time complexity.
- Testing considerations: Testing the solution with different input sizes and edge cases to ensure that it works correctly and efficiently.