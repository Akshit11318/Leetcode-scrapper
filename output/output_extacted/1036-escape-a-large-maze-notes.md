## Escape a Large Maze
**Problem Link:** https://leetcode.com/problems/escape-a-large-maze/description

**Problem Statement:**
- Input format and constraints: The problem involves a maze represented by a grid of size `m x n`, where `m` and `n` are integers. You are given the `start` position, `end` position, and a list of obstacles `blocked`. The goal is to determine if there exists a path from `start` to `end` that avoids the obstacles and does not exceed a certain distance limit.
- Expected output format: Return `true` if there is a path from `start` to `end`, and `false` otherwise.
- Key requirements and edge cases to consider: The maze has obstacles and a distance limit. The `start` and `end` positions are given, and there are blocked cells that must be avoided.
- Example test cases with explanations: 
    - Example 1: Given `start = [0,0]`, `end = [0,4]`, `blocked = [[0,1],[0,3]]`, return `false`.
    - Example 2: Given `start = [0,0]`, `end = [0,4]`, `blocked = [[0,1],[0,3],[0,2]]`, return `false`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves checking all possible paths from `start` to `end` and verifying if any of them avoid the obstacles and do not exceed the distance limit.
- Step-by-step breakdown of the solution:
    1. Generate all possible paths from `start` to `end`.
    2. For each path, check if it avoids the obstacles.
    3. If a path avoids the obstacles, check if its length does not exceed the distance limit.
- Why this approach comes to mind first: The brute force approach is straightforward and easy to understand. However, it is inefficient due to the large number of possible paths.

```cpp
#include <vector>
#include <utility>

class Solution {
public:
    bool isEscapePossible(std::vector<std::vector<int>>& blocked, std::vector<int>& source, std::vector<int>& target) {
        // Define the directions for DFS
        std::vector<std::pair<int, int>> directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        
        // Define the function to check if a position is valid
        auto isValid = [&](int x, int y) {
            return x >= 0 && x < 1e6 && y >= 0 && y < 1e6;
        };
        
        // Define the function to check if a position is blocked
        auto isBlocked = [&](int x, int y) {
            for (const auto& block : blocked) {
                if (block[0] == x && block[1] == y) {
                    return true;
                }
            }
            return false;
        };
        
        // Perform DFS from the source
        std::function<bool(int, int, int)> dfs = [&](int x, int y, int step) {
            if (step >= 200) {
                return true;
            }
            if (x == target[0] && y == target[1]) {
                return true;
            }
            for (const auto& direction : directions) {
                int newX = x + direction.first;
                int newY = y + direction.second;
                if (isValid(newX, newY) && !isBlocked(newX, newY)) {
                    if (dfs(newX, newY, step + 1)) {
                        return true;
                    }
                }
            }
            return false;
        };
        
        return dfs(source[0], source[1], 0);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(4^{200} \cdot b)$, where $b$ is the number of blocked cells. This is because in the worst case, we need to explore all possible paths of length up to 200.
> - **Space Complexity:** $O(b)$, where $b$ is the number of blocked cells. This is because we need to store the blocked cells.
> - **Why these complexities occur:** The brute force approach has high time complexity due to the large number of possible paths, and the space complexity is due to the storage of blocked cells.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The key insight is to use a breadth-first search (BFS) algorithm to explore the maze and check if there is a path from `start` to `end` that avoids the obstacles and does not exceed the distance limit.
- Detailed breakdown of the approach:
    1. Perform BFS from the `start` position and explore all neighboring cells.
    2. For each neighboring cell, check if it is valid (i.e., within the maze boundaries and not blocked).
    3. If a neighboring cell is valid, mark it as visited and add it to the queue.
    4. Repeat steps 1-3 until the queue is empty or the `end` position is reached.
- Proof of optimality: The BFS algorithm is optimal because it explores the maze level by level, ensuring that the shortest path is found first.

```cpp
#include <vector>
#include <queue>
#include <unordered_set>

class Solution {
public:
    bool isEscapePossible(std::vector<std::vector<int>>& blocked, std::vector<int>& source, std::vector<int>& target) {
        // Define the directions for BFS
        std::vector<std::pair<int, int>> directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        
        // Define the function to check if a position is valid
        auto isValid = [&](int x, int y) {
            return x >= 0 && x < 1e6 && y >= 0 && y < 1e6;
        };
        
        // Define the set to store blocked cells
        std::unordered_set<std::string> blockSet;
        for (const auto& block : blocked) {
            blockSet.insert(std::to_string(block[0]) + "," + std::to_string(block[1]));
        }
        
        // Perform BFS from the source
        std::queue<std::pair<int, int>> queue;
        std::unordered_set<std::string> visited;
        queue.push({source[0], source[1]});
        visited.insert(std::to_string(source[0]) + "," + std::to_string(source[1]));
        
        int step = 0;
        while (!queue.empty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                auto [x, y] = queue.front();
                queue.pop();
                if (x == target[0] && y == target[1]) {
                    return true;
                }
                for (const auto& direction : directions) {
                    int newX = x + direction.first;
                    int newY = y + direction.second;
                    if (isValid(newX, newY) && blockSet.find(std::to_string(newX) + "," + std::to_string(newY)) == blockSet.end() && visited.find(std::to_string(newX) + "," + std::to_string(newY)) == visited.end()) {
                        queue.push({newX, newY});
                        visited.insert(std::to_string(newX) + "," + std::to_string(newY));
                    }
                }
            }
            step++;
            if (step >= 200) {
                break;
            }
        }
        
        return false;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(b + 10^4)$, where $b$ is the number of blocked cells. This is because we need to explore at most $10^4$ cells in the maze.
> - **Space Complexity:** $O(b + 10^4)$, where $b$ is the number of blocked cells. This is because we need to store the blocked cells and the visited cells.
> - **Optimality proof:** The BFS algorithm is optimal because it explores the maze level by level, ensuring that the shortest path is found first. The time complexity is reduced by using a queue to store the cells to be visited, and the space complexity is reduced by using a set to store the visited cells.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: BFS algorithm, queue data structure, and set data structure.
- Problem-solving patterns identified: The problem can be solved by using a BFS algorithm to explore the maze and check if there is a path from `start` to `end` that avoids the obstacles and does not exceed the distance limit.
- Optimization techniques learned: The time complexity can be reduced by using a queue to store the cells to be visited, and the space complexity can be reduced by using a set to store the visited cells.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if a cell is valid before visiting it, not marking a cell as visited after visiting it, and not using a queue to store the cells to be visited.
- Edge cases to watch for: The maze boundaries, the blocked cells, and the distance limit.
- Performance pitfalls: Using a recursive function to perform BFS, not using a set to store the visited cells, and not using a queue to store the cells to be visited.
- Testing considerations: Test the function with different inputs, including edge cases, to ensure that it works correctly.