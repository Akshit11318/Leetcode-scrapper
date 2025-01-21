## Number of Enclaves
**Problem Link:** https://leetcode.com/problems/number-of-enclaves/description

**Problem Statement:**
- Input format and constraints: Given a 2D array `A` of size `m x n`, where `A[i][j]` is either 0 or 1, representing a grid of land and water. The task is to find the number of `enclaves`, which are groups of 1s that are not connected to the boundary of the grid.
- Expected output format: The number of enclaves.
- Key requirements and edge cases to consider: The grid can contain multiple enclaves, and the boundary of the grid is considered to be the first and last row, as well as the first and last column.
- Example test cases with explanations:
  - Example 1: 
    ```
    Input: A = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
    Output: 3
    Explanation: There are three enclaves in the given grid.
    ```
  - Example 2: 
    ```
    Input: A = [[0,1,1,0],[0,0,1,0],[0,1,0,0],[1,0,0,0]]
    Output: 0
    Explanation: There are no enclaves in the given grid.
    ```

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach would be to iterate over each cell in the grid, and for each cell that contains a 1, perform a depth-first search (DFS) to check if it is connected to the boundary. If it is not connected, then it is an enclave.
- Step-by-step breakdown of the solution:
  1. Iterate over each cell in the grid.
  2. For each cell that contains a 1, perform a DFS to check if it is connected to the boundary.
  3. If the cell is not connected to the boundary, then it is an enclave.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, but it has a high time complexity due to the repeated DFS operations.

```cpp
class Solution {
public:
    int numEnclaves(vector<vector<int>>& A) {
        int m = A.size();
        int n = A[0].size();
        int count = 0;
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (A[i][j] == 1) {
                    bool isConnected = false;
                    vector<vector<bool>> visited(m, vector<bool>(n, false));
                    
                    if (dfs(A, i, j, visited)) {
                        isConnected = true;
                    }
                    
                    if (!isConnected) {
                        count++;
                    }
                }
            }
        }
        
        return count;
    }
    
    bool dfs(vector<vector<int>>& A, int i, int j, vector<vector<bool>>& visited) {
        int m = A.size();
        int n = A[0].size();
        
        if (i < 0 || i >= m || j < 0 || j >= n || A[i][j] == 0 || visited[i][j]) {
            return false;
        }
        
        if (i == 0 || i == m - 1 || j == 0 || j == n - 1) {
            return true;
        }
        
        visited[i][j] = true;
        
        return dfs(A, i - 1, j, visited) || dfs(A, i + 1, j, visited) || dfs(A, i, j - 1, visited) || dfs(A, i, j + 1, visited);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n \cdot (m + n))$, where $m$ and $n$ are the dimensions of the grid. This is because in the worst case, we need to perform a DFS operation for each cell in the grid.
> - **Space Complexity:** $O(m \cdot n)$, where $m$ and $n$ are the dimensions of the grid. This is because we need to store the visited cells in the DFS operation.
> - **Why these complexities occur:** The high time complexity occurs because we are performing a DFS operation for each cell in the grid, and the DFS operation itself has a time complexity of $O(m + n)$. The space complexity occurs because we need to store the visited cells in the DFS operation.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of performing a DFS operation for each cell in the grid, we can perform a DFS operation only for the cells that are connected to the boundary. This is because the cells that are not connected to the boundary are the enclaves.
- Detailed breakdown of the approach:
  1. Perform a DFS operation for the cells that are connected to the boundary.
  2. Mark the cells that are connected to the boundary as visited.
  3. Iterate over the grid and count the number of cells that are not visited and contain a 1.
- Proof of optimality: This approach is optimal because we are only performing a DFS operation for the cells that are connected to the boundary, which reduces the time complexity to $O(m \cdot n)$.

```cpp
class Solution {
public:
    int numEnclaves(vector<vector<int>>& A) {
        int m = A.size();
        int n = A[0].size();
        
        // Perform DFS operation for the cells that are connected to the boundary
        for (int i = 0; i < m; i++) {
            dfs(A, i, 0);
            dfs(A, i, n - 1);
        }
        
        for (int j = 0; j < n; j++) {
            dfs(A, 0, j);
            dfs(A, m - 1, j);
        }
        
        int count = 0;
        
        // Count the number of cells that are not visited and contain a 1
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (A[i][j] == 1) {
                    count++;
                }
            }
        }
        
        return count;
    }
    
    void dfs(vector<vector<int>>& A, int i, int j) {
        int m = A.size();
        int n = A[0].size();
        
        if (i < 0 || i >= m || j < 0 || j >= n || A[i][j] == 0) {
            return;
        }
        
        A[i][j] = 0;
        
        dfs(A, i - 1, j);
        dfs(A, i + 1, j);
        dfs(A, i, j - 1);
        dfs(A, i, j + 1);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ and $n$ are the dimensions of the grid. This is because we are performing a DFS operation for the cells that are connected to the boundary, and then iterating over the grid to count the number of enclaves.
> - **Space Complexity:** $O(m \cdot n)$, where $m$ and $n$ are the dimensions of the grid. This is because we need to store the visited cells in the DFS operation.
> - **Optimality proof:** This approach is optimal because we are only performing a DFS operation for the cells that are connected to the boundary, which reduces the time complexity to $O(m \cdot n)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: DFS, boundary checking, and counting.
- Problem-solving patterns identified: Reducing the problem to a simpler subproblem, and using a DFS operation to solve the subproblem.
- Optimization techniques learned: Reducing the number of DFS operations by only performing them for the cells that are connected to the boundary.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for boundary conditions, and not marking the visited cells in the DFS operation.
- Edge cases to watch for: Grids with a single cell, and grids with no enclaves.
- Performance pitfalls: Performing a DFS operation for each cell in the grid, which can result in a high time complexity.
- Testing considerations: Testing the solution with different grid sizes, and testing the solution with grids that have no enclaves.