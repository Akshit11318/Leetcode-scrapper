## Minimum Cost to Make at Least One Valid Path in a Grid

**Problem Link:** https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/description

**Problem Statement:**
- Input format: A 2D grid of integers `grid` where `grid[i][j]` represents the cost to make the cell at position `(i, j)` valid, and two integers `startRow` and `startColumn` representing the starting position.
- Constraints: The grid size is `m x n`, and `0 <= startRow < m` and `0 <= startColumn < n`.
- Expected output format: The minimum cost to make at least one valid path from the starting position to any cell in the grid.
- Key requirements and edge cases to consider:
  - The grid can contain obstacles or cells that cannot be made valid.
  - The cost to make a cell valid can vary.
  - The path must be valid, meaning it must not contain any obstacles or invalid cells.
- Example test cases:
  - `grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]`, `startRow = 0`, `startColumn = 0`. The minimum cost to make at least one valid path is `3`.
  - `grid = [[1,1,3],[3,2,2],[1,1,4]]`, `startRow = 2`, `startColumn = 0`. The minimum cost to make at least one valid path is `1`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can try all possible paths from the starting position to any cell in the grid and calculate the minimum cost for each path.
- Step-by-step breakdown of the solution:
  1. Iterate over all cells in the grid.
  2. For each cell, try all possible paths from the starting position to that cell.
  3. Calculate the minimum cost for each path by summing up the costs of the cells in the path.
  4. Update the minimum cost if a path with a lower cost is found.
- Why this approach comes to mind first: It is a straightforward and intuitive approach to try all possible paths and calculate the minimum cost.

```cpp
#include <vector>
#include <climits>

int minCost(vector<vector<int>>& grid, int startRow, int startColumn) {
    int m = grid.size();
    int n = grid[0].size();
    int minCost = INT_MAX;
    
    // Try all possible paths
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            int cost = 0;
            int row = startRow;
            int col = startColumn;
            bool isValidPath = true;
            
            // Try to reach the cell (i, j) from the starting position
            while (row != i || col != j) {
                if (row < i) row++;
                else if (row > i) row--;
                else if (col < j) col++;
                else if (col > j) col--;
                
                cost += grid[row][col];
                
                // If the cost exceeds the current minimum cost, stop trying this path
                if (cost > minCost) break;
            }
            
            // Update the minimum cost if a path with a lower cost is found
            if (cost < minCost) minCost = cost;
        }
    }
    
    return minCost;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m^2 \cdot n^2)$, where $m$ is the number of rows and $n$ is the number of columns in the grid. This is because we try all possible paths from the starting position to any cell in the grid.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the minimum cost and the current cost.
> - **Why these complexities occur:** The time complexity occurs because we try all possible paths, and the space complexity occurs because we only use a constant amount of space.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: We can use a priority queue to efficiently explore the cells in the grid in order of their minimum cost.
- Detailed breakdown of the approach:
  1. Initialize a priority queue with the starting position and its cost.
  2. While the priority queue is not empty, extract the cell with the minimum cost and explore its neighbors.
  3. Update the minimum cost for each neighbor and add it to the priority queue if it has not been visited before.
  4. Repeat steps 2-3 until the priority queue is empty.
- Proof of optimality: This approach is optimal because it explores the cells in the grid in order of their minimum cost, ensuring that we find the minimum cost to make at least one valid path.

```cpp
#include <vector>
#include <queue>
#include <climits>

using namespace std;

struct Cell {
    int row;
    int col;
    int cost;
};

struct Compare {
    bool operator()(const Cell& a, const Cell& b) {
        return a.cost > b.cost;
    }
};

int minCost(vector<vector<int>>& grid, int startRow, int startColumn) {
    int m = grid.size();
    int n = grid[0].size();
    vector<vector<bool>> visited(m, vector<bool>(n, false));
    priority_queue<Cell, vector<Cell>, Compare> pq;
    
    // Initialize the priority queue with the starting position
    pq.push({startRow, startColumn, grid[startRow][startColumn]});
    visited[startRow][startColumn] = true;
    
    // Explore the cells in the grid in order of their minimum cost
    while (!pq.empty()) {
        Cell cell = pq.top();
        pq.pop();
        
        // If the current cell is a valid path, return its cost
        if (cell.row == 0 || cell.row == m - 1 || cell.col == 0 || cell.col == n - 1) {
            return cell.cost;
        }
        
        // Explore the neighbors of the current cell
        for (int dr = -1; dr <= 1; dr++) {
            for (int dc = -1; dc <= 1; dc++) {
                if (abs(dr) + abs(dc) != 1) continue;
                
                int nr = cell.row + dr;
                int nc = cell.col + dc;
                
                if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
                
                if (!visited[nr][nc]) {
                    visited[nr][nc] = true;
                    pq.push({nr, nc, cell.cost + grid[nr][nc]});
                }
            }
        }
    }
    
    return -1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n \cdot \log(m \cdot n))$, where $m$ is the number of rows and $n$ is the number of columns in the grid. This is because we use a priority queue to efficiently explore the cells in the grid.
> - **Space Complexity:** $O(m \cdot n)$, as we use a priority queue to store the cells to be explored and a visited matrix to keep track of the visited cells.
> - **Optimality proof:** This approach is optimal because it explores the cells in the grid in order of their minimum cost, ensuring that we find the minimum cost to make at least one valid path.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Priority queue, graph traversal.
- Problem-solving patterns identified: Using a priority queue to efficiently explore the cells in the grid.
- Optimization techniques learned: Using a priority queue to reduce the time complexity.
- Similar problems to practice: Minimum cost to make at least one valid path in a weighted graph.

**Mistakes to Avoid:**
- Common implementation errors: Not using a priority queue to efficiently explore the cells in the grid.
- Edge cases to watch for: Handling the case where the starting position is a valid path.
- Performance pitfalls: Not using a visited matrix to keep track of the visited cells, resulting in infinite loops.
- Testing considerations: Testing the implementation with different grid sizes and starting positions to ensure correctness and efficiency.