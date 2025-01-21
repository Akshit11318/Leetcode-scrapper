## Minimum Knight Moves

**Problem Link:** https://leetcode.com/problems/minimum-knight-moves/description

**Problem Statement:**
- Input format: The input will be two integers `x` and `y`, which represent the coordinates of the target position.
- Constraints: `-100 <= x, y <= 100`
- Expected output format: The minimum number of moves required for the knight to reach the target position.
- Key requirements and edge cases to consider: The knight moves in an L-shape (two squares in one direction, then one square to the side), and we need to find the shortest path to the target position.
- Example test cases with explanations: 
    - Input: `x = 2, y = 1`
    - Output: `1`
    - Explanation: The knight can move from `(0, 0)` to `(2, 1)` in one move.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can use a recursive approach to try all possible moves and find the shortest path.
- Step-by-step breakdown of the solution: 
    1. Define a recursive function that takes the current position and the target position as input.
    2. If the current position is the target position, return 0.
    3. Otherwise, try all possible moves from the current position and recursively call the function for each move.
    4. Return the minimum number of moves required to reach the target position.
- Why this approach comes to mind first: It is a straightforward approach that tries all possible solutions.

```cpp
class Solution {
public:
    int minKnightMoves(int x, int y) {
        // Define the possible moves of the knight
        int dx[] = {-2, -1, 1, 2, -2, -1, 1, 2};
        int dy[] = {-1, -2, -2, -1, 1, 2, 2, 1};
        
        // Create a queue for BFS and add the initial position
        queue<pair<int, int>> q;
        q.push({0, 0});
        
        // Create a set to store visited positions
        set<pair<int, int>> visited;
        visited.insert({0, 0});
        
        int moves = 0;
        while (!q.empty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                auto [currX, currY] = q.front();
                q.pop();
                
                // If the current position is the target position, return the number of moves
                if (currX == abs(x) && currY == abs(y)) {
                    return moves;
                }
                
                // Try all possible moves from the current position
                for (int j = 0; j < 8; j++) {
                    int newX = currX + dx[j];
                    int newY = currY + dy[j];
                    
                    // If the new position is not visited and is within the bounds, add it to the queue and mark it as visited
                    if (!visited.count({newX, newY}) && newX >= -100 && newX <= 100 && newY >= -100 && newY <= 100) {
                        q.push({newX, newY});
                        visited.insert({newX, newY});
                    }
                }
            }
            moves++;
        }
        return -1; // If the target position is not reachable
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(8^d)$, where $d$ is the number of moves required to reach the target position. This is because in the worst case, we try all possible moves from each position.
> - **Space Complexity:** $O(8^d)$, because we store all visited positions in the set.
> - **Why these complexities occur:** The brute force approach tries all possible solutions, which leads to exponential time and space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a BFS approach to find the shortest path to the target position. This is because the knight's moves are symmetric, and we can explore the positions in a level-order manner.
- Detailed breakdown of the approach: 
    1. Create a queue to store positions to be visited.
    2. Add the initial position to the queue.
    3. Create a set to store visited positions.
    4. While the queue is not empty, dequeue a position and try all possible moves from it.
    5. If a new position is not visited and is within the bounds, add it to the queue and mark it as visited.
    6. Repeat this process until we reach the target position or the queue is empty.
- Proof of optimality: This approach is optimal because it explores the positions in a level-order manner, ensuring that we find the shortest path to the target position.

```cpp
class Solution {
public:
    int minKnightMoves(int x, int y) {
        // Define the possible moves of the knight
        int dx[] = {-2, -1, 1, 2, -2, -1, 1, 2};
        int dy[] = {-1, -2, -2, -1, 1, 2, 2, 1};
        
        // Create a queue for BFS and add the initial position
        queue<pair<int, int>> q;
        q.push({0, 0});
        
        // Create a set to store visited positions
        set<pair<int, int>> visited;
        visited.insert({0, 0});
        
        int moves = 0;
        while (!q.empty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                auto [currX, currY] = q.front();
                q.pop();
                
                // If the current position is the target position, return the number of moves
                if (currX == abs(x) && currY == abs(y)) {
                    return moves;
                }
                
                // Try all possible moves from the current position
                for (int j = 0; j < 8; j++) {
                    int newX = currX + dx[j];
                    int newY = currY + dy[j];
                    
                    // If the new position is not visited and is within the bounds, add it to the queue and mark it as visited
                    if (!visited.count({newX, newY}) && newX >= -100 && newX <= 100 && newY >= -100 && newY <= 100) {
                        q.push({newX, newY});
                        visited.insert({newX, newY});
                    }
                }
            }
            moves++;
        }
        return -1; // If the target position is not reachable
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(|x| + |y|)$, where $x$ and $y$ are the coordinates of the target position. This is because in the worst case, we explore all positions up to the target position.
> - **Space Complexity:** $O(|x| + |y|)$, because we store all visited positions in the set.
> - **Optimality proof:** This approach is optimal because it explores the positions in a level-order manner, ensuring that we find the shortest path to the target position.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: BFS, level-order traversal, and symmetric moves.
- Problem-solving patterns identified: Using a queue to store positions to be visited and a set to store visited positions.
- Optimization techniques learned: Exploring positions in a level-order manner to find the shortest path.
- Similar problems to practice: Other graph traversal problems, such as finding the shortest path in a grid or a graph.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for visited positions, not handling edge cases, and not using a queue to store positions to be visited.
- Edge cases to watch for: Positions outside the bounds, positions that are not reachable, and positions that are already visited.
- Performance pitfalls: Using a recursive approach instead of an iterative approach, not using a set to store visited positions, and not exploring positions in a level-order manner.
- Testing considerations: Test the solution with different input values, including edge cases, to ensure that it works correctly and efficiently.