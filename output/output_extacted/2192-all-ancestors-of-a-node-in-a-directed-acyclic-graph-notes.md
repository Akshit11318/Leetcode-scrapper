## All Ancestors of a Node in a Directed Acyclic Graph

**Problem Link:** https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/description

**Problem Statement:**
- Input format: `n` (number of nodes) and `edges` (list of directed edges)
- Constraints: $1 \leq n \leq 100$, $0 \leq edges.length \leq 100$
- Expected output format: List of lists, where each inner list contains all ancestors of the corresponding node
- Key requirements and edge cases to consider:
  - The graph is a Directed Acyclic Graph (DAG)
  - Each edge is represented as an array `[u, v]`, where `u` is the parent and `v` is the child
  - Each node has a unique index from `0` to `n-1`
- Example test cases with explanations:
  - `n = 5`, `edges = [[0, 1], [0, 2], [0, 3], [3, 4]]`
    - The ancestors of node `0` are `[]`
    - The ancestors of node `1` are `[0]`
    - The ancestors of node `2` are `[0]`
    - The ancestors of node `3` are `[0]`
    - The ancestors of node `4` are `[0, 3]`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Perform a depth-first search (DFS) from each node to find all its ancestors
- Step-by-step breakdown of the solution:
  1. Initialize an adjacency list to represent the graph
  2. Iterate over each node
  3. For each node, perform a DFS to find all its ancestors
- Why this approach comes to mind first: It's a straightforward way to explore the graph and find all ancestors of each node

```cpp
vector<vector<int>> getAncestors(int n, vector<vector<int>>& edges) {
    vector<vector<int>> graph(n);
    for (auto& edge : edges) {
        graph[edge[0]].push_back(edge[1]);
    }
    
    vector<vector<int>> ancestors(n);
    for (int i = 0; i < n; i++) {
        vector<bool> visited(n, false);
        dfs(graph, i, visited, ancestors[i]);
    }
    
    return ancestors;
}

void dfs(vector<vector<int>>& graph, int node, vector<bool>& visited, vector<int>& ancestors) {
    visited[node] = true;
    for (int neighbor : graph[node]) {
        if (!visited[neighbor]) {
            dfs(graph, neighbor, visited, ancestors);
        }
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 + m)$, where $n$ is the number of nodes and $m$ is the number of edges. The DFS operation takes $O(n + m)$ time, and we perform it $n$ times.
> - **Space Complexity:** $O(n + m)$, where $n$ is the number of nodes and $m$ is the number of edges. We need to store the adjacency list and the ancestors of each node.
> - **Why these complexities occur:** The DFS operation is the main contributor to the time complexity. We need to explore all nodes and edges in the graph to find all ancestors.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a transitive closure approach to find all ancestors of each node
- Detailed breakdown of the approach:
  1. Initialize a matrix to represent the transitive closure of the graph
  2. Iterate over each node and update the matrix accordingly
- Proof of optimality: This approach has a time complexity of $O(n^3)$, which is optimal for finding all ancestors in a DAG
- Why further optimization is impossible: The transitive closure approach is the most efficient way to find all ancestors in a DAG

```cpp
vector<vector<int>> getAncestors(int n, vector<vector<int>>& edges) {
    vector<vector<int>> graph(n, vector<int>(n, 0));
    for (auto& edge : edges) {
        graph[edge[0]][edge[1]] = 1;
    }
    
    // Compute transitive closure
    for (int k = 0; k < n; k++) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                graph[i][j] = graph[i][j] || (graph[i][k] && graph[k][j]);
            }
        }
    }
    
    vector<vector<int>> ancestors(n);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (graph[j][i]) {
                ancestors[i].push_back(j);
            }
        }
    }
    
    return ancestors;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the number of nodes. We need to compute the transitive closure of the graph.
> - **Space Complexity:** $O(n^2)$, where $n$ is the number of nodes. We need to store the transitive closure matrix and the ancestors of each node.
> - **Optimality proof:** This approach has the optimal time complexity for finding all ancestors in a DAG.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Transitive closure, DFS
- Problem-solving patterns identified: Using a matrix to represent the transitive closure of a graph
- Optimization techniques learned: Computing the transitive closure to find all ancestors in a DAG
- Similar problems to practice: Finding all descendants in a DAG, finding the shortest path in a weighted graph

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the matrix correctly, not updating the matrix correctly
- Edge cases to watch for: Empty graph, graph with no edges
- Performance pitfalls: Using an inefficient algorithm to compute the transitive closure
- Testing considerations: Test the function with different graph sizes and structures to ensure correctness and performance.