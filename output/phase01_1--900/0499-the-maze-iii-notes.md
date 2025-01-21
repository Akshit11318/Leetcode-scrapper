## The Maze III

**Problem Link:** https://leetcode.com/problems/the-maze-iii/description

**Problem Statement:**
- Input format and constraints: The problem involves a maze represented by a `2D grid`, where each cell can be either a wall (`#`), a hole (`.`), or the starting position (`S`). The goal is to find the shortest path to the destination (`T`) using a ball that can move in four directions (`up`, `down`, `left`, `right`) until it hits a wall or reaches the destination.
- Expected output format: The function should return the shortest path from the start to the destination. If there is no path, return "impossible".
- Key requirements and edge cases to consider:
  - The ball can only move in the four main directions (up, down, left, right).
  - The ball stops when it hits a wall or reaches the destination.
  - There can be holes in the maze that the ball can fall into.
- Example test cases with explanations:
  - A simple maze with a clear path from start to destination.
  - A maze with a hole that the ball can fall into, requiring a different path.
  - A maze with no path from start to destination.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible paths from the start to the destination, exploring each direction until the ball hits a wall or reaches the destination.
- Step-by-step breakdown of the solution:
  1. Initialize a queue with the starting position and an empty path.
  2. Dequeue the current position and path.
  3. Explore all four directions from the current position.
  4. For each direction, simulate the ball's movement until it hits a wall or reaches the destination.
  5. If the ball reaches the destination, return the path taken.
  6. If the ball hits a wall, backtrack and try the next direction.
- Why this approach comes to mind first: It's a straightforward way to explore all possible paths in the maze.

```cpp
#include <iostream>
#include <queue>
#include <vector>
#include <string>

using namespace std;

struct Position {
    int x, y;
    string path;
};

string shortestPath(vector<vector<char>>& maze, vector<int>& ball, vector<int>& hole) {
    queue<Position> q;
    q.push({ball[0], ball[1], ""});
    vector<vector<bool>> visited(maze.size(), vector<bool>(maze[0].size(), false));
    while (!q.empty()) {
        Position curr = q.front();
        q.pop();
        if (curr.x == hole[0] && curr.y == hole[1]) {
            return curr.path;
        }
        if (visited[curr.x][curr.y]) continue;
        visited[curr.x][curr.y] = true;
        // Explore all four directions
        vector<vector<int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        for (int i = 0; i < 4; i++) {
            int newX = curr.x, newY = curr.y;
            string newPath = curr.path;
            while (true) {
                newX += directions[i][0];
                newY += directions[i][1];
                if (newX < 0 || newX >= maze.size() || newY < 0 || newY >= maze[0].size() || maze[newX][newY] == '#') {
                    break;
                }
                if (newX == hole[0] && newY == hole[1]) {
                    return newPath + getDirection(i);
                }
                newPath += getDirection(i);
            }
            q.push({newX - directions[i][0], newY - directions[i][1], newPath});
        }
    }
    return "impossible";
}

string getDirection(int i) {
    switch (i) {
        case 0: return "u";
        case 1: return "d";
        case 2: return "l";
        case 3: return "r";
    }
}

int main() {
    vector<vector<char>> maze = {
        {'#', '#', '#', '#', '#', '#'},
        {'#', 'S', '.', '.', '.', '#'},
        {'#', '#', '#', '.', '#', '#'},
        {'#', '.', '.', '.', '.', '#'},
        {'#', '#', '#', '.', '#', '#'},
        {'#', 'T', '.', '.', '.', '#'},
        {'#', '#', '#', '#', '#', '#'}
    };
    vector<int> ball = {1, 1};
    vector<int> hole = {5, 1};
    cout << shortestPath(maze, ball, hole) << endl;
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(4^{n \cdot m})$, where $n$ and $m$ are the dimensions of the maze. This is because in the worst case, we might have to explore all possible paths of length $n \cdot m$.
> - **Space Complexity:** $O(n \cdot m)$, where $n$ and $m$ are the dimensions of the maze. This is because we need to store the visited positions in the maze.
> - **Why these complexities occur:** The brute force approach explores all possible paths in the maze, resulting in exponential time complexity. The space complexity is linear because we only need to store the visited positions.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a `BFS` (Breadth-First Search) algorithm to explore the maze level by level, keeping track of the shortest path to each position.
- Detailed breakdown of the approach:
  1. Initialize a queue with the starting position and an empty path.
  2. Dequeue the current position and path.
  3. Explore all four directions from the current position.
  4. For each direction, simulate the ball's movement until it hits a wall or reaches the destination.
  5. If the ball reaches the destination, return the path taken.
  6. If the ball hits a wall, backtrack and try the next direction.
- Why further optimization is impossible: The BFS algorithm explores the maze level by level, ensuring that we find the shortest path to the destination.

```cpp
#include <iostream>
#include <queue>
#include <vector>
#include <string>

using namespace std;

struct Position {
    int x, y;
    string path;
};

string shortestPath(vector<vector<char>>& maze, vector<int>& ball, vector<int>& hole) {
    queue<Position> q;
    q.push({ball[0], ball[1], ""});
    vector<vector<bool>> visited(maze.size(), vector<bool>(maze[0].size(), false));
    while (!q.empty()) {
        Position curr = q.front();
        q.pop();
        if (curr.x == hole[0] && curr.y == hole[1]) {
            return curr.path;
        }
        if (visited[curr.x][curr.y]) continue;
        visited[curr.x][curr.y] = true;
        // Explore all four directions
        vector<vector<int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        for (int i = 0; i < 4; i++) {
            int newX = curr.x, newY = curr.y;
            string newPath = curr.path;
            while (true) {
                newX += directions[i][0];
                newY += directions[i][1];
                if (newX < 0 || newX >= maze.size() || newY < 0 || newY >= maze[0].size() || maze[newX][newY] == '#') {
                    break;
                }
                if (newX == hole[0] && newY == hole[1]) {
                    return newPath + getDirection(i);
                }
                newPath += getDirection(i);
            }
            q.push({newX - directions[i][0], newY - directions[i][1], newPath});
        }
    }
    return "impossible";
}

string getDirection(int i) {
    switch (i) {
        case 0: return "u";
        case 1: return "d";
        case 2: return "l";
        case 3: return "r";
    }
}

int main() {
    vector<vector<char>> maze = {
        {'#', '#', '#', '#', '#', '#'},
        {'#', 'S', '.', '.', '.', '#'},
        {'#', '#', '#', '.', '#', '#'},
        {'#', '.', '.', '.', '.', '#'},
        {'#', '#', '#', '.', '#', '#'},
        {'#', 'T', '.', '.', '.', '#'},
        {'#', '#', '#', '#', '#', '#'}
    };
    vector<int> ball = {1, 1};
    vector<int> hole = {5, 1};
    cout << shortestPath(maze, ball, hole) << endl;
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ and $m$ are the dimensions of the maze. This is because we explore the maze level by level using BFS.
> - **Space Complexity:** $O(n \cdot m)$, where $n$ and $m$ are the dimensions of the maze. This is because we need to store the visited positions in the maze.
> - **Optimality proof:** The BFS algorithm ensures that we find the shortest path to the destination by exploring the maze level by level.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: BFS, queue data structure, maze exploration.
- Problem-solving patterns identified: Using BFS to find the shortest path in a maze.
- Optimization techniques learned: Using BFS to reduce the time complexity from exponential to linear.
- Similar problems to practice: Other maze-related problems, such as finding the shortest path in a weighted maze.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for visited positions, not handling edge cases correctly.
- Edge cases to watch for: Maze boundaries, holes, walls, and the destination.
- Performance pitfalls: Using an inefficient algorithm, such as DFS, to explore the maze.
- Testing considerations: Test the implementation with different maze configurations, including edge cases.