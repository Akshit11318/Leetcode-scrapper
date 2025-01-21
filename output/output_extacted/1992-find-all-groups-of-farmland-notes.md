## Find All Groups of Farmland

**Problem Link:** https://leetcode.com/problems/find-all-groups-of-farmland/description

**Problem Statement:**
- Input: A 2D array `land` representing a map of farmland, where `1` denotes a plot of farmland and `0` denotes an empty plot.
- Expected Output: A list of coordinates of all groups of farmland, where each group is represented by the coordinates of its top-left and bottom-right plots.
- Key Requirements:
  - A group of farmland is defined as a set of adjacent plots (horizontally or vertically) with a value of `1`.
  - The coordinates of each group should be represented as `[x1, y1, x2, y2]`, where `(x1, y1)` is the top-left plot and `(x2, y2)` is the bottom-right plot.
- Example Test Cases:
  - Input: `[[1,0,0],[0,1,1],[0,1,1]]`
  - Output: `[[0,0,0,0],[1,1,2,2]]`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through the entire `land` array to find each plot of farmland and then expand to find the boundaries of each group.
- Step-by-step breakdown:
  1. Iterate through each plot in the `land` array.
  2. If a plot is a part of farmland (`1`), perform a depth-first search (DFS) to find the boundaries of the current group.
  3. During the DFS, mark visited plots to avoid revisiting them.
  4. Once the boundaries of a group are found, add its coordinates to the result list.
- Why this approach comes to mind first: It's a straightforward, intuitive method to find all groups of farmland by checking each plot individually.

```cpp
#include <vector>
#include <stack>

using namespace std;

void dfs(vector<vector<int>>& land, int x, int y, int& minX, int& minY, int& maxX, int& maxY) {
    if (x < 0 || x >= land.size() || y < 0 || y >= land[0].size() || land[x][y] == 0) return;
    land[x][y] = 0; // Mark as visited
    minX = min(minX, x);
    minY = min(minY, y);
    maxX = max(maxX, x);
    maxY = max(maxY, y);
    dfs(land, x-1, y, minX, minY, maxX, maxY);
    dfs(land, x+1, y, minX, minY, maxX, maxY);
    dfs(land, x, y-1, minX, minY, maxX, maxY);
    dfs(land, x, y+1, minX, minY, maxX, maxY);
}

vector<vector<int>> findFarmland(vector<vector<int>>& land) {
    vector<vector<int>> result;
    for (int i = 0; i < land.size(); i++) {
        for (int j = 0; j < land[0].size(); j++) {
            if (land[i][j] == 1) {
                int minX = i, minY = j, maxX = i, maxY = j;
                dfs(land, i, j, minX, minY, maxX, maxY);
                result.push_back({minX, minY, maxX, maxY});
            }
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(R \cdot C \cdot (R + C))$, where $R$ is the number of rows and $C$ is the number of columns in the `land` array. This is because in the worst case, we might need to perform DFS from each plot.
> - **Space Complexity:** $O(R \cdot C)$ for the recursion stack in the worst case.
> - **Why these complexities occur:** The brute force approach involves checking each plot and potentially performing DFS from each one, leading to the stated time and space complexities.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of performing DFS from each plot, we can iterate through the `land` array and whenever we find a plot of farmland, we check if it's the top-left plot of a group. If it is, we perform DFS to find the boundaries of the group.
- Detailed breakdown:
  1. Iterate through each plot in the `land` array.
  2. If a plot is a part of farmland and it's the top-left plot of a group (i.e., the plot above and to the left are both `0` or out of bounds), perform DFS to find the boundaries of the group.
  3. During the DFS, mark visited plots to avoid revisiting them.
  4. Once the boundaries of a group are found, add its coordinates to the result list.
- Why further optimization is impossible: This approach already minimizes the number of DFS operations by only performing them from the top-left plot of each group.

```cpp
void dfs(vector<vector<int>>& land, int x, int y, int& minX, int& minY, int& maxX, int& maxY) {
    if (x < 0 || x >= land.size() || y < 0 || y >= land[0].size() || land[x][y] == 0) return;
    land[x][y] = 0; // Mark as visited
    minX = min(minX, x);
    minY = min(minY, y);
    maxX = max(maxX, x);
    maxY = max(maxY, y);
    dfs(land, x-1, y, minX, minY, maxX, maxY);
    dfs(land, x+1, y, minX, minY, maxX, maxY);
    dfs(land, x, y-1, minX, minY, maxX, maxY);
    dfs(land, x, y+1, minX, minY, maxX, maxY);
}

vector<vector<int>> findFarmland(vector<vector<int>>& land) {
    vector<vector<int>> result;
    for (int i = 0; i < land.size(); i++) {
        for (int j = 0; j < land[0].size(); j++) {
            if (land[i][j] == 1 && (i == 0 || land[i-1][j] == 0) && (j == 0 || land[i][j-1] == 0)) {
                int minX = i, minY = j, maxX = i, maxY = j;
                dfs(land, i, j, minX, minY, maxX, maxY);
                result.push_back({minX, minY, maxX, maxY});
            }
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(R \cdot C)$, where $R$ is the number of rows and $C$ is the number of columns in the `land` array, because each plot is visited at most twice (once during the iteration and once during the DFS).
> - **Space Complexity:** $O(R \cdot C)$ for the recursion stack in the worst case.
> - **Optimality proof:** This approach is optimal because it minimizes the number of DFS operations by only performing them from the top-left plot of each group, resulting in a linear time complexity with respect to the size of the input array.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Depth-first search (DFS), iteration through a 2D array, and optimization by minimizing unnecessary operations.
- Problem-solving patterns identified: Checking for the top-left plot of a group to minimize DFS operations.
- Optimization techniques learned: Reducing the number of DFS operations by identifying and only processing the top-left plot of each group.

**Mistakes to Avoid:**
- Common implementation errors: Failing to mark visited plots during DFS, leading to infinite loops.
- Edge cases to watch for: Plots on the boundaries of the array, which require special handling during DFS.
- Performance pitfalls: Performing DFS from every plot, leading to inefficient time complexity.
- Testing considerations: Ensuring that the solution works correctly for arrays with no farmland, single plots of farmland, and multiple groups of farmland.