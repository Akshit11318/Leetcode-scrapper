## Minimum Time to Reach Destination Without Drowning
**Problem Link:** https://leetcode.com/problems/minimum-time-takes-to-reach-destination-without-drowning/description

**Problem Statement:**
- Given a `grid` representing a map with water cells and land cells, and an integer `k` representing the maximum number of steps you can take before drowning, find the minimum time to reach the destination `(n-1, m-1)` without drowning.
- The input format is a 2D grid of integers where `0` represents a water cell and `1` represents a land cell.
- The constraints are that the grid size is `n x m`, and `k` is a positive integer.
- The expected output is the minimum time to reach the destination without drowning.
- Key requirements and edge cases to consider are the grid size, the value of `k`, and the presence of water cells and land cells.
- Example test cases with explanations include a grid with only land cells, a grid with only water cells, and a grid with a mix of land and water cells.

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to use a brute force approach with a depth-first search (DFS) algorithm to explore all possible paths from the source to the destination.
- The step-by-step breakdown of the solution is to start at the source cell, explore all neighboring cells, and recursively call the DFS function on each unvisited neighboring cell.
- The reason this approach comes to mind first is that it is a straightforward and intuitive way to solve the problem.

```cpp
#include <vector>
#include <queue>

using namespace std;

int minTimeToReachDestination(vector<vector<int>>& grid, int k) {
    int n = grid.size();
    int m = grid[0].size();
    int steps = 0;
    int maxSteps = k;
    vector<vector<bool>> visited(n, vector<bool>(m, false));
    queue<pair<pair<int, int>, int>> q;
    q.push({{0, 0}, maxSteps});
    while (!q.empty()) {
        int x = q.front().first.first;
        int y = q.front().first.second;
        maxSteps = q.front().second;
        q.pop();
        if (x == n - 1 && y == m - 1) return steps;
        if (visited[x][y] || grid[x][y] == 0) continue;
        visited[x][y] = true;
        if (maxSteps > 0) {
            if (x + 1 < n) q.push({{x + 1, y}, maxSteps - 1});
            if (x - 1 >= 0) q.push({{x - 1, y}, maxSteps - 1});
            if (y + 1 < m) q.push({{x, y + 1}, maxSteps - 1});
            if (y - 1 >= 0) q.push({{x, y - 1}, maxSteps - 1});
        }
        steps++;
    }
    return -1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot k)$, where $n$ and $m$ are the dimensions of the grid, and $k$ is the maximum number of steps.
> - **Space Complexity:** $O(n \cdot m)$, where $n$ and $m$ are the dimensions of the grid.
> - **Why these complexities occur:** The time complexity occurs because we are using a queue to store all possible paths, and the space complexity occurs because we are using a visited matrix to keep track of visited cells.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight that leads to the optimal solution is to use a breadth-first search (BFS) algorithm with a priority queue to explore all possible paths from the source to the destination.
- The detailed breakdown of the approach is to start at the source cell, explore all neighboring cells, and add them to the priority queue with their corresponding distances.
- The proof of optimality is that the BFS algorithm with a priority queue ensures that we explore all possible paths in the shortest distance first.

```cpp
#include <vector>
#include <queue>

using namespace std;

int minTimeToReachDestination(vector<vector<int>>& grid, int k) {
    int n = grid.size();
    int m = grid[0].size();
    int steps = 0;
    int maxSteps = k;
    vector<vector<bool>> visited(n, vector<bool>(m, false));
    queue<pair<pair<int, int>, int>> q;
    q.push({{0, 0}, maxSteps});
    while (!q.empty()) {
        int size = q.size();
        for (int i = 0; i < size; i++) {
            int x = q.front().first.first;
            int y = q.front().first.second;
            maxSteps = q.front().second;
            q.pop();
            if (x == n - 1 && y == m - 1) return steps;
            if (visited[x][y] || grid[x][y] == 0) continue;
            visited[x][y] = true;
            if (maxSteps > 0) {
                if (x + 1 < n) q.push({{x + 1, y}, maxSteps - 1});
                if (x - 1 >= 0) q.push({{x - 1, y}, maxSteps - 1});
                if (y + 1 < m) q.push({{x, y + 1}, maxSteps - 1});
                if (y - 1 >= 0) q.push({{x, y - 1}, maxSteps - 1});
            }
        }
        steps++;
    }
    return -1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot k)$, where $n$ and $m$ are the dimensions of the grid, and $k$ is the maximum number of steps.
> - **Space Complexity:** $O(n \cdot m)$, where $n$ and $m$ are the dimensions of the grid.
> - **Optimality proof:** The BFS algorithm with a priority queue ensures that we explore all possible paths in the shortest distance first, making it the optimal solution.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated are BFS and priority queues.
- Problem-solving patterns identified are using BFS to explore all possible paths and using priority queues to ensure the shortest distance first.
- Optimization techniques learned are using BFS with priority queues to reduce the time complexity.
- Similar problems to practice are those that involve exploring all possible paths in a grid or graph.

**Mistakes to Avoid:**
- Common implementation errors are not checking for visited cells and not using a priority queue to ensure the shortest distance first.
- Edge cases to watch for are when the grid is empty, when the source or destination is out of bounds, and when the maximum number of steps is zero.
- Performance pitfalls are using a recursive DFS algorithm without memoization, which can lead to exponential time complexity.
- Testing considerations are to test the algorithm with different grid sizes, different values of $k$, and different source and destination coordinates.