## Last Day Where You Can Still Cross

**Problem Link:** https://leetcode.com/problems/last-day-where-you-can-still-cross/description

**Problem Statement:**
- Input format: `int[][] cells` - a 2D array representing a grid where each cell contains a day when it becomes flooded.
- Constraints: The grid is guaranteed to have at least one cell, and the number of cells is at most $10^5$.
- Expected output format: The last day on which you can still cross from the top left to the bottom right using a path of unflooded cells.
- Key requirements and edge cases to consider:
  - A path can only be formed by moving right or down.
  - A cell is considered unflooded if its value is greater than the current day.
- Example test cases with explanations:
  - For `cells = [[1,2,3],[4,5,6]]`, the output should be `4` because on the fourth day, you can still cross from the top left to the bottom right.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The most straightforward way to solve this problem is to check every possible path from the top left to the bottom right for each day.
- Step-by-step breakdown of the solution:
  1. Iterate through each day.
  2. For each day, check every possible path from the top left to the bottom right to see if it's flooded.
  3. If a path exists where all cells are unflooded, then this day is a potential solution.
- Why this approach comes to mind first: It directly addresses the problem statement by simulating the flooding process day by day and checking for paths.

```cpp
#include <iostream>
#include <vector>

using namespace std;

bool canCross(vector<vector<int>>& cells, int day) {
    int m = cells.size();
    int n = cells[0].size();
    vector<vector<bool>> visited(m, vector<bool>(n, false));

    // Helper function for DFS
    function<bool(int, int)> dfs = [&](int i, int j) {
        if (i == m - 1 && j == n - 1) return true; // Reached the bottom right
        visited[i][j] = true;

        if (i + 1 < m && !visited[i + 1][j] && cells[i + 1][j] > day) {
            if (dfs(i + 1, j)) return true;
        }
        if (j + 1 < n && !visited[i][j + 1] && cells[i][j + 1] > day) {
            if (dfs(i, j + 1)) return true;
        }
        return false;
    };

    return dfs(0, 0);
}

int latestDayToCross(vector<vector<int>>& cells) {
    int low = 1;
    int high = 2e5; // Maximum possible value for the cells

    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (canCross(cells, mid)) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    return high;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n \cdot \log{D})$ where $m$ and $n$ are the dimensions of the grid and $D$ is the maximum possible day. This is because in the worst case, we perform a depth-first search for each cell in the grid for each possible day, and we do this $\log{D}$ times due to the binary search.
> - **Space Complexity:** $O(m \cdot n)$ for the visited array used in the DFS.
> - **Why these complexities occur:** The brute force approach involves a lot of repeated work, especially in the DFS, which is why the time complexity is so high.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of checking every path for each day, we can use binary search to find the last day on which we can cross. This involves checking if we can cross on a given day and adjusting our search range accordingly.
- Detailed breakdown of the approach:
  1. Define a helper function `canCross` that checks if we can cross from the top left to the bottom right on a given day using DFS.
  2. Use binary search to find the last day on which we can cross. If we can cross on the current day, move the search range to the right half; otherwise, move it to the left half.
- Proof of optimality: This approach is optimal because it minimizes the number of times we need to check for a path, reducing the time complexity significantly compared to the brute force approach.

```cpp
// The code for the optimal approach is already provided in the brute force section,
// as the optimal approach is essentially an optimization of the brute force method
// through the use of binary search to find the last day on which we can cross.
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n \cdot \log{D})$ where $m$ and $n$ are the dimensions of the grid and $D$ is the maximum possible day. This is because we perform a DFS for each cell in the grid for each possible day, and we do this $\log{D}$ times due to the binary search.
> - **Space Complexity:** $O(m \cdot n)$ for the visited array used in the DFS.
> - **Optimality proof:** This approach is optimal because it reduces the number of times we need to perform the DFS, which is the most expensive operation in terms of time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Binary search, DFS.
- Problem-solving patterns identified: Using binary search to find the last occurrence of a certain condition.
- Optimization techniques learned: Reducing the search space by using binary search.
- Similar problems to practice: Other problems that involve finding the last occurrence of a certain condition, such as the last day on which a certain event can occur.

**Mistakes to Avoid:**
- Common implementation errors: Not properly handling the base cases for the DFS, not correctly updating the search range in the binary search.
- Edge cases to watch for: The grid being empty, the maximum possible day being very large.
- Performance pitfalls: Using a brute force approach without any optimization, not using memoization or dynamic programming when applicable.
- Testing considerations: Testing the function with different inputs, including edge cases, to ensure it works correctly.