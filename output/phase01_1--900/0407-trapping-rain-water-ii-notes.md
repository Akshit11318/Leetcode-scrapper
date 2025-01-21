## Trapping Rain Water II

**Problem Link:** https://leetcode.com/problems/trapping-rain-water-ii/description

**Problem Statement:**
- Input: A 2D grid of integers representing the height of each cell.
- Constraints: The grid will contain at least one cell, and all cells will have a height between 1 and $10^5$.
- Expected Output: The amount of water that can be trapped between the cells.
- Key Requirements:
  - The water can flow in any of the four directions (up, down, left, right) from a cell.
  - A cell can trap water if its height is less than the minimum height of its neighboring cells.
- Example Test Cases:
  - Input: `heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]`
  - Output: `4`
  - Explanation: Water can be trapped between the cells with heights 3 and 2 in the first row.

---

### Brute Force Approach

**Explanation:**
- The brute force approach involves calculating the amount of water that can be trapped at each cell by comparing its height with the heights of its neighboring cells.
- For each cell, we calculate the minimum height of its neighboring cells and subtract the height of the current cell from it to get the amount of water that can be trapped.
- We repeat this process for all cells in the grid and sum up the amounts of water that can be trapped at each cell.

```cpp
int trapRainWater(vector<vector<int>>& heightMap) {
    int m = heightMap.size();
    int n = heightMap[0].size();
    int result = 0;
    
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            int minHeight = INT_MAX;
            for (int x = -1; x <= 1; x++) {
                for (int y = -1; y <= 1; y++) {
                    if (abs(x) + abs(y) == 1) {
                        int nx = i + x;
                        int ny = j + y;
                        if (nx >= 0 && nx < m && ny >= 0 && ny < n) {
                            minHeight = min(minHeight, heightMap[nx][ny]);
                        }
                    }
                }
            }
            if (minHeight > heightMap[i][j]) {
                result += minHeight - heightMap[i][j];
            }
        }
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n \cdot 4)$, where $m$ is the number of rows and $n$ is the number of columns in the grid. This is because we are iterating over all cells in the grid and for each cell, we are iterating over its neighboring cells.
> - **Space Complexity:** $O(1)$, as we are not using any extra space that scales with the input size.
> - **Why these complexities occur:** The time complexity occurs because we are using nested loops to iterate over the cells and their neighboring cells. The space complexity is constant because we are only using a fixed amount of space to store the result and the minimum height of the neighboring cells.

---

### Optimal Approach (Required)

**Explanation:**
- The optimal approach involves using a priority queue to keep track of the cells with the lowest heights.
- We start by adding all the cells on the border of the grid to the priority queue, as these cells cannot trap water.
- Then, we repeatedly remove the cell with the lowest height from the priority queue and add its neighboring cells to the queue if they have not been visited before.
- For each neighboring cell, we calculate the amount of water that can be trapped by subtracting its height from the height of the cell we just removed from the queue.
- We repeat this process until the priority queue is empty.

```cpp
int trapRainWater(vector<vector<int>>& heightMap) {
    int m = heightMap.size();
    int n = heightMap[0].size();
    int result = 0;
    priority_queue<pair<int, pair<int, int>>, vector<pair<int, pair<int, int>>>, greater<pair<int, pair<int, int>>>> pq;
    vector<vector<bool>> visited(m, vector<bool>(n, false));
    
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (i == 0 || j == 0 || i == m - 1 || j == n - 1) {
                pq.push({heightMap[i][j], {i, j}});
                visited[i][j] = true;
            }
        }
    }
    
    while (!pq.empty()) {
        auto [h, pos] = pq.top();
        pq.pop();
        int x = pos.first;
        int y = pos.second;
        
        for (int dx = -1; dx <= 1; dx++) {
            for (int dy = -1; dy <= 1; dy++) {
                if (abs(dx) + abs(dy) == 1) {
                    int nx = x + dx;
                    int ny = y + dy;
                    if (nx >= 0 && nx < m && ny >= 0 && ny < n && !visited[nx][ny]) {
                        if (h > heightMap[nx][ny]) {
                            result += h - heightMap[nx][ny];
                        }
                        pq.push({max(h, heightMap[nx][ny]), {nx, ny}});
                        visited[nx][ny] = true;
                    }
                }
            }
        }
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n \cdot \log(m \cdot n))$, where $m$ is the number of rows and $n$ is the number of columns in the grid. This is because we are using a priority queue to keep track of the cells with the lowest heights.
> - **Space Complexity:** $O(m \cdot n)$, as we are using a priority queue and a visited array to keep track of the cells.
> - **Optimality proof:** This approach is optimal because it uses a priority queue to keep track of the cells with the lowest heights, which ensures that we are always processing the cell with the lowest height first. This is necessary to calculate the amount of water that can be trapped at each cell correctly.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: priority queue, visited array, and nested loops.
- Problem-solving patterns identified: using a priority queue to keep track of the cells with the lowest heights and calculating the amount of water that can be trapped at each cell.
- Optimization techniques learned: using a priority queue to reduce the time complexity.
- Similar problems to practice: Trapping Rain Water, Trapping Rain Water III.

**Mistakes to Avoid:**
- Common implementation errors: not checking for the border cells, not using a priority queue to keep track of the cells with the lowest heights.
- Edge cases to watch for: empty grid, grid with only one cell, grid with all cells having the same height.
- Performance pitfalls: using a brute force approach, not using a priority queue to keep track of the cells with the lowest heights.
- Testing considerations: test the solution with different grid sizes, test the solution with different height values, test the solution with edge cases.