## Length of the Longest Increasing Path

**Problem Link:** https://leetcode.com/problems/length-of-the-longest-increasing-path/description

**Problem Statement:**
- Input format and constraints: Given an `m x n` integer matrix `matrix`, find the length of the longest increasing path.
- Expected output format: Return the length of the longest increasing path.
- Key requirements and edge cases to consider: The path must be strictly increasing, and you can move in any of the four directions (up, down, left, right).
- Example test cases with explanations:
  - Example 1: Input: `matrix = [[9,9,4],[6,6,8],[2,1,1]]`, Output: `4`, Explanation: The longest increasing path is `[1, 2, 6, 9]`.
  - Example 2: Input: `matrix = [[3,4,5],[3,2,6],[2,2,1]]`, Output: `4`, Explanation: The longest increasing path is `[3, 4, 5, 6]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible paths from each cell to find the longest increasing path.
- Step-by-step breakdown of the solution:
  1. Define a function to perform DFS from each cell.
  2. In the DFS function, check all four directions (up, down, left, right) for a valid increasing path.
  3. Keep track of the maximum length of the increasing path found so far.
- Why this approach comes to mind first: It is a straightforward way to explore all possible paths, but it is inefficient due to the repeated computation.

```cpp
class Solution {
public:
    int longestIncreasingPath(vector<vector<int>>& matrix) {
        if (matrix.empty() || matrix[0].empty()) return 0;
        int m = matrix.size(), n = matrix[0].size();
        int maxLen = 0;
        vector<vector<int>> directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        
        function<int(int, int)> dfs = [&](int i, int j) {
            int maxPath = 1;
            for (auto& dir : directions) {
                int x = i + dir[0], y = j + dir[1];
                if (x >= 0 && x < m && y >= 0 && y < n && matrix[x][y] > matrix[i][j]) {
                    maxPath = max(maxPath, 1 + dfs(x, y));
                }
            }
            return maxPath;
        };
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                maxLen = max(maxLen, dfs(i, j));
            }
        }
        return maxLen;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{m \times n})$, where $m$ and $n$ are the dimensions of the matrix. This is because in the worst case, we might need to explore all cells from each cell.
> - **Space Complexity:** $O(m \times n)$, due to the recursion stack.
> - **Why these complexities occur:** The brute force approach explores all possible paths, leading to exponential time complexity. The space complexity is due to the recursion stack.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use memoization to store the length of the longest increasing path from each cell to avoid repeated computation.
- Detailed breakdown of the approach:
  1. Define a memoization table `memo` of the same size as the input matrix.
  2. Initialize all values in `memo` to 0.
  3. Define a function to perform DFS with memoization from each cell.
  4. In the DFS function, check all four directions (up, down, left, right) for a valid increasing path.
  5. If the length of the longest increasing path from the current cell is already computed, return the stored value.
  6. Otherwise, compute the length of the longest increasing path and store it in the `memo` table.
- Proof of optimality: This approach ensures that each cell is visited at most once, reducing the time complexity to $O(m \times n)$.

```cpp
class Solution {
public:
    int longestIncreasingPath(vector<vector<int>>& matrix) {
        if (matrix.empty() || matrix[0].empty()) return 0;
        int m = matrix.size(), n = matrix[0].size();
        int maxLen = 0;
        vector<vector<int>> directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        vector<vector<int>> memo(m, vector<int>(n, 0));
        
        function<int(int, int)> dfs = [&](int i, int j) {
            if (memo[i][j] > 0) return memo[i][j];
            int maxPath = 1;
            for (auto& dir : directions) {
                int x = i + dir[0], y = j + dir[1];
                if (x >= 0 && x < m && y >= 0 && y < n && matrix[x][y] > matrix[i][j]) {
                    maxPath = max(maxPath, 1 + dfs(x, y));
                }
            }
            memo[i][j] = maxPath;
            return maxPath;
        };
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                maxLen = max(maxLen, dfs(i, j));
            }
        }
        return maxLen;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \times n)$, where $m$ and $n$ are the dimensions of the matrix. This is because each cell is visited at most once.
> - **Space Complexity:** $O(m \times n)$, due to the memoization table and recursion stack.
> - **Optimality proof:** The optimal approach ensures that each cell is visited at most once, reducing the time complexity to $O(m \times n)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: DFS, memoization.
- Problem-solving patterns identified: Using memoization to avoid repeated computation.
- Optimization techniques learned: Reducing time complexity by avoiding repeated computation.
- Similar problems to practice: Other problems that involve finding the longest path in a graph or matrix.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to initialize the memoization table or not checking for valid increasing paths.
- Edge cases to watch for: Empty input matrix or matrix with a single cell.
- Performance pitfalls: Not using memoization, leading to exponential time complexity.
- Testing considerations: Test the solution with different input matrices, including edge cases.