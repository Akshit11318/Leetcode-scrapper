## Number of Good Paths
**Problem Link:** https://leetcode.com/problems/number-of-good-paths/description

**Problem Statement:**
- Input: `n` representing the number of nodes in the graph and `edges` representing the edges between nodes, and `vals` representing the values of each node.
- Expected Output: The number of `good paths` in the graph, where a `good path` is defined as a path where the values of the two nodes are the same.
- Key Requirements: The solution should be able to handle large inputs and find the number of good paths efficiently.
- Example Test Cases:
  - `n = 3`, `edges = [[0,1],[1,2],[2,0]]`, `vals = [1,1,1]`, Expected Output: `3`
  - `n = 2`, `edges = [[0,1]]`, `vals = [1,2]`, Expected Output: `0`

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to iterate over all possible pairs of nodes in the graph.
- For each pair of nodes, check if there is a path between them.
- If there is a path and the values of the two nodes are the same, increment the count of good paths.
- This approach comes to mind first because it is straightforward to implement, but it is inefficient for large inputs.

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
    void unionNodes(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX != rootY) {
            parent[rootX] = rootY;
        }
    }
};

int numberOfGoodPaths(vector<int>& vals, vector<vector<int>>& edges) {
    int n = vals.size();
    UnionFind uf(n);
    for (auto& edge : edges) {
        uf.unionNodes(edge[0], edge[1]);
    }
    map<int, vector<int>> groups;
    for (int i = 0; i < n; i++) {
        int group = uf.find(i);
        groups[group].push_back(i);
    }
    int goodPaths = 0;
    for (auto& group : groups) {
        map<int, int> count;
        for (int node : group.second) {
            count[vals[node]]++;
        }
        for (auto& pair : count) {
            int freq = pair.second;
            goodPaths += (freq * (freq - 1)) / 2;
        }
    }
    return goodPaths;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$ where $n$ is the number of nodes and $m$ is the number of edges, because we iterate over all nodes and edges once.
> - **Space Complexity:** $O(n)$ because we use a `UnionFind` object to store the parent information of each node.
> - **Why these complexities occur:** The time complexity occurs because we iterate over all nodes and edges once, and the space complexity occurs because we use a `UnionFind` object to store the parent information of each node.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is to use a `UnionFind` object to group nodes with the same value together.
- We use a `map` to store the count of each value in each group.
- We then calculate the number of good paths in each group by counting the number of pairs of nodes with the same value.
- This approach is optimal because it uses a `UnionFind` object to group nodes efficiently, and it uses a `map` to count the number of good paths in each group efficiently.

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
    void unionNodes(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX != rootY) {
            parent[rootX] = rootY;
        }
    }
};

int numberOfGoodPaths(vector<int>& vals, vector<vector<int>>& edges) {
    int n = vals.size();
    UnionFind uf(n);
    for (auto& edge : edges) {
        if (vals[edge[0]] == vals[edge[1]]) {
            uf.unionNodes(edge[0], edge[1]);
        }
    }
    map<int, vector<int>> groups;
    for (int i = 0; i < n; i++) {
        int group = uf.find(i);
        groups[group].push_back(i);
    }
    int goodPaths = 0;
    for (auto& group : groups) {
        map<int, int> count;
        for (int node : group.second) {
            count[vals[node]]++;
        }
        for (auto& pair : count) {
            int freq = pair.second;
            goodPaths += (freq * (freq - 1)) / 2;
        }
    }
    return goodPaths;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$ where $n$ is the number of nodes and $m$ is the number of edges, because we iterate over all nodes and edges once.
> - **Space Complexity:** $O(n)$ because we use a `UnionFind` object to store the parent information of each node.
> - **Optimality proof:** This approach is optimal because it uses a `UnionFind` object to group nodes efficiently, and it uses a `map` to count the number of good paths in each group efficiently.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: `UnionFind`, `map`, and counting pairs of nodes with the same value.
- Problem-solving patterns identified: using a `UnionFind` object to group nodes with the same value together, and using a `map` to count the number of good paths in each group.
- Optimization techniques learned: using a `UnionFind` object to group nodes efficiently, and using a `map` to count the number of good paths in each group efficiently.
- Similar problems to practice: problems involving `UnionFind` and counting pairs of nodes with the same value.

**Mistakes to Avoid:**
- Common implementation errors: not using a `UnionFind` object to group nodes with the same value together, and not using a `map` to count the number of good paths in each group.
- Edge cases to watch for: nodes with the same value but different parents in the `UnionFind` object.
- Performance pitfalls: not using a `UnionFind` object to group nodes efficiently, and not using a `map` to count the number of good paths in each group efficiently.
- Testing considerations: testing the solution with different inputs and edge cases to ensure correctness.