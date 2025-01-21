## Find if Path Exists in Graph

**Problem Link:** https://leetcode.com/problems/find-if-path-exists-in-graph/description

**Problem Statement:**
- Input format and constraints: The input is an undirected graph represented as an adjacency list (`n` nodes, `edges` list of pairs of nodes), and two nodes `start` and `end`.
- Expected output format: A boolean indicating whether there exists a path from `start` to `end`.
- Key requirements and edge cases to consider: The graph may be disconnected, and nodes may have no edges.
- Example test cases with explanations:
  - Example 1: `n = 3, edges = [[0, 1], [1, 2], [2, 0]], start = 0, end = 2` returns `true` because there's a path from node 0 to node 2.
  - Example 2: `n = 6, edges = [[0, 1], [1, 2], [2, 0]], start = 0, end = 3` returns `false` because there's no path from node 0 to node 3.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To check if there's a path between two nodes, we can start from the `start` node and try to reach every other node in the graph by exploring all possible paths.
- Step-by-step breakdown of the solution:
  1. Create an adjacency list representation of the graph.
  2. Perform a depth-first search (DFS) from the `start` node.
  3. During DFS, mark visited nodes to avoid revisiting them.
  4. If we reach the `end` node during DFS, return `true`.
  5. If DFS completes without finding a path to the `end` node, return `false`.
- Why this approach comes to mind first: It's a straightforward method to check connectivity in a graph.

```cpp
class Solution {
public:
    bool validPath(int n, vector<vector<int>>& edges, int start, int end) {
        // Create adjacency list
        vector<vector<int>> graph(n);
        for (auto& edge : edges) {
            graph[edge[0]].push_back(edge[1]);
            graph[edge[1]].push_back(edge[0]);
        }
        
        vector<bool> visited(n, false);
        
        // Perform DFS
        function<bool(int)> dfs = [&](int node) {
            if (node == end) return true;
            visited[node] = true;
            for (int neighbor : graph[node]) {
                if (!visited[neighbor] && dfs(neighbor)) return true;
            }
            return false;
        };
        
        return dfs(start);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of nodes and $m$ is the number of edges, because in the worst case, we visit every node and edge once.
> - **Space Complexity:** $O(n + m)$, for storing the adjacency list and the visited array.
> - **Why these complexities occur:** The DFS traversal ensures we visit each node and edge at most once, leading to linear time complexity. The space complexity is due to the storage needed for the adjacency list and visited array.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The same approach as the brute force is already optimal because we must at least visit each node and edge once to determine if a path exists.
- Detailed breakdown of the approach: Same as the brute force approach.
- Proof of optimality: Any algorithm must at least read the input, which takes $O(n + m)$ time, making the DFS approach optimal.
- Why further optimization is impossible: We cannot do better than linear time because we must examine each node and edge at least once.

```cpp
class Solution {
public:
    bool validPath(int n, vector<vector<int>>& edges, int start, int end) {
        // Create adjacency list
        vector<vector<int>> graph(n);
        for (auto& edge : edges) {
            graph[edge[0]].push_back(edge[1]);
            graph[edge[1]].push_back(edge[0]);
        }
        
        vector<bool> visited(n, false);
        
        // Perform DFS
        function<bool(int)> dfs = [&](int node) {
            if (node == end) return true;
            visited[node] = true;
            for (int neighbor : graph[node]) {
                if (!visited[neighbor] && dfs(neighbor)) return true;
            }
            return false;
        };
        
        return dfs(start);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of nodes and $m$ is the number of edges.
> - **Space Complexity:** $O(n + m)$, for storing the adjacency list and the visited array.
> - **Optimality proof:** This is the best possible time complexity because we must at least examine each node and edge once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Depth-First Search (DFS), graph traversal, and adjacency list representation.
- Problem-solving patterns identified: Using DFS for connectivity problems in graphs.
- Optimization techniques learned: Ensuring each node and edge is visited at most once.
- Similar problems to practice: Finding connected components, testing whether a graph is connected, or finding a path between two nodes in a directed graph.

**Mistakes to Avoid:**
- Common implementation errors: Failing to mark visited nodes, not handling the case where the graph is empty, or incorrectly implementing the DFS recursion.
- Edge cases to watch for: Disconnected graphs, graphs with no edges, or graphs with a single node.
- Performance pitfalls: Using an inefficient graph representation or algorithm that revisits nodes unnecessarily.
- Testing considerations: Test with various graph structures, including connected and disconnected graphs, to ensure the solution works correctly in all scenarios.