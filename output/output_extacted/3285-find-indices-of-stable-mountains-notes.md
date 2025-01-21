## Find Indices of Stable Mountains
**Problem Link:** https://leetcode.com/problems/find-indices-of-stable-mountains/description

**Problem Statement:**
- Input: A 2D array `mat` of integers where each row represents a mountain range and each integer represents the height of a mountain.
- Constraints: The input array `mat` will have at least one row and one column, and all integers will be between 0 and 100.
- Expected Output: A vector of vectors, where each inner vector contains two integers representing the row and column indices of a stable mountain.
- Key Requirements:
  - A mountain is considered stable if it is not adjacent to another mountain with the same height.
  - The problem requires finding the indices of all stable mountains in the given mountain ranges.
- Example Test Cases:
  - Input: `mat = [[2,2,2],[3,3,3],[0,1,1]]`
    - Expected Output: `[[0,0],[0,1],[0,2]]`
  - Input: `mat = [[2,2,2],[3,3,3],[1,1,1]]`
    - Expected Output: `[[0,0],[0,1],[0,2]]`

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Iterate over each cell in the matrix, checking if it's a mountain and if it's stable by comparing its height with all adjacent cells.
- Step-by-step breakdown:
  1. Iterate over each cell `(i, j)` in the matrix.
  2. Check if the cell is a mountain by ensuring it's not on the edge of the matrix and its height is greater than its neighbors' heights.
  3. If it's a mountain, check if it's stable by comparing its height with all adjacent cells (up, down, left, right, and diagonals).
  4. If no adjacent cell has the same height, mark the mountain as stable and record its indices.

```cpp
vector<vector<int>> findStableMountains(vector<vector<int>>& mat) {
    vector<vector<int>> stableMountains;
    int rows = mat.size();
    int cols = mat[0].size();
    
    for (int i = 1; i < rows - 1; i++) {
        for (int j = 1; j < cols - 1; j++) {
            // Check if it's a mountain
            if (mat[i][j] > mat[i-1][j] && mat[i][j] > mat[i+1][j] && 
                mat[i][j] > mat[i][j-1] && mat[i][j] > mat[i][j+1]) {
                bool isStable = true;
                // Check stability
                for (int x = -1; x <= 1; x++) {
                    for (int y = -1; y <= 1; y++) {
                        if (x == 0 && y == 0) continue; // Skip itself
                        int nx = i + x;
                        int ny = j + y;
                        if (nx >= 0 && nx < rows && ny >= 0 && ny < cols) {
                            if (mat[nx][ny] == mat[i][j]) {
                                isStable = false;
                                break;
                            }
                        }
                    }
                    if (!isStable) break;
                }
                if (isStable) {
                    stableMountains.push_back({i, j});
                }
            }
        }
    }
    return stableMountains;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(rows \times cols \times adjacentCells)$, where $adjacentCells = 8$ for each cell (including diagonals), simplifying to $O(rows \times cols)$ because $adjacentCells$ is a constant.
> - **Space Complexity:** $O(rows \times cols)$ in the worst case, where every mountain is stable and we need to store all their indices.
> - **Why these complexities occur:** The brute force approach checks each cell once for being a mountain and then checks its stability by comparing with all adjacent cells, leading to a linear time complexity with respect to the total number of cells and a space complexity linear with the number of stable mountains.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight: The brute force approach is already quite optimal because we must check each cell to determine if it's a stable mountain. However, we can slightly optimize by directly checking the conditions for a mountain and stability without redundant comparisons.
- Detailed breakdown: Similar to the brute force approach but with a more streamlined check for mountain and stability conditions.

```cpp
vector<vector<int>> findStableMountainsOptimal(vector<vector<int>>& mat) {
    vector<vector<int>> stableMountains;
    int rows = mat.size();
    int cols = mat[0].size();
    
    for (int i = 1; i < rows - 1; i++) {
        for (int j = 1; j < cols - 1; j++) {
            bool isMountain = (mat[i][j] > mat[i-1][j] && mat[i][j] > mat[i+1][j] && 
                                mat[i][j] > mat[i][j-1] && mat[i][j] > mat[i][j+1]);
            bool isStable = true;
            for (int x = -1; x <= 1; x++) {
                for (int y = -1; y <= 1; y++) {
                    if (x == 0 && y == 0) continue; // Skip itself
                    int nx = i + x;
                    int ny = j + y;
                    if (nx >= 0 && nx < rows && ny >= 0 && ny < cols) {
                        if (mat[nx][ny] == mat[i][j]) {
                            isStable = false;
                            break;
                        }
                    }
                }
                if (!isStable) break;
            }
            if (isMountain && isStable) {
                stableMountains.push_back({i, j});
            }
        }
    }
    return stableMountains;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(rows \times cols)$, because we're checking each cell once and then potentially checking its adjacent cells for stability.
> - **Space Complexity:** $O(rows \times cols)$ in the worst case, where every mountain is stable.
> - **Optimality proof:** This approach is optimal because we must check each cell at least once to determine if it's a stable mountain. The optimization lies in directly checking the conditions without redundant comparisons, but the overall time complexity remains linear with respect to the input size.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: Iteration, conditional checks, and understanding of the problem constraints.
- Problem-solving patterns: Breaking down the problem into smaller checks (is it a mountain? is it stable?) and optimizing these checks.
- Optimization techniques: Reducing redundant comparisons and directly checking conditions.

**Mistakes to Avoid:**
- Incorrectly identifying mountains or stable mountains due to oversight in conditional checks.
- Failing to consider edge cases, such as mountains on the edges of the matrix.
- Not optimizing the checks for stability, leading to unnecessary comparisons.