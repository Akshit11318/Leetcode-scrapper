## Minimum Number of Visited Cells in a Grid

**Problem Link:** https://leetcode.com/problems/minimum-number-of-visited-cells-in-a-grid/description

**Problem Statement:**
- Input: A `m x n` grid, where each cell contains a value `val` representing the number of cells that can be visited.
- Constraints: `1 <= m, n <= 10^5`, `1 <= val <= 10^6`.
- Expected Output: The minimum number of visited cells in the grid.
- Key Requirements:
  - The grid is represented as a 2D array `grid`, where `grid[i][j]` is the value in the cell at row `i` and column `j`.
  - The function should return the minimum number of visited cells.

**Example Test Cases:**
- `grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]`, output: `3`
- `grid = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]`, output: `1`

---

### Brute Force Approach

**Explanation:**
- The brute force approach involves iterating over each cell in the grid and checking if it can be visited.
- We keep track of the minimum number of visited cells.

```cpp
class Solution {
public:
    int minimumVisitedCells(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        int minVisited = INT_MAX;
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                bool visited[m][n];
                memset(visited, false, sizeof(visited));
                int visitedCells = 0;
                
                // Perform DFS from each cell
                dfs(grid, i, j, visited, visitedCells);
                
                // Update minimum visited cells
                minVisited = min(minVisited, visitedCells);
            }
        }
        
        return minVisited;
    }
    
    void dfs(vector<vector<int>>& grid, int i, int j, bool visited[100005][100005], int& visitedCells) {
        int m = grid.size();
        int n = grid[0].size();
        
        if (i < 0 || i >= m || j < 0 || j >= n || visited[i][j]) {
            return;
        }
        
        visited[i][j] = true;
        visitedCells++;
        
        // Visit all cells that can be reached from the current cell
        for (int k = 1; k <= grid[i][j]; k++) {
            dfs(grid, i + k, j, visited, visitedCells);
            dfs(grid, i, j + k, visited, visitedCells);
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n \cdot \sum_{i=1}^{m} \sum_{j=1}^{n} val_{ij})$, where $val_{ij}$ is the value in the cell at row `i` and column `j`.
> - **Space Complexity:** $O(m \cdot n)$, where $m$ and $n$ are the dimensions of the grid.
> - **Why these complexities occur:** The brute force approach involves iterating over each cell in the grid and performing a depth-first search (DFS) from each cell. The time complexity is dominated by the DFS operations, which can visit up to $\sum_{i=1}^{m} \sum_{j=1}^{n} val_{ij}$ cells. The space complexity is due to the recursive call stack and the visited array.

---

### Optimal Approach (Required)

**Explanation:**
- The optimal approach involves using a priority queue to keep track of the cells that can be visited next.
- We start by adding the cell at position `(0, 0)` to the priority queue.
- Then, we iteratively extract the cell with the minimum value from the priority queue and add its neighbors to the queue.
- We keep track of the minimum number of visited cells.

```cpp
class Solution {
public:
    int minimumVisitedCells(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        int minVisited = INT_MAX;
        bool visited[m][n];
        memset(visited, false, sizeof(visited));
        
        priority_queue<pair<int, pair<int, int>>, vector<pair<int, pair<int, int>>>, greater<pair<int, pair<int, int>>>> pq;
        pq.push({grid[0][0], {0, 0}});
        visited[0][0] = true;
        
        while (!pq.empty()) {
            auto [val, pos] = pq.top();
            pq.pop();
            int i = pos.first;
            int j = pos.second;
            
            // Update minimum visited cells
            minVisited = min(minVisited, i + j + 1);
            
            // Add neighbors to the priority queue
            for (int k = 1; k <= val; k++) {
                if (i + k < m && !visited[i + k][j]) {
                    pq.push({grid[i + k][j], {i + k, j}});
                    visited[i + k][j] = true;
                }
                if (j + k < n && !visited[i][j + k]) {
                    pq.push({grid[i][j + k], {i, j + k}});
                    visited[i][j + k] = true;
                }
            }
        }
        
        return minVisited;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n \cdot \log(m \cdot n))$, where $m$ and $n$ are the dimensions of the grid.
> - **Space Complexity:** $O(m \cdot n)$, where $m$ and $n$ are the dimensions of the grid.
> - **Optimality proof:** The optimal approach uses a priority queue to keep track of the cells that can be visited next. This ensures that we always visit the cell with the minimum value first, which minimizes the number of visited cells. The time complexity is dominated by the priority queue operations, which take $O(\log(m \cdot n))$ time per operation. The space complexity is due to the priority queue and the visited array.

---

### Final Notes

**Learning Points:**
- The importance of using data structures like priority queues to optimize the solution.
- The use of `memset` to initialize arrays.
- The importance of keeping track of visited cells to avoid infinite loops.

**Mistakes to Avoid:**
- Not checking for visited cells before adding them to the priority queue.
- Not updating the minimum visited cells correctly.
- Not handling edge cases correctly.