## Maximum Number of K-Divisible Components

**Problem Link:** https://leetcode.com/problems/maximum-number-of-k-divisible-components/description

**Problem Statement:**
- Input format: `n` (number of nodes), `edges` (list of undirected edges), and `k` (divisor)
- Constraints: $1 \leq n \leq 10^5$, $1 \leq k \leq 10^6$, $1 \leq edges.length \leq 10^5$, $1 \leq u, v \leq n$
- Expected output format: The maximum number of connected components that are divisible by `k`
- Key requirements and edge cases to consider: Disjoint sets, graph traversal, divisibility checks
- Example test cases with explanations:
  - A simple connected graph with all nodes divisible by `k`
  - A graph with multiple connected components, some of which are divisible by `k`
  - An empty graph or a graph with no edges

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate over all possible subsets of nodes and check if they form a connected component that is divisible by `k`.
- Step-by-step breakdown of the solution:
  1. Generate all possible subsets of nodes.
  2. For each subset, check if the nodes are connected using a graph traversal algorithm (e.g., DFS).
  3. If the nodes are connected, calculate the sum of the node values and check if it is divisible by `k`.
- Why this approach comes to mind first: It is a straightforward, exhaustive approach that checks all possibilities.

```cpp
#include <iostream>
#include <vector>

using namespace std;

int maxComponents(vector<int>& vals, vector<vector<int>>& edges, int k) {
    int n = vals.size();
    int maxCount = 0;
    
    // Generate all possible subsets of nodes
    for (int mask = 0; mask < (1 << n); mask++) {
        int subsetSum = 0;
        vector<int> subsetNodes;
        
        // Iterate over nodes in the subset
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) != 0) {
                subsetSum += vals[i];
                subsetNodes.push_back(i);
            }
        }
        
        // Check if the subset is connected
        if (isConnected(subsetNodes, edges)) {
            // Check if the subset sum is divisible by k
            if (subsetSum % k == 0) {
                maxCount++;
            }
        }
    }
    
    return maxCount;
}

bool isConnected(vector<int>& subsetNodes, vector<vector<int>>& edges) {
    int n = subsetNodes.size();
    vector<bool> visited(n, false);
    vector<vector<int>> adjList(n);
    
    // Build adjacency list
    for (auto& edge : edges) {
        if (find(subsetNodes.begin(), subsetNodes.end(), edge[0]) != subsetNodes.end() &&
            find(subsetNodes.begin(), subsetNodes.end(), edge[1]) != subsetNodes.end()) {
            adjList[edge[0]].push_back(edge[1]);
            adjList[edge[1]].push_back(edge[0]);
        }
    }
    
    // Perform DFS to check connectivity
    dfs(subsetNodes[0], visited, adjList);
    
    // Check if all nodes in the subset are visited
    for (bool visit : visited) {
        if (!visit) {
            return false;
        }
    }
    
    return true;
}

void dfs(int node, vector<bool>& visited, vector<vector<int>>& adjList) {
    visited[node] = true;
    
    for (int neighbor : adjList[node]) {
        if (!visited[neighbor]) {
            dfs(neighbor, visited, adjList);
        }
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n \cdot (n + m))$, where $n$ is the number of nodes and $m$ is the number of edges. This is due to generating all possible subsets of nodes and performing DFS for each subset.
> - **Space Complexity:** $O(n + m)$, where $n$ is the number of nodes and $m$ is the number of edges. This is due to storing the adjacency list and visited nodes.
> - **Why these complexities occur:** The brute force approach has exponential time complexity due to generating all possible subsets of nodes, and linear space complexity due to storing the adjacency list and visited nodes.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of generating all possible subsets of nodes, we can use a union-find data structure to efficiently find connected components in the graph.
- Detailed breakdown of the approach:
  1. Initialize a union-find data structure with each node as its own set.
  2. Iterate over the edges and union the sets containing the nodes of each edge.
  3. Iterate over the nodes and calculate the sum of the node values for each connected component.
  4. Check if the sum of each connected component is divisible by `k`.
- Proof of optimality: This approach has a time complexity of $O(n + m)$, which is optimal for finding connected components in a graph.

```cpp
#include <iostream>
#include <vector>

using namespace std;

class UnionFind {
public:
    vector<int> parent;
    vector<int> size;
    
    UnionFind(int n) : parent(n), size(n, 1) {
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
        int rootX = find(x);
        int rootY = find(y);
        
        if (rootX != rootY) {
            if (size[rootX] < size[rootY]) {
                parent[rootX] = rootY;
                size[rootY] += size[rootX];
            } else {
                parent[rootY] = rootX;
                size[rootX] += size[rootY];
            }
        }
    }
};

int maxComponents(vector<int>& vals, vector<vector<int>>& edges, int k) {
    int n = vals.size();
    UnionFind uf(n);
    
    // Union sets containing nodes of each edge
    for (auto& edge : edges) {
        uf.unionSets(edge[0], edge[1]);
    }
    
    // Calculate sum of node values for each connected component
    vector<int> componentSums(n, 0);
    for (int i = 0; i < n; i++) {
        int root = uf.find(i);
        componentSums[root] += vals[i];
    }
    
    // Count connected components with sum divisible by k
    int maxCount = 0;
    for (int sum : componentSums) {
        if (sum % k == 0) {
            maxCount++;
        }
    }
    
    return maxCount;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of nodes and $m$ is the number of edges. This is due to iterating over the edges and nodes.
> - **Space Complexity:** $O(n)$, where $n$ is the number of nodes. This is due to storing the union-find data structure.
> - **Optimality proof:** This approach has a time complexity of $O(n + m)$, which is optimal for finding connected components in a graph.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Union-find data structure, graph traversal, divisibility checks
- Problem-solving patterns identified: Using a union-find data structure to efficiently find connected components in a graph
- Optimization techniques learned: Avoiding exponential time complexity by using a union-find data structure instead of generating all possible subsets of nodes
- Similar problems to practice: Finding connected components in a graph, checking if a graph is connected, finding the minimum spanning tree of a graph

**Mistakes to Avoid:**
- Common implementation errors: Not properly initializing the union-find data structure, not correctly implementing the union and find operations
- Edge cases to watch for: Handling the case where the graph is empty or has no edges, handling the case where the sum of a connected component is zero
- Performance pitfalls: Using an exponential time complexity approach instead of a union-find data structure
- Testing considerations: Testing the implementation with different graph structures and edge cases to ensure correctness and efficiency.