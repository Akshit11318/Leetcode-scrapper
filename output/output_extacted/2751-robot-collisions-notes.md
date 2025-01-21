## Robot Collisions
**Problem Link:** https://leetcode.com/problems/robot-collisions/description

**Problem Statement:**
- Input format: `int n`, `vector<vector<int>> obstacles`, where each obstacle is represented as `[x, y]`.
- Constraints: `1 <= n <= 100`, `0 <= x, y <= 100`.
- Expected output format: The number of robot collisions.
- Key requirements and edge cases to consider:
  - The robot moves in a grid from `(0, 0)` to `(x, y)`, where `x` and `y` are the coordinates of the cell.
  - If the robot hits an obstacle, it stops moving.
  - The robot only moves right or down.
- Example test cases with explanations:
  - Example 1: `n = 5`, `obstacles = [[2,2],[4,1],[1,0]]`, the output is `2`.
  - Example 2: `n = 3`, `obstacles = [[1,0],[1,1],[2,1]]`, the output is `2`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible paths and count the number of collisions.
- Step-by-step breakdown of the solution:
  1. Initialize a `visited` set to keep track of visited cells.
  2. Define a recursive function `dfs` to try all possible paths.
  3. In the `dfs` function, check if the current cell is an obstacle. If it is, return 1 (collision).
  4. If the current cell is not an obstacle, try moving right and down.
  5. If the current cell is the destination, return 0 (no collision).
- Why this approach comes to mind first: It is a straightforward way to try all possible paths.

```cpp
class Solution {
public:
    int robotSim(int n, vector<vector<int>>& obstacles) {
        set<pair<int, int>> obstacleSet;
        for (auto& obstacle : obstacles) {
            obstacleSet.insert({obstacle[0], obstacle[1]});
        }
        int ans = 0;
        int x = 0, y = 0;
        int dx = 0, dy = 1;
        for (int i = 0; i < n; i++) {
            if (obstacleSet.count({x + dx, y + dy})) {
                ans++;
            } else {
                x += dx;
                y += dy;
            }
        }
        return ans;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of moves.
> - **Space Complexity:** $O(m)$, where $m$ is the number of obstacles.
> - **Why these complexities occur:** The time complexity is $O(n)$ because we try all possible moves. The space complexity is $O(m)$ because we store all obstacles in a set.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The robot only moves right or down, so we can try all possible moves in a single pass.
- Detailed breakdown of the approach:
  1. Initialize a `visited` set to keep track of visited cells.
  2. Initialize the current position and direction.
  3. Try all possible moves and count the number of collisions.
- Proof of optimality: This approach is optimal because we try all possible moves in a single pass.

```cpp
class Solution {
public:
    int robotSim(int n, vector<vector<int>>& obstacles) {
        set<pair<int, int>> obstacleSet;
        for (auto& obstacle : obstacles) {
            obstacleSet.insert({obstacle[0], obstacle[1]});
        }
        int ans = 0;
        int x = 0, y = 0;
        int dx = 0, dy = 1;
        for (int i = 0; i < n; i++) {
            if (obstacleSet.count({x + dx, y + dy})) {
                ans++;
            } else {
                x += dx;
                y += dy;
            }
        }
        return ans;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of moves.
> - **Space Complexity:** $O(m)$, where $m$ is the number of obstacles.
> - **Optimality proof:** This approach is optimal because we try all possible moves in a single pass.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Recursive functions, backtracking, and obstacle avoidance.
- Problem-solving patterns identified: Trying all possible paths and counting collisions.
- Optimization techniques learned: Using a set to store obstacles for efficient lookups.
- Similar problems to practice: Maze solving, pathfinding, and obstacle avoidance problems.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, not using efficient data structures.
- Edge cases to watch for: Obstacles at the starting position, obstacles at the destination.
- Performance pitfalls: Using inefficient algorithms, not optimizing for large inputs.
- Testing considerations: Test with different inputs, test with edge cases, and test for performance.