## Minimum Edge Reversals so Every Node is Reachable

**Problem Link:** https://leetcode.com/problems/minimum-edge-reversals-so-every-node-is-reachable/description

**Problem Statement:**
- Input format: `n` (number of nodes), `edges` (list of directed edges)
- Constraints: $1 \leq n \leq 1000$, $0 \leq edges.length \leq n \times (n - 1)$
- Expected output format: Minimum number of edge reversals to make every node reachable from every other node
- Key requirements and edge cases to consider: Handle cases where no solution exists, consider the direction of edges
- Example test cases with explanations: 
  - For a graph with 3 nodes and edges [[0,1],[1,2],[2,0]], the minimum number of reversals is 0 because every node is already reachable.
  - For a graph with 3 nodes and edges [[0,1],[1,2]], the minimum number of reversals is 2 because we need to reverse both edges to make every node reachable.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of edge reversals and check if every node is reachable from every other node.
- Step-by-step breakdown of the solution:
  1. Generate all possible subsets of edges to reverse.
  2. For each subset, reverse the edges in the subset.
  3. Check if every node is reachable from every other node by performing a depth-first search (DFS) from each node.
  4. If every node is reachable, return the size of the subset as the minimum number of reversals.
- Why this approach comes to mind first: It is a straightforward way to ensure all possibilities are considered.

```cpp
#include <vector>
#include <iostream>

using namespace std;

int minReversalsBruteForce(int n, vector<vector<int>>& edges) {
    int minReversals = INT_MAX;
    int totalEdges = edges.size();
    
    // Generate all possible subsets of edges
    for (int mask = 0; mask < (1 << totalEdges); mask++) {
        int reversals = 0;
        vector<vector<int>> graph(n);
        
        // Create a graph with the current subset of edges reversed
        for (int i = 0; i < totalEdges; i++) {
            int u = edges[i][0], v = edges[i][1];
            if ((mask & (1 << i)) == 0) {
                graph[u].push_back(v);
            } else {
                graph[v].push_back(u);
                reversals++;
            }
        }
        
        // Check if every node is reachable from every other node
        bool reachable = true;
        for (int i = 0; i < n; i++) {
            vector<bool> visited(n, false);
            visited[i] = true;
            vector<int> stack = {i};
            while (!stack.empty()) {
                int node = stack.back();
                stack.pop_back();
                for (int neighbor : graph[node]) {
                    if (!visited[neighbor]) {
                        visited[neighbor] = true;
                        stack.push_back(neighbor);
                    }
                }
            }
            for (int j = 0; j < n; j++) {
                if (!visited[j]) {
                    reachable = false;
                    break;
                }
            }
            if (!reachable) break;
        }
        
        if (reachable) {
            minReversals = min(minReversals, reversals);
        }
    }
    
    return minReversals == INT_MAX ? -1 : minReversals;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{totalEdges} \cdot n \cdot (n + totalEdges))$ where $totalEdges$ is the number of edges, because for each subset of edges, we perform a DFS from each node.
> - **Space Complexity:** $O(n + totalEdges)$ for storing the graph and the visited nodes during DFS.
> - **Why these complexities occur:** The brute force approach generates all possible subsets of edges, leading to an exponential time complexity. The space complexity is linear due to the storage needed for the graph and visited nodes.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a union-find data structure to keep track of connected components in the graph. By iterating through the edges and reversing them if necessary to connect components, we can find the minimum number of reversals.
- Detailed breakdown of the approach:
  1. Initialize a union-find data structure with each node in its own set.
  2. Iterate through the edges. For each edge, if the two nodes are not in the same set, reverse the edge and union the sets.
  3. The number of reversals is the minimum number of edge reversals needed to make every node reachable from every other node.
- Proof of optimality: This approach ensures that we only reverse edges when necessary to connect components, resulting in the minimum number of reversals.

```cpp
class UnionFind {
public:
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
    void unionSets(int x, int y) {
        int rootX = find(x), rootY = find(y);
        if (rootX != rootY) {
            if (rank[rootX] > rank[rootY]) {
                parent[rootY] = rootX;
            } else if (rank[rootX] < rank[rootY]) {
                parent[rootX] = rootY;
            } else {
                parent[rootY] = rootX;
                rank[rootX]++;
            }
        }
    }
};

int minReversalsOptimal(int n, vector<vector<int>>& edges) {
    UnionFind uf(n);
    int reversals = 0;
    
    for (auto& edge : edges) {
        int u = edge[0], v = edge[1];
        if (uf.find(u) != uf.find(v)) {
            uf.unionSets(u, v);
        } else {
            reversals++;
        }
    }
    
    // Check if all nodes are in the same set
    int root = uf.find(0);
    for (int i = 1; i < n; i++) {
        if (uf.find(i) != root) {
            return -1; // No solution exists
        }
    }
    
    return reversals;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + totalEdges \cdot \alpha(n))$ where $\alpha(n)$ is the inverse Ackermann function, which grows very slowly. This is because the union-find operations (find and union) have an amortized time complexity of $\alpha(n)$.
> - **Space Complexity:** $O(n + totalEdges)$ for storing the union-find data structure and the graph.
> - **Optimality proof:** The optimal approach ensures that we only reverse edges when necessary to connect components, resulting in the minimum number of reversals. The use of a union-find data structure allows for efficient management of connected components.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Union-find data structure, graph traversal (DFS), and optimization techniques.
- Problem-solving patterns identified: Breaking down the problem into smaller sub-problems (connected components) and using data structures to manage these sub-problems efficiently.
- Optimization techniques learned: Using a union-find data structure to minimize the number of edge reversals needed.

**Mistakes to Avoid:**
- Common implementation errors: Not properly handling the union-find data structure or incorrectly counting the number of reversals.
- Edge cases to watch for: Handling cases where no solution exists (i.e., it's impossible to make every node reachable from every other node).
- Performance pitfalls: Using an inefficient algorithm or data structure, leading to high time or space complexity.
- Testing considerations: Thoroughly testing the implementation with various inputs, including edge cases, to ensure correctness and efficiency.