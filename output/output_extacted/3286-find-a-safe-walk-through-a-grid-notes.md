## Find a Safe Walk through a Grid
**Problem Link:** https://leetcode.com/problems/find-a-safe-walk-through-a-grid/description

**Problem Statement:**
- Input: A 2D grid of integers representing land (`0`) and obstacles (`1`).
- Constraints: The grid will have at least one row and one column.
- Expected Output: The minimum number of steps to reach the bottom right corner from the top left corner, avoiding obstacles. If no path exists, return `-1`.
- Key Requirements:
  - The path can only move right or down.
  - The path must avoid obstacles.
- Example Test Cases:
  - `grid = [[0,0,0],[0,1,0],[0,0,0]]`, Output: `4`
  - `grid = [[0,1,0],[0,1,0],[0,0,0]]`, Output: `-1`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible paths from the top left corner to the bottom right corner.
- Step-by-step breakdown:
  1. Define a recursive function to explore all possible paths.
  2. At each cell, check if it's an obstacle. If so, return infinity to indicate this path is not viable.
  3. If the cell is not an obstacle, explore the right and down paths recursively.
  4. Keep track of the minimum path length that reaches the bottom right corner.

```cpp
#include <vector>
#include <climits>

using namespace std;

int dfs(vector<vector<int>>& grid, int x, int y, vector<vector<int>>& memo) {
    int m = grid.size();
    int n = grid[0].size();
    if (x == m - 1 && y == n - 1) return 0; // base case
    if (memo[x][y] != -1) return memo[x][y]; // memoization
    
    if (grid[x][y] == 1) { // obstacle
        memo[x][y] = INT_MAX;
        return INT_MAX;
    }
    
    int right = INT_MAX;
    int down = INT_MAX;
    
    if (y + 1 < n) {
        right = dfs(grid, x, y + 1, memo);
    }
    if (x + 1 < m) {
        down = dfs(grid, x + 1, y, memo);
    }
    
    memo[x][y] = min(right, down) + 1;
    return memo[x][y];
}

int findSafeWalk(vector<vector<int>>& grid) {
    int m = grid.size();
    int n = grid[0].size();
    vector<vector<int>> memo(m, vector<int>(n, -1));
    
    int steps = dfs(grid, 0, 0, memo);
    return steps == INT_MAX ? -1 : steps;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$ due to the recursive DFS and memoization.
> - **Space Complexity:** $O(m \cdot n)$ for the memoization table.
> - **Why these complexities occur:** The DFS explores all cells in the grid once, and memoization prevents redundant calculations.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: The problem can be solved using a modified BFS algorithm that keeps track of the minimum distance to each cell.
- Detailed breakdown:
  1. Initialize a queue with the starting cell and a distance of 0.
  2. Use a visited set to keep track of explored cells.
  3. For each cell in the queue, explore its right and down neighbors if they are not obstacles and have not been visited.
  4. Update the distance to each neighbor and mark it as visited.
  5. If the bottom right corner is reached, return the distance.

```cpp
#include <vector>
#include <queue>

using namespace std;

int findSafeWalk(vector<vector<int>>& grid) {
    int m = grid.size();
    int n = grid[0].size();
    vector<vector<bool>> visited(m, vector<bool>(n, false));
    queue<pair<int, int>> q; // (x, y)
    q.push({0, 0});
    visited[0][0] = true;
    int steps = 0;
    
    while (!q.empty()) {
        int size = q.size();
        for (int i = 0; i < size; i++) {
            auto [x, y] = q.front();
            q.pop();
            
            if (x == m - 1 && y == n - 1) {
                return steps;
            }
            
            if (y + 1 < n && grid[x][y + 1] == 0 && !visited[x][y + 1]) {
                q.push({x, y + 1});
                visited[x][y + 1] = true;
            }
            if (x + 1 < m && grid[x + 1][y] == 0 && !visited[x + 1][y]) {
                q.push({x + 1, y});
                visited[x + 1][y] = true;
            }
        }
        steps++;
    }
    
    return -1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$ due to the BFS algorithm exploring all cells.
> - **Space Complexity:** $O(m \cdot n)$ for the queue and visited set.
> - **Optimality proof:** This approach is optimal because it explores all possible paths in a level-order manner, ensuring the minimum distance to the bottom right corner is found.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: DFS, BFS, memoization, and level-order traversal.
- Problem-solving patterns: Using a visited set to avoid redundant calculations and exploring neighbors in a level-order manner.
- Optimization techniques: Memoization and using a queue to explore cells in a level-order manner.
- Similar problems to practice: Shortest Path in a Grid, Minimum Path Sum, and Unique Paths.

**Mistakes to Avoid:**
- Not using memoization or a visited set to avoid redundant calculations.
- Not exploring neighbors in a level-order manner, leading to incorrect distances.
- Not handling edge cases, such as an empty grid or a grid with no path to the bottom right corner.
- Not testing the solution thoroughly to ensure correctness.