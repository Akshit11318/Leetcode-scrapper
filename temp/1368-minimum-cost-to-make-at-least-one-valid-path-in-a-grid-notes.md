## Minimum Cost to Make at Least One Valid Path in a Grid

**Problem Link:** [leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/description](https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/description)

**Problem Statement (in your own words):**

Given a grid where each cell represents a cost to move in a specific direction (up, down, left, right), find the minimum cost to make at least one valid path from the top-left cell to the bottom-right cell. A valid path is one where the total cost is minimized.

---

### Brute Force Approach

**Explanation:**

The brute force approach would involve trying all possible paths from the top-left cell to the bottom-right cell, calculating the total cost for each path, and keeping track of the minimum cost found. This can be achieved using a recursive depth-first search (DFS) algorithm.

```cpp
#include <vector>
#include <climits>

using namespace std;

int minCost(vector<vector<int>>& grid) {
    int rows = grid.size();
    int cols = grid[0].size();
    int minCost = INT_MAX;

    vector<vector<int>> directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

    function<void(int, int, int)> dfs = [&](int x, int y, int cost) {
        if (x == rows - 1 && y == cols - 1) {
            minCost = min(minCost, cost);
            return;
        }

        for (auto& direction : directions) {
            int newX = x + direction[0];
            int newY = y + direction[1];

            if (newX >= 0 && newX < rows && newY >= 0 && newY < cols) {
                dfs(newX, newY, cost + grid[newX][newY]);
            }
        }
    };

    dfs(0, 0, grid[0][0]);
    return minCost;
}
```

> Complexity Analysis:
> 
> **Time Complexity:** O(4^(rows * cols)) because in the worst case, we might have to explore all possible paths, and each path can have up to 4 directions to move.
> 
> **Space Complexity:** O(rows * cols) due to the recursive call stack.

---

### Optimal Approach

**Explanation:**

A more efficient approach is to use dynamic programming to build up a solution. We can maintain a 2D array `dp` where `dp[i][j]` represents the minimum cost to reach cell `(i, j)` from the top-left cell. We can fill up this array by iterating through the grid and at each cell, considering the minimum cost to reach the cell above, below, to the left, and to the right, and adding the cost of the current cell.

```cpp
#include <vector>
#include <climits>

using namespace std;

int minCost(vector<vector<int>>& grid) {
    int rows = grid.size();
    int cols = grid[0].size();
    vector<vector<int>> dp(rows, vector<int>(cols, INT_MAX));

    dp[0][0] = grid[0][0];

    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            if (i > 0) {
                dp[i][j] = min(dp[i][j], dp[i - 1][j] + grid[i][j]);
            }
            if (j > 0) {
                dp[i][j] = min(dp[i][j], dp[i][j - 1] + grid[i][j]);
            }
        }
    }

    return dp[rows - 1][cols - 1];
}
```

> Complexity Analysis:
> 
> - **Time Complexity:** O(rows * cols) because we make a single pass through the grid.
> - **Space Complexity:** O(rows * cols) for the `dp` array.

---

### Alternative/Greedy Approach (if applicable)

**Explanation:**

Another approach is to use Dijkstra's algorithm to find the shortest path in the grid. This involves maintaining a priority queue of cells to visit, where the priority of each cell is its minimum cost to reach from the top-left cell.

```cpp
#include <vector>
#include <queue>
#include <climits>

using namespace std;

struct Cell {
    int x, y, cost;
};

struct Compare {
    bool operator()(const Cell& a, const Cell& b) {
        return a.cost > b.cost;
    }
};

int minCost(vector<vector<int>>& grid) {
    int rows = grid.size();
    int cols = grid[0].size();
    vector<vector<int>> distances(rows, vector<int>(cols, INT_MAX));
    distances[0][0] = grid[0][0];

    priority_queue<Cell, vector<Cell>, Compare> pq;
    pq.push({0, 0, grid[0][0]});

    vector<vector<int>> directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

    while (!pq.empty()) {
        Cell current = pq.top();
        pq.pop();

        for (auto& direction : directions) {
            int newX = current.x + direction[0];
            int newY = current.y + direction[1];

            if (newX >= 0 && newX < rows && newY >= 0 && newY < cols) {
                int newCost = current.cost + grid[newX][newY];

                if (newCost < distances[newX][newY]) {
                    distances[newX][newY] = newCost;
                    pq.push({newX, newY, newCost});
                }
            }
        }
    }

    return distances[rows - 1][cols - 1];
}
```

> Complexity Analysis:
> 
> - **Time Complexity:** O(rows * cols * log(rows * cols)) due to the priority queue operations.
> - **Space Complexity:** O(rows * cols) for the `distances` array and the priority queue.

---

### Final Notes

**Learning Points:**

1. **Dynamic Programming:** The optimal solution uses dynamic programming to build up a solution by maintaining a 2D array `dp` where `dp[i][j]` represents the minimum cost to reach cell `(i, j)`.
2. **Dijkstra's Algorithm:** The alternative solution uses Dijkstra's algorithm to find the shortest path in the grid, which involves maintaining a priority queue of cells to visit.
3. **Efficient Data Structures:** The use of efficient data structures such as priority queues and 2D arrays can significantly improve the performance of the solution.

**Mistakes to Avoid:**

1. **Incorrect Initialization:** Failing to initialize the `dp` array or the `distances` array correctly can lead to incorrect results.
2. **Insufficient Exploration:** Failing to explore all possible directions (up, down, left, right) can lead to missing the optimal solution.
3. **Inefficient Algorithms:** Using inefficient algorithms such as brute force or recursive DFS can lead to exponential time complexity and poor performance.