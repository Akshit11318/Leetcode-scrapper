## Remove Max Number of Edges to Keep Graph Fully Traversable
**Problem Link:** https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/description

**Problem Statement:**
- Input format: `n` nodes, `edges` list of triples `(u, v, is_alice_edge)`, where `u` and `v` are nodes and `is_alice_edge` indicates if the edge belongs to Alice.
- Constraints: `1 <= n <= 1000`, `0 <= edges.length <= 1000`.
- Expected output format: Maximum number of edges to remove such that the graph remains fully traversable by both Alice and Bob.
- Key requirements: Ensure that after removing edges, there is a path between every pair of nodes for both Alice and Bob.
- Example test cases:
  - Input: `n = 4`, `edges = [[1,2,0],[1,3,1],[2,3,0],[1,4,0],[3,4,1]]`.
    - Output: `2`.
    - Explanation: Remove edges `(1,3)` and `(3,4)`.

### Brute Force Approach
**Explanation:**
- Generate all possible subsets of edges.
- For each subset, check if removing these edges results in a graph that is still fully traversable by both Alice and Bob.
- Keep track of the maximum number of edges that can be removed while maintaining full traversability.

```cpp
#include <iostream>
#include <vector>
using namespace std;

int maxNumEdgesToRemove(int n, vector<vector<int>>& edges) {
    int maxRemoved = 0;
    // Generate all possible subsets of edges
    for (int mask = 0; mask < (1 << edges.size()); ++mask) {
        vector<vector<int>> graph(n + 1);
        int aliceEdges = 0, bobEdges = 0;
        // For each subset, build the graph
        for (int i = 0; i < edges.size(); ++i) {
            if (mask & (1 << i)) {
                int u = edges[i][0], v = edges[i][1];
                graph[u].push_back(v);
                graph[v].push_back(u);
                if (edges[i][2] == 0) bobEdges++;
                else aliceEdges++;
            }
        }
        // Check if the graph is fully traversable
        if (isFullyTraversable(graph, n)) {
            maxRemoved = max(maxRemoved, __builtin_popcount(mask));
        }
    }
    return maxRemoved;
}

bool isFullyTraversable(vector<vector<int>>& graph, int n) {
    // Perform DFS to check connectivity
    vector<bool> visited(n + 1, false);
    dfs(graph, 1, visited);
    for (int i = 1; i <= n; ++i) {
        if (!visited[i]) return false;
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
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{edges.length} \cdot n)$, where $edges.length$ is the number of edges and $n$ is the number of nodes.
> - **Space Complexity:** $O(n + edges.length)$, for storing the graph and visited nodes.
> - **Why these complexities occur:** The brute force approach generates all possible subsets of edges, leading to exponential time complexity. The space complexity is due to the storage needed for the graph and visited nodes.

### Optimal Approach (Required)
**Explanation:**
- Use Union-Find to keep track of connected components for both Alice and Bob.
- Iterate through the edges, adding them to the graph if they connect different components for either Alice or Bob.
- Count the number of edges that are not added to the graph.

```cpp
class UnionFind {
public:
    vector<int> parent;
    vector<int> rank;
    int components;

    UnionFind(int n) : parent(n + 1), rank(n + 1, 0), components(n) {
        for (int i = 1; i <= n; ++i) {
            parent[i] = i;
        }
    }

    int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    void unionNodes(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX != rootY) {
            if (rank[rootX] > rank[rootY]) {
                parent[rootY] = rootX;
            } else if (rank[rootX] < rank[rootY]) {
                parent[rootX] = rootY;
            } else {
                parent[rootY] = rootX;
                rank[rootX]++;
            }
            components--;
        }
    }
};

int maxNumEdgesToRemove(int n, vector<vector<int>>& edges) {
    UnionFind alice(n);
    UnionFind bob(n);
    int removed = 0;

    // Add edges that connect different components for either Alice or Bob
    for (auto& edge : edges) {
        if (edge[2] == 1) { // Alice's edge
            if (alice.find(edge[0]) != alice.find(edge[1])) {
                alice.unionNodes(edge[0], edge[1]);
            } else {
                removed++;
            }
        }
    }
    for (auto& edge : edges) {
        if (edge[2] == 0) { // Bob's edge
            if (bob.find(edge[0]) != bob.find(edge[1])) {
                bob.unionNodes(edge[0], edge[1]);
            } else {
                removed++;
            }
        }
    }
    // Check if the remaining edges can connect the graph for both Alice and Bob
    if (alice.components > 1 || bob.components > 1) {
        return -1; // Graph cannot be fully traversable
    }
    return removed;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + edges.length \cdot \alpha(n))$, where $\alpha(n)$ is the inverse Ackermann function, which grows very slowly.
> - **Space Complexity:** $O(n + edges.length)$, for storing the Union-Find data structures and edges.
> - **Optimality proof:** The optimal approach uses Union-Find to efficiently manage the connected components, ensuring that the graph remains fully traversable while removing the maximum number of edges.

### Final Notes

**Learning Points:**
- **Union-Find** data structure for managing connected components.
- **Graph traversal** techniques to check for full traversability.
- **Optimization** by counting removed edges instead of generating all subsets.

**Mistakes to Avoid:**
- Not checking for full traversability after removing edges.
- Not using an efficient data structure like Union-Find.
- Not considering the case where the graph cannot be fully traversable.