## Making a Large Island

**Problem Link:** https://leetcode.com/problems/making-a-large-island/description

**Problem Statement:**
- Input: A 2D array `grid` of size `n x n`, where each cell is either `0` (water) or `1` (land).
- Expected Output: The maximum area of an island that can be created by changing at most one `0` cell to `1`.
- Key Requirements and Edge Cases:
  - The grid may contain multiple islands.
  - The grid may be empty or contain only one island.
  - The grid size `n` is within the range `[1, 50]`.
- Example Test Cases:
  - `grid = [[1,0],[0,1]]`, Output: `3`
  - `grid = [[1,1],[1,0]]`, Output: `4`
  - `grid = [[0,0],[0,0]]`, Output: `1`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate over each cell in the grid, and for each cell, check all possible configurations where we can change one `0` to `1`.
- Step-by-step breakdown of the solution:
  1. Iterate over each cell `(i, j)` in the grid.
  2. If the cell is `0`, try changing it to `1` and calculate the area of the new island using DFS.
  3. Keep track of the maximum area found.
- Why this approach comes to mind first: It's a straightforward way to consider all possible configurations.

```cpp
class Solution {
public:
    int largestIsland(vector<vector<int>>& grid) {
        int n = grid.size();
        int maxArea = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 0) {
                    grid[i][j] = 1;
                    maxArea = max(maxArea, getArea(grid, i, j));
                    grid[i][j] = 0;
                }
            }
        }
        return maxArea == 0 ? n * n : maxArea;
    }

    int getArea(vector<vector<int>>& grid, int i, int j) {
        int n = grid.size();
        int area = 0;
        vector<vector<int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        stack<pair<int, int>> st;
        st.push({i, j});
        while (!st.empty()) {
            int x = st.top().first;
            int y = st.top().second;
            st.pop();
            if (x < 0 || x >= n || y < 0 || y >= n || grid[x][y] == 0) continue;
            area++;
            grid[x][y] = 0;
            for (auto& dir : directions) {
                st.push({x + dir[0], y + dir[1]});
            }
        }
        return area;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^4)$, where $n$ is the size of the grid. This is because we're iterating over each cell and performing DFS for each cell.
> - **Space Complexity:** $O(n^2)$, where $n$ is the size of the grid. This is because we're using a stack to store cells to visit.
> - **Why these complexities occur:** The brute force approach has high time complexity due to the nested iterations and DFS operations.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of trying all possible configurations, we can first identify all islands and their areas. Then, for each `0` cell, we can check which islands it can connect to and calculate the new area.
- Detailed breakdown of the approach:
  1. Identify all islands and their areas using DFS.
  2. For each `0` cell, check which islands it can connect to.
  3. Calculate the new area by adding the areas of the connected islands and the `0` cell.
- Proof of optimality: This approach considers all possible configurations and has a lower time complexity than the brute force approach.

```cpp
class Solution {
public:
    int largestIsland(vector<vector<int>>& grid) {
        int n = grid.size();
        int maxArea = 0;
        vector<vector<int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        unordered_map<int, int> areaMap;
        int index = 2;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    int area = dfs(grid, i, j, index, directions);
                    areaMap[index] = area;
                    index++;
                }
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 0) {
                    unordered_set<int> neighbors;
                    for (auto& dir : directions) {
                        int x = i + dir[0];
                        int y = j + dir[1];
                        if (x >= 0 && x < n && y >= 0 && y < n && grid[x][y] > 1) {
                            neighbors.insert(grid[x][y]);
                        }
                    }
                    int area = 1;
                    for (int neighbor : neighbors) {
                        area += areaMap[neighbor];
                    }
                    maxArea = max(maxArea, area);
                }
            }
        }
        return maxArea == 0 ? n * n : maxArea;
    }

    int dfs(vector<vector<int>>& grid, int i, int j, int index, vector<vector<int>>& directions) {
        int n = grid.size();
        int area = 1;
        grid[i][j] = index;
        for (auto& dir : directions) {
            int x = i + dir[0];
            int y = j + dir[1];
            if (x >= 0 && x < n && y >= 0 && y < n && grid[x][y] == 1) {
                area += dfs(grid, x, y, index, directions);
            }
        }
        return area;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the size of the grid. This is because we're iterating over each cell and performing DFS for each island.
> - **Space Complexity:** $O(n^2)$, where $n$ is the size of the grid. This is because we're using a stack to store cells to visit and an unordered map to store island areas.
> - **Optimality proof:** This approach has a lower time complexity than the brute force approach and considers all possible configurations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: DFS, island identification, and area calculation.
- Problem-solving patterns identified: Breaking down complex problems into smaller sub-problems and using data structures to store and retrieve information efficiently.
- Optimization techniques learned: Reducing time complexity by avoiding unnecessary iterations and using efficient data structures.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly handling edge cases, such as an empty grid or a grid with no islands.
- Edge cases to watch for: Grids with multiple islands, grids with no islands, and grids with a single island.
- Performance pitfalls: Using inefficient algorithms or data structures, such as using a brute force approach or a data structure with high time complexity.
- Testing considerations: Thoroughly testing the solution with different inputs and edge cases to ensure correctness and efficiency.