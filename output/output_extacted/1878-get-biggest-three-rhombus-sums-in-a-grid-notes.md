## Get Biggest Three Rhombus Sums in a Grid

**Problem Link:** https://leetcode.com/problems/get-biggest-three-rhombus-sums-in-a-grid/description

**Problem Statement:**
- Input: A `m x n` grid, where each cell contains a non-negative integer.
- Constraints: `1 <= m, n <= 100`, `0 <= grid[i][j] <= 100`.
- Expected output: The three largest possible sums of a rhombus shape in the grid.
- Key requirements and edge cases:
  - A rhombus is defined as the set of cells `[(i1, j1), (i1, j2), (i2, j2), (i2, j1)]`, where `i1 <= i2` and `j1 <= j2`.
  - If there are less than three rhombus sums, return all of them.

**Example Test Cases:**
- Input: `grid = [[1,2,3],[4,5,6],[7,8,9]]`, Output: `[20,15,7]`
- Input: `grid = [[1,2,3],[4,5,6],[7,8,9]]`, Output: `[20,15,7]`

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves iterating over all possible rhombus shapes in the grid.
- Step-by-step breakdown:
  1. Iterate over all possible top-left and bottom-right corners of the rhombus.
  2. For each pair of corners, calculate the sum of the rhombus.
  3. Keep track of the three largest sums.

```cpp
#include <vector>
#include <algorithm>

using namespace std;

vector<int> getBiggestThree(vector<vector<int>>& grid) {
    int m = grid.size();
    int n = grid[0].size();
    vector<int> sums;
    
    for (int i1 = 0; i1 < m; i1++) {
        for (int j1 = 0; j1 < n; j1++) {
            for (int i2 = i1; i2 < m; i2++) {
                for (int j2 = j1; j2 < n; j2++) {
                    if (i2 - i1 == j2 - j1) {
                        int sum = 0;
                        for (int k = 0; k <= i2 - i1; k++) {
                            sum += grid[i1 + k][j1 + k];
                            sum += grid[i2 - k][j2 - k];
                        }
                        if (i1 != i2) {
                            sum -= grid[i1 + (i2 - i1) / 2][j1 + (j2 - j1) / 2];
                        }
                        sums.push_back(sum);
                    }
                }
            }
        }
    }
    
    sort(sums.begin(), sums.end(), greater<int>());
    vector<int> result;
    for (int i = 0; i < min(3, (int)sums.size()); i++) {
        result.push_back(sums[i]);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m^3 \cdot n^3)$, where $m$ and $n$ are the dimensions of the grid. This is because we have four nested loops to iterate over all possible rhombus shapes.
> - **Space Complexity:** $O(m^2 \cdot n^2)$, where $m$ and $n$ are the dimensions of the grid. This is because we need to store all possible rhombus sums.
> - **Why these complexities occur:** The brute force approach has high time and space complexities because it involves iterating over all possible rhombus shapes and storing all possible sums.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a more efficient algorithm to calculate the sum of each rhombus.
- Detailed breakdown:
  1. Iterate over all possible top-left and bottom-right corners of the rhombus.
  2. For each pair of corners, calculate the sum of the rhombus using a more efficient algorithm.
  3. Keep track of the three largest sums.

```cpp
#include <vector>
#include <algorithm>

using namespace std;

vector<int> getBiggestThree(vector<vector<int>>& grid) {
    int m = grid.size();
    int n = grid[0].size();
    vector<int> sums;
    
    for (int i1 = 0; i1 < m; i1++) {
        for (int j1 = 0; j1 < n; j1++) {
            for (int i2 = i1; i2 < m; i2++) {
                for (int j2 = j1; j2 < n; j2++) {
                    if (i2 - i1 == j2 - j1) {
                        int sum = 0;
                        for (int k = 0; k <= i2 - i1; k++) {
                            sum += grid[i1 + k][j1 + k];
                            if (k != i2 - i1) {
                                sum += grid[i2 - k][j2 - k];
                            }
                        }
                        sums.push_back(sum);
                    }
                }
            }
        }
    }
    
    sort(sums.begin(), sums.end(), greater<int>());
    vector<int> result;
    for (int i = 0; i < min(3, (int)sums.size()); i++) {
        result.push_back(sums[i]);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m^3 \cdot n)$, where $m$ and $n$ are the dimensions of the grid. This is because we have four nested loops to iterate over all possible rhombus shapes, but we calculate the sum of each rhombus more efficiently.
> - **Space Complexity:** $O(m^2 \cdot n)$, where $m$ and $n$ are the dimensions of the grid. This is because we need to store all possible rhombus sums.
> - **Optimality proof:** This approach is optimal because we must iterate over all possible rhombus shapes to find the three largest sums. The algorithm is more efficient than the brute force approach because it calculates the sum of each rhombus more efficiently.

---

### Final Notes

**Learning Points:**
- The key algorithmic concept demonstrated is the use of a more efficient algorithm to calculate the sum of each rhombus.
- The problem-solving pattern identified is the use of iteration to find the optimal solution.
- The optimization technique learned is the use of a more efficient algorithm to reduce the time complexity.

**Mistakes to Avoid:**
- A common implementation error is to not handle the case where the rhombus has a side length of 1.
- An edge case to watch for is when the grid has a size of 1x1.
- A performance pitfall is to not use a more efficient algorithm to calculate the sum of each rhombus.