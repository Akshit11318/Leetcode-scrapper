# Movement of Robots

**Problem Link:** https://leetcode.com/problems/movement-of-robots/description

**Problem Statement:**
- Input format and constraints: The problem involves `n` robots and `m` obstacles in a grid. Each robot is represented by its initial position `(xi, yi)` and direction `di`. The goal is to find the minimum number of moves required for all robots to reach their target positions `(xt, yt)` while avoiding obstacles.
- Expected output format: The output should be the minimum number of moves required for all robots to reach their target positions.
- Key requirements and edge cases to consider: 
  - Robots can move in four directions: up, down, left, and right.
  - Robots cannot move to a cell occupied by an obstacle or another robot.
  - The grid is bounded by walls, and robots cannot move outside the grid.
- Example test cases with explanations:
  - A simple case with one robot and no obstacles.
  - A case with multiple robots and obstacles.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to simulate the movement of each robot and check all possible moves until all robots reach their target positions.
- Step-by-step breakdown of the solution:
  1. Initialize the positions and directions of all robots.
  2. For each robot, explore all possible moves (up, down, left, right) and check if the new position is valid (not outside the grid, not occupied by an obstacle or another robot).
  3. If a valid move is found, update the robot's position and direction.
  4. Repeat steps 2-3 until all robots reach their target positions or no valid moves are left.
- Why this approach comes to mind first: This approach is intuitive because it directly simulates the movement of robots and checks all possible moves.

```cpp
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

struct Robot {
    int x, y, dir;
};

bool isValidMove(vector<vector<int>>& grid, int x, int y, int n, int m) {
    return x >= 0 && x < n && y >= 0 && y < m && grid[x][y] == 0;
}

int minMoves(vector<vector<int>>& grid, vector<Robot>& robots, vector<vector<int>>& targets) {
    int n = grid.size();
    int m = grid[0].size();
    int moves = 0;
    
    while (true) {
        bool allReached = true;
        for (int i = 0; i < robots.size(); i++) {
            if (robots[i].x != targets[i][0] || robots[i].y != targets[i][1]) {
                allReached = false;
                break;
            }
        }
        if (allReached) break;
        
        for (int i = 0; i < robots.size(); i++) {
            int newX = robots[i].x;
            int newY = robots[i].y;
            switch (robots[i].dir) {
                case 0: // up
                    newX--;
                    break;
                case 1: // down
                    newX++;
                    break;
                case 2: // left
                    newY--;
                    break;
                case 3: // right
                    newY++;
                    break;
            }
            if (isValidMove(grid, newX, newY, n, m)) {
                robots[i].x = newX;
                robots[i].y = newY;
            }
        }
        moves++;
    }
    return moves;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot k)$, where $n$ and $m$ are the dimensions of the grid, and $k$ is the number of robots. This is because in the worst case, we might need to explore all possible moves for all robots.
> - **Space Complexity:** $O(n \cdot m + k)$, where $n \cdot m$ is the space required to store the grid, and $k$ is the space required to store the robots' information.
> - **Why these complexities occur:** These complexities occur because we are simulating the movement of all robots and checking all possible moves, which requires exploring the entire grid and storing the information of all robots.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution involves using a breadth-first search (BFS) algorithm to find the shortest path for each robot to reach its target position while avoiding obstacles and other robots.
- Detailed breakdown of the approach:
  1. Initialize a queue to store the current positions and directions of all robots.
  2. For each robot, explore all possible moves (up, down, left, right) and check if the new position is valid (not outside the grid, not occupied by an obstacle or another robot).
  3. If a valid move is found, add the new position and direction to the queue.
  4. Repeat steps 2-3 until the queue is empty or all robots reach their target positions.
- Proof of optimality: This approach is optimal because it uses BFS to find the shortest path for each robot, which ensures that the minimum number of moves is used.

```cpp
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

struct Robot {
    int x, y, dir, moves;
};

bool isValidMove(vector<vector<int>>& grid, int x, int y, int n, int m) {
    return x >= 0 && x < n && y >= 0 && y < m && grid[x][y] == 0;
}

int minMoves(vector<vector<int>>& grid, vector<Robot>& robots, vector<vector<int>>& targets) {
    int n = grid.size();
    int m = grid[0].size();
    int moves = 0;
    queue<Robot> q;
    
    for (int i = 0; i < robots.size(); i++) {
        q.push({robots[i].x, robots[i].y, robots[i].dir, 0});
    }
    
    while (!q.empty()) {
        Robot current = q.front();
        q.pop();
        
        if (current.x == targets[current.dir][0] && current.y == targets[current.dir][1]) {
            moves = max(moves, current.moves);
            continue;
        }
        
        for (int i = 0; i < 4; i++) {
            int newX = current.x;
            int newY = current.y;
            switch (i) {
                case 0: // up
                    newX--;
                    break;
                case 1: // down
                    newX++;
                    break;
                case 2: // left
                    newY--;
                    break;
                case 3: // right
                    newY++;
                    break;
            }
            if (isValidMove(grid, newX, newY, n, m)) {
                q.push({newX, newY, i, current.moves + 1});
            }
        }
    }
    return moves;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot k \cdot 4^d)$, where $n$ and $m$ are the dimensions of the grid, $k$ is the number of robots, and $d$ is the maximum distance between a robot and its target position. This is because in the worst case, we might need to explore all possible moves for all robots up to a depth of $d$.
> - **Space Complexity:** $O(n \cdot m + k \cdot 4^d)$, where $n \cdot m$ is the space required to store the grid, and $k \cdot 4^d$ is the space required to store the queue.
> - **Optimality proof:** This approach is optimal because it uses BFS to find the shortest path for each robot, which ensures that the minimum number of moves is used.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: BFS, queue data structure, and graph traversal.
- Problem-solving patterns identified: Using BFS to find the shortest path in an unweighted graph.
- Optimization techniques learned: Using a queue to store the current positions and directions of all robots, and exploring all possible moves to find the shortest path.
- Similar problems to practice: Other graph traversal problems, such as finding the shortest path between two nodes in a weighted graph.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for valid moves, not updating the queue correctly, and not handling the case where a robot reaches its target position.
- Edge cases to watch for: Robots moving outside the grid, robots moving to a cell occupied by an obstacle or another robot, and robots not reaching their target positions.
- Performance pitfalls: Using a recursive approach instead of an iterative approach, which can lead to stack overflow errors for large inputs.
- Testing considerations: Testing the implementation with different input scenarios, such as different grid sizes, different robot positions and directions, and different target positions.