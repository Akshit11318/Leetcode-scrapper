## Maximum Trailing Zeros in a Cornered Path

**Problem Link:** https://leetcode.com/problems/maximum-trailing-zeros-in-a_cornered-path/description

**Problem Statement:**
- Input: A 2D array `grid` of integers, representing the number of factors of 2 and 5 in each cell.
- Output: The maximum number of trailing zeros in a cornered path from top-left to bottom-right.
- Key requirements:
  - A cornered path is a path that only moves either down or right.
  - The number of trailing zeros in a path is the minimum number of factors of 2 and 5 in all cells in the path.
- Edge cases:
  - If there are no factors of 2 or 5 in a cell, the number of trailing zeros is 0.
  - If there are no valid paths, the output is 0.

**Example Test Cases:**
- `grid = [[1,2,3],[0,6,2],[0,5,1]]`: The maximum number of trailing zeros is 2.
- `grid = [[2,3,0],[0,6,4],[0,0,5]]`: The maximum number of trailing zeros is 2.
- `grid = [[0,0,0],[0,0,0],[0,0,0]]`: The maximum number of trailing zeros is 0.

### Brute Force Approach

**Explanation:**
- The brute force approach involves finding all possible cornered paths from top-left to bottom-right and calculating the minimum number of factors of 2 and 5 in each path.
- This approach is straightforward but inefficient due to the large number of possible paths.

```cpp
class Solution {
public:
    int maxTrailingZeros(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        int maxZeros = 0;
        
        // Generate all possible paths
        vector<vector<pair<int, int>>> paths;
        generatePaths(0, 0, m, n, {}, paths);
        
        // Calculate the minimum number of factors of 2 and 5 in each path
        for (auto& path : paths) {
            int minFactors = INT_MAX;
            for (auto& cell : path) {
                int factors = min(getFactorsOf2(grid[cell.first][cell.second]), getFactorsOf5(grid[cell.first][cell.second]));
                minFactors = min(minFactors, factors);
            }
            maxZeros = max(maxZeros, minFactors);
        }
        
        return maxZeros;
    }
    
    void generatePaths(int i, int j, int m, int n, vector<pair<int, int>> currentPath, vector<vector<pair<int, int>>>& paths) {
        if (i == m - 1 && j == n - 1) {
            paths.push_back(currentPath);
            return;
        }
        
        if (i < m - 1) {
            currentPath.push_back({i + 1, j});
            generatePaths(i + 1, j, m, n, currentPath, paths);
            currentPath.pop_back();
        }
        
        if (j < n - 1) {
            currentPath.push_back({i, j + 1});
            generatePaths(i, j + 1, m, n, currentPath, paths);
            currentPath.pop_back();
        }
    }
    
    int getFactorsOf2(int num) {
        int count = 0;
        while (num % 2 == 0) {
            num /= 2;
            count++;
        }
        return count;
    }
    
    int getFactorsOf5(int num) {
        int count = 0;
        while (num % 5 == 0) {
            num /= 5;
            count++;
        }
        return count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{m + n - 2} \cdot (m + n - 1))$, where $m$ and $n$ are the dimensions of the grid. This is because we generate all possible paths and calculate the minimum number of factors of 2 and 5 in each path.
> - **Space Complexity:** $O(m + n - 1)$, where $m$ and $n$ are the dimensions of the grid. This is because we store the current path and the minimum number of factors of 2 and 5 in each cell.
> - **Why these complexities occur:** The brute force approach involves generating all possible paths and calculating the minimum number of factors of 2 and 5 in each path, which leads to exponential time complexity.

### Optimal Approach (Required)

**Explanation:**
- The optimal approach involves using dynamic programming to calculate the maximum number of trailing zeros in each cell.
- We use two 2D arrays, `dp1` and `dp2`, to store the maximum number of trailing zeros in each cell when moving down and right, respectively.
- We initialize `dp1` and `dp2` with the minimum number of factors of 2 and 5 in each cell.
- We then update `dp1` and `dp2` by considering the maximum number of trailing zeros in the previous cell and adding the minimum number of factors of 2 and 5 in the current cell.

```cpp
class Solution {
public:
    int maxTrailingZeros(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        vector<vector<int>> dp1(m, vector<int>(n));
        vector<vector<int>> dp2(m, vector<int>(n));
        
        // Initialize dp1 and dp2
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int factors = min(getFactorsOf2(grid[i][j]), getFactorsOf5(grid[i][j]));
                dp1[i][j] = factors;
                dp2[i][j] = factors;
            }
        }
        
        // Update dp1 and dp2
        for (int i = 1; i < m; i++) {
            for (int j = 0; j < n; j++) {
                dp1[i][j] = min(dp1[i - 1][j], dp1[i][j]);
            }
        }
        
        for (int i = 0; i < m; i++) {
            for (int j = 1; j < n; j++) {
                dp2[i][j] = min(dp2[i][j - 1], dp2[i][j]);
            }
        }
        
        int maxZeros = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                maxZeros = max(maxZeros, min(dp1[i][j], dp2[i][j]));
            }
        }
        
        return maxZeros;
    }
    
    int getFactorsOf2(int num) {
        int count = 0;
        while (num % 2 == 0) {
            num /= 2;
            count++;
        }
        return count;
    }
    
    int getFactorsOf5(int num) {
        int count = 0;
        while (num % 5 == 0) {
            num /= 5;
            count++;
        }
        return count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ and $n$ are the dimensions of the grid. This is because we iterate over each cell once to update `dp1` and `dp2`.
> - **Space Complexity:** $O(m \cdot n)$, where $m$ and $n$ are the dimensions of the grid. This is because we store the maximum number of trailing zeros in each cell in `dp1` and `dp2`.
> - **Optimality proof:** The optimal approach uses dynamic programming to calculate the maximum number of trailing zeros in each cell, which leads to linear time complexity. This is because we only consider the maximum number of trailing zeros in the previous cell and add the minimum number of factors of 2 and 5 in the current cell.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: dynamic programming, minimum number of factors of 2 and 5.
- Problem-solving patterns identified: using dynamic programming to calculate the maximum number of trailing zeros in each cell.
- Optimization techniques learned: using dynamic programming to reduce time complexity from exponential to linear.

**Mistakes to Avoid:**
- Common implementation errors: not initializing `dp1` and `dp2` correctly, not updating `dp1` and `dp2` correctly.
- Edge cases to watch for: when there are no factors of 2 or 5 in a cell, when there are no valid paths.
- Performance pitfalls: using brute force approach, not using dynamic programming to calculate the maximum number of trailing zeros in each cell.
- Testing considerations: testing with different grid sizes, testing with different numbers of factors of 2 and 5 in each cell.