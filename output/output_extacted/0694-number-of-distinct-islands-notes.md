## Number of Distinct Islands

**Problem Link:** https://leetcode.com/problems/number-of-distinct-islands/description

**Problem Statement:**
- Given a non-empty 2D array `grid` which consists of only 1s (land) and 0s (water), find the number of distinct islands.
- An island is a group of connected 1s (horizontally or vertically).
- Two islands are considered the same if one island can be translated (not rotated or reflected) to match the other.
- Input format: `grid` is a 2D array of integers where `grid[i][j]` is either 0 or 1.
- Constraints: The number of rows and columns in the grid is in the range `[1, 50]`.
- Expected output format: The number of distinct islands.
- Key requirements and edge cases to consider: Islands must be distinct when translated but not when rotated or reflected. For example, an island that looks like a "1" shape and one that looks like a "7" are considered distinct because one cannot be translated into the other.

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves finding all islands, then checking each pair of islands to see if they are the same by trying all possible translations.
- Step-by-step breakdown of the solution:
  1. Find all islands in the grid by using a depth-first search (DFS) or breadth-first search (BFS) to identify connected components of 1s.
  2. For each pair of islands, compare them by translating one island over the other in all possible ways and checking if they match.
- Why this approach comes to mind first: It's a straightforward way to ensure that all islands are found and compared, but it's inefficient because it involves many unnecessary comparisons and translations.

```cpp
#include <vector>
#include <unordered_set>
using namespace std;

void dfs(vector<vector<int>>& grid, int i, int j, vector<pair<int, int>>& island) {
    if (i < 0 || j < 0 || i >= grid.size() || j >= grid[0].size() || grid[i][j] == 0) {
        return;
    }
    grid[i][j] = 0; // Mark as visited
    island.push_back({i, j});
    dfs(grid, i-1, j, island);
    dfs(grid, i+1, j, island);
    dfs(grid, i, j-1, island);
    dfs(grid, i, j+1, island);
}

string normalizeIsland(vector<pair<int, int>>& island) {
    int minX = INT_MAX, minY = INT_MAX;
    for (auto& point : island) {
        minX = min(minX, point.first);
        minY = min(minY, point.second);
    }
    string normalized;
    for (auto& point : island) {
        normalized += to_string(point.first - minX) + "," + to_string(point.second - minY) + ";";
    }
    return normalized;
}

int numDistinctIslands(vector<vector<int>>& grid) {
    unordered_set<string> distinctIslands;
    for (int i = 0; i < grid.size(); i++) {
        for (int j = 0; j < grid[0].size(); j++) {
            if (grid[i][j] == 1) {
                vector<pair<int, int>> island;
                dfs(grid, i, j, island);
                string normalized = normalizeIsland(island);
                distinctIslands.insert(normalized);
            }
        }
    }
    return distinctIslands.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(R \cdot C \cdot R \cdot C)$ where $R$ is the number of rows and $C$ is the number of columns in the grid. This is because in the worst case, we might have to explore every cell for every island.
> - **Space Complexity:** $O(R \cdot C)$ for storing the visited cells and the current island.
> - **Why these complexities occur:** The brute force approach involves exploring the grid for islands and then comparing these islands, which leads to a high time complexity. The space complexity is due to the need to store the current island and the visited cells.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of comparing all pairs of islands, we can normalize each island by translating it to a standard position (e.g., its top-left corner is at (0,0)) and then use a hash set to store unique islands.
- Detailed breakdown of the approach:
  1. Find all islands using DFS or BFS.
  2. For each island, normalize it by translating it so its top-leftmost point is at (0,0).
  3. Store the normalized islands in a set to automatically eliminate duplicates.
- Proof of optimality: This approach ensures we only need to explore the grid once to find all islands and normalize them, making it more efficient than the brute force approach.

```cpp
#include <vector>
#include <unordered_set>
using namespace std;

void dfs(vector<vector<int>>& grid, int i, int j, vector<pair<int, int>>& island) {
    if (i < 0 || j < 0 || i >= grid.size() || j >= grid[0].size() || grid[i][j] == 0) {
        return;
    }
    grid[i][j] = 0; // Mark as visited
    island.push_back({i, j});
    dfs(grid, i-1, j, island);
    dfs(grid, i+1, j, island);
    dfs(grid, i, j-1, island);
    dfs(grid, i, j+1, island);
}

string normalizeIsland(vector<pair<int, int>>& island) {
    int minX = INT_MAX, minY = INT_MAX;
    for (auto& point : island) {
        minX = min(minX, point.first);
        minY = min(minY, point.second);
    }
    string normalized;
    for (auto& point : island) {
        normalized += to_string(point.first - minX) + "," + to_string(point.second - minY) + ";";
    }
    return normalized;
}

int numDistinctIslands(vector<vector<int>>& grid) {
    unordered_set<string> distinctIslands;
    for (int i = 0; i < grid.size(); i++) {
        for (int j = 0; j < grid[0].size(); j++) {
            if (grid[i][j] == 1) {
                vector<pair<int, int>> island;
                dfs(grid, i, j, island);
                string normalized = normalizeIsland(island);
                distinctIslands.insert(normalized);
            }
        }
    }
    return distinctIslands.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(R \cdot C)$ where $R$ is the number of rows and $C$ is the number of columns in the grid. This is because we visit each cell once.
> - **Space Complexity:** $O(R \cdot C)$ for storing the visited cells and the current island.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the grid to find and normalize all islands, eliminating the need for redundant comparisons.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Depth-First Search (DFS), normalization of geometric shapes, and use of hash sets for efficient storage and lookup of unique elements.
- Problem-solving patterns identified: The importance of normalization in comparing geometric shapes and the efficiency of using hash sets for storing unique elements.
- Optimization techniques learned: Reducing time complexity by avoiding redundant comparisons and using a single pass through the data.

**Mistakes to Avoid:**
- Common implementation errors: Failing to mark visited cells during DFS, not correctly normalizing islands, and not using a hash set to store unique islands.
- Edge cases to watch for: Empty grid, grid with no islands, and grid with a single island.
- Performance pitfalls: Using a brute force approach that compares all pairs of islands, leading to a high time complexity.