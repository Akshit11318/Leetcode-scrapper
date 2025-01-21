## Checking Existence of Edge Length Limited Paths
**Problem Link:** https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/description

**Problem Statement:**
- Input format: An integer `n` representing the number of nodes in a graph and an integer `m` representing the number of edges. Each edge is represented by three integers: `u`, `v`, and `w`, where `u` and `v` are the nodes connected by the edge and `w` is the weight of the edge. 
- Expected output format: A boolean array of size `q`, where `q` is the number of queries, indicating whether there exists a path between two nodes with a weight limit.
- Key requirements and edge cases to consider: The graph is undirected and may contain multiple edges between the same pair of nodes. Each query is represented by three integers: `u`, `v`, and `limit`, where `u` and `v` are the nodes to check for a path and `limit` is the maximum weight of the path.
- Example test cases with explanations:
  - For a graph with nodes 1, 2, and 3, and edges (1, 2, 3) and (2, 3, 4), a query (1, 3, 5) should return true because there exists a path from 1 to 3 with a total weight less than or equal to 5.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The most straightforward way to solve this problem is to use a brute force approach by iterating through all possible paths between two nodes and checking if the total weight of each path is within the given limit.
- Step-by-step breakdown of the solution:
  1. Create an adjacency list representation of the graph.
  2. For each query, use a depth-first search (DFS) or breadth-first search (BFS) to find all possible paths between the given nodes.
  3. For each path, calculate the total weight and check if it is within the given limit.
  4. If a path is found with a total weight within the limit, return true. If no such path is found after checking all possible paths, return false.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, but it is inefficient for large graphs due to its high time complexity.

```cpp
#include <vector>
#include <queue>
using namespace std;

bool dfs(vector<vector<pair<int, int>>>& graph, int u, int v, int limit, vector<bool>& visited) {
    if (u == v) return true;
    visited[u] = true;
    for (auto& edge : graph[u]) {
        int neighbor = edge.first;
        int weight = edge.second;
        if (!visited[neighbor] && weight <= limit) {
            if (dfs(graph, neighbor, v, limit - weight, visited)) return true;
        }
    }
    return false;
}

vector<bool> distanceLimitedPathsExist(int n, vector<vector<int>>& edgeList, vector<vector<int>>& queries) {
    vector<vector<pair<int, int>>> graph(n);
    for (auto& edge : edgeList) {
        int u = edge[0];
        int v = edge[1];
        int w = edge[2];
        graph[u].emplace_back(v, w);
        graph[v].emplace_back(u, w); // For undirected graph
    }
    vector<bool> result;
    for (auto& query : queries) {
        int u = query[0];
        int v = query[1];
        int limit = query[2];
        vector<bool> visited(n, false);
        result.push_back(dfs(graph, u, v, limit, visited));
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(q \cdot n \cdot m)$ where $q$ is the number of queries, $n$ is the number of nodes, and $m$ is the number of edges. This is because in the worst case, we might have to traverse all edges for each query.
> - **Space Complexity:** $O(n + m)$ for storing the graph and $O(n)$ for the recursion stack, where $n$ is the number of nodes and $m$ is the number of edges.
> - **Why these complexities occur:** The high time complexity is due to the brute force nature of checking all possible paths for each query.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of checking all possible paths for each query, we can use a more efficient algorithm like Dijkstra's or Bellman-Ford to find the shortest path between two nodes. However, since we are dealing with a limit on the path weight, we need to modify our approach to directly address the limit constraint.
- Detailed breakdown of the approach:
  1. Sort the queries by their limit in ascending order.
  2. Sort the edges by their weight in ascending order.
  3. Use a union-find data structure to keep track of connected components as we add edges.
  4. Iterate through the sorted edges, adding each edge to the graph and checking if it connects the nodes of the current query. If it does, mark the query as having a path within the limit.
- Proof of optimality: This approach is optimal because it ensures that we only consider edges that could potentially be part of a path within the limit for each query, thus minimizing unnecessary computations.

```cpp
#include <vector>
#include <queue>
using namespace std;

struct UnionFind {
    vector<int> parent;
    UnionFind(int n) : parent(n) {
        for (int i = 0; i < n; ++i) parent[i] = i;
    }
    int find(int x) {
        if (parent[x] != x) parent[x] = find(parent[x]);
        return parent[x];
    }
    void unite(int x, int y) {
        parent[find(x)] = find(y);
    }
};

vector<bool> distanceLimitedPathsExist(int n, vector<vector<int>>& edgeList, vector<vector<int>>& queries) {
    vector<vector<int>> queriesWithIndex;
    for (int i = 0; i < queries.size(); ++i) {
        queriesWithIndex.push_back({queries[i][0], queries[i][1], queries[i][2], i});
    }
    sort(queriesWithIndex.begin(), queriesWithIndex.end(), [](const vector<int>& a, const vector<int>& b) {
        return a[2] < b[2];
    });
    sort(edgeList.begin(), edgeList.end(), [](const vector<int>& a, const vector<int>& b) {
        return a[2] < b[2];
    });
    UnionFind uf(n);
    vector<bool> result(queries.size(), false);
    int edgeIndex = 0;
    for (auto& query : queriesWithIndex) {
        int u = query[0];
        int v = query[1];
        int limit = query[2];
        int index = query[3];
        while (edgeIndex < edgeList.size() && edgeList[edgeIndex][2] <= limit) {
            int x = edgeList[edgeIndex][0];
            int y = edgeList[edgeIndex][1];
            uf.unite(x, y);
            edgeIndex++;
        }
        if (uf.find(u) == uf.find(v)) result[index] = true;
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(q \log q + m \log m + q + m)$ due to sorting queries and edges, and then iterating through them once. $q$ is the number of queries and $m$ is the number of edges.
> - **Space Complexity:** $O(n + m)$ for storing the union-find data structure and the sorted queries and edges.
> - **Optimality proof:** This approach is optimal because it minimizes the number of operations required to determine if a path exists within the given limit for each query, leveraging the properties of the union-find data structure and the sorting of queries and edges.