## Cut Off Trees for Golf Event

**Problem Link:** https://leetcode.com/problems/cut-off-trees-for-golf-event/description

**Problem Statement:**
- Input format and constraints: Given an `m x n` grid `forest`, where `forest[i][j]` represents the height of the tree at position `(i, j)`. 
- Expected output format: The minimum number of steps to cut all trees in the forest.
- Key requirements and edge cases to consider: 
  - If it is impossible to cut all the trees, return `-1`.
  - A tree can only be cut if its height is less than or equal to the height of the previous tree.
- Example test cases with explanations:
  - For example, given `forest = [[1,2,3],[0,0,4],[7,6,5]]`, the output is `6`.
  - Another example, given `forest = [[1,2,3],[0,0,0],[7,6,5]]`, the output is `-1`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: One possible approach is to try all possible orders of cutting the trees and calculate the minimum number of steps required for each order.
- Step-by-step breakdown of the solution:
  1. Generate all permutations of the trees in the forest.
  2. For each permutation, calculate the minimum number of steps required to cut all trees in that order.
  3. Keep track of the minimum number of steps across all permutations.
- Why this approach comes to mind first: This approach is straightforward and guarantees to find the optimal solution if it exists. However, it is not efficient due to the large number of permutations.

```cpp
#include <vector>
#include <algorithm>

using namespace std;

int cutOffTree(vector<vector<int>>& forest) {
    vector<vector<int>> trees;
    int m = forest.size(), n = forest[0].size();
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (forest[i][j] > 0) {
                trees.push_back({forest[i][j], i, j});
            }
        }
    }
    sort(trees.begin(), trees.end());
    int res = 0;
    int sx = 0, sy = 0;
    for (auto& tree : trees) {
        int tx = tree[1], ty = tree[2];
        int dist = bfs(forest, sx, sy, tx, ty);
        if (dist == -1) return -1;
        res += dist;
        sx = tx, sy = ty;
    }
    return res;
}

int bfs(vector<vector<int>>& forest, int sx, int sy, int tx, int ty) {
    int m = forest.size(), n = forest[0].size();
    vector<vector<bool>> visited(m, vector<bool>(n, false));
    vector<pair<int, int>> directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    queue<pair<int, int>> q;
    q.push({sx, sy});
    visited[sx][sy] = true;
    int steps = 0;
    while (!q.empty()) {
        int size = q.size();
        for (int i = 0; i < size; i++) {
            auto [x, y] = q.front();
            q.pop();
            if (x == tx && y == ty) return steps;
            for (auto& dir : directions) {
                int nx = x + dir.first, ny = y + dir.second;
                if (nx >= 0 && nx < m && ny >= 0 && ny < n && !visited[nx][ny] && forest[nx][ny] != 0) {
                    q.push({nx, ny});
                    visited[nx][ny] = true;
                }
            }
        }
        steps++;
    }
    return -1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n \cdot k! \cdot (m + n))$, where $k$ is the number of trees in the forest. This is because we generate all permutations of the trees and for each permutation, we perform a BFS traversal.
> - **Space Complexity:** $O(m \cdot n)$, where $m$ and $n$ are the dimensions of the forest. This is because we use a visited matrix to keep track of the visited cells during the BFS traversal.
> - **Why these complexities occur:** The time complexity is high due to the large number of permutations and the BFS traversal for each permutation. The space complexity is moderate due to the visited matrix.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of generating all permutations of the trees, we can use a priority queue to keep track of the trees that need to be cut and their distances from the current position.
- Detailed breakdown of the approach:
  1. Initialize a priority queue with the current position and distance 0.
  2. While the priority queue is not empty, pop the tree with the minimum distance and cut it.
  3. Update the current position and distance.
  4. Push the neighboring trees into the priority queue if they have not been cut yet.
- Proof of optimality: This approach is optimal because it always chooses the tree with the minimum distance from the current position, which minimizes the total number of steps.

```cpp
#include <vector>
#include <queue>

using namespace std;

int cutOffTree(vector<vector<int>>& forest) {
    int m = forest.size(), n = forest[0].size();
    vector<vector<int>> trees;
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (forest[i][j] > 0) {
                trees.push_back({forest[i][j], i, j});
            }
        }
    }
    sort(trees.begin(), trees.end());
    int res = 0;
    int sx = 0, sy = 0;
    for (auto& tree : trees) {
        int tx = tree[1], ty = tree[2];
        int dist = bfs(forest, sx, sy, tx, ty);
        if (dist == -1) return -1;
        res += dist;
        sx = tx, sy = ty;
    }
    return res;
}

int bfs(vector<vector<int>>& forest, int sx, int sy, int tx, int ty) {
    int m = forest.size(), n = forest[0].size();
    vector<vector<bool>> visited(m, vector<bool>(n, false));
    vector<pair<int, int>> directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    queue<pair<int, int>> q;
    q.push({sx, sy});
    visited[sx][sy] = true;
    int steps = 0;
    while (!q.empty()) {
        int size = q.size();
        for (int i = 0; i < size; i++) {
            auto [x, y] = q.front();
            q.pop();
            if (x == tx && y == ty) return steps;
            for (auto& dir : directions) {
                int nx = x + dir.first, ny = y + dir.second;
                if (nx >= 0 && nx < m && ny >= 0 && ny < n && !visited[nx][ny] && forest[nx][ny] != 0) {
                    q.push({nx, ny});
                    visited[nx][ny] = true;
                }
            }
        }
        steps++;
    }
    return -1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(k \cdot (m + n))$, where $k$ is the number of trees in the forest. This is because we perform a BFS traversal for each tree.
> - **Space Complexity:** $O(m \cdot n)$, where $m$ and $n$ are the dimensions of the forest. This is because we use a visited matrix to keep track of the visited cells during the BFS traversal.
> - **Optimality proof:** This approach is optimal because it always chooses the tree with the minimum distance from the current position, which minimizes the total number of steps.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: BFS traversal, priority queue.
- Problem-solving patterns identified: Using a priority queue to keep track of the trees that need to be cut and their distances from the current position.
- Optimization techniques learned: Choosing the tree with the minimum distance from the current position.
- Similar problems to practice: Other problems that involve finding the minimum number of steps to reach a target, such as the "Shortest Path" problem.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if the neighboring cells are within the bounds of the forest.
- Edge cases to watch for: The case where there are no trees in the forest, or the case where the target tree is not reachable from the current position.
- Performance pitfalls: Using a brute force approach that generates all permutations of the trees.
- Testing considerations: Testing the code with different inputs, including edge cases, to ensure that it works correctly.