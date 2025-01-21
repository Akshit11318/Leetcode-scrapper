## Minimum Weighted Subgraph with the Required Paths

**Problem Link:** https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths/description

**Problem Statement:**
- Input format: `n` nodes, `edges` list of pairs of nodes with weights, `startNodes` and `endNodes` lists of nodes.
- Constraints: `1 <= n <= 10^5`, `1 <= edges.length <= 5 * 10^5`, `1 <= startNodes.length, endNodes.length <= n`.
- Expected output format: Minimum total weight of the subgraph that includes all required paths.
- Key requirements: Find the minimum weighted subgraph that includes paths from all `startNodes` to all `endNodes`.
- Example test cases:
  - Example 1: Given `n = 6`, `edges = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [0, 3, 5], [3, 5, 1], [1, 5, 1]]`, `startNodes = [0, 1]`, `endNodes = [5]`, the output is `2`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to generate all possible subgraphs and calculate their weights.
- Then, check each subgraph to see if it includes paths from all `startNodes` to all `endNodes`.
- If it does, update the minimum weight if the current subgraph's weight is smaller.

```cpp
#include <vector>
#include <climits>

using namespace std;

struct Edge {
    int from, to, weight;
};

int minWeightSubgraph(int n, vector<Edge>& edges, vector<int>& startNodes, vector<int>& endNodes) {
    int minWeight = INT_MAX;
    
    // Generate all possible subgraphs
    for (int mask = 0; mask < (1 << edges.size()); mask++) {
        int currentWeight = 0;
        vector<Edge> currentEdges;
        
        // Select edges based on the current mask
        for (int i = 0; i < edges.size(); i++) {
            if (mask & (1 << i)) {
                currentWeight += edges[i].weight;
                currentEdges.push_back(edges[i]);
            }
        }
        
        // Check if the current subgraph includes all required paths
        bool hasAllPaths = true;
        for (int start : startNodes) {
            for (int end : endNodes) {
                if (!hasPath(currentEdges, start, end)) {
                    hasAllPaths = false;
                    break;
                }
            }
            if (!hasAllPaths) break;
        }
        
        if (hasAllPaths) {
            minWeight = min(minWeight, currentWeight);
        }
    }
    
    return minWeight == INT_MAX ? -1 : minWeight;
}

bool hasPath(vector<Edge>& edges, int start, int end) {
    vector<bool> visited(edges.size());
    return dfs(edges, start, end, visited);
}

bool dfs(vector<Edge>& edges, int current, int end, vector<bool>& visited) {
    if (current == end) return true;
    
    visited[current] = true;
    for (Edge edge : edges) {
        if (edge.from == current && !visited[edge.to]) {
            if (dfs(edges, edge.to, end, visited)) return true;
        }
    }
    
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{m} \cdot (n + m))$, where $m$ is the number of edges and $n$ is the number of nodes, because we generate all possible subgraphs and for each, we check if it has all required paths.
> - **Space Complexity:** $O(m + n)$ for storing the current subgraph and the visited nodes during DFS.
> - **Why these complexities occur:** The brute force approach has high complexity due to generating all possible subgraphs and checking each for the required paths.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a union-find data structure to keep track of connected components.
- We start with an empty subgraph and iteratively add edges with the smallest weight that connect any `startNode` to any `endNode`.
- We use a priority queue to efficiently select the next edge to add.

```cpp
#include <queue>
#include <vector>

using namespace std;

struct Edge {
    int from, to, weight;
};

struct UnionFind {
    vector<int> parent, rank;
    
    UnionFind(int n) : parent(n), rank(n, 0) {
        for (int i = 0; i < n; i++) {
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
        int rootX = find(x), rootY = find(y);
        if (rootX != rootY) {
            if (rank[rootX] < rank[rootY]) {
                parent[rootX] = rootY;
            } else if (rank[rootX] > rank[rootY]) {
                parent[rootY] = rootX;
            } else {
                parent[rootY] = rootX;
                rank[rootX]++;
            }
        }
    }
};

int minWeightSubgraph(int n, vector<Edge>& edges, vector<int>& startNodes, vector<int>& endNodes) {
    int minWeight = 0;
    UnionFind uf(n);
    
    // Create a priority queue to store edges
    priority_queue<Edge, vector<Edge>, function<bool(const Edge&, const Edge&)>> pq(
        [](const Edge& a, const Edge& b) { return a.weight > b.weight; });
    
    for (Edge edge : edges) {
        pq.push(edge);
    }
    
    // Add edges to the subgraph until all startNodes are connected to all endNodes
    while (!pq.empty()) {
        Edge edge = pq.top();
        pq.pop();
        
        // Check if adding this edge connects any startNode to any endNode
        bool connectsStartToEnd = false;
        for (int start : startNodes) {
            for (int end : endNodes) {
                if (uf.find(start) != uf.find(end) && (edge.from == start || edge.to == start) && (edge.from == end || edge.to == end)) {
                    connectsStartToEnd = true;
                    break;
                }
            }
            if (connectsStartToEnd) break;
        }
        
        if (connectsStartToEnd) {
            minWeight += edge.weight;
            uf.unionNodes(edge.from, edge.to);
        }
    }
    
    return minWeight;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \log m + n)$, where $m$ is the number of edges and $n$ is the number of nodes, because we use a priority queue to select edges and a union-find data structure to keep track of connected components.
> - **Space Complexity:** $O(m + n)$ for storing the edges and the union-find data structure.
> - **Optimality proof:** This approach is optimal because it adds edges to the subgraph in non-decreasing order of their weights and stops as soon as all required paths are included.

---

### Final Notes

**Learning Points:**
- The importance of using the right data structures (e.g., union-find, priority queue) to solve graph problems efficiently.
- How to approach problems that require finding a minimum weighted subgraph with specific properties.
- The trade-offs between different approaches (e.g., brute force vs. optimal).

**Mistakes to Avoid:**
- Not considering the use of data structures that can efficiently handle graph operations.
- Failing to analyze the time and space complexity of the solution.
- Not testing the solution thoroughly with different inputs and edge cases.