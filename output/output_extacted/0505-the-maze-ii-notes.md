## The Maze II

**Problem Link:** https://leetcode.com/problems/the-maze-ii/description

**Problem Statement:**
- Input format: A 2D grid `maze` and two points `ball` and `hole`.
- Constraints: The maze is a rectangular grid, the ball and hole are within the maze, and there are no obstacles at the ball or hole.
- Expected output format: The shortest path from the ball to the hole, or -1 if no path exists.
- Key requirements: Find the shortest path in terms of the number of steps to reach the hole from the ball.
- Example test cases:
  - A maze with a clear path from the ball to the hole.
  - A maze with no path from the ball to the hole.
  - A maze with multiple possible paths, where the shortest one is required.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible directions from the ball until we reach the hole or all paths are exhausted.
- Step-by-step breakdown of the solution:
  1. Start at the ball position.
  2. Explore all four directions (up, down, left, right) from the current position.
  3. For each direction, move as far as possible until hitting a wall or the edge of the maze.
  4. If the hole is reached, record the path taken.
  5. If not, backtrack and try another direction.
- Why this approach comes to mind first: It's a straightforward, exhaustive search that guarantees finding the shortest path if one exists.

```cpp
#include <vector>
#include <queue>
using namespace std;

struct Point {
    int x, y, dist;
    Point(int x, int y, int dist) : x(x), y(y), dist(dist) {}
};

int shortestDistance(vector<vector<int>>& maze, vector<int>& ball, vector<int>& hole) {
    int m = maze.size(), n = maze[0].size();
    vector<vector<int>> directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    queue<Point> q;
    q.push(Point(ball[0], ball[1], 0));
    vector<vector<bool>> visited(m, vector<bool>(n, false));
    visited[ball[0]][ball[1]] = true;

    while (!q.empty()) {
        Point p = q.front();
        q.pop();
        if (p.x == hole[0] && p.y == hole[1]) {
            return p.dist;
        }
        for (auto& dir : directions) {
            int nx = p.x, ny = p.y;
            while (0 <= nx && nx < m && 0 <= ny && ny < n && maze[nx][ny] == 0) {
                nx += dir[0];
                ny += dir[1];
            }
            nx -= dir[0];
            ny -= dir[1];
            if (!visited[nx][ny]) {
                visited[nx][ny] = true;
                q.push(Point(nx, ny, p.dist + 1));
            }
        }
    }
    return -1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n \cdot (m + n))$, where $m$ and $n$ are the dimensions of the maze. This is because in the worst case, we might explore all cells in all four directions.
> - **Space Complexity:** $O(m \cdot n)$ for storing the visited cells and the queue.
> - **Why these complexities occur:** The brute force approach involves exploring all possible paths, which can lead to a high number of steps in large mazes.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Utilize a breadth-first search (BFS) algorithm to explore the maze level by level, ensuring the shortest path is found first.
- Detailed breakdown of the approach:
  1. Initialize a queue with the starting point (the ball) and a distance of 0.
  2. Mark the starting point as visited.
  3. Explore all possible directions from the current point, moving as far as possible without hitting a wall.
  4. If a new point is reached that has not been visited, mark it as visited and add it to the queue with the updated distance.
  5. Repeat steps 3-4 until the hole is reached or the queue is empty.
- Proof of optimality: BFS is guaranteed to find the shortest path in an unweighted graph, which is the case here since all moves have the same cost (one step).

```cpp
int shortestDistance(vector<vector<int>>& maze, vector<int>& ball, vector<int>& hole) {
    int m = maze.size(), n = maze[0].size();
    vector<vector<int>> directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    queue<pair<int, pair<int, int>>> q;
    q.push({0, {ball[0], ball[1]}});
    vector<vector<bool>> visited(m, vector<bool>(n, false));
    visited[ball[0]][ball[1]] = true;

    while (!q.empty()) {
        auto [dist, pos] = q.front();
        q.pop();
        if (pos.first == hole[0] && pos.second == hole[1]) {
            return dist;
        }
        for (auto& dir : directions) {
            int nx = pos.first, ny = pos.second;
            while (0 <= nx && nx < m && 0 <= ny && ny < n && maze[nx][ny] == 0) {
                nx += dir[0];
                ny += dir[1];
            }
            nx -= dir[0];
            ny -= dir[1];
            if (!visited[nx][ny]) {
                visited[nx][ny] = true;
                q.push({dist + 1, {nx, ny}});
            }
        }
    }
    return -1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n \cdot (m + n))$, similar to the brute force approach because we're still exploring all reachable cells in the worst case.
> - **Space Complexity:** $O(m \cdot n)$ for storing visited cells and the queue.
> - **Optimality proof:** This approach is optimal because it uses BFS, which is guaranteed to find the shortest path in an unweighted graph.

---

### Final Notes

**Learning Points:**
- The importance of choosing the right algorithm for the problem (BFS for shortest paths in unweighted graphs).
- Understanding how to apply graph traversal algorithms to solve problems involving paths and distances.
- Recognizing the trade-offs between different approaches in terms of time and space complexity.

**Mistakes to Avoid:**
- Not considering the constraints of the problem (e.g., the maze's dimensions, the presence of walls).
- Failing to mark visited cells, leading to infinite loops.
- Not using the most efficient data structures for the problem (e.g., using a queue for BFS).