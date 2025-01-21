## Race Car
**Problem Link:** https://leetcode.com/problems/race-car/description

**Problem Statement:**
- Input: An integer `target` representing the target position.
- Output: The minimum number of instructions required to reach the target position.
- Key requirements and edge cases to consider:
  - The car can only move in one direction (forward) with a constant acceleration.
  - The car can only change its speed by using an instruction to accelerate or reverse.
  - The car starts at position 0 with a speed of 1.
- Example test cases with explanations:
  - Input: `target = 3`, Output: `2`, Explanation: The car can reach the target position in two instructions by accelerating to position 2 and then reversing to position 3.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of instructions to reach the target position.
- Step-by-step breakdown of the solution:
  1. Initialize a queue with the initial state of the car (position 0, speed 1).
  2. For each state in the queue, try all possible instructions (accelerate, reverse).
  3. For each new state, check if it has reached the target position. If so, return the number of instructions.
  4. If not, add the new state to the queue and repeat the process.
- Why this approach comes to mind first: It is a straightforward and intuitive approach to try all possible combinations of instructions.

```cpp
#include <queue>
#include <unordered_set>

class Solution {
public:
    int racecar(int target) {
        std::queue<std::pair<int, int>> q; // (position, speed)
        std::unordered_set<std::pair<int, int>> visited;
        q.push({0, 1});
        int steps = 0;
        while (!q.empty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                auto [pos, speed] = q.front();
                q.pop();
                if (pos == target) return steps;
                if (visited.find({pos, speed}) != visited.end()) continue;
                visited.insert({pos, speed});
                // Accelerate
                int new_pos = pos + speed;
                int new_speed = speed * 2;
                if (new_pos <= 2 * target) {
                    q.push({new_pos, new_speed});
                }
                // Reverse
                if (speed > 0) {
                    new_speed = -1;
                } else {
                    new_speed = 1;
                }
                q.push({pos, new_speed});
            }
            steps++;
        }
        return -1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{target})$, where each state can have two possible next states (accelerate or reverse).
> - **Space Complexity:** $O(2^{target})$, where we need to store all possible states in the queue.
> - **Why these complexities occur:** The brute force approach tries all possible combinations of instructions, resulting in exponential time and space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a breadth-first search (BFS) algorithm with a more efficient state representation.
- Detailed breakdown of the approach:
  1. Use a queue to store states in the form of `(position, speed, steps)`.
  2. For each state, try two possible instructions: accelerate and reverse.
  3. For each new state, check if it has reached the target position. If so, return the number of steps.
  4. If not, add the new state to the queue and repeat the process.
- Proof of optimality: The BFS algorithm ensures that we find the shortest path to the target position.

```cpp
#include <queue>
#include <unordered_set>

class Solution {
public:
    int racecar(int target) {
        std::queue<std::tuple<int, int, int>> q; // (position, speed, steps)
        std::unordered_set<std::pair<int, int>> visited;
        q.push({0, 1, 0});
        while (!q.empty()) {
            auto [pos, speed, steps] = q.front();
            q.pop();
            if (pos == target) return steps;
            if (visited.find({pos, speed}) != visited.end()) continue;
            visited.insert({pos, speed});
            // Accelerate
            int new_pos = pos + speed;
            int new_speed = speed * 2;
            if (new_pos <= 2 * target) {
                q.push({new_pos, new_speed, steps + 1});
            }
            // Reverse
            int new_speed_rev = (speed > 0) ? -1 : 1;
            q.push({pos, new_speed_rev, steps + 1});
        }
        return -1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(target \log target)$, where we need to try all possible speeds and positions.
> - **Space Complexity:** $O(target \log target)$, where we need to store all possible states in the queue.
> - **Optimality proof:** The BFS algorithm ensures that we find the shortest path to the target position, and the state representation is efficient enough to avoid redundant calculations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: BFS, state representation, and optimality proof.
- Problem-solving patterns identified: Using a more efficient state representation to reduce the search space.
- Optimization techniques learned: Using a queue to store states and avoiding redundant calculations.
- Similar problems to practice: Other problems that involve finding the shortest path in a graph or network.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases correctly, such as when the target position is 0.
- Performance pitfalls: Not using an efficient state representation, resulting in exponential time and space complexity.
- Testing considerations: Testing the algorithm with different target positions and speeds to ensure correctness and optimality.