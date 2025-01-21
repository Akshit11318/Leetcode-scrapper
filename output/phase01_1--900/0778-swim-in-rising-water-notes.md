## Swim in Rising Water
**Problem Link:** https://leetcode.com/problems/swim-in-rising-water/description

**Problem Statement:**
- Input format: A 2D `grid` of integers, where `grid[i][j]` represents the height of the cell at position `(i, j)`.
- Constraints: The grid is a square of size `n x n`, where `n` is an integer between 1 and 200.
- Expected output format: The minimum time it takes to swim from the top-left cell to the bottom-right cell.
- Key requirements and edge cases to consider: The swimmer can only move to adjacent cells (up, down, left, right) if the height of the destination cell is less than or equal to the current time.
- Example test cases with explanations:
  - If the grid is `[[0,2],[1,3]]`, the minimum time is 3 because the swimmer can move from (0,0) to (0,1) to (1,1).
  - If the grid is `[[3,2],[0,1]]`, the minimum time is 3 because the swimmer can move from (0,0) to (1,0) to (1,1).

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible paths from the top-left cell to the bottom-right cell and keep track of the minimum time.
- Step-by-step breakdown of the solution:
  1. Initialize the minimum time to infinity.
  2. Define a recursive function to explore all possible paths.
  3. In the recursive function, check if the current cell is the bottom-right cell. If so, update the minimum time if necessary.
  4. Otherwise, try moving to all adjacent cells and recursively call the function.
- Why this approach comes to mind first: It's a straightforward way to explore all possible solutions, but it's inefficient due to the large number of possible paths.

```cpp
class Solution {
public:
    int swimInWater(vector<vector<int>>& grid) {
        int n = grid.size();
        int minTime = INT_MAX;
        
        function<void(int, int, int)> dfs = [&](int i, int j, int time) {
            if (i == n - 1 && j == n - 1) {
                minTime = min(minTime, time);
                return;
            }
            
            vector<pair<int, int>> dirs = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
            for (auto& dir : dirs) {
                int ni = i + dir.first;
                int nj = j + dir.second;
                if (ni >= 0 && ni < n && nj >= 0 && nj < n && grid[ni][nj] <= time) {
                    dfs(ni, nj, max(time, grid[ni][nj]));
                }
            }
        };
        
        dfs(0, 0, grid[0][0]);
        return minTime;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{n^2})$ because in the worst case, we might need to explore all possible paths.
> - **Space Complexity:** $O(n^2)$ because of the recursive call stack.
> - **Why these complexities occur:** The brute force approach explores all possible paths, which leads to exponential time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a priority queue to keep track of the cells with the minimum time.
- Detailed breakdown of the approach:
  1. Initialize a priority queue with the top-left cell and its time.
  2. Initialize a visited set to keep track of visited cells.
  3. While the priority queue is not empty, pop the cell with the minimum time and mark it as visited.
  4. If the popped cell is the bottom-right cell, return its time.
  5. Otherwise, try moving to all adjacent cells and push them to the priority queue if they have not been visited before.
- Proof of optimality: This approach is optimal because it always explores the cell with the minimum time first, which guarantees the minimum time to reach the bottom-right cell.

```cpp
class Solution {
public:
    int swimInWater(vector<vector<int>>& grid) {
        int n = grid.size();
        priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<>> pq;
        pq.push({grid[0][0], 0, 0});
        vector<vector<bool>> visited(n, vector<bool>(n, false));
        visited[0][0] = true;
        
        vector<pair<int, int>> dirs = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        while (!pq.empty()) {
            auto [time, i, j] = pq.top();
            pq.pop();
            if (i == n - 1 && j == n - 1) {
                return time;
            }
            
            for (auto& dir : dirs) {
                int ni = i + dir.first;
                int nj = j + dir.second;
                if (ni >= 0 && ni < n && nj >= 0 && nj < n && !visited[ni][nj]) {
                    pq.push({max(time, grid[ni][nj]), ni, nj});
                    visited[ni][nj] = true;
                }
            }
        }
        
        return -1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \log n)$ because we use a priority queue to keep track of the cells with the minimum time.
> - **Space Complexity:** $O(n^2)$ because of the priority queue and the visited set.
> - **Optimality proof:** This approach is optimal because it always explores the cell with the minimum time first, which guarantees the minimum time to reach the bottom-right cell.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Priority queue, graph traversal, and dynamic programming.
- Problem-solving patterns identified: Using a priority queue to keep track of the minimum time and exploring the graph in a greedy manner.
- Optimization techniques learned: Using a priority queue to reduce the time complexity from exponential to polynomial.
- Similar problems to practice: Other graph traversal problems, such as Dijkstra's algorithm and Bellman-Ford algorithm.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for visited cells before pushing them to the priority queue.
- Edge cases to watch for: The grid size can be 1x1, and the time can be 0.
- Performance pitfalls: Using a brute force approach can lead to exponential time complexity.
- Testing considerations: Test the solution with different grid sizes and time values to ensure correctness.