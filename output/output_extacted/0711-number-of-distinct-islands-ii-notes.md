## Number of Distinct Islands II

**Problem Link:** https://leetcode.com/problems/number-of-distinct-islands-ii/description

**Problem Statement:**
- Input format: A 2D grid `grid` of size `m x n`, where `grid[i][j]` can be either `0` (water) or `1` (land).
- Constraints: `m == grid.length`, `n == grid[0].length`, `1 <= m, n <= 50`, and `grid[i][j]` is either `0` or `1`.
- Expected output format: The number of distinct islands, where an island is considered distinct if it has a unique shape.
- Key requirements and edge cases to consider: Islands can be rotated and reflected, and the grid can contain multiple islands.

**Example Test Cases:**
- Example 1: `grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]`, output: `1`
- Example 2: `grid = [[1,1,0,0,0],[0,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]`, output: `2`

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to iterate over each cell in the grid and perform a depth-first search (DFS) to find all connected land cells.
- For each island found, we can then normalize its shape by translating it to the origin, rotating it, and reflecting it to find its unique representation.
- We can use a set to store the unique representations of islands.

```cpp
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

vector<vector<int>> normalize(vector<vector<int>>& island) {
    // Translate to origin
    int minX = island[0][0], minY = island[0][1];
    for (auto& point : island) {
        minX = min(minX, point[0]);
        minY = min(minY, point[1]);
    }
    for (auto& point : island) {
        point[0] -= minX;
        point[1] -= minY;
    }

    // Rotate and reflect
    vector<vector<int>> rotations[4];
    for (int i = 0; i < 4; i++) {
        rotations[i] = island;
        for (auto& point : rotations[i]) {
            swap(point[0], point[1]);
            point[1] = -point[1];
        }
    }
    vector<vector<int>> reflections[4];
    for (int i = 0; i < 4; i++) {
        reflections[i] = rotations[i];
        for (auto& point : reflections[i]) {
            point[0] = -point[0];
        }
    }

    // Find the smallest representation
    vector<vector<int>> smallest = rotations[0];
    for (int i = 0; i < 4; i++) {
        if (rotations[i] < smallest) smallest = rotations[i];
        if (reflections[i] < smallest) smallest = reflections[i];
    }
    return smallest;
}

int numDistinctIslands(vector<vector<int>>& grid) {
    set<vector<vector<int>>> uniqueIslands;
    for (int i = 0; i < grid.size(); i++) {
        for (int j = 0; j < grid[0].size(); j++) {
            if (grid[i][j] == 1) {
                vector<vector<int>> island;
                vector<vector<int>> stack = {{i, j}};
                while (!stack.empty()) {
                    vector<int> point = stack.back();
                    stack.pop_back();
                    if (grid[point[0]][point[1]] == 1) {
                        grid[point[0]][point[1]] = 0;
                        island.push_back({point[0] - i, point[1] - j});
                        if (point[0] > 0 && grid[point[0] - 1][point[1]] == 1) stack.push_back({point[0] - 1, point[1]});
                        if (point[0] < grid.size() - 1 && grid[point[0] + 1][point[1]] == 1) stack.push_back({point[0] + 1, point[1]});
                        if (point[1] > 0 && grid[point[0]][point[1] - 1] == 1) stack.push_back({point[0], point[1] - 1});
                        if (point[1] < grid[0].size() - 1 && grid[point[0]][point[1] + 1] == 1) stack.push_back({point[0], point[1] + 1});
                    }
                }
                if (!island.empty()) {
                    vector<vector<int>> normalized = normalize(island);
                    uniqueIslands.insert(normalized);
                }
            }
        }
    }
    return uniqueIslands.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n \cdot k^2)$, where $m$ and $n$ are the dimensions of the grid, and $k$ is the maximum size of an island. This is because for each cell in the grid, we perform a DFS to find all connected land cells, and then normalize the island by rotating and reflecting it.
> - **Space Complexity:** $O(m \cdot n + k^2)$, where $m$ and $n$ are the dimensions of the grid, and $k$ is the maximum size of an island. This is because we need to store the grid and the set of unique islands.
> - **Why these complexities occur:** The time complexity occurs because we need to iterate over all cells in the grid and perform a DFS to find all connected land cells. The space complexity occurs because we need to store the grid and the set of unique islands.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a more efficient algorithm to normalize the islands.
- Instead of rotating and reflecting each island, we can use a more efficient algorithm to find the smallest representation of the island.
- We can use a set to store the unique representations of islands.

```cpp
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

vector<pair<int, int>> normalize(vector<pair<int, int>>& island) {
    // Translate to origin
    int minX = island[0].first, minY = island[0].second;
    for (auto& point : island) {
        minX = min(minX, point.first);
        minY = min(minY, point.second);
    }
    for (auto& point : island) {
        point.first -= minX;
        point.second -= minY;
    }

    // Find the smallest representation
    vector<pair<int, int>> smallest = island;
    for (int i = 0; i < 4; i++) {
        vector<pair<int, int>> rotation = island;
        for (auto& point : rotation) {
            swap(point.first, point.second);
            point.second = -point.second;
        }
        if (rotation < smallest) smallest = rotation;
        vector<pair<int, int>> reflection = rotation;
        for (auto& point : reflection) {
            point.first = -point.first;
        }
        if (reflection < smallest) smallest = reflection;
    }
    return smallest;
}

int numDistinctIslands(vector<vector<int>>& grid) {
    set<vector<pair<int, int>>> uniqueIslands;
    for (int i = 0; i < grid.size(); i++) {
        for (int j = 0; j < grid[0].size(); j++) {
            if (grid[i][j] == 1) {
                vector<pair<int, int>> island;
                vector<pair<int, int>> stack = {{i, j}};
                while (!stack.empty()) {
                    pair<int, int> point = stack.back();
                    stack.pop_back();
                    if (grid[point.first][point.second] == 1) {
                        grid[point.first][point.second] = 0;
                        island.push_back({point.first - i, point.second - j});
                        if (point.first > 0 && grid[point.first - 1][point.second] == 1) stack.push_back({point.first - 1, point.second});
                        if (point.first < grid.size() - 1 && grid[point.first + 1][point.second] == 1) stack.push_back({point.first + 1, point.second});
                        if (point.second > 0 && grid[point.first][point.second - 1] == 1) stack.push_back({point.first, point.second - 1});
                        if (point.second < grid[0].size() - 1 && grid[point.first][point.second + 1] == 1) stack.push_back({point.first, point.second + 1});
                    }
                }
                if (!island.empty()) {
                    vector<pair<int, int>> normalized = normalize(island);
                    uniqueIslands.insert(normalized);
                }
            }
        }
    }
    return uniqueIslands.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n \cdot k)$, where $m$ and $n$ are the dimensions of the grid, and $k$ is the maximum size of an island. This is because for each cell in the grid, we perform a DFS to find all connected land cells, and then normalize the island.
> - **Space Complexity:** $O(m \cdot n + k)$, where $m$ and $n$ are the dimensions of the grid, and $k$ is the maximum size of an island. This is because we need to store the grid and the set of unique islands.
> - **Optimality proof:** The time complexity is optimal because we need to iterate over all cells in the grid and perform a DFS to find all connected land cells. The space complexity is optimal because we need to store the grid and the set of unique islands.

---

### Final Notes

**Learning Points:**
- The key algorithmic concept demonstrated is the use of a set to store unique representations of islands.
- The problem-solving pattern identified is the use of a DFS to find all connected land cells.
- The optimization technique learned is the use of a more efficient algorithm to normalize the islands.

**Mistakes to Avoid:**
- A common implementation error is to not properly handle the case where an island is empty.
- An edge case to watch for is when the grid contains multiple islands with the same shape but different orientations.
- A performance pitfall is to not use a set to store unique representations of islands, which can lead to duplicate islands being counted.