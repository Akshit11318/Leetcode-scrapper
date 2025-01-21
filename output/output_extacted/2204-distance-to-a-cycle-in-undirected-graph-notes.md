## Distance to a Cycle in Undirected Graph
**Problem Link:** https://leetcode.com/problems/distance-to-a-cycle-in-undirected-graph/description

**Problem Statement:**
- Given an undirected graph, find the shortest distance from each node to a cycle in the graph.
- Input: `n` (number of nodes), `edges` (list of undirected edges)
- Output: An array of distances, where the value at index `i` represents the shortest distance from node `i` to a cycle in the graph.
- Key requirements:
  - If a node is part of a cycle, its distance is `0`.
  - If a node is not reachable from any cycle, its distance is `-1`.
- Example test cases:
  - `n = 4`, `edges = [[0, 1], [1, 2], [2, 3], [3, 0]]`: The graph contains a cycle involving all nodes, so the output is `[0, 0, 0, 0]`.
  - `n = 4`, `edges = [[0, 1], [1, 2], [2, 3]]`: The graph does not contain a cycle, so the output is `[-1, -1, -1, -1]`.

---

### Brute Force Approach
**Explanation:**
- The initial thought process involves checking every possible path from each node to detect cycles and calculate distances.
- We can use a depth-first search (DFS) or breadth-first search (BFS) to explore the graph from each node.
- We keep track of visited nodes and the current path to detect cycles.

```cpp
#include <vector>
#include <queue>
#include <unordered_set>

std::vector<int> distanceToCycle(int n, std::vector<std::vector<int>>& edges) {
    std::vector<std::vector<int>> graph(n);
    for (const auto& edge : edges) {
        graph[edge[0]].push_back(edge[1]);
        graph[edge[1]].push_back(edge[0]);
    }

    std::vector<int> distances(n, -1);

    for (int i = 0; i < n; ++i) {
        std::unordered_set<int> visited;
        std::queue<std::pair<int, int>> queue; // node, distance
        queue.push({i, 0});
        visited.insert(i);

        while (!queue.empty()) {
            int node = queue.front().first;
            int distance = queue.front().second;
            queue.pop();

            for (int neighbor : graph[node]) {
                if (visited.find(neighbor) == visited.end()) {
                    queue.push({neighbor, distance + 1});
                    visited.insert(neighbor);
                } else if (distance > 0) { // cycle detected
                    distances[i] = distance;
                    break;
                }
            }
            if (distances[i] != -1) break;
        }
    }

    return distances;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot (n + m))$, where $n$ is the number of nodes and $m$ is the number of edges, because in the worst case, we perform a BFS from each node, exploring all edges.
> - **Space Complexity:** $O(n + m)$, for storing the graph and the visited nodes during BFS.
> - **Why these complexities occur:** The brute force approach involves exploring the graph from each node, which leads to high time complexity. The space complexity is due to storing the graph and the visited nodes.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is to detect cycles in the graph first and then perform a BFS from each cycle to calculate the distances.
- We can use a union-find data structure to detect cycles efficiently.
- Once we have detected all cycles, we perform a BFS from each cycle to calculate the distances.

```cpp
#include <vector>
#include <queue>
#include <unordered_set>

class UnionFind {
public:
    std::vector<int> parent;
    std::vector<int> rank;

    UnionFind(int n) : parent(n), rank(n, 0) {
        for (int i = 0; i < n; ++i) {
            parent[i] = i;
        }
    }

    int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    void unionSet(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
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

std::vector<int> distanceToCycle(int n, std::vector<std::vector<int>>& edges) {
    UnionFind uf(n);
    std::vector<std::vector<int>> graph(n);
    std::unordered_set<int> cycleNodes;

    for (const auto& edge : edges) {
        graph[edge[0]].push_back(edge[1]);
        graph[edge[1]].push_back(edge[0]);
        if (uf.find(edge[0]) == uf.find(edge[1])) {
            cycleNodes.insert(edge[0]);
            cycleNodes.insert(edge[1]);
        } else {
            uf.unionSet(edge[0], edge[1]);
        }
    }

    std::vector<int> distances(n, -1);
    for (int node : cycleNodes) {
        distances[node] = 0;
    }

    std::queue<std::pair<int, int>> queue; // node, distance
    for (int node : cycleNodes) {
        queue.push({node, 0});
    }

    while (!queue.empty()) {
        int node = queue.front().first;
        int distance = queue.front().second;
        queue.pop();

        for (int neighbor : graph[node]) {
            if (distances[neighbor] == -1) {
                distances[neighbor] = distance + 1;
                queue.push({neighbor, distance + 1});
            }
        }
    }

    return distances;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of nodes and $m$ is the number of edges, because we perform a union-find operation for each edge and a BFS from each cycle.
> - **Space Complexity:** $O(n + m)$, for storing the graph, the union-find data structure, and the visited nodes during BFS.
> - **Optimality proof:** This approach is optimal because we detect cycles efficiently using a union-find data structure and then calculate distances using a BFS, which has a linear time complexity in terms of the number of nodes and edges.

---

### Final Notes

**Learning Points:**
- The importance of detecting cycles in graphs
- Using union-find data structures for efficient cycle detection
- Performing BFS from each cycle to calculate distances
- Optimizing the brute force approach by using more efficient algorithms and data structures

**Mistakes to Avoid:**
- Not handling edge cases, such as an empty graph or a graph with no cycles
- Not using an efficient data structure for detecting cycles
- Not optimizing the BFS traversal to calculate distances
- Not considering the trade-offs between time and space complexity in the solution.