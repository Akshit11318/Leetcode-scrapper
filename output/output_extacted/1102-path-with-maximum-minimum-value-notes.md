## Path with Maximum Minimum Value

**Problem Link:** https://leetcode.com/problems/path-with-maximum-minimum-value/description

**Problem Statement:**
- Input format: A 2D grid `grid` of size `m x n`, where each cell contains an integer value.
- Constraints: `1 <= m, n <= 100`, `1 <= grid[i][j] <= 10^9`.
- Expected output format: The maximum minimum value along all possible paths from the top-left cell to the bottom-right cell.
- Key requirements and edge cases to consider:
  - The path must consist of only right and down movements.
  - The minimum value along the path is the smallest value among all cells in the path.
- Example test cases with explanations:
  - `grid = [[5,4,5],[1,0,1],[5,1,1]]`, the output should be `4`, as the path with the maximum minimum value is `5 -> 4 -> 5 -> 1 -> 1 -> 1`.
  - `grid = [[2,2,1],[1,2,1],[1,2,1]]`, the output should be `2`, as the path with the maximum minimum value is `2 -> 2 -> 2 -> 2 -> 2`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To find the maximum minimum value along all possible paths, we can generate all possible paths and calculate the minimum value for each path.
- Step-by-step breakdown of the solution:
  1. Generate all possible paths from the top-left cell to the bottom-right cell using only right and down movements.
  2. For each path, calculate the minimum value by iterating through all cells in the path.
  3. Keep track of the maximum minimum value found among all paths.
- Why this approach comes to mind first: It is a straightforward approach that considers all possible paths and calculates the minimum value for each path.

```cpp
class Solution {
public:
    int maximumMinimumPath(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        vector<vector<int>> directions = {{0, 1}, {1, 0}};
        int maxMin = INT_MIN;
        
        function<void(int, int, int, int)> dfs = [&](int x, int y, int minVal, int pathLen) {
            if (x == m - 1 && y == n - 1) {
                maxMin = max(maxMin, minVal);
                return;
            }
            int currentMin = min(minVal, grid[x][y]);
            for (auto& dir : directions) {
                int newX = x + dir[0];
                int newY = y + dir[1];
                if (newX >= 0 && newX < m && newY >= 0 && newY < n) {
                    dfs(newX, newY, currentMin, pathLen + 1);
                }
            }
        };
        
        dfs(0, 0, grid[0][0], 0);
        return maxMin;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{m + n})$, as in the worst case, we may need to explore all possible paths.
> - **Space Complexity:** $O(m + n)$, for the recursive call stack.
> - **Why these complexities occur:** The brute force approach explores all possible paths, resulting in exponential time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a priority queue to efficiently explore the paths with the maximum minimum value.
- Detailed breakdown of the approach:
  1. Initialize a priority queue with the top-left cell and its value.
  2. While the priority queue is not empty, pop the cell with the maximum minimum value and explore its neighbors.
  3. For each neighbor, calculate the minimum value by taking the minimum of the current cell's value and the neighbor's value.
  4. Push the neighbor into the priority queue if it has not been visited before.
  5. Repeat the process until the bottom-right cell is reached.
- Proof of optimality: This approach ensures that we always explore the paths with the maximum minimum value first, resulting in the optimal solution.

```cpp
class Solution {
public:
    int maximumMinimumPath(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        vector<vector<int>> directions = {{0, 1}, {1, 0}};
        vector<vector<bool>> visited(m, vector<bool>(n, false));
        priority_queue<pair<int, pair<int, int>>, vector<pair<int, pair<int, int>>>, greater<pair<int, pair<int, int>>>> pq;
        pq.push({grid[0][0], {0, 0}});
        
        while (!pq.empty()) {
            auto [val, pos] = pq.top();
            pq.pop();
            int x = pos.first;
            int y = pos.second;
            visited[x][y] = true;
            
            if (x == m - 1 && y == n - 1) {
                return val;
            }
            
            for (auto& dir : directions) {
                int newX = x + dir[0];
                int newY = y + dir[1];
                if (newX >= 0 && newX < m && newY >= 0 && newY < n && !visited[newX][newY]) {
                    pq.push({min(val, grid[newX][newY]), {newX, newY}});
                }
            }
        }
        
        return -1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n \cdot \log(m \cdot n))$, as we use a priority queue to explore the cells.
> - **Space Complexity:** $O(m \cdot n)$, for the visited matrix and the priority queue.
> - **Optimality proof:** This approach ensures that we always explore the paths with the maximum minimum value first, resulting in the optimal solution.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Priority queue, graph traversal.
- Problem-solving patterns identified: Using a priority queue to efficiently explore the paths with the maximum minimum value.
- Optimization techniques learned: Using a priority queue to reduce the time complexity.
- Similar problems to practice: Path with Maximum Minimum Value, Minimum Path Sum, etc.

**Mistakes to Avoid:**
- Common implementation errors: Not handling the boundary cases correctly.
- Edge cases to watch for: The grid may contain negative values, and the path may not exist.
- Performance pitfalls: Using a brute force approach that results in exponential time complexity.
- Testing considerations: Test the solution with different grid sizes and values to ensure its correctness and performance.