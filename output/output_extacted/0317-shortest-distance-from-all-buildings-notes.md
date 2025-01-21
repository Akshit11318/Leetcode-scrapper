## Shortest Distance from All Buildings

**Problem Link:** https://leetcode.com/problems/shortest-distance-from-all-buildings/description

**Problem Statement:**
- Input: A 2D grid where `0` represents an empty land, `1` represents a building, and `2` represents an obstacle.
- Expected Output: The minimum sum of distances from all buildings to a given empty land.
- Key Requirements: Calculate the shortest distance from all buildings to each empty land and return the minimum sum of distances.
- Edge Cases: Handle cases where there are no buildings, no empty lands, or no accessible empty lands.

**Example Test Cases:**

- Input: 
```cpp
[
  [1,0,2,0,1],
  [0,0,0,0,0],
  [0,0,1,0,0]
]
```
- Expected Output: `7`
- Explanation: The minimum sum of distances is achieved at the position `(1, 3)` or `(2, 2)`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to calculate the shortest distance from each building to every empty land using a breadth-first search (BFS) algorithm.
- For each building, perform BFS to find the shortest distance to all accessible empty lands.
- Calculate the sum of distances from all buildings to each empty land and return the minimum sum.

```cpp
#include <vector>
#include <queue>
#include <limits>

using namespace std;

int shortestDistance(vector<vector<int>>& grid) {
    int m = grid.size();
    int n = grid[0].size();
    vector<vector<int>> directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    vector<vector<int>> distance(m, vector<int>(n, 0));
    vector<vector<bool>> visited(m, vector<bool>(n, false));
    
    // Find all buildings
    vector<pair<int, int>> buildings;
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (grid[i][j] == 1) {
                buildings.push_back({i, j});
            }
        }
    }
    
    // For each building, perform BFS to find the shortest distance to all accessible empty lands
    for (auto& building : buildings) {
        queue<pair<int, int>> q;
        q.push(building);
        visited[building.first][building.second] = true;
        int dist = 1;
        
        while (!q.empty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                auto current = q.front();
                q.pop();
                
                for (auto& dir : directions) {
                    int x = current.first + dir[0];
                    int y = current.second + dir[1];
                    
                    if (x >= 0 && x < m && y >= 0 && y < n && !visited[x][y] && grid[x][y] != 2) {
                        if (grid[x][y] == 0) {
                            distance[x][y] += dist;
                        }
                        q.push({x, y});
                        visited[x][y] = true;
                    }
                }
            }
            dist++;
        }
        
        // Reset visited matrix for the next building
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                visited[i][j] = false;
            }
        }
    }
    
    // Find the minimum sum of distances
    int minSum = numeric_limits<int>::max();
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (grid[i][j] == 0 && distance[i][j] != 0) {
                minSum = min(minSum, distance[i][j]);
            }
        }
    }
    
    return minSum == numeric_limits<int>::max() ? -1 : minSum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n \cdot b \cdot (m + n))$, where $m$ and $n$ are the dimensions of the grid, and $b$ is the number of buildings. This is because we perform BFS from each building, which takes $O(m + n)$ time, and we do this for all buildings.
> - **Space Complexity:** $O(m \cdot n)$, as we need to store the `distance` and `visited` matrices.
> - **Why these complexities occur:** The time complexity is high due to the repeated BFS operations from each building, and the space complexity is due to the need to store the `distance` and `visited` matrices.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to perform BFS from each empty land instead of from each building. This reduces the number of BFS operations from $b$ to $e$, where $e$ is the number of empty lands.
- For each empty land, perform BFS to find the shortest distance to all accessible buildings.
- Calculate the sum of distances from all buildings to the current empty land and update the minimum sum.

```cpp
int shortestDistance(vector<vector<int>>& grid) {
    int m = grid.size();
    int n = grid[0].size();
    vector<vector<int>> directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    vector<vector<int>> distance(m, vector<int>(n, 0));
    vector<vector<bool>> visited(m, vector<bool>(n, false));
    
    // Find all buildings
    vector<pair<int, int>> buildings;
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (grid[i][j] == 1) {
                buildings.push_back({i, j});
            }
        }
    }
    
    int minSum = numeric_limits<int>::max();
    
    // For each empty land, perform BFS to find the shortest distance to all accessible buildings
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (grid[i][j] == 0) {
                queue<pair<int, int>> q;
                q.push({i, j});
                visited[i][j] = true;
                int dist = 0;
                int sum = 0;
                int count = 0;
                
                while (!q.empty()) {
                    int size = q.size();
                    for (int k = 0; k < size; k++) {
                        auto current = q.front();
                        q.pop();
                        
                        for (auto& dir : directions) {
                            int x = current.first + dir[0];
                            int y = current.second + dir[1];
                            
                            if (x >= 0 && x < m && y >= 0 && y < n && !visited[x][y] && grid[x][y] != 2) {
                                if (grid[x][y] == 1) {
                                    sum += dist + 1;
                                    count++;
                                }
                                q.push({x, y});
                                visited[x][y] = true;
                            }
                        }
                    }
                    dist++;
                }
                
                // Reset visited matrix for the next empty land
                for (int x = 0; x < m; x++) {
                    for (int y = 0; y < n; y++) {
                        visited[x][y] = false;
                    }
                }
                
                // Update the minimum sum
                if (count == buildings.size()) {
                    minSum = min(minSum, sum);
                }
            }
        }
    }
    
    return minSum == numeric_limits<int>::max() ? -1 : minSum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n \cdot (m + n))$, where $m$ and $n$ are the dimensions of the grid. This is because we perform BFS from each empty land, which takes $O(m + n)$ time, and we do this for all empty lands.
> - **Space Complexity:** $O(m \cdot n)$, as we need to store the `distance` and `visited` matrices.
> - **Optimality proof:** This solution is optimal because we only perform BFS from each empty land, which reduces the number of BFS operations from $b$ to $e$, where $e$ is the number of empty lands. This results in a significant reduction in time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: BFS, distance calculation, and optimization techniques.
- Problem-solving patterns identified: reducing the number of BFS operations by changing the starting point.
- Optimization techniques learned: using BFS from each empty land instead of from each building.
- Similar problems to practice: finding the shortest distance from all buildings to a given point, finding the minimum sum of distances from all points to a given set of points.

**Mistakes to Avoid:**
- Common implementation errors: not resetting the visited matrix after each BFS operation, not checking for out-of-bounds conditions.
- Edge cases to watch for: handling cases where there are no buildings, no empty lands, or no accessible empty lands.
- Performance pitfalls: using a brute-force approach that results in high time complexity.
- Testing considerations: testing the solution with different grid sizes, building and empty land configurations, and obstacle placements.