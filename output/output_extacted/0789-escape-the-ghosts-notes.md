## Escape the Ghosts
**Problem Link:** https://leetcode.com/problems/escape-the-ghosts/description

**Problem Statement:**
- Input format: You are given a 2D integer array `ghosts` where each `ghosts[i] = [xi, yi]` represents the position of a ghost. You are also given a 2D integer array `target = [x, y]` representing the position of the target. It is guaranteed that the target position is not a position occupied by a ghost.
- Expected output format: Return `true` if it is possible to escape the ghosts, and `false` otherwise.
- Key requirements and edge cases to consider: The game takes place on a grid where the player can move in any of the four directions (up, down, left, right) and the ghosts can move in any of the four directions as well.
- Example test cases with explanations: 
    - Input: `ghosts = [[1,0],[0,3]]`, `target = [0,1]`
    Output: `true`
    Explanation: The player can move from `(0,1)` to `(0,0)` and then to `(1,0)` and escape the ghosts.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To determine if it's possible to escape the ghosts, we can simulate the movement of the player and the ghosts. We can try all possible movements for the player and check if the ghosts can catch up to the player.
- Step-by-step breakdown of the solution: 
    1. Initialize the player's position to `(0,0)`.
    2. For each possible movement of the player (up, down, left, right), calculate the Manhattan distance between the player's new position and the target position.
    3. For each ghost, calculate the Manhattan distance between the ghost's position and the player's new position.
    4. If the ghost's distance to the player is less than or equal to the player's distance to the target, the ghost can catch up to the player, so return `false`.
    5. If the player reaches the target position without being caught by a ghost, return `true`.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it has an exponential time complexity due to the recursive nature of simulating all possible movements.

```cpp
class Solution {
public:
    bool escapeGhosts(vector<vector<int>>& ghosts, vector<int>& target) {
        int playerDistance = abs(target[0]) + abs(target[1]);
        for (auto& ghost : ghosts) {
            int ghostDistance = abs(ghost[0] - target[0]) + abs(ghost[1] - target[1]);
            if (ghostDistance <= playerDistance) return false;
        }
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of ghosts. This is because we are iterating over each ghost once.
> - **Space Complexity:** $O(1)$ as we are not using any extra space that scales with input size.
> - **Why these complexities occur:** The time complexity is linear because we are only iterating over the ghosts once, and the space complexity is constant because we are not using any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The key insight here is that the player can escape the ghosts if and only if the player's Manhattan distance to the target is less than the Manhattan distance from any ghost to the target.
- Detailed breakdown of the approach: We can simply calculate the Manhattan distance from the player to the target and compare it with the Manhattan distance from each ghost to the target.
- Proof of optimality: This approach is optimal because it has a linear time complexity and uses constant space, which is the best we can achieve for this problem.
- Why further optimization is impossible: Further optimization is impossible because we must at least iterate over the ghosts once to calculate their distances to the target.

```cpp
class Solution {
public:
    bool escapeGhosts(vector<vector<int>>& ghosts, vector<int>& target) {
        int playerDistance = abs(target[0]) + abs(target[1]);
        for (auto& ghost : ghosts) {
            int ghostDistance = abs(ghost[0] - target[0]) + abs(ghost[1] - target[1]);
            if (ghostDistance <= playerDistance) return false;
        }
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of ghosts. This is because we are iterating over each ghost once.
> - **Space Complexity:** $O(1)$ as we are not using any extra space that scales with input size.
> - **Optimality proof:** This approach is optimal because it has a linear time complexity and uses constant space, which is the best we can achieve for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Manhattan distance calculation and comparison.
- Problem-solving patterns identified: Using a simple and efficient approach to solve the problem.
- Optimization techniques learned: Avoiding unnecessary calculations and using constant space.
- Similar problems to practice: Other problems that involve calculating distances and comparing them.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as an empty `ghosts` array.
- Edge cases to watch for: An empty `ghosts` array, or a `target` position that is not reachable.
- Performance pitfalls: Using an exponential time complexity approach, such as simulating all possible movements.
- Testing considerations: Testing the function with different inputs, such as an empty `ghosts` array, or a `target` position that is not reachable.