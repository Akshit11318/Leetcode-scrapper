## Dungeon Game

**Problem Link:** [https://leetcode.com/problems/dungeon-game/description](https://leetcode.com/problems/dungeon-game/description)

**Problem Statement:**
- Input format: A 2D grid `dungeon` where each cell represents the amount of health gained or lost.
- Constraints: `1 <= dungeon.length <= 8`, `1 <= dungeon[0].length <= 8`, `-10^3 <= dungeon[i][j] <= 10^3`.
- Expected output format: The minimum amount of health required to reach the princess.
- Key requirements: The knight starts at the top-left corner, and the princess is at the bottom-right corner. The knight can move either right or down.
- Example test cases:
  - Input: `dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]`
  - Output: `7`
  - Explanation: The knight starts with 7 health and moves to the right, then down, then right, then down, and finally to the right.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible paths and calculate the minimum health required for each path.
- Step-by-step breakdown:
  1. Generate all possible paths from the top-left corner to the bottom-right corner.
  2. For each path, calculate the total health gained or lost.
  3. Keep track of the minimum health required for each path.
- Why this approach comes to mind first: It is a straightforward approach that tries all possible solutions.

```cpp
class Solution {
public:
    int calculateMinimumHP(vector<vector<int>>& dungeon) {
        int rows = dungeon.size();
        int cols = dungeon[0].size();
        vector<vector<int>> minHealth(rows, vector<int>(cols, INT_MAX));
        
        // Try all possible paths
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                // Calculate the minimum health required for the current path
                int health = calculateHealth(dungeon, i, j, minHealth);
                minHealth[i][j] = health;
            }
        }
        
        return minHealth[0][0];
    }
    
    int calculateHealth(vector<vector<int>>& dungeon, int i, int j, vector<vector<int>>& minHealth) {
        int rows = dungeon.size();
        int cols = dungeon[0].size();
        
        // Base case: If we are at the bottom-right corner, return 1
        if (i == rows - 1 && j == cols - 1) {
            return max(1, 1 - dungeon[i][j]);
        }
        
        // If we have already calculated the minimum health for the current path, return it
        if (minHealth[i][j] != INT_MAX) {
            return minHealth[i][j];
        }
        
        // Try moving right and down
        int minHealthRight = INT_MAX;
        int minHealthDown = INT_MAX;
        if (j < cols - 1) {
            minHealthRight = calculateHealth(dungeon, i, j + 1, minHealth);
        }
        if (i < rows - 1) {
            minHealthDown = calculateHealth(dungeon, i + 1, j, minHealth);
        }
        
        // Calculate the minimum health required for the current path
        int minHealthCurrent = max(1, min(minHealthRight, minHealthDown) - dungeon[i][j]);
        
        return minHealthCurrent;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{rows \cdot cols})$ because we are trying all possible paths.
> - **Space Complexity:** $O(rows \cdot cols)$ because we are storing the minimum health required for each path.
> - **Why these complexities occur:** The brute force approach tries all possible paths, which results in exponential time complexity. The space complexity is linear because we are storing the minimum health required for each path.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: We can use dynamic programming to calculate the minimum health required for each cell.
- Detailed breakdown:
  1. Initialize a 2D array `dp` with the same size as the `dungeon` array.
  2. Fill in the `dp` array from the bottom-right corner to the top-left corner.
  3. For each cell, calculate the minimum health required based on the minimum health required for the cells below and to the right.
- Proof of optimality: This approach is optimal because it uses dynamic programming to avoid trying all possible paths.

```cpp
class Solution {
public:
    int calculateMinimumHP(vector<vector<int>>& dungeon) {
        int rows = dungeon.size();
        int cols = dungeon[0].size();
        vector<vector<int>> dp(rows, vector<int>(cols, 0));
        
        // Fill in the dp array from the bottom-right corner to the top-left corner
        dp[rows - 1][cols - 1] = max(1, 1 - dungeon[rows - 1][cols - 1]);
        for (int i = rows - 2; i >= 0; i--) {
            dp[i][cols - 1] = max(1, dp[i + 1][cols - 1] - dungeon[i][cols - 1]);
        }
        for (int j = cols - 2; j >= 0; j--) {
            dp[rows - 1][j] = max(1, dp[rows - 1][j + 1] - dungeon[rows - 1][j]);
        }
        for (int i = rows - 2; i >= 0; i--) {
            for (int j = cols - 2; j >= 0; j--) {
                dp[i][j] = max(1, min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j]);
            }
        }
        
        return dp[0][0];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(rows \cdot cols)$ because we are filling in the `dp` array once.
> - **Space Complexity:** $O(rows \cdot cols)$ because we are storing the minimum health required for each cell.
> - **Optimality proof:** This approach is optimal because it uses dynamic programming to avoid trying all possible paths, resulting in linear time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, memoization.
- Problem-solving patterns identified: Using dynamic programming to avoid trying all possible solutions.
- Optimization techniques learned: Using memoization to store intermediate results and avoid redundant calculations.
- Similar problems to practice: Other dynamic programming problems, such as the `Unique Paths` problem.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to initialize the `dp` array, or not filling it in correctly.
- Edge cases to watch for: Handling the case where the input array is empty, or where the minimum health required is 1.
- Performance pitfalls: Using a brute force approach instead of dynamic programming, resulting in exponential time complexity.
- Testing considerations: Testing the solution with different input arrays, including edge cases and large inputs.