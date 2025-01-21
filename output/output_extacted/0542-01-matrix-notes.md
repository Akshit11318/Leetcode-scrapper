## 01 Matrix
**Problem Link:** https://leetcode.com/problems/01-matrix/description

**Problem Statement:**
- Input format: A 2D array `mat` of integers, where each integer is either 0 or 1.
- Constraints: The input matrix `mat` will have dimensions `m x n`, where `1 <= m, n <= 100`.
- Expected output format: A 2D array where each element at position `(i, j)` represents the distance from the cell `(i, j)` to the nearest cell containing a `0`.
- Key requirements and edge cases to consider: All cells containing a `1` must be assigned a value representing their distance to the nearest cell containing a `0`. Cells containing a `0` should have a value of `0`.
- Example test cases with explanations:
  - Given `mat = [[0,0,0],[0,1,0],[1,1,1]]`, the output should be `[[0,0,0],[0,1,0],[1,2,1]]`.
  - Given `mat = [[0,1,0,1,1],[0,1,0,0,1],[0,0,0,1,0],[1,0,1,1,0]]`, the output should be `[[0,1,0,1,1],[0,1,0,0,1],[0,0,0,1,0],[1,0,1,1,0]]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: For each cell in the matrix, check all other cells to find the nearest cell containing a `0`.
- Step-by-step breakdown of the solution:
  1. Iterate over each cell in the matrix.
  2. For each cell, iterate over all other cells in the matrix.
  3. Check if the other cell contains a `0`.
  4. If it does, calculate the distance between the current cell and the cell containing a `0`.
  5. Keep track of the minimum distance found for each cell.
- Why this approach comes to mind first: It is the most straightforward way to solve the problem, as it involves checking all possible distances.

```cpp
vector<vector<int>> updateMatrix(vector<vector<int>>& mat) {
    int m = mat.size();
    int n = mat[0].size();
    vector<vector<int>> result(m, vector<int>(n, INT_MAX));
    
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (mat[i][j] == 0) {
                result[i][j] = 0;
            } else {
                for (int x = 0; x < m; x++) {
                    for (int y = 0; y < n; y++) {
                        if (mat[x][y] == 0) {
                            int distance = abs(x - i) + abs(y - j);
                            result[i][j] = min(result[i][j], distance);
                        }
                    }
                }
            }
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m^2 * n^2)$, where $m$ and $n$ are the dimensions of the input matrix. This is because for each cell, we are potentially checking all other cells.
> - **Space Complexity:** $O(m * n)$, as we are creating a result matrix of the same size as the input matrix.
> - **Why these complexities occur:** The brute force approach involves nested loops that check all cells for each cell, leading to a high time complexity. The space complexity is due to the creation of the result matrix.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a breadth-first search (BFS) approach, starting from all cells containing a `0`. This way, we only need to visit each cell once.
- Detailed breakdown of the approach:
  1. Initialize a result matrix with all values set to a large number.
  2. Create a queue and add all cells containing a `0` to the queue, with their distance set to `0`.
  3. Perform BFS: For each cell in the queue, check its neighbors. If a neighbor's distance is larger than the current cell's distance plus one, update the neighbor's distance and add it to the queue.
- Proof of optimality: This approach ensures that we visit each cell in the shortest possible order, resulting in the minimum distance to the nearest cell containing a `0`.
- Why further optimization is impossible: We must visit each cell at least once to determine its distance to the nearest `0`, making this approach optimal in terms of time complexity.

```cpp
vector<vector<int>> updateMatrix(vector<vector<int>>& mat) {
    int m = mat.size();
    int n = mat[0].size();
    vector<vector<int>> result(m, vector<int>(n, INT_MAX));
    queue<pair<int, int>> q;
    
    // Add all cells containing a 0 to the queue
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (mat[i][j] == 0) {
                result[i][j] = 0;
                q.push({i, j});
            }
        }
    }
    
    vector<int> dx = {-1, 1, 0, 0};
    vector<int> dy = {0, 0, -1, 1};
    
    // Perform BFS
    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
        
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            
            if (nx >= 0 && nx < m && ny >= 0 && ny < n) {
                if (result[nx][ny] > result[x][y] + 1) {
                    result[nx][ny] = result[x][y] + 1;
                    q.push({nx, ny});
                }
            }
        }
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m * n)$, where $m$ and $n$ are the dimensions of the input matrix. This is because we visit each cell at most once.
> - **Space Complexity:** $O(m * n)$, due to the creation of the result matrix and the queue in the worst case.
> - **Optimality proof:** The BFS approach ensures that we find the shortest distance to the nearest cell containing a `0` for each cell, making it optimal.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: BFS, queue data structure, and distance calculation.
- Problem-solving patterns identified: Using BFS to find shortest distances in an unweighted graph.
- Optimization techniques learned: Reducing time complexity by visiting each cell only once.
- Similar problems to practice: Other graph traversal problems, such as finding the shortest path between two nodes.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly updating distances or forgetting to check all neighbors.
- Edge cases to watch for: Handling cells on the boundary of the matrix.
- Performance pitfalls: Using an inefficient algorithm, such as the brute force approach, for large inputs.
- Testing considerations: Verifying the correctness of the solution for different input sizes and edge cases.