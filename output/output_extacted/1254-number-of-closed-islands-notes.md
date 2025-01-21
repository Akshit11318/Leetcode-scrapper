## Number of Closed Islands

**Problem Link:** https://leetcode.com/problems/number-of-closed-islands/description

**Problem Statement:**
- Input format: a 2D grid `grid` of integers where `grid[i][j]` can be either `0` (representing water) or `1` (representing land).
- Constraints: $1 \leq n, m \leq 10^2$, where `n` and `m` are the dimensions of the grid.
- Expected output format: the number of `closed islands`, which are islands (groups of `1`s) that are not connected to the boundary of the grid.
- Key requirements and edge cases to consider:
  - Islands are considered closed if they are not connected to the boundary of the grid.
  - The grid can contain multiple islands, and some may be open (connected to the boundary) while others are closed.
  - An island is considered connected if there is a path of `1`s connecting it to the boundary.
- Example test cases with explanations:
  - For the grid `[[1,1,1,1,1],[1,1,1,1,1],[1,1,0,1,1],[1,1,1,1,1],[1,1,1,1,1]]`, the output should be `1` because there is only one closed island (the single `0` in the middle).
  - For the grid `[[0,0,1,0,0],[0,1,1,1,0],[0,1,0,1,0],[0,1,1,1,0],[0,0,0,0,0]]`, the output should be `2` because there are two closed islands.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The most straightforward way to solve this problem is to check each cell in the grid and perform a depth-first search (DFS) to see if it is part of an island. If the island is not connected to the boundary, it is a closed island.
- Step-by-step breakdown of the solution:
  1. Iterate over each cell in the grid.
  2. If the cell is `1` (land) and has not been visited yet, perform a DFS from this cell.
  3. During the DFS, mark all visited cells as `visited` to avoid revisiting them.
  4. If the DFS reaches the boundary, mark the current island as an open island.
  5. After checking all cells, count the number of closed islands.

```cpp
#include <vector>
using namespace std;

void dfs(vector<vector<int>>& grid, int i, int j, vector<vector<bool>>& visited) {
    if (i < 0 || i >= grid.size() || j < 0 || j >= grid[0].size() || grid[i][j] == 0 || visited[i][j]) {
        return;
    }
    visited[i][j] = true;
    dfs(grid, i - 1, j, visited);
    dfs(grid, i + 1, j, visited);
    dfs(grid, i, j - 1, visited);
    dfs(grid, i, j + 1, visited);
}

int closedIsland(vector<vector<int>>& grid) {
    int n = grid.size();
    int m = grid[0].size();
    vector<vector<bool>> visited(n, vector<bool>(m, false));
    int count = 0;
    
    // Mark all islands connected to the boundary as visited
    for (int i = 0; i < n; i++) {
        dfs(grid, i, 0, visited);
        dfs(grid, i, m - 1, visited);
    }
    for (int j = 0; j < m; j++) {
        dfs(grid, 0, j, visited);
        dfs(grid, n - 1, j, visited);
    }
    
    // Count the number of closed islands
    for (int i = 1; i < n - 1; i++) {
        for (int j = 1; j < m - 1; j++) {
            if (grid[i][j] == 1 && !visited[i][j]) {
                dfs(grid, i, j, visited);
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ and $m$ are the dimensions of the grid. This is because in the worst case, we visit each cell once during the DFS.
> - **Space Complexity:** $O(n \cdot m)$, for the `visited` grid.
> - **Why these complexities occur:** The time complexity is linear because we potentially visit each cell once, and the space complexity is also linear because we need to keep track of visited cells.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of checking each cell and performing a DFS, we can first identify all islands connected to the boundary and mark them as visited. Then, we only need to count the number of islands that are not marked as visited.
- Detailed breakdown of the approach:
  1. Perform a DFS from the boundary to mark all islands connected to the boundary as visited.
  2. Iterate over the grid again to count the number of islands that are not marked as visited.
- Proof of optimality: This approach is optimal because it only requires two passes over the grid: one to mark visited islands and another to count closed islands.

```cpp
int closedIsland(vector<vector<int>>& grid) {
    int n = grid.size();
    int m = grid[0].size();
    vector<vector<bool>> visited(n, vector<bool>(m, false));
    
    // Mark all islands connected to the boundary as visited
    for (int i = 0; i < n; i++) {
        dfs(grid, i, 0, visited);
        dfs(grid, i, m - 1, visited);
    }
    for (int j = 0; j < m; j++) {
        dfs(grid, 0, j, visited);
        dfs(grid, n - 1, j, visited);
    }
    
    int count = 0;
    for (int i = 1; i < n - 1; i++) {
        for (int j = 1; j < m - 1; j++) {
            if (grid[i][j] == 1 && !visited[i][j]) {
                dfs(grid, i, j, visited);
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, because we make two passes over the grid: one to mark visited islands and another to count closed islands.
> - **Space Complexity:** $O(n \cdot m)$, for the `visited` grid.
> - **Optimality proof:** This is the optimal solution because it minimizes the number of operations required to solve the problem, only visiting each cell a constant number of times.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: DFS, grid traversal, and island counting.
- Problem-solving patterns identified: identifying connected components in a graph (in this case, the grid) and using a visited matrix to keep track of visited cells.
- Optimization techniques learned: reducing the number of DFS calls by first marking visited islands connected to the boundary.

**Mistakes to Avoid:**
- Not properly marking visited cells, leading to incorrect counts of closed islands.
- Not checking for boundary conditions during DFS, potentially leading to out-of-bounds errors.
- Not optimizing the solution by first marking visited islands, potentially leading to inefficient solutions.