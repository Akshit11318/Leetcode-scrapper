## Cat and Mouse II
**Problem Link:** https://leetcode.com/problems/cat-and-mouse-ii/description

**Problem Statement:**
- Input format and constraints: The problem is played on an $n \times n$ grid, where the cat starts at the top-left corner (0,0) and the mouse starts at the bottom-right corner (n-1,n-1). The cat and the mouse move in turns. The cat can move up, down, left, or right, while the mouse can move up, down, left, or right, and also stay in place.
- Expected output format: Determine whether the cat can catch the mouse.
- Key requirements and edge cases to consider: The cat and the mouse can only move to an empty cell. If the cat and the mouse are in the same cell, the cat catches the mouse. If the mouse reaches the top-left corner, the mouse escapes.
- Example test cases with explanations: 
    - For a 3x3 grid, the cat can catch the mouse.
    - For a 4x4 grid, the cat cannot catch the mouse.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves simulating all possible moves of the cat and the mouse.
- Step-by-step breakdown of the solution:
    1. Initialize the positions of the cat and the mouse.
    2. For each possible move of the cat, simulate all possible moves of the mouse.
    3. Check if the cat can catch the mouse in the current position.
    4. If the cat cannot catch the mouse, update the positions of the cat and the mouse.
- Why this approach comes to mind first: It is a straightforward approach that involves simulating all possible scenarios.

```cpp
#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    bool canMouseWin(vector<vector<char>>& grid, int catJump, int mouseJump) {
        int n = grid.size();
        int m = grid[0].size();
        
        // Initialize the positions of the cat and the mouse
        int catX = 0, catY = 0;
        int mouseX = n - 1, mouseY = m - 1;
        
        // Simulate all possible moves of the cat and the mouse
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == 'C') {
                    catX = i;
                    catY = j;
                } else if (grid[i][j] == 'M') {
                    mouseX = i;
                    mouseY = j;
                }
            }
        }
        
        // Simulate all possible moves
        return dfs(grid, catX, catY, mouseX, mouseY, catJump, mouseJump);
    }
    
    bool dfs(vector<vector<char>>& grid, int catX, int catY, int mouseX, int mouseY, int catJump, int mouseJump) {
        int n = grid.size();
        int m = grid[0].size();
        
        // Check if the cat can catch the mouse
        if (catX == mouseX && catY == mouseY) {
            return false;
        }
        
        // Check if the mouse has reached the top-left corner
        if (mouseX == 0 && mouseY == 0) {
            return true;
        }
        
        // Simulate all possible moves of the cat
        for (int dx = -catJump; dx <= catJump; dx++) {
            for (int dy = -catJump; dy <= catJump; dy++) {
                int newCatX = catX + dx;
                int newCatY = catY + dy;
                
                // Check if the new position is valid
                if (newCatX >= 0 && newCatX < n && newCatY >= 0 && newCatY < m && grid[newCatX][newCatY] != 'F') {
                    // Simulate all possible moves of the mouse
                    for (int mdx = -mouseJump; mdx <= mouseJump; mdx++) {
                        for (int mdy = -mouseJump; mdy <= mouseJump; mdy++) {
                            int newMouseX = mouseX + mdx;
                            int newMouseY = mouseY + mdy;
                            
                            // Check if the new position is valid
                            if (newMouseX >= 0 && newMouseX < n && newMouseY >= 0 && newMouseY < m && grid[newMouseX][newMouseY] != 'F') {
                                // Recursively simulate the next move
                                if (!dfs(grid, newCatX, newCatY, newMouseX, newMouseY, catJump, mouseJump)) {
                                    return true;
                                }
                            }
                        }
                    }
                }
            }
        }
        
        // If the cat cannot catch the mouse, return false
        return false;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot m^2 \cdot (catJump + mouseJump)^2)$
> - **Space Complexity:** $O(n^2 \cdot m^2)$
> - **Why these complexities occur:** The brute force approach involves simulating all possible moves of the cat and the mouse, which leads to an exponential time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution involves using a breadth-first search (BFS) algorithm to simulate the moves of the cat and the mouse.
- Detailed breakdown of the approach:
    1. Initialize the positions of the cat and the mouse.
    2. Use a BFS algorithm to simulate all possible moves of the cat and the mouse.
    3. Check if the cat can catch the mouse in the current position.
- Why further optimization is impossible: The BFS algorithm is the most efficient way to simulate all possible moves of the cat and the mouse.

```cpp
#include <vector>
#include <queue>
#include <iostream>

using namespace std;

class Solution {
public:
    bool canMouseWin(vector<vector<char>>& grid, int catJump, int mouseJump) {
        int n = grid.size();
        int m = grid[0].size();
        
        // Initialize the positions of the cat and the mouse
        int catX = 0, catY = 0;
        int mouseX = n - 1, mouseY = m - 1;
        
        // Initialize the queue for BFS
        queue<vector<int>> q;
        q.push({catX, catY, mouseX, mouseY});
        
        // Initialize the set to keep track of visited positions
        set<vector<int>> visited;
        visited.insert({catX, catY, mouseX, mouseY});
        
        // Perform BFS
        while (!q.empty()) {
            vector<int> state = q.front();
            q.pop();
            
            catX = state[0];
            catY = state[1];
            mouseX = state[2];
            mouseY = state[3];
            
            // Check if the cat can catch the mouse
            if (catX == mouseX && catY == mouseY) {
                return false;
            }
            
            // Check if the mouse has reached the top-left corner
            if (mouseX == 0 && mouseY == 0) {
                return true;
            }
            
            // Simulate all possible moves of the cat
            for (int dx = -catJump; dx <= catJump; dx++) {
                for (int dy = -catJump; dy <= catJump; dy++) {
                    int newCatX = catX + dx;
                    int newCatY = catY + dy;
                    
                    // Check if the new position is valid
                    if (newCatX >= 0 && newCatX < n && newCatY >= 0 && newCatY < m && grid[newCatX][newCatY] != 'F') {
                        // Simulate all possible moves of the mouse
                        for (int mdx = -mouseJump; mdx <= mouseJump; mdx++) {
                            for (int mdy = -mouseJump; mdy <= mouseJump; mdy++) {
                                int newMouseX = mouseX + mdx;
                                int newMouseY = mouseY + mdy;
                                
                                // Check if the new position is valid
                                if (newMouseX >= 0 && newMouseX < n && newMouseY >= 0 && newMouseY < m && grid[newMouseX][newMouseY] != 'F') {
                                    // Check if the new position has been visited
                                    vector<int> newState = {newCatX, newCatY, newMouseX, newMouseY};
                                    if (visited.find(newState) == visited.end()) {
                                        q.push(newState);
                                        visited.insert(newState);
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        
        // If the cat cannot catch the mouse, return false
        return false;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot m^2 \cdot (catJump + mouseJump)^2)$
> - **Space Complexity:** $O(n^2 \cdot m^2)$
> - **Optimality proof:** The BFS algorithm is the most efficient way to simulate all possible moves of the cat and the mouse, as it explores all possible positions in the grid.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: BFS algorithm, simulation of all possible moves.
- Problem-solving patterns identified: Using a BFS algorithm to simulate all possible moves.
- Optimization techniques learned: Using a set to keep track of visited positions.
- Similar problems to practice: Other problems that involve simulating all possible moves, such as the "Escape from the Maze" problem.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if a position has been visited before exploring it.
- Edge cases to watch for: The cat and the mouse being in the same position, the mouse reaching the top-left corner.
- Performance pitfalls: Not using a set to keep track of visited positions, which can lead to exponential time complexity.
- Testing considerations: Testing the algorithm with different grid sizes, cat and mouse jump values, and obstacle positions.