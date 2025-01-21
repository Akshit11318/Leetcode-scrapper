## Shortest Bridge

**Problem Link:** https://leetcode.com/problems/shortest-bridge/description

**Problem Statement:**
- Input format and constraints: Given a 2D binary matrix `A` containing only `0`s and `1`s, find the length of the shortest bridge.
- Expected output format: The length of the shortest bridge.
- Key requirements and edge cases to consider: The input matrix `A` is guaranteed to be non-empty and have exactly two islands.
- Example test cases with explanations: For example, given `A = [[0,1,0],[0,0,0],[0,0,1]]`, the output should be `2`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first step is to identify the two islands in the matrix. We can do this by performing a depth-first search (DFS) from each cell in the matrix.
- Step-by-step breakdown of the solution:
  1. Perform a DFS from each cell in the matrix to identify the two islands.
  2. For each island, perform a BFS to find the shortest path to the other island.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, but it is not efficient because it involves performing a DFS and BFS for each cell in the matrix.

```cpp
class Solution {
public:
    int shortestBridge(vector<vector<int>>& A) {
        int rows = A.size();
        int cols = A[0].size();
        
        // Function to perform DFS
        function<void(int, int)> dfs = [&](int r, int c) {
            if (r < 0 || r >= rows || c < 0 || c >= cols || A[r][c] == 0) return;
            A[r][c] = 0;
            dfs(r - 1, c);
            dfs(r + 1, c);
            dfs(r, c - 1);
            dfs(r, c + 1);
        };
        
        // Find the first island
        bool found = false;
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (A[r][c] == 1) {
                    dfs(r, c);
                    found = true;
                    break;
                }
            }
            if (found) break;
        }
        
        // Perform BFS to find the shortest bridge
        queue<pair<int, int>> q;
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (A[r][c] == 0) {
                    q.push({r, c});
                }
            }
        }
        
        int steps = 0;
        vector<vector<int>> dirs = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        while (!q.empty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                int r = q.front().first;
                int c = q.front().second;
                q.pop();
                for (auto& dir : dirs) {
                    int nr = r + dir[0];
                    int nc = c + dir[1];
                    if (nr < 0 || nr >= rows || nc < 0 || nc >= cols || A[nr][nc] == -1) continue;
                    if (A[nr][nc] == 1) return steps;
                    A[nr][nc] = -1;
                    q.push({nr, nc});
                }
            }
            steps++;
        }
        
        return -1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(R \times C)$, where $R$ and $C$ are the number of rows and columns in the matrix, respectively. This is because we perform a DFS and BFS for each cell in the matrix.
> - **Space Complexity:** $O(R \times C)$, where $R$ and $C$ are the number of rows and columns in the matrix, respectively. This is because we use a queue to store the cells to be processed.
> - **Why these complexities occur:** These complexities occur because we perform a DFS and BFS for each cell in the matrix.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of performing a DFS and BFS for each cell in the matrix, we can perform a DFS to identify the two islands and then perform a BFS to find the shortest bridge between them.
- Detailed breakdown of the approach:
  1. Perform a DFS to identify the two islands.
  2. For each island, perform a BFS to find the shortest bridge to the other island.
- Proof of optimality: This approach is optimal because it only requires a single DFS and BFS to find the shortest bridge between the two islands.

```cpp
class Solution {
public:
    int shortestBridge(vector<vector<int>>& A) {
        int rows = A.size();
        int cols = A[0].size();
        
        // Function to perform DFS
        function<void(int, int)> dfs = [&](int r, int c) {
            if (r < 0 || r >= rows || c < 0 || c >= cols || A[r][c] == 0) return;
            A[r][c] = -1;
            dfs(r - 1, c);
            dfs(r + 1, c);
            dfs(r, c - 1);
            dfs(r, c + 1);
        };
        
        // Find the first island
        bool found = false;
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (A[r][c] == 1) {
                    dfs(r, c);
                    found = true;
                    break;
                }
            }
            if (found) break;
        }
        
        // Perform BFS to find the shortest bridge
        queue<pair<int, int>> q;
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (A[r][c] == -1) {
                    q.push({r, c});
                }
            }
        }
        
        int steps = 0;
        vector<vector<int>> dirs = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        while (!q.empty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                int r = q.front().first;
                int c = q.front().second;
                q.pop();
                for (auto& dir : dirs) {
                    int nr = r + dir[0];
                    int nc = c + dir[1];
                    if (nr < 0 || nr >= rows || nc < 0 || nc >= cols || A[nr][nc] == -1) continue;
                    if (A[nr][nc] == 1) return steps;
                    A[nr][nc] = -1;
                    q.push({nr, nc});
                }
            }
            steps++;
        }
        
        return -1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(R \times C)$, where $R$ and $C$ are the number of rows and columns in the matrix, respectively. This is because we perform a single DFS and BFS to find the shortest bridge.
> - **Space Complexity:** $O(R \times C)$, where $R$ and $C$ are the number of rows and columns in the matrix, respectively. This is because we use a queue to store the cells to be processed.
> - **Optimality proof:** This approach is optimal because it only requires a single DFS and BFS to find the shortest bridge between the two islands.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: DFS, BFS, and graph traversal.
- Problem-solving patterns identified: Identifying the two islands and finding the shortest bridge between them.
- Optimization techniques learned: Reducing the number of DFS and BFS operations by performing them only once.
- Similar problems to practice: Other graph traversal problems, such as finding the shortest path between two nodes in a graph.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for invalid input or edge cases.
- Edge cases to watch for: The input matrix may be empty or contain only one island.
- Performance pitfalls: Performing multiple DFS and BFS operations for each cell in the matrix.
- Testing considerations: Test the solution with different input matrices, including edge cases.