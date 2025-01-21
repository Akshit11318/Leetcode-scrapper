## Number of Islands II
**Problem Link:** https://leetcode.com/problems/number-of-islands-ii/description

**Problem Statement:**
- Input format: `m` (number of rows), `n` (number of columns), and a list of `positions` where islands will appear.
- Constraints: `1 <= m, n <= 100`, `1 <= positions.length <= 10000`, `positions[i].length == 2`, and `0 <= positions[i][0] < m` and `0 <= positions[i][1] < n`.
- Expected output format: A list of integers representing the number of islands after each island appearance.
- Key requirements and edge cases to consider: Handling island merges, counting distinct islands, and updating island counts after each new island appearance.
- Example test cases with explanations:
  - Example 1: `m = 3, n = 3, positions = [[0,0],[0,1],[1,2],[2,1]]` should return `[1,1,2,3]`.
  - Example 2: `m = 3, n = 3, positions = [[0,0],[0,1],[1,2],[2,1],[1,0]]` should return `[1,1,2,3,3]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Create a grid representing the map and iterate through each position to add islands. After adding each island, perform a depth-first search (DFS) or breadth-first search (BFS) to count the number of distinct islands.
- Step-by-step breakdown of the solution:
  1. Initialize a grid with all zeros.
  2. For each position, mark the corresponding grid cell as an island (1).
  3. Perform DFS or BFS from each island to find connected islands and count them as one island.
  4. Update the island count after each new island appearance.
- Why this approach comes to mind first: It directly simulates the process of adding islands and counting them, making it an intuitive first step.

```cpp
class Solution {
public:
    vector<int> numIslands2(int m, int n, vector<vector<int>>& positions) {
        vector<vector<int>> grid(m, vector<int>(n, 0));
        vector<int> res;
        int islandCount = 0;
        
        for (auto& pos : positions) {
            int x = pos[0], y = pos[1];
            if (grid[x][y] == 0) {
                grid[x][y] = 1;
                islandCount++;
                // Perform DFS or BFS to count connected islands
                for (int dx = -1; dx <= 1; dx++) {
                    for (int dy = -1; dy <= 1; dy++) {
                        if (abs(dx) + abs(dy) == 1) {
                            int nx = x + dx, ny = y + dy;
                            if (nx >= 0 && nx < m && ny >= 0 && ny < n && grid[nx][ny] == 1) {
                                // Merge islands if they are connected
                                islandCount--;
                            }
                        }
                    }
                }
            }
            res.push_back(islandCount);
        }
        return res;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n \cdot positions.length)$ due to the nested loops for each position and the potential DFS/BFS for each island.
> - **Space Complexity:** $O(m \cdot n)$ for storing the grid.
> - **Why these complexities occur:** The brute force approach involves iterating over the entire grid for each new island, leading to high time complexity. The space complexity is due to the grid used to represent the map.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Using a union-find data structure to efficiently manage island connections and counts.
- Detailed breakdown of the approach:
  1. Initialize a union-find data structure with each cell as its own set.
  2. For each new island position, union it with its neighboring islands if they exist.
  3. Update the island count based on the number of distinct sets (islands) in the union-find data structure.
- Proof of optimality: The union-find data structure allows for $O(\alpha(n))$ time complexity for union and find operations, where $\alpha(n)$ is the inverse Ackermann function, which grows very slowly. This is much more efficient than the brute force approach, especially for large inputs.

```cpp
class UnionFind {
public:
    vector<int> parent;
    vector<int> rank;
    int count;
    
    UnionFind(int m, int n) : parent(m * n), rank(m * n, 0), count(0) {
        for (int i = 0; i < m * n; i++) {
            parent[i] = i;
        }
    }
    
    int find(int i) {
        if (parent[i] != i) {
            parent[i] = find(parent[i]);
        }
        return parent[i];
    }
    
    void unionSet(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX != rootY) {
            if (rank[rootX] < rank[rootY]) {
                parent[rootX] = rootY;
            } else if (rank[rootX] > rank[rootY]) {
                parent[rootY] = rootX;
            } else {
                parent[rootY] = rootX;
                rank[rootX]++;
            }
            count--;
        }
    }
};

class Solution {
public:
    vector<int> numIslands2(int m, int n, vector<vector<int>>& positions) {
        UnionFind uf(m, n);
        vector<int> res;
        vector<int> directions = {-n, 1, n, -1};
        
        for (auto& pos : positions) {
            int x = pos[0], y = pos[1];
            int index = x * n + y;
            uf.count++;
            for (int i = 0; i < 4; i++) {
                int nx = x + directions[i];
                int ny = y + directions[i] / n * n + directions[i] % n;
                if (nx >= 0 && nx < m && ny >= 0 && ny < n && (nx != x || ny != y)) {
                    int nIndex = nx * n + ny;
                    if (uf.parent[nIndex] != -1) {
                        uf.unionSet(index, nIndex);
                    }
                }
            }
            res.push_back(uf.count);
        }
        return res;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(positions.length \cdot \alpha(n))$ due to the union-find operations for each new island.
> - **Space Complexity:** $O(m \cdot n)$ for the union-find data structure.
> - **Optimality proof:** The use of a union-find data structure minimizes the time complexity by efficiently managing island connections and counts, making this approach optimal for large inputs.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Union-find data structure for efficient set management.
- Problem-solving patterns identified: Using the right data structure to simplify complex problems.
- Optimization techniques learned: Minimizing time complexity through efficient data structure choices.
- Similar problems to practice: Other problems involving set management, such as finding connected components in a graph.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly implementing the union-find data structure or not considering edge cases.
- Edge cases to watch for: Handling cases where new islands are added at the boundary of the grid or where islands merge.
- Performance pitfalls: Using a brute force approach for large inputs, leading to high time complexity.
- Testing considerations: Thoroughly testing the solution with various input sizes and edge cases to ensure correctness and efficiency.