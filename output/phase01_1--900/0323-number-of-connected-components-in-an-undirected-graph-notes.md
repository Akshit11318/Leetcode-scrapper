## Number of Connected Components in an Undirected Graph

**Problem Link:** https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/description

**Problem Statement:**
- Input format: The problem takes an integer `n` representing the number of nodes in the graph and an array `edges` of pairs representing the edges between nodes.
- Constraints: The nodes are numbered from 1 to `n`, and the edges are given as pairs of node numbers.
- Expected output format: The output should be the number of connected components in the graph.
- Key requirements and edge cases to consider: Disconnected graphs, graphs with a single connected component, and the possibility of self-loops or parallel edges.
- Example test cases with explanations:
  - For `n = 5` and `edges = [[0, 1], [1, 2], [3, 4]]`, there are 2 connected components: one containing nodes 0, 1, and 2, and another containing nodes 3 and 4.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To find the number of connected components, we can think of performing a depth-first search (DFS) from each node to identify all connected nodes.
- Step-by-step breakdown of the solution:
  1. Initialize a visited array to keep track of visited nodes.
  2. Iterate through all nodes. For each unvisited node, perform a DFS to mark all reachable nodes as visited.
  3. Increment the count of connected components each time a new unvisited node is encountered.
- Why this approach comes to mind first: It's a straightforward method to ensure all nodes are visited and to count the distinct groups of connected nodes.

```cpp
class Solution {
public:
    int countComponents(int n, vector<vector<int>>& edges) {
        vector<bool> visited(n, false);
        int components = 0;
        
        for (int i = 0; i < n; ++i) {
            if (!visited[i]) {
                components++;
                dfs(i, visited, edges);
            }
        }
        
        return components;
    }
    
    void dfs(int node, vector<bool>& visited, vector<vector<int>>& edges) {
        visited[node] = true;
        
        for (auto& edge : edges) {
            if (edge[0] == node && !visited[edge[1]]) {
                dfs(edge[1], visited, edges);
            } else if (edge[1] == node && !visited[edge[0]]) {
                dfs(edge[0], visited, edges);
            }
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$ where $n$ is the number of nodes and $m$ is the number of edges, because in the worst case, we visit each node and each edge once.
> - **Space Complexity:** $O(n + m)$ for the visited array and the recursive call stack in the worst case.
> - **Why these complexities occur:** The time complexity is linear because we potentially visit each node and edge once. The space complexity is also linear due to the storage needed for the visited array and the maximum depth of the recursive call stack.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of using an adjacency list or edges directly for DFS, we can create an adjacency list representation of the graph first. This allows for more efficient DFS traversal.
- Detailed breakdown of the approach:
  1. Create an adjacency list representation of the graph from the given edges.
  2. Perform DFS from each unvisited node to count connected components.
- Proof of optimality: This approach is optimal because it minimizes the number of operations needed to traverse the graph and count connected components.

```cpp
class Solution {
public:
    int countComponents(int n, vector<vector<int>>& edges) {
        vector<vector<int>> graph(n);
        for (auto& edge : edges) {
            graph[edge[0]].push_back(edge[1]);
            graph[edge[1]].push_back(edge[0]);
        }
        
        vector<bool> visited(n, false);
        int components = 0;
        
        for (int i = 0; i < n; ++i) {
            if (!visited[i]) {
                components++;
                dfs(i, visited, graph);
            }
        }
        
        return components;
    }
    
    void dfs(int node, vector<bool>& visited, vector<vector<int>>& graph) {
        visited[node] = true;
        
        for (int neighbor : graph[node]) {
            if (!visited[neighbor]) {
                dfs(neighbor, visited, graph);
            }
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of nodes and $m$ is the number of edges, because creating the adjacency list and performing DFS both take linear time.
> - **Space Complexity:** $O(n + m)$ for the adjacency list and the visited array.
> - **Optimality proof:** This is the best possible time complexity for this problem because we must at least read the input, which takes $O(n + m)$ time.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: DFS, graph traversal, and connected component counting.
- Problem-solving patterns identified: Creating an adjacency list for efficient graph traversal and using a visited array to keep track of visited nodes.
- Optimization techniques learned: Minimizing the number of operations by using an adjacency list for DFS.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the visited array, not handling edge cases like self-loops or parallel edges.
- Edge cases to watch for: Disconnected graphs, graphs with a single connected component.
- Performance pitfalls: Using an inefficient graph representation or traversal algorithm.
- Testing considerations: Ensure the solution works for various graph structures and edge cases.