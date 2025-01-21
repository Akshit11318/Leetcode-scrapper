## Bricks Falling When Hit
**Problem Link:** https://leetcode.com/problems/bricks-falling-when-hit/description

**Problem Statement:**
- Input: A 2D grid `grid` representing a wall of bricks where `grid[i][j] = 1` means a brick is present and `grid[i][j] = 0` means no brick is present, an array `hits` representing the cells where the ball hits, and an integer `rows` and `cols` representing the number of rows and columns in the grid.
- Expected output: An array where the `i-th` element represents the number of bricks that will fall after the `i-th` hit.
- Key requirements and edge cases: The wall is initially composed of bricks, and each hit causes the bricks above it to fall. We need to consider the order of hits and the structure of the wall to determine which bricks will fall.

**Example Test Cases:**
- Input: `grid = [[1,0,0],[1,1,0],[1,1,0]]`, `hits = [[0,0],[0,2],[1,1]]`
- Output: `[2,0,0]`
- Explanation: 
  1. After the first hit at `[0,0]`, two bricks will fall because the brick at `[0,0]` and the brick above it at `[1,0]` will both fall.
  2. After the second hit at `[0,2]`, no bricks will fall because there are no bricks above the hit position.
  3. After the third hit at `[1,1]`, no bricks will fall because there are no bricks above the hit position.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: For each hit, simulate the process of bricks falling by checking which bricks above the hit position are connected to the hit brick and will fall.
- Step-by-step breakdown:
  1. Iterate over each hit in the `hits` array.
  2. For each hit, check the bricks above it to see if they are connected and will fall.
  3. If a brick is connected and will fall, remove it from the grid and continue checking the bricks above it.
- Why this approach comes to mind first: It's the most straightforward way to simulate the process of bricks falling.

```cpp
class Solution {
public:
    vector<int> hitBricks(vector<vector<int>>& grid, vector<vector<int>>& hits) {
        int rows = grid.size();
        int cols = grid[0].size();
        vector<int> result;
        
        // Iterate over each hit
        for (auto& hit : hits) {
            int x = hit[0];
            int y = hit[1];
            // Check if the brick at the hit position exists
            if (grid[x][y] == 1) {
                // Temporarily remove the brick at the hit position
                grid[x][y] = 0;
                int count = 0;
                // Check the bricks above the hit position
                for (int i = x + 1; i < rows; i++) {
                    for (int j = 0; j < cols; j++) {
                        // If a brick is connected to the hit brick and will fall, remove it and increment the count
                        if (grid[i][j] == 1 && isConnected(grid, i, j, x, y)) {
                            grid[i][j] = 0;
                            count++;
                        }
                    }
                }
                // Add the count to the result array
                result.push_back(count);
                // Restore the brick at the hit position
                grid[x][y] = 1;
            } else {
                result.push_back(0);
            }
        }
        return result;
    }
    
    // Function to check if a brick is connected to the hit brick and will fall
    bool isConnected(vector<vector<int>>& grid, int x, int y, int hitX, int hitY) {
        // Check if the brick is directly above the hit brick
        if (x == hitX + 1 && y == hitY) {
            return true;
        }
        // Check if the brick is connected to a brick that is directly above the hit brick
        for (int i = x + 1; i < grid.size(); i++) {
            for (int j = 0; j < grid[0].size(); j++) {
                if (grid[i][j] == 1 && isConnected(grid, i, j, hitX, hitY)) {
                    return true;
                }
            }
        }
        return false;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$ where $n$ is the number of rows in the grid. This is because for each hit, we are potentially checking all bricks in the grid.
> - **Space Complexity:** $O(1)$ because we are not using any additional space that scales with the input size.
> - **Why these complexities occur:** The time complexity is high because we are using a recursive function to check if a brick is connected to the hit brick and will fall. The space complexity is low because we are not using any additional data structures that scale with the input size.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight: Instead of simulating the process of bricks falling for each hit, we can simulate the process of building the wall by iterating over the hits in reverse order and checking which bricks will be connected to the ceiling after each hit.
- Detailed breakdown:
  1. Iterate over the hits in reverse order.
  2. For each hit, check if the brick at the hit position is connected to the ceiling after the previous hits.
  3. If the brick is connected, increment the count of bricks that will fall after the current hit.
- Why this is the optimal solution: This approach avoids the need to simulate the process of bricks falling for each hit, which reduces the time complexity.

```cpp
class Solution {
public:
    vector<int> hitBricks(vector<vector<int>>& grid, vector<vector<int>>& hits) {
        int rows = grid.size();
        int cols = grid[0].size();
        vector<int> result(hits.size(), 0);
        
        // Mark all the hit positions
        for (auto& hit : hits) {
            grid[hit[0]][hit[1]] = 0;
        }
        
        // Iterate over the hits in reverse order
        for (int i = hits.size() - 1; i >= 0; i--) {
            int x = hits[i][0];
            int y = hits[i][1];
            // Check if the brick at the hit position is connected to the ceiling
            if (isConnected(grid, x, y)) {
                // Count the number of bricks that will fall after the current hit
                int count = countFallenBricks(grid, x, y);
                result[i] = count;
            }
            // Restore the brick at the hit position
            grid[x][y] = 1;
        }
        return result;
    }
    
    // Function to check if a brick is connected to the ceiling
    bool isConnected(vector<vector<int>>& grid, int x, int y) {
        if (x == 0) {
            return true;
        }
        vector<pair<int, int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        for (auto& direction : directions) {
            int newX = x + direction.first;
            int newY = y + direction.second;
            if (newX >= 0 && newX < grid.size() && newY >= 0 && newY < grid[0].size() && grid[newX][newY] == 1) {
                if (isConnected(grid, newX, newY)) {
                    return true;
                }
            }
        }
        return false;
    }
    
    // Function to count the number of bricks that will fall after a hit
    int countFallenBricks(vector<vector<int>>& grid, int x, int y) {
        vector<pair<int, int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        int count = 0;
        queue<pair<int, int>> q;
        q.push({x, y});
        while (!q.empty()) {
            int currX = q.front().first;
            int currY = q.front().second;
            q.pop();
            if (currX < 0 || currX >= grid.size() || currY < 0 || currY >= grid[0].size() || grid[currX][currY] == 0) {
                continue;
            }
            count++;
            grid[currX][currY] = 0;
            for (auto& direction : directions) {
                int newX = currX + direction.first;
                int newY = currY + direction.second;
                q.push({newX, newY});
            }
        }
        return count - 1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ where $n$ is the number of rows in the grid. This is because we are iterating over the hits in reverse order and checking which bricks will be connected to the ceiling after each hit.
> - **Space Complexity:** $O(1)$ because we are not using any additional space that scales with the input size.
> - **Optimality proof:** This solution is optimal because it avoids the need to simulate the process of bricks falling for each hit, which reduces the time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Simulating the process of building the wall by iterating over the hits in reverse order.
- Problem-solving patterns identified: Avoiding the need to simulate the process of bricks falling for each hit.
- Optimization techniques learned: Using a queue to count the number of bricks that will fall after a hit.
- Similar problems to practice: Problems that involve simulating a process and optimizing it by reversing the order of operations.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if a brick is connected to the ceiling before counting the number of bricks that will fall.
- Edge cases to watch for: The case where the brick at the hit position is not connected to the ceiling.
- Performance pitfalls: Using a recursive function to check if a brick is connected to the ceiling, which can lead to a stack overflow.
- Testing considerations: Testing the solution with different input sizes and edge cases to ensure it works correctly.