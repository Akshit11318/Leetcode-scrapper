## Shortest Path in a Hidden Grid
**Problem Link:** https://leetcode.com/problems/shortest-path-in-a-hidden-grid/description

**Problem Statement:**
- Input format: A 2D grid represented by `m` and `n`, and a starting point `start`.
- Constraints: The grid is hidden and can only be revealed by visiting a cell.
- Expected output format: The length of the shortest path from `start` to the target if it exists, otherwise -1.
- Key requirements and edge cases to consider: Handling hidden cells, avoiding revisiting cells, and determining the shortest path in an unweighted grid.
- Example test cases with explanations:
    - For a grid with `m = 3`, `n = 3`, and `start = [1,1]`, the target cell is at `[2,2]`. The shortest path length would be 2 if we can move directly to the target without any obstacles.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Explore all possible paths from the start to the target.
- Step-by-step breakdown of the solution:
    1. Initialize a queue with the starting point.
    2. Perform BFS, exploring all possible directions (up, down, left, right) from each cell.
    3. Keep track of visited cells to avoid revisiting them.
    4. If the target cell is reached, return the path length.
- Why this approach comes to mind first: It's a straightforward method to explore all possible paths in an unweighted grid.

```cpp
#include <queue>
#include <vector>
using namespace std;

int shortestPath(vector<vector<int>>& grid, vector<int>& start) {
    int m = grid.size();
    int n = grid[0].size();
    vector<vector<bool>> visited(m, vector<bool>(n, false));
    queue<pair<vector<int>, int>> q; // cell coordinates and path length
    q.push({start, 0});
    visited[start[0]][start[1]] = true;
    
    while (!q.empty()) {
        auto [cell, length] = q.front();
        q.pop();
        
        if (cell[0] == grid.size() - 1 && cell[1] == grid[0].size() - 1) {
            return length;
        }
        
        vector<vector<int>> directions = {{-1,0}, {1,0}, {0,-1}, {0,1}};
        for (auto& dir : directions) {
            int newRow = cell[0] + dir[0];
            int newCol = cell[1] + dir[1];
            
            if (newRow >= 0 && newRow < m && newCol >= 0 && newCol < n && !visited[newRow][newCol]) {
                q.push({{newRow, newCol}, length + 1});
                visited[newRow][newCol] = true;
            }
        }
    }
    
    return -1; // target not reachable
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ and $n$ are the dimensions of the grid, because in the worst case, we visit every cell.
> - **Space Complexity:** $O(m \cdot n)$ for the queue and visited matrix.
> - **Why these complexities occur:** The brute force approach explores all possible paths, resulting in a time complexity proportional to the grid size and space complexity for storing visited cells and the queue.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Utilize a more efficient data structure or algorithm that takes advantage of the grid's structure.
- Detailed breakdown of the approach: Since the grid is unweighted, BFS is the optimal algorithm. However, we can optimize the brute force approach by using a more efficient data structure for visited cells, such as a `set`, and by only exploring reachable cells.
- Proof of optimality: BFS is guaranteed to find the shortest path in an unweighted graph or grid, and using a `set` for visited cells reduces the lookup time to constant, making the overall time complexity optimal.
- Why further optimization is impossible: The grid's hidden nature means we must explore all reachable cells, and BFS with a `set` for visited cells achieves this with the minimum number of operations.

```cpp
#include <queue>
#include <vector>
#include <unordered_set>
using namespace std;

int shortestPath(vector<vector<int>>& grid, vector<int>& start) {
    int m = grid.size();
    int n = grid[0].size();
    unordered_set<string> visited;
    queue<pair<vector<int>, int>> q; // cell coordinates and path length
    q.push({start, 0});
    visited.insert(to_string(start[0]) + "," + to_string(start[1]));
    
    while (!q.empty()) {
        auto [cell, length] = q.front();
        q.pop();
        
        if (cell[0] == grid.size() - 1 && cell[1] == grid[0].size() - 1) {
            return length;
        }
        
        vector<vector<int>> directions = {{-1,0}, {1,0}, {0,-1}, {0,1}};
        for (auto& dir : directions) {
            int newRow = cell[0] + dir[0];
            int newCol = cell[1] + dir[1];
            
            if (newRow >= 0 && newRow < m && newCol >= 0 && newCol < n) {
                string newCell = to_string(newRow) + "," + to_string(newCol);
                if (visited.find(newCell) == visited.end()) {
                    q.push({{newRow, newCol}, length + 1});
                    visited.insert(newCell);
                }
            }
        }
    }
    
    return -1; // target not reachable
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ and $n$ are the dimensions of the grid, because in the worst case, we visit every cell.
> - **Space Complexity:** $O(m \cdot n)$ for the queue and visited set.
> - **Optimality proof:** The use of BFS ensures the shortest path is found, and the `set` for visited cells reduces lookup time to constant, making the overall approach optimal.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: BFS, use of efficient data structures for visited cells.
- Problem-solving patterns identified: Utilizing the grid's structure to optimize the algorithm.
- Optimization techniques learned: Using a `set` for visited cells to reduce lookup time.
- Similar problems to practice: Other pathfinding problems in grids or graphs, such as finding the shortest path in a weighted graph.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly handling edge cases, such as cells outside the grid boundaries.
- Edge cases to watch for: Grids with no path to the target, grids with obstacles.
- Performance pitfalls: Using inefficient data structures or algorithms, such as DFS for finding the shortest path in an unweighted grid.
- Testing considerations: Thoroughly testing the algorithm with different grid sizes, start and target positions, and edge cases.