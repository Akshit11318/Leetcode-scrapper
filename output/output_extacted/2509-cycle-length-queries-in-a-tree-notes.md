## Cycle Length Queries in a Tree
**Problem Link:** https://leetcode.com/problems/cycle-length-queries-in-a-tree/description

**Problem Statement:**
- Input: A tree with `n` nodes, and `q` queries, where each query is a pair of nodes `(u, v)`.
- Constraints: `1 <= n <= 10^5`, `1 <= q <= 10^5`.
- Expected output: For each query, find the length of the cycle that contains both `u` and `v`, or return `-1` if no such cycle exists.
- Key requirements and edge cases to consider: 
    - Handling non-existent cycles.
    - Efficiently calculating cycle lengths.
- Example test cases with explanations:
    - For a tree with nodes 1, 2, and 3, where 1 is connected to 2, and 2 is connected to 3, a query `(1, 3)` should return `-1` because there is no cycle.
    - For a tree with nodes 1, 2, 3, and 4, where 1 is connected to 2, 2 is connected to 3, and 3 is connected to 4, and an additional edge from 4 to 1, a query `(1, 3)` should return `4` because the cycle `1 -> 2 -> 3 -> 4 -> 1` has length 4.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: To solve this problem, we can start by checking if there is a path between `u` and `v`. If there is, we can then try to find a cycle that includes both `u` and `v`.
- Step-by-step breakdown of the solution:
    1. Perform a depth-first search (DFS) from `u` to find all reachable nodes.
    2. Perform another DFS from `v` to find all reachable nodes.
    3. Check if the sets of reachable nodes from `u` and `v` intersect. If they do, it means there is a path between `u` and `v`.
    4. If a path exists, try to find a cycle by exploring all possible paths from `u` to `v` and back to `u`.
- Why this approach comes to mind first: It's a straightforward way to explore the tree and check for cycles.

```cpp
vector<vector<int>> graph;
vector<bool> visited;
vector<int> path;

bool dfs(int node, int target) {
    visited[node] = true;
    path.push_back(node);
    if (node == target) return true;
    for (int neighbor : graph[node]) {
        if (!visited[neighbor] && dfs(neighbor, target)) {
            return true;
        }
    }
    path.pop_back();
    return false;
}

int findCycleLength(int u, int v) {
    // Find path from u to v
    path.clear();
    visited.assign(graph.size(), false);
    if (!dfs(u, v)) return -1;

    // Try to find a cycle
    for (int i = 0; i < path.size(); i++) {
        for (int j = i + 1; j < path.size(); j++) {
            if (path[i] == path[j]) {
                // Found a cycle
                return j - i + 1;
            }
        }
    }
    return -1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of nodes in the tree, because in the worst case, we might need to explore all nodes from `u` and `v`.
> - **Space Complexity:** $O(n)$, for storing the visited nodes and the current path.
> - **Why these complexities occur:** The brute force approach involves exploring all possible paths, which leads to high time complexity.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Instead of exploring all possible paths, we can use a more efficient algorithm to find cycles.
- Detailed breakdown of the approach:
    1. Perform a DFS from each node to find all cycles in the tree.
    2. Store the cycles in a data structure that allows for efficient lookup.
    3. For each query, check if there is a cycle that contains both `u` and `v`.
- Proof of optimality: This approach is optimal because it only requires a single pass through the tree to find all cycles, and then it can answer queries in constant time.

```cpp
vector<vector<int>> graph;
vector<bool> visited;
vector<int> path;
set<vector<int>> cycles;

void dfs(int node, int parent) {
    visited[node] = true;
    path.push_back(node);
    for (int neighbor : graph[node]) {
        if (neighbor == parent) continue;
        if (visited[neighbor]) {
            // Found a cycle
            vector<int> cycle;
            int i = path.size() - 1;
            while (path[i] != neighbor) {
                cycle.push_back(path[i]);
                i--;
            }
            cycle.push_back(neighbor);
            cycles.insert(cycle);
        } else {
            dfs(neighbor, node);
        }
    }
    path.pop_back();
}

int findCycleLength(int u, int v) {
    for (auto cycle : cycles) {
        if (find(cycle.begin(), cycle.end(), u) != cycle.end() && find(cycle.begin(), cycle.end(), v) != cycle.end()) {
            return cycle.size();
        }
    }
    return -1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + q)$, where $n$ is the number of nodes in the tree, and $q$ is the number of queries.
> - **Space Complexity:** $O(n)$, for storing the cycles.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the tree to find all cycles, and then it can answer queries in constant time.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: DFS, cycle detection.
- Problem-solving patterns identified: Using a more efficient algorithm to find cycles.
- Optimization techniques learned: Storing cycles in a data structure for efficient lookup.
- Similar problems to practice: Cycle detection in graphs, finding shortest paths.

**Mistakes to Avoid:**
- Common implementation errors: Not handling non-existent cycles.
- Edge cases to watch for: Queries with non-existent nodes.
- Performance pitfalls: Using a brute force approach.
- Testing considerations: Test with different tree structures and query types.