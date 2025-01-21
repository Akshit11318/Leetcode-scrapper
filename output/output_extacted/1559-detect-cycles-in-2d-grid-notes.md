## Detect Cycles in 2D Grid
**Problem Link:** https://leetcode.com/problems/detect-cycles-in-2d-grid/description

**Problem Statement:**
- Input format and constraints: The problem takes a 2D grid of characters as input and asks to detect whether there are any cycles in the grid. A cycle is defined as a sequence of characters that starts and ends with the same character, with each character being reachable from the previous one in the sequence through a path of adjacent cells.
- Expected output format: The function should return `true` if a cycle is detected, and `false` otherwise.
- Key requirements and edge cases to consider: The grid can contain any number of characters, and the function should handle cases where the grid is empty or contains only one character.
- Example test cases with explanations:
  - Example 1: `grid = [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]` should return `true` because there is a cycle of 'a's.
  - Example 2: `grid = [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]` should return `true` because there is a cycle of 'c's.
  - Example 3: `grid = [["a","b","c"],["d","e","f"],["g","h","i"]]` should return `false` because there are no cycles.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: One way to solve this problem is to use a brute force approach that checks all possible paths in the grid.
- Step-by-step breakdown of the solution:
  1. Iterate over each cell in the grid.
  2. For each cell, perform a depth-first search (DFS) to explore all possible paths.
  3. During the DFS, keep track of the characters visited and the current path.
  4. If a cycle is detected (i.e., a character is visited again and it's not the first character in the current path), return `true`.
- Why this approach comes to mind first: The brute force approach is often the simplest to understand and implement, as it involves checking all possible cases.

```cpp
class Solution {
public:
    bool containsCycle(vector<vector<char>>& grid) {
        int m = grid.size();
        if (m == 0) return false;
        int n = grid[0].size();
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (dfs(grid, i, j, -1, -1, grid[i][j])) {
                    return true;
                }
            }
        }
        
        return false;
    }
    
    bool dfs(vector<vector<char>>& grid, int i, int j, int pi, int pj, char c) {
        int m = grid.size();
        int n = grid[0].size();
        
        if (i < 0 || i >= m || j < 0 || j >= n || grid[i][j] != c) {
            return false;
        }
        
        if (i == pi && j == pj && (i != -1 || j != -1)) {
            return true;
        }
        
        char temp = grid[i][j];
        grid[i][j] = '#';
        
        bool found = dfs(grid, i - 1, j, i, j, c) || 
                      dfs(grid, i + 1, j, i, j, c) || 
                      dfs(grid, i, j - 1, i, j, c) || 
                      dfs(grid, i, j + 1, i, j, c);
        
        grid[i][j] = temp;
        
        return found;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n \cdot 4^{m \cdot n})$ where $m$ and $n$ are the dimensions of the grid. This is because in the worst case, we might have to explore all possible paths from each cell.
> - **Space Complexity:** $O(m \cdot n)$ for the recursive call stack.
> - **Why these complexities occur:** The time complexity is high due to the brute force nature of the approach, which checks all possible paths. The space complexity is due to the recursive call stack.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of using a brute force approach, we can use a more efficient algorithm that keeps track of the length of the path and the characters visited.
- Detailed breakdown of the approach:
  1. Iterate over each cell in the grid.
  2. For each cell, perform a DFS to explore all possible paths.
  3. During the DFS, keep track of the characters visited and the current path length.
  4. If a cycle is detected (i.e., a character is visited again and the path length is greater than 2), return `true`.
- Proof of optimality: This approach is optimal because it only explores each cell once and keeps track of the minimum path length required to detect a cycle.

```cpp
class Solution {
public:
    bool containsCycle(vector<vector<char>>& grid) {
        int m = grid.size();
        if (m == 0) return false;
        int n = grid[0].size();
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (dfs(grid, i, j, -1, -1, grid[i][j], 1)) {
                    return true;
                }
            }
        }
        
        return false;
    }
    
    bool dfs(vector<vector<char>>& grid, int i, int j, int pi, int pj, char c, int len) {
        int m = grid.size();
        int n = grid[0].size();
        
        if (i < 0 || i >= m || j < 0 || j >= n || grid[i][j] != c) {
            return false;
        }
        
        if (i == pi && j == pj && len > 2) {
            return true;
        }
        
        char temp = grid[i][j];
        grid[i][j] = '#';
        
        bool found = dfs(grid, i - 1, j, i, j, c, len + 1) || 
                      dfs(grid, i + 1, j, i, j, c, len + 1) || 
                      dfs(grid, i, j - 1, i, j, c, len + 1) || 
                      dfs(grid, i, j + 1, i, j, c, len + 1);
        
        grid[i][j] = temp;
        
        return found;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$ where $m$ and $n$ are the dimensions of the grid. This is because we only visit each cell once.
> - **Space Complexity:** $O(m \cdot n)$ for the recursive call stack.
> - **Optimality proof:** This approach is optimal because it only explores each cell once and keeps track of the minimum path length required to detect a cycle.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: DFS, path length tracking, and cycle detection.
- Problem-solving patterns identified: Using a more efficient algorithm to reduce time complexity.
- Optimization techniques learned: Keeping track of the minimum path length required to detect a cycle.
- Similar problems to practice: Other graph traversal problems, such as finding the shortest path or detecting connected components.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for out-of-bounds conditions or not keeping track of the path length.
- Edge cases to watch for: Empty grid or grid with only one character.
- Performance pitfalls: Using a brute force approach that checks all possible paths.
- Testing considerations: Testing with different grid sizes and characters to ensure the algorithm works correctly.