## Walking Robot Simulation II

**Problem Link:** https://leetcode.com/problems/walking-robot-simulation-ii/description

**Problem Statement:**
- Input format: An array of commands where each command is one of the following: `start`, `move forward`, `move backward`, or `turn left/right`.
- Constraints: The robot is initially at the origin (0, 0) facing north.
- Expected output format: Return the final position and direction of the robot.
- Key requirements and edge cases to consider: The robot moves in a 2D grid and can turn left or right by 90 degrees.
- Example test cases with explanations:
  - The robot starts at the origin, moves forward, and then turns left. What is its final position and direction?
  - The robot starts at the origin, turns right, and then moves backward. What is its final position and direction?

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Simulate the robot's movements step by step, keeping track of its position and direction.
- Step-by-step breakdown of the solution:
  1. Initialize the robot's position and direction.
  2. Iterate through the commands, updating the robot's position and direction accordingly.
- Why this approach comes to mind first: It directly simulates the robot's movements, making it easy to understand and implement.

```cpp
#include <iostream>
#include <vector>
#include <string>

struct Command {
    std::string type;
    int distance;
};

struct Position {
    int x, y;
    std::string direction;
};

Position simulateRobot(std::vector<Command> commands) {
    Position position = {0, 0, "north"};
    std::vector<std::string> directions = {"north", "east", "south", "west"};

    for (auto command : commands) {
        if (command.type == "start") {
            continue;
        } else if (command.type == "move forward") {
            if (position.direction == "north") {
                position.y += command.distance;
            } else if (position.direction == "east") {
                position.x += command.distance;
            } else if (position.direction == "south") {
                position.y -= command.distance;
            } else if (position.direction == "west") {
                position.x -= command.distance;
            }
        } else if (command.type == "move backward") {
            if (position.direction == "north") {
                position.y -= command.distance;
            } else if (position.direction == "east") {
                position.x -= command.distance;
            } else if (position.direction == "south") {
                position.y += command.distance;
            } else if (position.direction == "west") {
                position.x += command.distance;
            }
        } else if (command.type == "turn left") {
            int index = std::find(directions.begin(), directions.end(), position.direction) - directions.begin();
            position.direction = directions[(index - 1 + 4) % 4];
        } else if (command.type == "turn right") {
            int index = std::find(directions.begin(), directions.end(), position.direction) - directions.begin();
            position.direction = directions[(index + 1) % 4];
        }
    }

    return position;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of commands. Each command is processed once.
> - **Space Complexity:** $O(1)$, as the space used does not grow with the input size.
> - **Why these complexities occur:** The brute force approach simulates each command once, resulting in linear time complexity. The space complexity is constant because the robot's state (position and direction) uses a fixed amount of space.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The robot's movements can be represented as changes in its position and direction. We can update these changes based on the commands.
- Detailed breakdown of the approach:
  1. Initialize the robot's position and direction.
  2. Iterate through the commands, updating the robot's position and direction accordingly.
- Proof of optimality: This approach has the same time complexity as the brute force approach but is more concise and efficient in practice.

```cpp
#include <iostream>
#include <vector>
#include <string>

struct Command {
    std::string type;
    int distance;
};

struct Position {
    int x, y;
    std::string direction;
};

Position simulateRobot(std::vector<Command> commands) {
    Position position = {0, 0, "north"};
    std::vector<std::string> directions = {"north", "east", "south", "west"};
    int dx[] = {0, 1, 0, -1};
    int dy[] = {1, 0, -1, 0};

    int index = 0;
    for (auto command : commands) {
        if (command.type == "start") {
            continue;
        } else if (command.type == "move forward") {
            position.x += dx[index] * command.distance;
            position.y += dy[index] * command.distance;
        } else if (command.type == "move backward") {
            position.x -= dx[index] * command.distance;
            position.y -= dy[index] * command.distance;
        } else if (command.type == "turn left") {
            index = (index - 1 + 4) % 4;
            position.direction = directions[index];
        } else if (command.type == "turn right") {
            index = (index + 1) % 4;
            position.direction = directions[index];
        }
    }

    return position;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of commands. Each command is processed once.
> - **Space Complexity:** $O(1)$, as the space used does not grow with the input size.
> - **Optimality proof:** The optimal approach has the same time complexity as the brute force approach but is more concise and efficient in practice.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Simulation, state updates, and command processing.
- Problem-solving patterns identified: Breaking down complex problems into simpler steps and using iteration to process commands.
- Optimization techniques learned: Using arrays to represent directions and movements, reducing code duplication.
- Similar problems to practice: Other simulation problems, such as simulating a robot in a 3D space or a robot with more complex movements.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as invalid commands or movements outside the grid.
- Edge cases to watch for: Commands that move the robot outside the grid, or commands that turn the robot in an invalid direction.
- Performance pitfalls: Using inefficient data structures or algorithms, such as using a list to represent the robot's position and direction.
- Testing considerations: Testing the robot's movements and directions, as well as edge cases and invalid commands.