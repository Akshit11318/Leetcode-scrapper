## Divide Nodes Into the Maximum Number of Groups
**Problem Link:** https://leetcode.com/problems/divide-nodes-into-the-maximum-number-of-groups/description

**Problem Statement:**
- Input format: An integer `n` and a 2D array `edges` representing the nodes in the graph.
- Constraints: `1 <= n <= 10^5`, `1 <= edges.length <= 2 * 10^5`, `edges[i].length == 2`, `0 <= edges[i][0], edges[i][1] < n`.
- Expected output format: The maximum number of groups that can be formed.
- Key requirements: Find the maximum number of groups such that each group is a tree (i.e., it is connected and has no cycles).
- Example test cases:
  - `n = 6`, `edges = [[0,1],[0,2],[1,3],[1,4],[2,5]]`. The maximum number of groups is 3.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of nodes to form groups and check if each group is a tree.
- Step-by-step breakdown of the solution:
  1. Generate all possible combinations of nodes.
  2. For each combination, check if the subgraph induced by the nodes in the combination is a tree.
  3. If it is a tree, increment the count of groups.
- Why this approach comes to mind first: It is a straightforward approach that tries all possibilities.

```cpp
#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

// Function to check if a graph is a tree
bool isTree(const vector<vector<int>>& graph) {
    unordered_set<int> visited;
    vector<int> stack;
    stack.push_back(0);
    
    while (!stack.empty()) {
        int node = stack.back();
        stack.pop_back();
        
        if (visited.find(node) != visited.end()) {
            return false; // Cycle detected
        }
        
        visited.insert(node);
        
        for (int neighbor : graph[node]) {
            if (visited.find(neighbor) == visited.end()) {
                stack.push_back(neighbor);
            }
        }
    }
    
    return visited.size() == graph.size(); // All nodes visited
}

int maxGroups(int n, vector<vector<int>>& edges) {
    int maxGroups = 0;
    
    // Generate all possible combinations of nodes
    for (int mask = 0; mask < (1 << n); mask++) {
        vector<vector<int>> subgraph(n);
        unordered_set<int> nodesInSubgraph;
        
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) != 0) {
                nodesInSubgraph.insert(i);
            }
        }
        
        for (const auto& edge : edges) {
            if (nodesInSubgraph.find(edge[0]) != nodesInSubgraph.end() &&
                nodesInSubgraph.find(edge[1]) != nodesInSubgraph.end()) {
                subgraph[edge[0]].push_back(edge[1]);
                subgraph[edge[1]].push_back(edge[0]);
            }
        }
        
        if (isTree(subgraph)) {
            maxGroups++;
        }
    }
    
    return maxGroups;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n \cdot m)$, where $n$ is the number of nodes and $m$ is the number of edges. This is because we generate all possible combinations of nodes ($2^n$) and for each combination, we check if the subgraph is a tree ($O(n \cdot m)$).
> - **Space Complexity:** $O(n + m)$, where $n$ is the number of nodes and $m$ is the number of edges. This is because we store the subgraph and the visited nodes.
> - **Why these complexities occur:** The brute force approach tries all possible combinations of nodes, which leads to an exponential time complexity. The space complexity is linear because we only store the subgraph and the visited nodes.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: The problem can be solved using a union-find data structure to keep track of the connected components in the graph.
- Detailed breakdown of the approach:
  1. Initialize the union-find data structure with each node as its own parent.
  2. Iterate through the edges and union the nodes if they are not in the same connected component.
  3. Count the number of connected components.
- Proof of optimality: This approach is optimal because it uses a union-find data structure, which has an amortized time complexity of $O(\alpha(n))$, where $\alpha(n)$ is the inverse Ackermann function. This is much faster than the brute force approach.

```cpp
class UnionFind {
public:
    vector<int> parent;
    vector<int> rank;
    
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
        }
    }
};

int maxGroups(int n, vector<vector<int>>& edges) {
    UnionFind uf(n);
    
    for (const auto& edge : edges) {
        uf.unionNodes(edge[0], edge[1]);
    }
    
    unordered_set<int> connectedComponents;
    
    for (int i = 0; i < n; i++) {
        connectedComponents.insert(uf.find(i));
    }
    
    return connectedComponents.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot \alpha(n) + m \cdot \alpha(n))$, where $n$ is the number of nodes and $m$ is the number of edges. This is because we use a union-find data structure, which has an amortized time complexity of $O(\alpha(n))$.
> - **Space Complexity:** $O(n)$, where $n$ is the number of nodes. This is because we store the union-find data structure.
> - **Optimality proof:** This approach is optimal because it uses a union-find data structure, which has an amortized time complexity of $O(\alpha(n))$. This is much faster than the brute force approach.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Union-find data structure, connected components.
- Problem-solving patterns identified: Using a union-find data structure to keep track of connected components.
- Optimization techniques learned: Using a union-find data structure to reduce the time complexity.
- Similar problems to practice: Finding the number of connected components in a graph, checking if a graph is connected.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the union-find data structure correctly, not using the `find` method correctly.
- Edge cases to watch for: Empty graph, graph with a single node.
- Performance pitfalls: Using a brute force approach, not using a union-find data structure.
- Testing considerations: Testing with different graph sizes, testing with different edge densities.