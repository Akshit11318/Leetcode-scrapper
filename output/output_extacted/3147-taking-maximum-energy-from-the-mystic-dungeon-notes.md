## Taking Maximum Energy from the Mystic Dungeon

**Problem Link:** https://leetcode.com/problems/taking-maximum-energy-from-the-mystic-dungeon/description

**Problem Statement:**
- Input format and constraints: You are given a 2D array `grid` where each cell represents the energy you can collect from that cell. The input grid is a rectangular grid with dimensions `m x n`.
- Expected output format: The goal is to find the maximum energy you can collect from the dungeon.
- Key requirements and edge cases to consider: You can only move right or down, and if your current energy is less than the energy required to enter a cell, you cannot enter that cell.
- Example test cases with explanations:
  - `grid = [[-2,-3,3],[-5,-10,1],[10,30,-5]]` should return `7` because the maximum energy you can collect is `7` by following the path `[-2, -3, 3, 1, 30, -5]`.
  - `grid = [[0]]` should return `0` because the maximum energy you can collect is `0` by staying in the same cell.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible paths from the top-left cell to the bottom-right cell and calculate the maximum energy for each path.
- Step-by-step breakdown of the solution:
  1. Define a recursive function that takes the current cell as input.
  2. If the current cell is out of bounds or the current energy is less than the energy required to enter the cell, return a negative infinity.
  3. If the current cell is the bottom-right cell, return the current energy.
  4. Otherwise, recursively call the function for the right and down cells and return the maximum energy.
- Why this approach comes to mind first: It is a straightforward approach to try all possible paths and calculate the maximum energy for each path.

```cpp
class Solution {
public:
    int calculateMinimumHP(vector<vector<int>>& dungeon) {
        int m = dungeon.size();
        int n = dungeon[0].size();
        int maxEnergy = INT_MIN;
        
        function<int(int, int, int)> dfs = [&](int i, int j, int energy) {
            if (i >= m || j >= n) return INT_MIN;
            if (i == m - 1 && j == n - 1) {
                maxEnergy = max(maxEnergy, energy + dungeon[i][j]);
                return energy + dungeon[i][j];
            }
            int right = dfs(i, j + 1, energy + dungeon[i][j]);
            int down = dfs(i + 1, j, energy + dungeon[i][j]);
            return max(right, down);
        };
        
        dfs(0, 0, 0);
        return -maxEnergy + 1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{m+n})$ because we are trying all possible paths.
> - **Space Complexity:** $O(m+n)$ because of the recursive call stack.
> - **Why these complexities occur:** The brute force approach tries all possible paths, which results in an exponential time complexity. The space complexity is due to the recursive call stack.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use dynamic programming to store the maximum energy for each cell and avoid trying all possible paths.
- Detailed breakdown of the approach:
  1. Create a 2D array `dp` with dimensions `m x n` to store the maximum energy for each cell.
  2. Initialize the `dp` array with negative infinity.
  3. Fill the `dp` array from the bottom-right cell to the top-left cell.
  4. For each cell, calculate the maximum energy by considering the right and down cells.
- Proof of optimality: The dynamic programming approach ensures that we consider all possible paths and calculate the maximum energy for each cell.

```cpp
class Solution {
public:
    int calculateMinimumHP(vector<vector<int>>& dungeon) {
        int m = dungeon.size();
        int n = dungeon[0].size();
        vector<vector<int>> dp(m, vector<int>(n, INT_MIN));
        
        dp[m - 1][n - 1] = dungeon[m - 1][n - 1];
        
        for (int i = m - 2; i >= 0; i--) {
            dp[i][n - 1] = max(1, dp[i + 1][n - 1] + dungeon[i][n - 1]);
        }
        
        for (int j = n - 2; j >= 0; j--) {
            dp[m - 1][j] = max(1, dp[m - 1][j + 1] + dungeon[m - 1][j]);
        }
        
        for (int i = m - 2; i >= 0; i--) {
            for (int j = n - 2; j >= 0; j--) {
                dp[i][j] = max(1, min(dp[i + 1][j], dp[i][j + 1]) + dungeon[i][j]);
            }
        }
        
        return dp[0][0];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(mn)$ because we are filling the `dp` array.
> - **Space Complexity:** $O(mn)$ because of the `dp` array.
> - **Optimality proof:** The dynamic programming approach ensures that we consider all possible paths and calculate the maximum energy for each cell, resulting in an optimal solution.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, recursion.
- Problem-solving patterns identified: Trying all possible paths, using dynamic programming to store intermediate results.
- Optimization techniques learned: Using dynamic programming to avoid trying all possible paths.
- Similar problems to practice: Other dynamic programming problems, such as the `Longest Common Subsequence` problem.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the `dp` array correctly, not considering the base cases.
- Edge cases to watch for: Negative energy values, zero energy values.
- Performance pitfalls: Trying all possible paths, not using dynamic programming to store intermediate results.
- Testing considerations: Test cases with negative energy values, test cases with zero energy values.