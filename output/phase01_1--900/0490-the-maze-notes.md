## The Maze

**Problem Link:** https://leetcode.com/problems/the-maze/description

**Problem Statement:**
- Input format: The maze is represented as a 2D grid, where `0` represents an empty space and `1` represents a wall. The ball and hole are represented as coordinates.
- Constraints: The maze is rectangular and has at least one empty space. The ball and hole are within the maze boundaries.
- Expected output format: The minimum number of steps required to move the ball from its initial position to the hole. If there is no path, return `-1`.
- Key requirements and edge cases to consider: The ball can only move in four directions (up, down, left, right) and stops when it hits a wall or reaches the hole. The maze can have multiple holes, but we are only interested in the first one we encounter.
- Example test cases with explanations:
  - A simple maze with a single hole: `[[0,0,1,0],[0,0,0,0],[0,0,1,0],[0,0,0,0]]`, ball at `(0,0)`, hole at `(3,3)`.
  - A maze with multiple holes: `[[0,0,1,0],[0,0,0,0],[0,0,1,0],[0,0,0,0]]`, ball at `(0,0)`, holes at `(1,1)` and `(3,3)`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible moves from the ball's initial position and explore the maze recursively.
- Step-by-step breakdown of the solution:
  1. Define a recursive function to explore the maze.
  2. In each recursive call, try all four possible moves (up, down, left, right).
  3. If the move is valid (i.e., the ball doesn't hit a wall), make the move and recursively explore the new position.
  4. If the ball reaches the hole, return the number of steps taken.
  5. If all possible moves have been tried and the ball hasn't reached the hole, return `-1`.
- Why this approach comes to mind first: It's a straightforward and intuitive way to solve the problem, but it's not efficient due to the large number of recursive calls.

```cpp
class Solution {
public:
    int shortestDistance(vector<vector<int>>& maze, vector<int>& start, vector<int>& destination) {
        int rows = maze.size();
        int cols = maze[0].size();
        vector<vector<int>> directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        vector<vector<int>> visited(rows, vector<int>(cols, -1));
        
        return dfs(maze, start, destination, directions, visited);
    }
    
    int dfs(vector<vector<int>>& maze, vector<int>& current, vector<int>& destination, vector<vector<int>>& directions, vector<vector<int>>& visited) {
        if (current == destination) return 0;
        
        if (visited[current[0]][current[1]] != -1) return visited[current[0]][current[1]];
        
        int min_steps = INT_MAX;
        
        for (auto& dir : directions) {
            int x = current[0];
            int y = current[1];
            int steps = 0;
            
            while (x + dir[0] >= 0 && x + dir[0] < maze.size() && y + dir[1] >= 0 && y + dir[1] < maze[0].size() && maze[x + dir[0]][y + dir[1]] == 0) {
                x += dir[0];
                y += dir[1];
                steps++;
            }
            
            if (x == destination[0] && y == destination[1]) {
                min_steps = min(min_steps, steps);
            } else {
                int next_steps = dfs(maze, {x, y}, destination, directions, visited);
                if (next_steps != -1) {
                    min_steps = min(min_steps, steps + next_steps);
                }
            }
        }
        
        visited[current[0]][current[1]] = min_steps == INT_MAX ? -1 : min_steps;
        
        return visited[current[0]][current[1]];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(4^{n \cdot m})$, where $n$ and $m$ are the dimensions of the maze. This is because in the worst case, we might need to explore all possible paths of length $n \cdot m$.
> - **Space Complexity:** $O(n \cdot m)$, where $n$ and $m$ are the dimensions of the maze. This is because we need to store the visited states.
> - **Why these complexities occur:** The recursive nature of the solution leads to an exponential time complexity, and the need to store visited states leads to a quadratic space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a queue-based BFS algorithm to explore the maze level by level, starting from the ball's initial position.
- Detailed breakdown of the approach:
  1. Define a queue to store the positions to be explored, along with the number of steps taken to reach each position.
  2. Enqueue the ball's initial position with 0 steps.
  3. While the queue is not empty, dequeue a position and explore its neighbors.
  4. If a neighbor is the hole, return the number of steps taken to reach it.
  5. If a neighbor is an empty space and has not been visited before, mark it as visited and enqueue it with the updated number of steps.
- Why further optimization is impossible: The BFS algorithm is guaranteed to find the shortest path to the hole, if one exists, and it does so in the minimum number of steps possible.

```cpp
class Solution {
public:
    int shortestDistance(vector<vector<int>>& maze, vector<int>& start, vector<int>& destination) {
        int rows = maze.size();
        int cols = maze[0].size();
        vector<vector<int>> directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        vector<vector<int>> visited(rows, vector<int>(cols, -1));
        queue<pair<vector<int>, int>> q;
        
        q.push({start, 0});
        visited[start[0]][start[1]] = 0;
        
        while (!q.empty()) {
            auto current = q.front();
            q.pop();
            
            if (current.first == destination) return current.second;
            
            for (auto& dir : directions) {
                int x = current.first[0];
                int y = current.first[1];
                int steps = current.second;
                
                while (x + dir[0] >= 0 && x + dir[0] < rows && y + dir[1] >= 0 && y + dir[1] < cols && maze[x + dir[0]][y + dir[1]] == 0) {
                    x += dir[0];
                    y += dir[1];
                    steps++;
                }
                
                x -= dir[0];
                y -= dir[1];
                steps--;
                
                if (visited[x][y] == -1 || visited[x][y] > steps) {
                    visited[x][y] = steps;
                    q.push({{x, y}, steps});
                }
            }
        }
        
        return -1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot 4^{d})$, where $n$ and $m$ are the dimensions of the maze, and $d$ is the maximum distance from the ball to the hole. This is because in the worst case, we might need to explore all possible paths of length $d$.
> - **Space Complexity:** $O(n \cdot m)$, where $n$ and $m$ are the dimensions of the maze. This is because we need to store the visited states.
> - **Optimality proof:** The BFS algorithm is guaranteed to find the shortest path to the hole, if one exists, and it does so in the minimum number of steps possible.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: BFS, queue-based exploration, visited state tracking.
- Problem-solving patterns identified: Using a queue to explore a graph or maze level by level, tracking visited states to avoid infinite loops.
- Optimization techniques learned: Using a BFS algorithm to find the shortest path in an unweighted graph or maze.
- Similar problems to practice: Finding the shortest path in a weighted graph or maze, exploring a graph or maze with multiple sources or sinks.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for visited states, not updating the number of steps correctly, not handling edge cases (e.g., ball or hole outside the maze).
- Edge cases to watch for: Ball or hole outside the maze, maze with no holes, maze with multiple holes.
- Performance pitfalls: Using a recursive algorithm with a large number of recursive calls, not using a queue to explore the maze level by level.
- Testing considerations: Testing with different maze sizes, testing with different ball and hole positions, testing with multiple holes.