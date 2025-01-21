## Minimize the Maximum Edge Weight of Graph
**Problem Link:** https://leetcode.com/problems/minimize-the-maximum-edge-weight-of-graph/description

**Problem Statement:**
- Input format and constraints: Given a graph with `n` nodes and `edges` list of edges where each edge is a list of three integers `[u, v, weight]`, find the minimum maximum edge weight such that the graph remains connected.
- Expected output format: The minimum maximum edge weight.
- Key requirements and edge cases to consider: The graph is undirected, and the weights are positive integers.
- Example test cases with explanations: 
    - For example, given `n = 4`, `edges = [[0,1,10],[0,2,6],[0,3,5],[1,3,15]]`, the output should be `5`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves checking all possible subsets of edges to find the minimum maximum edge weight that keeps the graph connected.
- Step-by-step breakdown of the solution:
    1. Generate all possible subsets of edges.
    2. For each subset, calculate the maximum edge weight.
    3. Check if the graph is connected using the subset of edges.
    4. Update the minimum maximum edge weight if the graph is connected and the maximum edge weight is smaller.
- Why this approach comes to mind first: This approach is straightforward but inefficient due to the exponential number of subsets.

```cpp
class UnionFind {
public:
    vector<int> parent;
    UnionFind(int n) : parent(n) {
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
    void union_(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX != rootY) {
            parent[rootX] = rootY;
        }
    }
};

int minMaxEdgeWeight(int n, vector<vector<int>>& edges) {
    sort(edges.begin(), edges.end(), [](const vector<int>& a, const vector<int>& b) {
        return a[2] < b[2];
    });
    int minMaxWeight = INT_MAX;
    for (int i = 0; i < (1 << edges.size()); i++) {
        UnionFind uf(n);
        int maxWeight = 0;
        for (int j = 0; j < edges.size(); j++) {
            if ((i & (1 << j)) != 0) {
                uf.union_(edges[j][0], edges[j][1]);
                maxWeight = max(maxWeight, edges[j][2]);
            }
        }
        bool connected = true;
        for (int k = 1; k < n; k++) {
            if (uf.find(0) != uf.find(k)) {
                connected = false;
                break;
            }
        }
        if (connected) {
            minMaxWeight = min(minMaxWeight, maxWeight);
        }
    }
    return minMaxWeight;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{m} \cdot (n + m))$, where $m$ is the number of edges and $n$ is the number of nodes, due to the exponential number of subsets and the time complexity of the Union-Find algorithm.
> - **Space Complexity:** $O(n + m)$, for the Union-Find data structure and the subset of edges.
> - **Why these complexities occur:** The brute force approach generates all possible subsets of edges, leading to an exponential time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution involves using a binary search to find the minimum maximum edge weight.
- Detailed breakdown of the approach:
    1. Sort the edges by weight.
    2. Perform a binary search on the range of possible maximum edge weights.
    3. For each mid value, check if the graph is connected using the edges with weight less than or equal to mid.
    4. Update the search range based on the connectivity of the graph.
- Proof of optimality: The binary search approach ensures that we find the minimum maximum edge weight in $O(m \log w)$ time, where $w$ is the maximum weight.

```cpp
class UnionFind {
public:
    vector<int> parent;
    UnionFind(int n) : parent(n) {
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
    void union_(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX != rootY) {
            parent[rootX] = rootY;
        }
    }
};

int minMaxEdgeWeight(int n, vector<vector<int>>& edges) {
    sort(edges.begin(), edges.end(), [](const vector<int>& a, const vector<int>& b) {
        return a[2] < b[2];
    });
    int low = edges[0][2];
    int high = edges.back()[2];
    while (low < high) {
        int mid = (low + high) / 2;
        UnionFind uf(n);
        for (auto& edge : edges) {
            if (edge[2] <= mid) {
                uf.union_(edge[0], edge[1]);
            }
        }
        bool connected = true;
        for (int i = 1; i < n; i++) {
            if (uf.find(0) != uf.find(i)) {
                connected = false;
                break;
            }
        }
        if (connected) {
            high = mid;
        } else {
            low = mid + 1;
        }
    }
    return low;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \log w)$, where $w$ is the maximum weight, due to the binary search and the time complexity of the Union-Find algorithm.
> - **Space Complexity:** $O(n + m)$, for the Union-Find data structure and the edges.
> - **Optimality proof:** The binary search approach ensures that we find the minimum maximum edge weight in the optimal time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Binary search, Union-Find algorithm.
- Problem-solving patterns identified: Using binary search to find the minimum maximum value.
- Optimization techniques learned: Reducing the search space using binary search.
- Similar problems to practice: Finding the minimum spanning tree, finding the maximum flow in a network.

**Mistakes to Avoid:**
- Common implementation errors: Not updating the search range correctly, not handling edge cases.
- Edge cases to watch for: Empty graph, graph with a single node.
- Performance pitfalls: Using an inefficient algorithm, not optimizing the search space.
- Testing considerations: Testing with different graph sizes, testing with different weight ranges.