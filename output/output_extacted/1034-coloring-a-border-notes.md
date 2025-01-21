## Coloring a Border
**Problem Link:** https://leetcode.com/problems/coloring-a-border/description

**Problem Statement:**
- Input format: `int n`, `int m`, `vector<vector<int>> picture`, `int targetColor`, `int targetRow`, `int targetCol`
- Constraints: `1 <= n <= 100`, `1 <= m <= 100`, `picture.length == n`, `picture[i].length == m`, `0 <= targetRow < n`, `0 <= targetCol < m`, `1 <= targetColor <= 10^9`, `0 <= picture[i][j] <= 10^9`
- Expected output format: `vector<vector<int>>`
- Key requirements and edge cases to consider: The input picture may contain borders that need to be recolored, and the target color must be applied to all pixels that are part of the border of the target color component.
- Example test cases with explanations:
    - Example 1:
        - Input: `n = 3`, `m = 3`, `picture = [[1,1,1],[1,1,1],[1,1,1]]`, `targetColor = 2`, `targetRow = 1`, `targetCol = 1`
        - Output: `[[2,2,2],[2,1,2],[2,2,2]]`
    - Example 2:
        - Input: `n = 3`, `m = 3`, `picture = [[1,1,1],[1,3,1],[1,1,1]]`, `targetColor = 2`, `targetRow = 1`, `targetCol = 1`
        - Output: `[[1,1,1],[1,3,1],[1,1,1]]`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves checking every pixel in the picture to see if it is part of the border of the target color component.
- Step-by-step breakdown of the solution:
    1. Iterate over every pixel in the picture.
    2. For each pixel, perform a depth-first search (DFS) to see if it is part of the target color component.
    3. If the pixel is part of the target color component, check if it is on the border by checking its neighboring pixels.
    4. If the pixel is on the border, recolor it with the target color.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, but it is not efficient because it involves checking every pixel in the picture.

```cpp
vector<vector<int>> colorBorder(int n, int m, vector<vector<int>>& picture, int targetColor, int targetRow, int targetCol) {
    // Perform DFS to find the target color component
    vector<vector<bool>> visited(n, vector<bool>(m, false));
    vector<vector<int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    function<bool(int, int)> dfs = [&](int row, int col) {
        if (row < 0 || row >= n || col < 0 || col >= m || visited[row][col] || picture[row][col] != picture[targetRow][targetCol]) {
            return false;
        }
        visited[row][col] = true;
        for (auto& direction : directions) {
            dfs(row + direction[0], col + direction[1]);
        }
        return true;
    };
    dfs(targetRow, targetCol);

    // Recolor the border of the target color component
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (visited[i][j]) {
                bool isBorder = false;
                for (auto& direction : directions) {
                    int newRow = i + direction[0];
                    int newCol = j + direction[1];
                    if (newRow < 0 || newRow >= n || newCol < 0 || newCol >= m || !visited[newRow][newCol]) {
                        isBorder = true;
                        break;
                    }
                }
                if (isBorder) {
                    picture[i][j] = targetColor;
                }
            }
        }
    }

    return picture;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of rows in the picture and $m$ is the number of columns. This is because we are iterating over every pixel in the picture.
> - **Space Complexity:** $O(n \cdot m)$, where $n$ is the number of rows in the picture and $m$ is the number of columns. This is because we are using a visited matrix to keep track of the pixels that have been visited.
> - **Why these complexities occur:** These complexities occur because we are using a brute force approach that involves checking every pixel in the picture.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of checking every pixel in the picture, we can start from the target pixel and perform a DFS to find the target color component.
- Detailed breakdown of the approach:
    1. Perform a DFS from the target pixel to find the target color component.
    2. During the DFS, keep track of the pixels that are part of the border of the target color component.
    3. Recolor the border pixels with the target color.
- Proof of optimality: This approach is optimal because it only involves visiting the pixels that are part of the target color component, which is a subset of the pixels in the picture.

```cpp
vector<vector<int>> colorBorder(int n, int m, vector<vector<int>>& picture, int targetColor, int targetRow, int targetCol) {
    // Perform DFS to find the target color component and keep track of the border pixels
    vector<vector<bool>> visited(n, vector<bool>(m, false));
    vector<vector<int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    vector<pair<int, int>> borderPixels;
    function<void(int, int)> dfs = [&](int row, int col) {
        if (row < 0 || row >= n || col < 0 || col >= m || visited[row][col] || picture[row][col] != picture[targetRow][targetCol]) {
            return;
        }
        visited[row][col] = true;
        bool isBorder = false;
        for (auto& direction : directions) {
            int newRow = row + direction[0];
            int newCol = col + direction[1];
            if (newRow < 0 || newRow >= n || newCol < 0 || newCol >= m || picture[newRow][newCol] != picture[targetRow][targetCol]) {
                isBorder = true;
                break;
            }
        }
        if (isBorder) {
            borderPixels.push_back({row, col});
        }
        for (auto& direction : directions) {
            dfs(row + direction[0], col + direction[1]);
        }
    };
    dfs(targetRow, targetCol);

    // Recolor the border pixels with the target color
    for (auto& pixel : borderPixels) {
        picture[pixel.first][pixel.second] = targetColor;
    }

    return picture;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(k)$, where $k$ is the number of pixels in the target color component. This is because we are only visiting the pixels that are part of the target color component.
> - **Space Complexity:** $O(k)$, where $k$ is the number of pixels in the target color component. This is because we are using a visited matrix to keep track of the pixels that have been visited.
> - **Optimality proof:** This approach is optimal because it only involves visiting the pixels that are part of the target color component, which is a subset of the pixels in the picture.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: DFS, border detection
- Problem-solving patterns identified: starting from a specific point and exploring the surrounding area
- Optimization techniques learned: reducing the number of pixels to visit by starting from a specific point
- Similar problems to practice: finding connected components, detecting cycles in a graph

**Mistakes to Avoid:**
- Common implementation errors: not checking for out-of-bounds pixels, not keeping track of visited pixels
- Edge cases to watch for: empty picture, target pixel is not part of a connected component
- Performance pitfalls: visiting every pixel in the picture, not using a visited matrix to keep track of visited pixels
- Testing considerations: testing with different picture sizes, testing with different target colors and positions.