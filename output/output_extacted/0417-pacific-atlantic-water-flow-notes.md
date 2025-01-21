## Pacific Atlantic Water Flow

**Problem Link:** https://leetcode.com/problems/pacific-atlantic-water-flow/description

**Problem Statement:**
- Input: A `matrix` representing the heights of a map, and `m` and `n` representing the number of rows and columns respectively.
- Constraints: `m` and `n` are between 1 and 200.
- Expected Output: A list of coordinates `(i, j)` that can flow to both the Pacific and the Atlantic oceans.
- Key Requirements: Identify all cells that can flow to both oceans.
- Edge Cases: Empty matrix, matrix with a single cell.

**Example Test Case:**
```markdown
Input:
[
  [1,2,2,3,5],
  [3,2,3,4,4],
  [2,4,5,3,1],
  [6,7,1,4,5],
  [5,1,1,2,4]
]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
```

### Brute Force Approach

**Explanation:**
- Start by checking each cell to see if it can flow to the Pacific Ocean.
- Then, for each cell, check if it can flow to the Atlantic Ocean.
- Use a `depth-first search (DFS)` to traverse from each cell to the oceans.
- If a cell can flow to both oceans, add it to the result.

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& matrix) {
        if (matrix.empty() || matrix[0].empty()) return {};
        
        int m = matrix.size(), n = matrix[0].size();
        vector<vector<int>> pacific(m, vector<int>(n, 0));
        vector<vector<int>> atlantic(m, vector<int>(n, 0));
        vector<vector<int>> result;
        
        // Check Pacific Ocean
        for (int i = 0; i < m; i++) {
            dfs(matrix, pacific, i, 0, matrix[i][0]);
        }
        for (int j = 0; j < n; j++) {
            dfs(matrix, pacific, 0, j, matrix[0][j]);
        }
        
        // Check Atlantic Ocean
        for (int i = 0; i < m; i++) {
            dfs(matrix, atlantic, i, n - 1, matrix[i][n - 1]);
        }
        for (int j = 0; j < n; j++) {
            dfs(matrix, atlantic, m - 1, j, matrix[m - 1][j]);
        }
        
        // Find cells that can flow to both oceans
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (pacific[i][j] == 1 && atlantic[i][j] == 1) {
                    result.push_back({i, j});
                }
            }
        }
        
        return result;
    }
    
    void dfs(vector<vector<int>>& matrix, vector<vector<int>>& visited, int i, int j, int height) {
        int m = matrix.size(), n = matrix[0].size();
        if (i < 0 || i >= m || j < 0 || j >= n || visited[i][j] == 1 || matrix[i][j] < height) return;
        
        visited[i][j] = 1;
        
        dfs(matrix, visited, i - 1, j, matrix[i][j]);
        dfs(matrix, visited, i + 1, j, matrix[i][j]);
        dfs(matrix, visited, i, j - 1, matrix[i][j]);
        dfs(matrix, visited, i, j + 1, matrix[i][j]);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ and $n$ are the number of rows and columns in the matrix respectively. This is because we are performing a DFS from each cell in the matrix.
> - **Space Complexity:** $O(m \cdot n)$, where $m$ and $n$ are the number of rows and columns in the matrix respectively. This is because we are using two additional matrices to keep track of the cells that can flow to the Pacific and Atlantic oceans.

### Optimal Approach (Required)

**Explanation:**
- Instead of performing a DFS from each cell, we can start from the borders of the matrix and perform a DFS from there.
- This is because the cells that can flow to the Pacific Ocean must be connected to the Pacific border, and the cells that can flow to the Atlantic Ocean must be connected to the Atlantic border.
- We can use two separate matrices to keep track of the cells that can flow to the Pacific and Atlantic oceans.

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& matrix) {
        if (matrix.empty() || matrix[0].empty()) return {};
        
        int m = matrix.size(), n = matrix[0].size();
        vector<vector<int>> pacific(m, vector<int>(n, 0));
        vector<vector<int>> atlantic(m, vector<int>(n, 0));
        vector<vector<int>> result;
        
        // Check Pacific Ocean
        for (int i = 0; i < m; i++) {
            dfs(matrix, pacific, i, 0);
        }
        for (int j = 0; j < n; j++) {
            dfs(matrix, pacific, 0, j);
        }
        
        // Check Atlantic Ocean
        for (int i = 0; i < m; i++) {
            dfs(matrix, atlantic, i, n - 1);
        }
        for (int j = 0; j < n; j++) {
            dfs(matrix, atlantic, m - 1, j);
        }
        
        // Find cells that can flow to both oceans
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (pacific[i][j] == 1 && atlantic[i][j] == 1) {
                    result.push_back({i, j});
                }
            }
        }
        
        return result;
    }
    
    void dfs(vector<vector<int>>& matrix, vector<vector<int>>& visited, int i, int j) {
        int m = matrix.size(), n = matrix[0].size();
        if (i < 0 || i >= m || j < 0 || j >= n || visited[i][j] == 1) return;
        
        visited[i][j] = 1;
        
        if (i > 0 && matrix[i - 1][j] >= matrix[i][j]) {
            dfs(matrix, visited, i - 1, j);
        }
        if (i < m - 1 && matrix[i + 1][j] >= matrix[i][j]) {
            dfs(matrix, visited, i + 1, j);
        }
        if (j > 0 && matrix[i][j - 1] >= matrix[i][j]) {
            dfs(matrix, visited, i, j - 1);
        }
        if (j < n - 1 && matrix[i][j + 1] >= matrix[i][j]) {
            dfs(matrix, visited, i, j + 1);
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ and $n$ are the number of rows and columns in the matrix respectively. This is because we are performing a DFS from the borders of the matrix.
> - **Space Complexity:** $O(m \cdot n)$, where $m$ and $n$ are the number of rows and columns in the matrix respectively. This is because we are using two additional matrices to keep track of the cells that can flow to the Pacific and Atlantic oceans.

### Final Notes

**Learning Points:**
- The importance of understanding the problem and identifying the key constraints.
- The use of DFS to solve the problem.
- The optimization of the solution by starting from the borders of the matrix.

**Mistakes to Avoid:**
- Not checking for the base cases and edge cases.
- Not optimizing the solution by starting from the borders of the matrix.
- Not using the correct data structures to keep track of the cells that can flow to the Pacific and Atlantic oceans.