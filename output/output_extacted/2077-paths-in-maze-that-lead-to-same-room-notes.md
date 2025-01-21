## Paths in Maze That Lead to Same Room
**Problem Link:** https://leetcode.com/problems/paths-in-maze-that-lead-to-same-room/description

**Problem Statement:**
- Input format and constraints: The problem involves a maze represented as a grid where each cell can be a wall (`#`), an empty space (`.`), or a door (`D`). The goal is to find all paths from a given starting point to a target room (`D`) that lead to the same room.
- Expected output format: The output should be a list of all such paths.
- Key requirements and edge cases to consider: The maze can have multiple doors, and a path can only be considered valid if it ends at a door.
- Example test cases with explanations: For instance, given a maze with a single door and no obstacles, the output should include all possible paths from the start to the door.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to explore all possible paths from the starting point using a depth-first search (DFS) or breadth-first search (BFS) algorithm.
- Step-by-step breakdown of the solution:
  1. Initialize the starting point and the target door.
  2. Use DFS or BFS to explore all possible paths from the starting point.
  3. For each path, check if it ends at the target door. If it does, add it to the list of valid paths.
- Why this approach comes to mind first: It's a straightforward way to explore all possibilities without worrying about efficiency.

```cpp
#include <vector>
#include <string>

using namespace std;

vector<string> findPaths(vector<vector<char>>& maze, int startRow, int startCol) {
    vector<string> paths;
    vector<vector<bool>> visited(maze.size(), vector<bool>(maze[0].size(), false));
    string path = "";
    dfs(maze, startRow, startCol, path, visited, paths);
    return paths;
}

void dfs(vector<vector<char>>& maze, int row, int col, string& path, vector<vector<bool>>& visited, vector<string>& paths) {
    if (row < 0 || row >= maze.size() || col < 0 || col >= maze[0].size() || maze[row][col] == '#' || visited[row][col]) {
        return;
    }
    if (maze[row][col] == 'D') {
        paths.push_back(path);
        return;
    }
    visited[row][col] = true;
    path += to_string(row) + "," + to_string(col);
    dfs(maze, row - 1, col, path, visited, paths);
    dfs(maze, row + 1, col, path, visited, paths);
    dfs(maze, row, col - 1, path, visited, paths);
    dfs(maze, row, col + 1, path, visited, paths);
    path.erase(path.size() - 3);
    visited[row][col] = false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(4^{n \times m})$ where $n$ and $m$ are the dimensions of the maze, because in the worst case, we explore all possible paths.
> - **Space Complexity:** $O(n \times m)$ for the recursion stack and the visited matrix.
> - **Why these complexities occur:** The brute force approach explores all possible paths, leading to exponential time complexity. The space complexity is due to the recursion stack and the visited matrix.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of exploring all possible paths, we can use a more efficient algorithm that only explores paths that are likely to lead to the target door.
- Detailed breakdown of the approach:
  1. Initialize the starting point and the target door.
  2. Use a modified DFS or BFS algorithm that only explores paths that are in the direction of the target door.
  3. For each path, check if it ends at the target door. If it does, add it to the list of valid paths.
- Proof of optimality: The optimal approach has a time complexity of $O(n \times m)$ because we only explore paths that are in the direction of the target door.

```cpp
vector<string> findPathsOptimal(vector<vector<char>>& maze, int startRow, int startCol) {
    vector<string> paths;
    vector<vector<bool>> visited(maze.size(), vector<bool>(maze[0].size(), false));
    string path = "";
    int targetRow = -1, targetCol = -1;
    for (int i = 0; i < maze.size(); i++) {
        for (int j = 0; j < maze[0].size(); j++) {
            if (maze[i][j] == 'D') {
                targetRow = i;
                targetCol = j;
                break;
            }
        }
        if (targetRow != -1) break;
    }
    dfsOptimal(maze, startRow, startCol, path, visited, paths, targetRow, targetCol);
    return paths;
}

void dfsOptimal(vector<vector<char>>& maze, int row, int col, string& path, vector<vector<bool>>& visited, vector<string>& paths, int targetRow, int targetCol) {
    if (row < 0 || row >= maze.size() || col < 0 || col >= maze[0].size() || maze[row][col] == '#' || visited[row][col]) {
        return;
    }
    if (row == targetRow && col == targetCol) {
        paths.push_back(path);
        return;
    }
    visited[row][col] = true;
    path += to_string(row) + "," + to_string(col);
    if (row < targetRow) dfsOptimal(maze, row + 1, col, path, visited, paths, targetRow, targetCol);
    if (row > targetRow) dfsOptimal(maze, row - 1, col, path, visited, paths, targetRow, targetCol);
    if (col < targetCol) dfsOptimal(maze, row, col + 1, path, visited, paths, targetRow, targetCol);
    if (col > targetCol) dfsOptimal(maze, row, col - 1, path, visited, paths, targetRow, targetCol);
    path.erase(path.size() - 3);
    visited[row][col] = false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times m)$ where $n$ and $m$ are the dimensions of the maze, because we only explore paths that are in the direction of the target door.
> - **Space Complexity:** $O(n \times m)$ for the recursion stack and the visited matrix.
> - **Optimality proof:** The optimal approach has a time complexity of $O(n \times m)$ because we only explore paths that are in the direction of the target door.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: DFS, BFS, and modified DFS/BFS for optimal solution.
- Problem-solving patterns identified: Exploring all possible paths and optimizing the search by only exploring paths in the direction of the target.
- Optimization techniques learned: Reducing the search space by only exploring paths that are likely to lead to the target.
- Similar problems to practice: Maze problems, graph traversal, and optimization problems.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for out-of-bounds conditions, not handling visited cells correctly.
- Edge cases to watch for: Empty maze, maze with no doors, maze with multiple doors.
- Performance pitfalls: Exploring all possible paths without optimization.
- Testing considerations: Test cases with different maze sizes, different door positions, and different starting points.