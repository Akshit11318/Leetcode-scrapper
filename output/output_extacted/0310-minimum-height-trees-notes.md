## Minimum Height Trees

**Problem Link:** https://leetcode.com/problems/minimum-height-trees/description

**Problem Statement:**
- Input format: `n` nodes, `edges` list of pairs representing undirected edges between nodes.
- Constraints: `0 <= n <= 6 * 10^4`, `0 <= edges.length <= 10^5`.
- Expected output format: List of roots for Minimum Height Trees (MHTs).
- Key requirements: Find all possible roots that result in trees with the minimum height.
- Example test cases:
  - Input: `n = 6`, `edges = [[0, 1], [0, 2], [0, 3], [3, 4], [4, 5]]`
    Output: `[3, 4]`
  - Input: `n = 1`, `edges = []`
    Output: `[0]`
  - Input: `n = 2`, `edges = [[1, 0]]`
    Output: `[0, 1]`

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves considering each node as a potential root and calculating the height of the tree rooted at each node.
- Step-by-step breakdown:
  1. For each node, perform a depth-first search (DFS) or breadth-first search (BFS) to calculate the height of the tree rooted at that node.
  2. Keep track of the minimum height encountered and the nodes that result in this minimum height.

```cpp
#include <vector>
#include <queue>
using namespace std;

vector<int> findMinHeightTrees(int n, vector<vector<int>>& edges) {
    if (n == 1) return {0};
    
    vector<vector<int>> adj(n);
    for (auto& edge : edges) {
        adj[edge[0]].push_back(edge[1]);
        adj[edge[1]].push_back(edge[0]);
    }

    int minHeight = INT_MAX;
    vector<int> roots;

    for (int i = 0; i < n; ++i) {
        queue<int> q;
        q.push(i);
        vector<bool> visited(n, false);
        visited[i] = true;
        int height = 0;

        while (!q.empty()) {
            int size = q.size();
            for (int j = 0; j < size; ++j) {
                int node = q.front();
                q.pop();
                for (int neighbor : adj[node]) {
                    if (!visited[neighbor]) {
                        q.push(neighbor);
                        visited[neighbor] = true;
                    }
                }
            }
            height++;
        }

        if (height < minHeight) {
            minHeight = height;
            roots.clear();
            roots.push_back(i);
        } else if (height == minHeight) {
            roots.push_back(i);
        }
    }

    return roots;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, because for each node, we potentially visit all other nodes.
> - **Space Complexity:** $O(n)$, for the adjacency list representation of the graph and the queue used in BFS.
> - **Why these complexities occur:** The brute force approach involves calculating the height of the tree for each node, leading to quadratic time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: The optimal solution involves using a topological sorting approach, where we start by removing leaves from the graph until we are left with the roots of the MHTs.
- Detailed breakdown:
  1. Build the adjacency list representation of the graph.
  2. Find all leaves (nodes with degree 1) and remove them from the graph, updating the degrees of their neighbors.
  3. Repeat step 2 until we are left with 1 or 2 nodes, which are the roots of the MHTs.

```cpp
#include <vector>
#include <queue>
using namespace std;

vector<int> findMinHeightTrees(int n, vector<vector<int>>& edges) {
    if (n == 1) return {0};
    
    vector<int> degree(n, 0);
    vector<vector<int>> adj(n);
    for (auto& edge : edges) {
        degree[edge[0]]++;
        degree[edge[1]]++;
        adj[edge[0]].push_back(edge[1]);
        adj[edge[1]].push_back(edge[0]);
    }

    queue<int> q;
    for (int i = 0; i < n; ++i) {
        if (degree[i] == 1) {
            q.push(i);
        }
    }

    while (n > 2) {
        int size = q.size();
        n -= size;
        for (int i = 0; i < size; ++i) {
            int node = q.front();
            q.pop();
            for (int neighbor : adj[node]) {
                degree[neighbor]--;
                if (degree[neighbor] == 1) {
                    q.push(neighbor);
                }
            }
        }
    }

    vector<int> roots;
    while (!q.empty()) {
        roots.push_back(q.front());
        q.pop();
    }

    return roots;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, because we visit each node at most twice (once when we add it to the queue and once when we remove it).
> - **Space Complexity:** $O(n)$, for the adjacency list representation of the graph and the queue used.
> - **Optimality proof:** This approach is optimal because it takes advantage of the structure of the graph to efficiently find the roots of the MHTs.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: Topological sorting, graph traversal (BFS), and the importance of understanding the structure of the problem to find an efficient solution.
- Problem-solving patterns: Identifying the key characteristics of the problem (in this case, the need to find roots that minimize tree height) and using these insights to guide the solution.
- Optimization techniques: Using a queue to efficiently remove leaves from the graph and update the degrees of their neighbors.

**Mistakes to Avoid:**
- Common implementation errors: Failing to update the degrees of neighbors correctly when removing leaves.
- Edge cases to watch for: Handling the case where `n = 1` separately, as it does not fit the general pattern of removing leaves.
- Performance pitfalls: Using a brute force approach that results in quadratic time complexity.
- Testing considerations: Ensuring that the solution works correctly for different graph structures and sizes.