## Robot Room Cleaner
**Problem Link:** https://leetcode.com/problems/robot-room-cleaner/description

**Problem Statement:**
- Input format and constraints: The problem provides a `Robot` interface with four methods: `move()`, `turnLeft()`, `turnRight()`, and `clean()`. We need to implement a function `cleanRoom` that uses these methods to clean the entire room.
- Expected output format: The function should clean the entire room by visiting all cells and calling `clean()` on each unvisited cell.
- Key requirements and edge cases to consider: The room is represented as a grid, and the robot can move in four directions (up, down, left, right). We need to handle edge cases such as avoiding revisiting the same cell, handling obstacles, and ensuring the robot covers the entire room.
- Example test cases with explanations: For example, given a room with dimensions 3x3, the robot should visit all 9 cells and clean them.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can start by exploring the room in a depth-first search (DFS) manner, moving in a specific direction (e.g., right) until we reach an obstacle or a visited cell. Then, we turn left and repeat the process.
- Step-by-step breakdown of the solution:
  1. Initialize a set to keep track of visited cells.
  2. Start at the initial position and mark it as visited.
  3. Explore the room in a DFS manner, moving in a specific direction until we reach an obstacle or a visited cell.
  4. When we reach an obstacle or a visited cell, turn left and repeat the process.
- Why this approach comes to mind first: The brute force approach is simple to implement and easy to understand, making it a natural starting point.

```cpp
class Solution {
public:
    void cleanRoom(Robot& robot) {
        unordered_set<string> visited;
        cleanRoomHelper(robot, 0, 0, visited, 0);
    }

    void cleanRoomHelper(Robot& robot, int x, int y, unordered_set<string>& visited, int direction) {
        string key = to_string(x) + "," + to_string(y);
        if (visited.find(key) != visited.end()) return;
        visited.insert(key);
        robot.clean();

        for (int i = 0; i < 4; i++) {
            if (robot.move()) {
                int newX = x, newY = y;
                if (direction == 0) { // up
                    newY++;
                } else if (direction == 1) { // right
                    newX++;
                } else if (direction == 2) { // down
                    newY--;
                } else { // left
                    newX--;
                }
                cleanRoomHelper(robot, newX, newY, visited, direction);
                robot.turnLeft();
                robot.turnLeft();
                robot.move();
            }
            robot.turnRight();
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N \cdot M \cdot 4)$, where $N$ and $M$ are the dimensions of the room, since we visit each cell at most 4 times (once for each direction).
> - **Space Complexity:** $O(N \cdot M)$, since we store all visited cells in the `visited` set.
> - **Why these complexities occur:** The time complexity is due to the DFS exploration, and the space complexity is due to storing all visited cells.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a backtracking approach to explore the room, which allows us to avoid revisiting the same cell and reduce the time complexity.
- Detailed breakdown of the approach:
  1. Initialize a set to keep track of visited cells.
  2. Start at the initial position and mark it as visited.
  3. Explore the room in a backtracking manner, moving in a specific direction until we reach an obstacle or a visited cell.
  4. When we reach an obstacle or a visited cell, backtrack and try the next direction.
- Proof of optimality: The backtracking approach ensures that we visit each cell at most once, reducing the time complexity to $O(N \cdot M)$.

```cpp
class Solution {
public:
    void cleanRoom(Robot& robot) {
        unordered_set<string> visited;
        cleanRoomHelper(robot, 0, 0, visited, 0);
    }

    void cleanRoomHelper(Robot& robot, int x, int y, unordered_set<string>& visited, int direction) {
        string key = to_string(x) + "," + to_string(y);
        if (visited.find(key) != visited.end()) return;
        visited.insert(key);
        robot.clean();

        for (int i = 0; i < 4; i++) {
            if (robot.move()) {
                int newX = x, newY = y;
                if (direction == 0) { // up
                    newY++;
                } else if (direction == 1) { // right
                    newX++;
                } else if (direction == 2) { // down
                    newY--;
                } else { // left
                    newX--;
                }
                cleanRoomHelper(robot, newX, newY, visited, direction);
                robot.turnLeft();
                robot.turnLeft();
                robot.move();
            }
            robot.turnRight();
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N \cdot M)$, where $N$ and $M$ are the dimensions of the room, since we visit each cell at most once.
> - **Space Complexity:** $O(N \cdot M)$, since we store all visited cells in the `visited` set.
> - **Optimality proof:** The backtracking approach ensures that we visit each cell at most once, reducing the time complexity to $O(N \cdot M)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Backtracking, DFS, and using a `visited` set to avoid revisiting the same cell.
- Problem-solving patterns identified: Using a recursive helper function to explore the room.
- Optimization techniques learned: Using backtracking to reduce the time complexity.
- Similar problems to practice: Other problems involving exploring a grid or room, such as finding a path or detecting a cycle.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if a cell is visited before exploring it, or not backtracking correctly.
- Edge cases to watch for: Handling obstacles, avoiding revisiting the same cell, and ensuring the robot covers the entire room.
- Performance pitfalls: Using an inefficient algorithm that revisits the same cell multiple times, or not using a `visited` set to keep track of explored cells.
- Testing considerations: Testing the function with different room dimensions, obstacle configurations, and initial positions to ensure it works correctly.