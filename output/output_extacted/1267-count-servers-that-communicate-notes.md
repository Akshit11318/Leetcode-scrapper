## Count Servers That Communicate
**Problem Link:** https://leetcode.com/problems/count-servers-that-communicate/description

**Problem Statement:**
- Input format: A 2D grid `grid` where each cell can have one of two values: 0 (empty) or 1 (server).
- Constraints: The grid is not empty, and the number of rows and columns is in the range [1, 500].
- Expected output format: The number of servers that communicate with at least one other server.
- Key requirements and edge cases to consider: 
  - A server can communicate with another server if they are directly connected (horizontally or vertically).
  - A server can also communicate with another server if they are connected through a chain of servers.
- Example test cases with explanations:
  - For the grid `[[1,0],[0,1]]`, the output should be 2 because the two servers are connected.
  - For the grid `[[1,0],[1,1]]`, the output should be 3 because all three servers are connected.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: We need to check each cell in the grid to see if it's a server, and then check its neighbors to see if any of them are also servers.
- Step-by-step breakdown of the solution:
  1. Iterate over each cell in the grid.
  2. For each cell, check if it's a server (i.e., its value is 1).
  3. If it's a server, check its neighbors (up, down, left, right) to see if any of them are also servers.
  4. If a neighbor is a server, mark the current server as connected.
  5. Finally, count the number of connected servers.
- Why this approach comes to mind first: It's a straightforward, intuitive approach that checks each server's neighbors.

```cpp
int countServers(vector<vector<int>>& grid) {
    int m = grid.size();
    int n = grid[0].size();
    vector<vector<bool>> connected(m, vector<bool>(n, false));
    int count = 0;

    // Iterate over each cell in the grid
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            // Check if the current cell is a server
            if (grid[i][j] == 1) {
                // Check its neighbors to see if any of them are also servers
                for (int x = -1; x <= 1; x++) {
                    for (int y = -1; y <= 1; y++) {
                        // Skip the current cell
                        if (x == 0 && y == 0) continue;
                        // Check if the neighbor is within bounds
                        if (i + x < 0 || i + x >= m || j + y < 0 || j + y >= n) continue;
                        // Check if the neighbor is a server
                        if (grid[i + x][j + y] == 1) {
                            // Mark the current server as connected
                            connected[i][j] = true;
                            break;
                        }
                    }
                    // If we've already marked the current server as connected, we can stop checking its neighbors
                    if (connected[i][j]) break;
                }
            }
        }
    }

    // Count the number of connected servers
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (grid[i][j] == 1 && connected[i][j]) {
                count++;
            }
        }
    }

    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ is the number of rows and $n$ is the number of columns in the grid, because we're iterating over each cell in the grid.
> - **Space Complexity:** $O(m \cdot n)$, because we're using a separate grid to keep track of connected servers.
> - **Why these complexities occur:** The time complexity occurs because we're iterating over each cell in the grid, and the space complexity occurs because we're using a separate grid to keep track of connected servers.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We can use a union-find data structure to keep track of connected servers.
- Detailed breakdown of the approach:
  1. Initialize a union-find data structure with each server as its own set.
  2. Iterate over each cell in the grid.
  3. For each cell, check if it's a server (i.e., its value is 1).
  4. If it's a server, check its neighbors (up, down, left, right) to see if any of them are also servers.
  5. If a neighbor is a server, union the two servers' sets.
  6. Finally, count the number of servers in each set and return the total count.
- Proof of optimality: This approach is optimal because it only requires a single pass over the grid, and the union-find operations are constant time on average.

```cpp
class UnionFind {
public:
    vector<int> parent;
    vector<int> rank;
    vector<int> size;

    UnionFind(int n) {
        parent.resize(n);
        rank.resize(n);
        size.resize(n);
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            rank[i] = 0;
            size[i] = 1;
        }
    }

    int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    void unionSets(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX != rootY) {
            if (rank[rootX] < rank[rootY]) {
                parent[rootX] = rootY;
                size[rootY] += size[rootX];
            } else if (rank[rootX] > rank[rootY]) {
                parent[rootY] = rootX;
                size[rootX] += size[rootY];
            } else {
                parent[rootY] = rootX;
                rank[rootX]++;
                size[rootX] += size[rootY];
            }
        }
    }
};

int countServers(vector<vector<int>>& grid) {
    int m = grid.size();
    int n = grid[0].size();
    int serverCount = 0;
    vector<int> serverIndices;

    // Count the number of servers and store their indices
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (grid[i][j] == 1) {
                serverCount++;
                serverIndices.push_back(i * n + j);
            }
        }
    }

    // Initialize the union-find data structure
    UnionFind uf(serverCount);

    // Iterate over each server and union its neighbors
    for (int i = 0; i < serverCount; i++) {
        int serverIndex = serverIndices[i];
        int row = serverIndex / n;
        int col = serverIndex % n;

        // Check up, down, left, right neighbors
        for (int x = -1; x <= 1; x++) {
            for (int y = -1; y <= 1; y++) {
                // Skip the current cell
                if (x == 0 && y == 0) continue;
                // Check if the neighbor is within bounds
                if (row + x < 0 || row + x >= m || col + y < 0 || col + y >= n) continue;
                // Check if the neighbor is a server
                if (grid[row + x][col + y] == 1) {
                    int neighborIndex = (row + x) * n + col + y;
                    int neighborServerIndex = -1;
                    for (int j = 0; j < serverCount; j++) {
                        if (serverIndices[j] == neighborIndex) {
                            neighborServerIndex = j;
                            break;
                        }
                    }
                    // Union the two servers
                    uf.unionSets(i, neighborServerIndex);
                }
            }
        }
    }

    // Count the number of connected servers
    int connectedServerCount = 0;
    for (int i = 0; i < serverCount; i++) {
        int root = uf.find(i);
        if (uf.size[root] > 1) {
            connectedServerCount += uf.size[root];
        }
    }

    return connectedServerCount;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n + m \cdot n \cdot \alpha(m \cdot n))$, where $\alpha(n)$ is the inverse Ackermann function, because we're using a union-find data structure.
> - **Space Complexity:** $O(m \cdot n)$, because we're using a union-find data structure.
> - **Optimality proof:** This approach is optimal because it only requires a single pass over the grid, and the union-find operations are constant time on average.