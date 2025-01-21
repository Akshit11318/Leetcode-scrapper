## Minimum Obstacle Removal to Reach Corner
**Problem Link:** https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/description

**Problem Statement:**
- Input format: A 2D grid `grid` of integers representing obstacles and free paths.
- Constraints: The grid size is `m x n`, where `1 <= m, n <= 1000`.
- Expected output format: The minimum number of obstacles to remove to reach the bottom-right corner from the top-left corner.
- Key requirements: The path must be from the top-left to the bottom-right, moving only right or down.
- Edge cases: The grid may contain all obstacles, or there might be no obstacles at all.

**Example Test Cases:**
- Example 1: Given `grid = [[1,1,1],[1,0,1],[1,1,1]]`, the output should be `2` because we need to remove at least 2 obstacles to reach the bottom-right corner.
- Example 2: Given `grid = [[1,1,0],[1,1,0],[1,1,0]]`, the output should be `0` because there is already a clear path to the bottom-right corner.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves trying all possible paths from the top-left to the bottom-right corner and counting the number of obstacles in each path.
- This approach is a basic form of path exploration and can be achieved using recursion or backtracking.

```cpp
class Solution {
public:
    int minimumObstacles(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        int minObstacles = INT_MAX;
        
        function<void(int, int, int)> dfs = [&](int x, int y, int obstacles) {
            if (x == m - 1 && y == n - 1) {
                minObstacles = min(minObstacles, obstacles);
                return;
            }
            if (x >= m || y >= n) return;
            
            // Try moving right
            dfs(x, y + 1, obstacles + grid[x][y]);
            
            // Try moving down
            dfs(x + 1, y, obstacles + grid[x][y]);
        };
        
        dfs(0, 0, 0);
        return minObstacles;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{m+n})$ because in the worst case, we explore all possible paths from the top-left to the bottom-right corner, which can be up to $2^{m+n}$ paths.
> - **Space Complexity:** $O(m+n)$ due to the recursive call stack.
> - **Why these complexities occur:** These complexities occur because the brute force approach tries all possible paths without any optimization, leading to exponential time complexity and linear space complexity due to recursion.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight to the optimal solution involves using a priority queue (or a similar data structure) to keep track of the cell with the minimum number of obstacles encountered so far.
- This approach is essentially a form of Dijkstra's algorithm adapted for this specific problem, where the cost of reaching a cell is the number of obstacles encountered.

```cpp
class Solution {
public:
    int minimumObstacles(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        vector<vector<int>> directions = {{0, 1}, {1, 0}};
        vector<vector<int>> obstaclesCount(m, vector<int>(n, INT_MAX));
        obstaclesCount[0][0] = grid[0][0];
        
        priority_queue<pair<int, pair<int, int>>, vector<pair<int, pair<int, int>>>, greater<>> pq;
        pq.push({grid[0][0], {0, 0}});
        
        while (!pq.empty()) {
            auto [obstacles, pos] = pq.top();
            pq.pop();
            int x = pos.first;
            int y = pos.second;
            
            for (auto& dir : directions) {
                int nx = x + dir[0];
                int ny = y + dir[1];
                
                if (nx < 0 || nx >= m || ny < 0 || ny >= n) continue;
                
                int newObstacles = obstacles + grid[nx][ny];
                if (newObstacles < obstaclesCount[nx][ny]) {
                    obstaclesCount[nx][ny] = newObstacles;
                    pq.push({newObstacles, {nx, ny}});
                }
            }
        }
        
        return obstaclesCount[m - 1][n - 1];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n \cdot \log(m \cdot n))$ because each cell is inserted into the priority queue once, and each insertion and removal operation takes $\log(m \cdot n)$ time.
> - **Space Complexity:** $O(m \cdot n)$ for storing the obstacles count for each cell and the priority queue.
> - **Optimality proof:** This approach is optimal because it explores the grid in a way that always considers the path with the minimum number of obstacles first, ensuring that when it reaches the bottom-right corner, it has found the path with the minimum obstacles.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Priority queues, Dijkstra's algorithm adaptation.
- Problem-solving patterns identified: Using the most efficient data structure for the problem, optimizing the exploration order.
- Optimization techniques learned: Adapting algorithms for specific problem constraints.
- Similar problems to practice: Other pathfinding problems with obstacles or weights.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly updating the obstacles count, not checking for visited cells properly.
- Edge cases to watch for: Grids with all obstacles, grids with no obstacles.
- Performance pitfalls: Not using the most efficient data structure for the problem.
- Testing considerations: Ensure to test with different grid sizes, obstacle distributions, and edge cases.