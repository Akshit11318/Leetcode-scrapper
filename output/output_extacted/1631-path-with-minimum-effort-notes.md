## Path with Minimum Effort
**Problem Link:** https://leetcode.com/problems/path-with-minimum-effort/description

**Problem Statement:**
- Input: A 2D grid `heights` representing the heights of cells in a grid.
- Constraints: The grid is non-empty, and the number of rows and columns is between 1 and 10,000.
- Expected output: The minimum effort required to travel from the top-left cell to the bottom-right cell.
- Key requirements: The effort of a path is the maximum absolute difference in heights between two consecutive cells along the path.
- Example test cases:
  - Input: `[[1,2,2],[3,8,2],[5,3,5]]`
  - Output: `2`
  - Explanation: The path with the minimum effort is `1 -> 2 -> 2 -> 2 -> 3 -> 5`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can use a brute force approach to calculate the effort for all possible paths and return the minimum effort.
- Step-by-step breakdown of the solution:
  1. Generate all possible paths from the top-left cell to the bottom-right cell.
  2. For each path, calculate the effort by finding the maximum absolute difference in heights between two consecutive cells.
  3. Return the minimum effort among all paths.
- Why this approach comes to mind first: It is a straightforward approach that involves generating all possible solutions and selecting the best one.

```cpp
class Solution {
public:
    int minimumEffortPath(vector<vector<int>>& heights) {
        int rows = heights.size();
        int cols = heights[0].size();
        vector<vector<bool>> visited(rows, vector<bool>(cols, false));
        int minEffort = INT_MAX;
        
        function<void(int, int, int)> dfs = [&](int row, int col, int effort) {
            if (row == rows - 1 && col == cols - 1) {
                minEffort = min(minEffort, effort);
                return;
            }
            visited[row][col] = true;
            for (int dr = -1; dr <= 1; dr++) {
                for (int dc = -1; dc <= 1; dc++) {
                    if (abs(dr) + abs(dc) == 1) {
                        int nr = row + dr;
                        int nc = col + dc;
                        if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && !visited[nr][nc]) {
                            int newEffort = max(effort, abs(heights[nr][nc] - heights[row][col]));
                            dfs(nr, nc, newEffort);
                        }
                    }
                }
            }
            visited[row][col] = false;
        };
        
        dfs(0, 0, 0);
        return minEffort;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{rows \times cols})$, because in the worst case, we need to explore all possible paths.
> - **Space Complexity:** $O(rows \times cols)$, for the recursion stack and the visited matrix.
> - **Why these complexities occur:** The brute force approach involves generating all possible paths, which leads to exponential time complexity. The space complexity is due to the recursion stack and the visited matrix.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: We can use a priority queue to efficiently explore the cells with the minimum effort.
- Detailed breakdown of the approach:
  1. Create a priority queue to store cells to be explored, with the effort as the priority.
  2. Initialize the priority queue with the top-left cell and an effort of 0.
  3. While the priority queue is not empty, extract the cell with the minimum effort and explore its neighbors.
  4. For each neighbor, calculate the new effort and push it into the priority queue if it is not visited before.
  5. Return the effort when the bottom-right cell is reached.
- Proof of optimality: This approach is optimal because it always explores the cell with the minimum effort first, which guarantees that the minimum effort path is found.

```cpp
class Solution {
public:
    int minimumEffortPath(vector<vector<int>>& heights) {
        int rows = heights.size();
        int cols = heights[0].size();
        vector<vector<int>> efforts(rows, vector<int>(cols, INT_MAX));
        efforts[0][0] = 0;
        priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<tuple<int, int, int>>> pq;
        pq.push({0, 0, 0});
        
        while (!pq.empty()) {
            auto [effort, row, col] = pq.top();
            pq.pop();
            if (row == rows - 1 && col == cols - 1) {
                return effort;
            }
            for (int dr = -1; dr <= 1; dr++) {
                for (int dc = -1; dc <= 1; dc++) {
                    if (abs(dr) + abs(dc) == 1) {
                        int nr = row + dr;
                        int nc = col + dc;
                        if (nr >= 0 && nr < rows && nc >= 0 && nc < cols) {
                            int newEffort = max(effort, abs(heights[nr][nc] - heights[row][col]));
                            if (newEffort < efforts[nr][nc]) {
                                efforts[nr][nc] = newEffort;
                                pq.push({newEffort, nr, nc});
                            }
                        }
                    }
                }
            }
        }
        return -1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(rows \times cols \times \log(rows \times cols))$, because we use a priority queue to explore the cells.
> - **Space Complexity:** $O(rows \times cols)$, for the efforts matrix and the priority queue.
> - **Optimality proof:** This approach is optimal because it always explores the cell with the minimum effort first, which guarantees that the minimum effort path is found.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: priority queue, graph traversal.
- Problem-solving patterns identified: using a priority queue to efficiently explore the cells with the minimum effort.
- Optimization techniques learned: using a priority queue to reduce the time complexity.
- Similar problems to practice: `https://leetcode.com/problems/cheapest-flights-within-k-stops/`, `https://leetcode.com/problems/network-delay-time/`.

**Mistakes to Avoid:**
- Common implementation errors: not handling the edge cases correctly, not updating the efforts matrix correctly.
- Edge cases to watch for: when the input grid is empty, when the input grid has only one cell.
- Performance pitfalls: using a brute force approach, not using a priority queue to explore the cells.
- Testing considerations: testing the function with different input grids, testing the function with edge cases.