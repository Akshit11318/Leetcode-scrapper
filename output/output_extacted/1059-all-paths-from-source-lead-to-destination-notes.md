## All Paths from Source Lead to Destination
**Problem Link:** https://leetcode.com/problems/all-paths-from-source-lead-to-destination/description

**Problem Statement:**
- Given a directed graph with `n` nodes labeled from `0` to `n-1`, where `n` is the number of nodes in the graph.
- The graph is represented by a 2D array `graph`, where `graph[i]` is a list of nodes that can be reached directly from node `i`.
- The source node is `0` and the destination node is `n-1`.
- Input format and constraints: The input is a 2D array `graph`, and the constraints are `1 <= n <= 10^4`, `0 <= graph.length <= 10^4`, and `0 <= graph[i].length <= 10^4`.
- Expected output format: The output is a boolean indicating whether all paths from the source node lead to the destination node.
- Key requirements and edge cases to consider: The graph may contain cycles, and there may be nodes that are not reachable from the source node.
- Example test cases with explanations:
  - Example 1: `graph = [[1,2],[3],[3],[]]`, the output should be `true` because all paths from the source node `0` lead to the destination node `3`.
  - Example 2: `graph = [[1,2],[3],[3],[0]]`, the output should be `false` because there is a cycle in the graph that does not lead to the destination node.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can use a depth-first search (DFS) to traverse the graph from the source node and check if all paths lead to the destination node.
- Step-by-step breakdown of the solution:
  1. Start at the source node and perform a DFS traversal of the graph.
  2. Keep track of all nodes that have been visited.
  3. If we reach a node that has already been visited, it means there is a cycle in the graph.
  4. If we reach the destination node, we know that the current path leads to the destination node.
  5. If we have visited all nodes and have not found any paths that do not lead to the destination node, we can conclude that all paths from the source node lead to the destination node.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, but it may not be efficient for large graphs.

```cpp
class Solution {
public:
    bool leadsToDestination(int n, vector<vector<int>>& graph, int source, int destination) {
        vector<bool> visited(n, false);
        vector<bool> currentPath(n, false);
        return dfs(graph, source, destination, visited, currentPath);
    }
    
    bool dfs(vector<vector<int>>& graph, int node, int destination, vector<bool>& visited, vector<bool>& currentPath) {
        if (currentPath[node]) {
            return false; // cycle detected
        }
        if (visited[node]) {
            return true; // already visited and no cycle
        }
        visited[node] = true;
        currentPath[node] = true;
        for (int neighbor : graph[node]) {
            if (!dfs(graph, neighbor, destination, visited, currentPath)) {
                return false;
            }
        }
        currentPath[node] = false;
        return node == destination;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of nodes and $m$ is the number of edges, because we visit each node and edge once.
> - **Space Complexity:** $O(n)$, because we use a recursive call stack of size $n$ in the worst case.
> - **Why these complexities occur:** The time complexity occurs because we perform a DFS traversal of the graph, and the space complexity occurs because we use a recursive call stack to keep track of the current path.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a topological sorting to find all nodes that have no outgoing edges, and then check if the destination node is the only node with no outgoing edges.
- Detailed breakdown of the approach:
  1. Perform a topological sorting of the graph.
  2. Find all nodes that have no outgoing edges.
  3. Check if the destination node is the only node with no outgoing edges.
- Proof of optimality: This approach is optimal because it has a time complexity of $O(n + m)$, which is the best possible time complexity for this problem.
- Why further optimization is impossible: We must visit each node and edge at least once to determine if all paths lead to the destination node, so we cannot improve the time complexity further.

```cpp
class Solution {
public:
    bool leadsToDestination(int n, vector<vector<int>>& graph, int source, int destination) {
        vector<int> outDegree(n, 0);
        for (int i = 0; i < n; i++) {
            for (int j : graph[i]) {
                outDegree[j]++;
            }
        }
        for (int i = 0; i < n; i++) {
            if (i != destination && graph[i].empty()) {
                return false;
            }
        }
        vector<bool> visited(n, false);
        return !hasCycle(graph, source, visited);
    }
    
    bool hasCycle(vector<vector<int>>& graph, int node, vector<bool>& visited) {
        if (visited[node]) {
            return true;
        }
        visited[node] = true;
        for (int neighbor : graph[node]) {
            if (hasCycle(graph, neighbor, visited)) {
                return true;
            }
        }
        visited[node] = false;
        return false;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of nodes and $m$ is the number of edges, because we visit each node and edge once.
> - **Space Complexity:** $O(n)$, because we use a recursive call stack of size $n$ in the worst case.
> - **Optimality proof:** This approach is optimal because it has a time complexity of $O(n + m)$, which is the best possible time complexity for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: DFS, topological sorting, and cycle detection.
- Problem-solving patterns identified: using a topological sorting to find all nodes that have no outgoing edges.
- Optimization techniques learned: using a recursive call stack to keep track of the current path.
- Similar problems to practice: finding all paths from a source node to a destination node in a graph.

**Mistakes to Avoid:**
- Common implementation errors: not checking for cycles in the graph.
- Edge cases to watch for: nodes that are not reachable from the source node.
- Performance pitfalls: using a naive approach that has a high time complexity.
- Testing considerations: testing the solution with different graphs and edge cases.