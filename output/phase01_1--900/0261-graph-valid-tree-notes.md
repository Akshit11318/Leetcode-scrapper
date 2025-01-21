## Graph Valid Tree

**Problem Link:** https://leetcode.com/problems/graph-valid-tree/description

**Problem Statement:**
- Input format and constraints: Given `n` nodes, and an array of edges where each edge is represented as a pair of nodes `[u, v]`.
- Expected output format: Return `true` if the graph is a valid tree, and `false` otherwise.
- Key requirements and edge cases to consider: A graph is a valid tree if it has exactly `n-1` edges and is connected.
- Example test cases with explanations: For example, given `n = 5` and `edges = [[0,1],[0,2],[0,3],[1,4]]`, the graph is a valid tree because it has `4` edges and is connected.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To determine if a graph is a valid tree, we can first check if it has exactly `n-1` edges. Then, we can perform a depth-first search (DFS) or breadth-first search (BFS) to check if the graph is connected.
- Step-by-step breakdown of the solution: 
  1. Check if the number of edges is `n-1`.
  2. Create an adjacency list representation of the graph.
  3. Perform DFS or BFS from an arbitrary node to check if all nodes are reachable.
- Why this approach comes to mind first: This approach is straightforward and checks all the conditions for a graph to be a valid tree.

```cpp
class Solution {
public:
    bool validTree(int n, vector<vector<int>>& edges) {
        // Check if the number of edges is n-1
        if (edges.size() != n - 1) return false;
        
        // Create an adjacency list representation of the graph
        vector<vector<int>> graph(n);
        for (auto& edge : edges) {
            graph[edge[0]].push_back(edge[1]);
            graph[edge[1]].push_back(edge[0]);
        }
        
        // Perform DFS to check if the graph is connected
        vector<bool> visited(n, false);
        dfs(graph, 0, visited);
        
        // Check if all nodes are reachable
        for (bool v : visited) {
            if (!v) return false;
        }
        
        return true;
    }
    
    void dfs(vector<vector<int>>& graph, int node, vector<bool>& visited) {
        visited[node] = true;
        for (int neighbor : graph[node]) {
            if (!visited[neighbor]) {
                dfs(graph, neighbor, visited);
            }
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of nodes and $m$ is the number of edges, because we perform DFS on all nodes and edges.
> - **Space Complexity:** $O(n + m)$, because we store the adjacency list representation of the graph and the visited array.
> - **Why these complexities occur:** These complexities occur because we need to visit all nodes and edges to check if the graph is connected.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a union-find data structure to check if the graph is connected and has no cycles.
- Detailed breakdown of the approach: 
  1. Initialize the union-find data structure with `n` nodes.
  2. Iterate over the edges and union the nodes. If a cycle is detected, return `false`.
  3. Check if all nodes are connected by checking if the number of connected components is 1.
- Proof of optimality: This approach is optimal because it checks all the conditions for a graph to be a valid tree in linear time.

```cpp
class Solution {
public:
    bool validTree(int n, vector<vector<int>>& edges) {
        if (edges.size() != n - 1) return false;
        
        vector<int> parent(n);
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
        
        for (auto& edge : edges) {
            if (!unionNodes(parent, edge[0], edge[1])) {
                return false;
            }
        }
        
        int count = 0;
        for (int i = 0; i < n; i++) {
            if (parent[i] == i) {
                count++;
            }
        }
        
        return count == 1;
    }
    
    int findParent(vector<int>& parent, int node) {
        if (parent[node] != node) {
            parent[node] = findParent(parent, parent[node]);
        }
        return parent[node];
    }
    
    bool unionNodes(vector<int>& parent, int node1, int node2) {
        int parent1 = findParent(parent, node1);
        int parent2 = findParent(parent, node2);
        
        if (parent1 == parent2) {
            return false;
        }
        
        parent[parent1] = parent2;
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m \alpha(n))$, where $\alpha(n)$ is the inverse Ackermann function, because we use a union-find data structure with path compression and union by rank.
> - **Space Complexity:** $O(n)$, because we store the parent array.
> - **Optimality proof:** This approach is optimal because it checks all the conditions for a graph to be a valid tree in linear time, and the union-find data structure has an almost constant time complexity.