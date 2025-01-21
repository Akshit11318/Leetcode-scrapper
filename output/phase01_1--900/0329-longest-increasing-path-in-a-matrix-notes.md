## Longest Increasing Path in a Matrix

**Problem Link:** https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description

**Problem Statement:**
- Input format and constraints: The input is a 2D grid of integers, where each cell represents a height. The grid can be empty, and the number of rows and columns can vary. The task is to find the longest increasing path in the grid.
- Expected output format: The output should be the length of the longest increasing path.
- Key requirements and edge cases to consider: The path can only be constructed by moving in four directions (up, down, left, right) to a cell with a greater height. If the grid is empty, the output should be 0. If there are multiple paths with the same maximum length, any of them can be considered.
- Example test cases with explanations:
  - Input: `[[9,9,4],[6,6,8],[2,1,1]]`, Output: `4`
  - Input: `[[3,4,5],[3,2,6],[2,2,1]]`, Output: `4`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Start from each cell and try to move in all four directions to find a cell with a greater height.
- Step-by-step breakdown of the solution:
  1. Iterate over each cell in the grid.
  2. For each cell, try to move in all four directions (up, down, left, right).
  3. If the adjacent cell has a greater height, recursively try to move from that cell.
  4. Keep track of the maximum length of the path found so far.
- Why this approach comes to mind first: It's a straightforward way to explore all possible paths in the grid.

```cpp
class Solution {
public:
    int longestIncreasingPath(vector<vector<int>>& matrix) {
        if (matrix.empty()) return 0;
        int rows = matrix.size();
        int cols = matrix[0].size();
        int maxLen = 0;
        vector<vector<int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        
        function<int(int, int)> dfs = [&](int i, int j) {
            int len = 1;
            for (auto& dir : directions) {
                int x = i + dir[0];
                int y = j + dir[1];
                if (x >= 0 && x < rows && y >= 0 && y < cols && matrix[x][y] > matrix[i][j]) {
                    len = max(len, 1 + dfs(x, y));
                }
            }
            return len;
        };
        
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                maxLen = max(maxLen, dfs(i, j));
            }
        }
        
        return maxLen;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{rows \cdot cols})$, because in the worst case, we might need to explore all possible paths in the grid.
> - **Space Complexity:** $O(rows \cdot cols)$, because of the recursive call stack.
> - **Why these complexities occur:** The brute force approach has an exponential time complexity because it tries all possible paths in the grid. The space complexity is linear because of the recursive call stack.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use memoization to store the length of the longest increasing path starting from each cell. This way, we avoid recalculating the same paths multiple times.
- Detailed breakdown of the approach:
  1. Create a memoization table to store the length of the longest increasing path starting from each cell.
  2. Iterate over each cell in the grid.
  3. For each cell, try to move in all four directions (up, down, left, right).
  4. If the adjacent cell has a greater height, recursively try to move from that cell and update the memoization table.
  5. Keep track of the maximum length of the path found so far.
- Proof of optimality: The optimal approach has a time complexity of $O(rows \cdot cols)$, which is the best possible time complexity for this problem. This is because we need to visit each cell at least once to find the longest increasing path.

```cpp
class Solution {
public:
    int longestIncreasingPath(vector<vector<int>>& matrix) {
        if (matrix.empty()) return 0;
        int rows = matrix.size();
        int cols = matrix[0].size();
        int maxLen = 0;
        vector<vector<int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        vector<vector<int>> memo(rows, vector<int>(cols, 0));
        
        function<int(int, int)> dfs = [&](int i, int j) {
            if (memo[i][j] > 0) return memo[i][j];
            int len = 1;
            for (auto& dir : directions) {
                int x = i + dir[0];
                int y = j + dir[1];
                if (x >= 0 && x < rows && y >= 0 && y < cols && matrix[x][y] > matrix[i][j]) {
                    len = max(len, 1 + dfs(x, y));
                }
            }
            memo[i][j] = len;
            return len;
        };
        
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                maxLen = max(maxLen, dfs(i, j));
            }
        }
        
        return maxLen;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(rows \cdot cols)$, because we visit each cell at most once.
> - **Space Complexity:** $O(rows \cdot cols)$, because of the memoization table.
> - **Optimality proof:** The optimal approach has a time complexity of $O(rows \cdot cols)$, which is the best possible time complexity for this problem. This is because we need to visit each cell at least once to find the longest increasing path.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Memoization, Depth-First Search (DFS).
- Problem-solving patterns identified: Using memoization to avoid recalculating the same subproblems.
- Optimization techniques learned: Memoization.
- Similar problems to practice: Longest Increasing Subsequence, Shortest Path in a Grid.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to initialize the memoization table, not checking for out-of-bounds indices.
- Edge cases to watch for: Empty grid, grid with a single cell.
- Performance pitfalls: Not using memoization, which can lead to exponential time complexity.
- Testing considerations: Test the solution with different grid sizes, shapes, and values.