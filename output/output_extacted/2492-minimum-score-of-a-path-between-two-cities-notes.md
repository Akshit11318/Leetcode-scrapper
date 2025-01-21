## Minimum Score of a Path Between Two Cities

**Problem Link:** https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description

**Problem Statement:**
- Input format and constraints: Given a `n x n` grid, where each cell represents a city, and each city is connected to its adjacent cities (horizontally or vertically) with a certain score.
- Expected output format: The minimum score of a path between the top-left city and the bottom-right city.
- Key requirements and edge cases to consider: The path can only be constructed by moving either down or right from any cell.
- Example test cases with explanations:
  - Example 1:
    - Input: `[[5,4],[2,3]]`
    - Output: `6`
    - Explanation: The minimum score of a path from the top-left city to the bottom-right city is 5 + 1 = 6 (moving down from the top-left city to the bottom-left city, and then moving right to the bottom-right city).

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves generating all possible paths from the top-left city to the bottom-right city and calculating the minimum score of each path.
- Step-by-step breakdown of the solution:
  1. Initialize a 2D array `dp` of size `n x n` to store the minimum score of a path to each city.
  2. Initialize the minimum score of the top-left city to its score.
  3. For each city in the first row, calculate the minimum score of a path to that city by adding its score to the minimum score of the previous city in the row.
  4. For each city in the first column, calculate the minimum score of a path to that city by adding its score to the minimum score of the previous city in the column.
  5. For each remaining city, calculate the minimum score of a path to that city by adding its score to the minimum score of the city above it or to its left, whichever is smaller.
- Why this approach comes to mind first: This approach is straightforward and involves calculating the minimum score of a path to each city by considering all possible paths.

```cpp
int minPathScore(vector<vector<int>>& grid) {
    int n = grid.size();
    vector<vector<int>> dp(n, vector<int>(n, INT_MAX));
    dp[0][0] = grid[0][0];
    for (int i = 1; i < n; i++) {
        dp[i][0] = dp[i-1][0] + grid[i][0];
    }
    for (int j = 1; j < n; j++) {
        dp[0][j] = dp[0][j-1] + grid[0][j];
    }
    for (int i = 1; i < n; i++) {
        for (int j = 1; j < n; j++) {
            dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1]);
        }
    }
    return dp[n-1][n-1];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of cities in each row and column, since we are iterating over each city once.
> - **Space Complexity:** $O(n^2)$, since we are using a 2D array of size $n x n$ to store the minimum score of a path to each city.
> - **Why these complexities occur:** The time complexity occurs because we are iterating over each city once, and the space complexity occurs because we are using a 2D array to store the minimum score of a path to each city.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution involves using dynamic programming to calculate the minimum score of a path to each city, but with a more efficient approach.
- Detailed breakdown of the approach:
  1. Initialize a 2D array `dp` of size `n x n` to store the minimum score of a path to each city.
  2. Initialize the minimum score of the top-left city to its score.
  3. For each city in the first row, calculate the minimum score of a path to that city by adding its score to the minimum score of the previous city in the row.
  4. For each city in the first column, calculate the minimum score of a path to that city by adding its score to the minimum score of the previous city in the column.
  5. For each remaining city, calculate the minimum score of a path to that city by adding its score to the minimum score of the city above it or to its left, whichever is smaller.
- Proof of optimality: This approach is optimal because it involves calculating the minimum score of a path to each city using dynamic programming, which ensures that we are considering all possible paths and choosing the one with the minimum score.
- Why further optimization is impossible: Further optimization is impossible because we are already using dynamic programming to calculate the minimum score of a path to each city, which is the most efficient approach.

```cpp
int minPathScore(vector<vector<int>>& grid) {
    int n = grid.size();
    vector<vector<int>> dp(n, vector<int>(n, INT_MAX));
    dp[0][0] = grid[0][0];
    for (int i = 1; i < n; i++) {
        dp[i][0] = dp[i-1][0] + grid[i][0];
    }
    for (int j = 1; j < n; j++) {
        dp[0][j] = dp[0][j-1] + grid[0][j];
    }
    for (int i = 1; i < n; i++) {
        for (int j = 1; j < n; j++) {
            dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1]);
        }
    }
    return dp[n-1][n-1];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of cities in each row and column, since we are iterating over each city once.
> - **Space Complexity:** $O(n^2)$, since we are using a 2D array of size $n x n$ to store the minimum score of a path to each city.
> - **Optimality proof:** This approach is optimal because it involves calculating the minimum score of a path to each city using dynamic programming, which ensures that we are considering all possible paths and choosing the one with the minimum score.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, minimum score calculation.
- Problem-solving patterns identified: Using dynamic programming to calculate the minimum score of a path to each city.
- Optimization techniques learned: Using dynamic programming to optimize the calculation of the minimum score of a path to each city.
- Similar problems to practice: Minimum path sum, minimum score of a path in a grid.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the minimum score of the top-left city correctly, not updating the minimum score of each city correctly.
- Edge cases to watch for: Cities with zero score, cities with negative score.
- Performance pitfalls: Not using dynamic programming to calculate the minimum score of a path to each city, using a naive approach that involves iterating over all possible paths.
- Testing considerations: Testing the implementation with different inputs, including edge cases, to ensure that it is working correctly.