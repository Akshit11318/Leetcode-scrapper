## Walking Robot Simulation

**Problem Link:** https://leetcode.com/problems/walking-robot-simulation/description

**Problem Statement:**
- Input format: An integer array `commands` and an integer array `obstacles`.
- Constraints: `1 <= commands.length <= 10^4`, `0 <= commands[i] <= 10^4`, `0 <= obstacles.length <= 10^4`, `1 <= obstacles[i] <= 10^9`.
- Expected output format: The number of obstacles the robot collided with.
- Key requirements and edge cases to consider:
  - The robot starts at the origin (0, 0) facing north.
  - The robot only moves forward or backward.
  - The robot can turn left or right by 90 degrees.
  - If the robot encounters an obstacle, it stops and does not move further.
- Example test cases with explanations:
  - `commands = [4,-1,-1,3]`, `obstacles = [2]`: The robot moves 4 steps forward, then turns right, then turns right again, then moves 3 steps forward. The robot collides with the obstacle at position (2, 0).
  - `commands = [4,-1,-1,3,-2,-3,0,4,-2,-1,-1,2,-4,-1,-1,-1,0,1,-1,-1,-1,2,-4,-3,-3,0,3,-2,-3,-1,0,1,-4,-2,0,0,1,1,0,-4,-1,-2,0]`, `obstacles = [3,2,0,4,1]`: The robot moves according to the commands and collides with some obstacles.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Simulate the robot's movements step by step, checking for collisions with obstacles at each step.
- Step-by-step breakdown of the solution:
  1. Initialize the robot's position and direction.
  2. Iterate through the `commands` array.
  3. For each command, update the robot's position and direction accordingly.
  4. Check if the robot has collided with an obstacle.
  5. If a collision is detected, increment the collision counter.
- Why this approach comes to mind first: It is a straightforward simulation of the robot's movements.

```cpp
int robotSim(vector<int>& commands, vector<int>& obstacles) {
    int x = 0, y = 0; // initial position
    int dx = 0, dy = 1; // initial direction (north)
    set<pair<int, int>> obstacleSet; // set of obstacles for efficient lookup
    for (int obstacle : obstacles) {
        obstacleSet.insert({obstacle / 100, obstacle % 100});
    }
    int collisionCount = 0; // count of collisions

    for (int command : commands) {
        if (command == -2) { // turn left
            int temp = dx;
            dx = -dy;
            dy = temp;
        } else if (command == -1) { // turn right
            int temp = dx;
            dx = dy;
            dy = -temp;
        } else { // move forward
            for (int i = 1; i <= command; i++) {
                int newX = x + dx;
                int newY = y + dy;
                if (obstacleSet.count({newX, newY})) {
                    collisionCount++;
                    break; // stop moving if collision detected
                }
                x = newX;
                y = newY;
            }
        }
    }
    return collisionCount;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the length of the `commands` array and $m$ is the maximum number of steps in a single command.
> - **Space Complexity:** $O(o)$, where $o$ is the number of obstacles.
> - **Why these complexities occur:** The time complexity is due to the simulation of the robot's movements, and the space complexity is due to the storage of obstacles in a set.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a set to store the obstacles for efficient lookup, and only update the robot's position when a command is executed.
- Detailed breakdown of the approach:
  1. Initialize the robot's position and direction.
  2. Create a set of obstacles for efficient lookup.
  3. Iterate through the `commands` array.
  4. For each command, update the robot's position and direction accordingly.
  5. Check if the robot has collided with an obstacle.
  6. If a collision is detected, increment the collision counter.
- Proof of optimality: This approach has the optimal time complexity because it only iterates through the `commands` array once and uses a set for efficient obstacle lookup.

```cpp
int robotSim(vector<int>& commands, vector<int>& obstacles) {
    int x = 0, y = 0; // initial position
    int dx = 0, dy = 1; // initial direction (north)
    set<pair<int, int>> obstacleSet; // set of obstacles for efficient lookup
    for (int obstacle : obstacles) {
        obstacleSet.insert({obstacle / 100, obstacle % 100});
    }
    int collisionCount = 0; // count of collisions
    int maxDistance = 0; // maximum distance traveled in any direction

    for (int command : commands) {
        if (command == -2) { // turn left
            int temp = dx;
            dx = -dy;
            dy = temp;
        } else if (command == -1) { // turn right
            int temp = dx;
            dx = dy;
            dy = -temp;
        } else { // move forward
            for (int i = 1; i <= command; i++) {
                int newX = x + dx;
                int newY = y + dy;
                if (obstacleSet.count({newX, newY})) {
                    collisionCount++;
                    break; // stop moving if collision detected
                }
                x = newX;
                y = newY;
                maxDistance = max(maxDistance, max(abs(x), abs(y)));
            }
        }
    }
    return maxDistance;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the length of the `commands` array and $m$ is the maximum number of steps in a single command.
> - **Space Complexity:** $O(o)$, where $o$ is the number of obstacles.
> - **Optimality proof:** This approach has the optimal time complexity because it only iterates through the `commands` array once and uses a set for efficient obstacle lookup.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Simulation, set data structure, and efficient obstacle lookup.
- Problem-solving patterns identified: Breaking down complex problems into simpler steps and using data structures to improve efficiency.
- Optimization techniques learned: Using sets for efficient lookup and only updating the robot's position when necessary.
- Similar problems to practice: Other simulation-based problems, such as robot navigation or game simulations.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for collisions correctly or not updating the robot's position correctly.
- Edge cases to watch for: Handling commands that cause the robot to turn or move in invalid directions.
- Performance pitfalls: Using inefficient data structures or algorithms, such as iterating through the obstacles array for each command.
- Testing considerations: Testing the solution with different inputs and edge cases to ensure correctness and efficiency.