## Contain Virus
**Problem Link:** [https://leetcode.com/problems/contain-virus/description](https://leetcode.com/problems/contain-virus/description)

**Problem Statement:**
- The input is a 2D grid of integers where each cell can have one of the following values: 0 (uninfected), 1 (infected but not contained), or 2 (infected and contained).
- The goal is to find the minimum number of operations required to contain the virus by building walls around infected cells.
- Each operation involves selecting a group of infected cells (connected by edges) and containing them by building walls around the group.
- The virus spreads to adjacent uninfected cells in each step.
- The task is to find the minimum number of operations to contain the virus.

**Example Test Cases:**
- Input: `grid = [[0,1,0,0,0,0,0,1],[0,1,0,0,0,0,0,1],[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0]]`
- Output: `10`
- Explanation: The virus spreads and we need to build walls around the infected cells to contain it.

---

### Brute Force Approach
**Explanation:**
- The initial thought process involves trying all possible combinations of infected cell groups and calculating the minimum number of operations required to contain the virus.
- This approach involves iterating over the grid, identifying connected components of infected cells, and calculating the perimeter of each component to determine the number of operations required to contain it.
- However, this approach is inefficient due to the high time complexity of iterating over all possible combinations and calculating the perimeter of each component.

```cpp
int containVirus(vector<vector<int>>& grid) {
    int m = grid.size();
    int n = grid[0].size();
    int res = 0;
    while (true) {
        vector<vector<int>> clusters;
        vector<vector<int>> fronts;
        vector<vector<int>> walls;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    vector<int> cluster;
                    vector<int> front;
                    vector<int> wall;
                    dfs(grid, i, j, cluster, front, wall);
                    clusters.push_back(cluster);
                    fronts.push_back(front);
                    walls.push_back(wall);
                }
            }
        }
        if (clusters.empty()) break;
        int idx = 0;
        for (int i = 1; i < clusters.size(); i++) {
            if (fronts[i].size() > fronts[idx].size()) idx = i;
        }
        res += walls[idx].size();
        for (int i = 0; i < clusters.size(); i++) {
            if (i == idx) {
                for (int x : clusters[i]) {
                    grid[x / n][x % n] = -1;
                }
            } else {
                for (int x : fronts[i]) {
                    grid[x / n][x % n] = 1;
                }
            }
        }
    }
    return res;
}

void dfs(vector<vector<int>>& grid, int i, int j, vector<int>& cluster, vector<int>& front, vector<int>& wall) {
    int m = grid.size();
    int n = grid[0].size();
    if (i < 0 || i >= m || j < 0 || j >= n || grid[i][j] == -1) return;
    if (grid[i][j] == 1) {
        cluster.push_back(i * n + j);
        grid[i][j] = -1;
        dfs(grid, i - 1, j, cluster, front, wall);
        dfs(grid, i + 1, j, cluster, front, wall);
        dfs(grid, i, j - 1, cluster, front, wall);
        dfs(grid, i, j + 1, cluster, front, wall);
    } else if (grid[i][j] == 0) {
        front.push_back(i * n + j);
        wall.push_back(i * n + j);
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n \cdot k)$, where $m$ and $n$ are the dimensions of the grid and $k$ is the number of infected cell groups.
> - **Space Complexity:** $O(m \cdot n)$, where $m$ and $n$ are the dimensions of the grid.
> - **Why these complexities occur:** The time complexity is high due to the iteration over all possible combinations of infected cell groups and the calculation of the perimeter of each component. The space complexity is due to the storage of the grid and the infected cell groups.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is to use a breadth-first search (BFS) to identify the connected components of infected cells and calculate the perimeter of each component.
- We can use a `queue` data structure to perform the BFS and a `set` data structure to store the infected cell groups.
- We can also use a `map` data structure to store the perimeter of each infected cell group.
- The optimal approach involves iterating over the grid, identifying connected components of infected cells using BFS, and calculating the perimeter of each component.

```cpp
int containVirus(vector<vector<int>>& grid) {
    int m = grid.size();
    int n = grid[0].size();
    int res = 0;
    while (true) {
        vector<vector<int>> clusters;
        vector<vector<int>> fronts;
        vector<vector<int>> walls;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    vector<int> cluster;
                    vector<int> front;
                    vector<int> wall;
                    bfs(grid, i, j, cluster, front, wall);
                    clusters.push_back(cluster);
                    fronts.push_back(front);
                    walls.push_back(wall);
                }
            }
        }
        if (clusters.empty()) break;
        int idx = 0;
        for (int i = 1; i < clusters.size(); i++) {
            if (fronts[i].size() > fronts[idx].size()) idx = i;
        }
        res += walls[idx].size();
        for (int i = 0; i < clusters.size(); i++) {
            if (i == idx) {
                for (int x : clusters[i]) {
                    grid[x / n][x % n] = -1;
                }
            } else {
                for (int x : fronts[i]) {
                    grid[x / n][x % n] = 1;
                }
            }
        }
    }
    return res;
}

void bfs(vector<vector<int>>& grid, int i, int j, vector<int>& cluster, vector<int>& front, vector<int>& wall) {
    int m = grid.size();
    int n = grid[0].size();
    queue<pair<int, int>> q;
    q.push({i, j});
    cluster.push_back(i * n + j);
    grid[i][j] = -1;
    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
        vector<pair<int, int>> dirs = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        for (auto dir : dirs) {
            int nx = x + dir.first;
            int ny = y + dir.second;
            if (nx < 0 || nx >= m || ny < 0 || ny >= n || grid[nx][ny] == -1) continue;
            if (grid[nx][ny] == 1) {
                cluster.push_back(nx * n + ny);
                q.push({nx, ny});
                grid[nx][ny] = -1;
            } else if (grid[nx][ny] == 0) {
                front.push_back(nx * n + ny);
                wall.push_back(nx * n + ny);
            }
        }
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ and $n$ are the dimensions of the grid.
> - **Space Complexity:** $O(m \cdot n)$, where $m$ and $n$ are the dimensions of the grid.
> - **Optimality proof:** The optimal approach is to use BFS to identify the connected components of infected cells and calculate the perimeter of each component. This approach has a time complexity of $O(m \cdot n)$, which is optimal because we need to iterate over the grid to identify the infected cell groups.

---

### Final Notes

**Learning Points:**
- The key algorithmic concept demonstrated is the use of BFS to identify connected components of infected cells.
- The problem-solving pattern identified is the use of a `queue` data structure to perform BFS and a `set` data structure to store the infected cell groups.
- The optimization technique learned is the use of a `map` data structure to store the perimeter of each infected cell group.

**Mistakes to Avoid:**
- A common implementation error is to use a recursive approach instead of an iterative approach using BFS.
- An edge case to watch for is when the grid is empty or contains only one cell.
- A performance pitfall is to use a brute force approach instead of the optimal approach using BFS.