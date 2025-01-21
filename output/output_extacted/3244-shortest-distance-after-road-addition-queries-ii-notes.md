## Shortest Distance After Road Addition Queries II
**Problem Link:** https://leetcode.com/problems/shortest-distance-after-road-addition-queries-ii/description

**Problem Statement:**
- Input format: An integer `n` representing the number of nodes, a list of edges `edges` where each edge is represented as a list of two integers, and a list of queries `queries` where each query is a list of three integers.
- Constraints: $2 \leq n \leq 10^5$, $1 \leq m \leq \min(n*(n-1)/2, 10^5)$, and $1 \leq q \leq 10^5$.
- Expected output format: A list of integers representing the shortest distance between each query node and all other nodes after adding roads.
- Key requirements and edge cases to consider: The graph is undirected and connected, and each query adds a road between two nodes.
- Example test cases with explanations: The test cases provide examples of how to calculate the shortest distance between nodes after adding roads.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Calculate the shortest distance between each pair of nodes using Dijkstra's algorithm or Floyd-Warshall algorithm.
- Step-by-step breakdown of the solution:
  1. Create an adjacency list representation of the graph.
  2. For each query, add the new road to the graph.
  3. Calculate the shortest distance between each pair of nodes using Dijkstra's algorithm or Floyd-Warshall algorithm.
- Why this approach comes to mind first: It is a straightforward approach that uses well-known algorithms for calculating shortest distances.

```cpp
#include <vector>
#include <queue>
#include <limits>

using namespace std;

const int INF = numeric_limits<int>::max();

vector<vector<int>> shortestDistance(int n, vector<vector<int>>& edges, vector<vector<int>>& queries) {
    vector<vector<int>> graph(n, vector<int>(n, INF));
    for (int i = 0; i < n; i++) {
        graph[i][i] = 0;
    }
    for (const auto& edge : edges) {
        int u = edge[0], v = edge[1];
        graph[u][v] = graph[v][u] = 1;
    }
    for (int k = 0; k < n; k++) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j]);
            }
        }
    }
    vector<vector<int>> result;
    for (const auto& query : queries) {
        int u = query[0], v = query[1];
        graph[u][v] = graph[v][u] = 1;
        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j]);
                }
            }
        }
        vector<int> distances;
        for (int i = 0; i < n; i++) {
            distances.push_back(graph[query[2]][i]);
        }
        result.push_back(distances);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3 \cdot q)$, where $n$ is the number of nodes and $q$ is the number of queries. This is because we are using the Floyd-Warshall algorithm to calculate the shortest distances between all pairs of nodes for each query.
> - **Space Complexity:** $O(n^2)$, where $n$ is the number of nodes. This is because we are storing the adjacency matrix of the graph.
> - **Why these complexities occur:** The time complexity occurs because we are using a cubic algorithm to calculate the shortest distances between all pairs of nodes. The space complexity occurs because we are storing the adjacency matrix of the graph.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We can use a union-find data structure to keep track of the connected components of the graph. When a new road is added, we can update the distances between the nodes in the same connected component.
- Detailed breakdown of the approach:
  1. Create a union-find data structure to keep track of the connected components of the graph.
  2. For each query, add the new road to the graph and update the distances between the nodes in the same connected component.
- Proof of optimality: The optimal solution has a time complexity of $O(n \cdot \alpha(n) \cdot q)$, where $n$ is the number of nodes, $\alpha(n)$ is the inverse Ackermann function, and $q$ is the number of queries. This is because we are using a union-find data structure to keep track of the connected components of the graph, which has an amortized time complexity of $O(\alpha(n))$ per operation.

```cpp
#include <vector>

using namespace std;

class UnionFind {
public:
    vector<int> parent;
    vector<int> rank;
    vector<int> distance;

    UnionFind(int n) : parent(n), rank(n, 0), distance(n, 0) {
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
    }

    int find(int x) {
        if (parent[x] != x) {
            int root = find(parent[x]);
            distance[x] += distance[parent[x]];
            parent[x] = root;
        }
        return parent[x];
    }

    void union_(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX != rootY) {
            if (rank[rootX] < rank[rootY]) {
                parent[rootX] = rootY;
                distance[rootX] = distance[y] - distance[x];
            } else if (rank[rootX] > rank[rootY]) {
                parent[rootY] = rootX;
                distance[rootY] = distance[x] - distance[y];
            } else {
                parent[rootY] = rootX;
                distance[rootY] = distance[x] - distance[y];
                rank[rootX]++;
            }
        }
    }

    int getDistance(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX != rootY) {
            return -1;
        }
        return distance[x] - distance[y];
    }
};

vector<vector<int>> shortestDistance(int n, vector<vector<int>>& edges, vector<vector<int>>& queries) {
    UnionFind uf(n);
    for (const auto& edge : edges) {
        uf.union_(edge[0], edge[1]);
    }
    vector<vector<int>> result;
    for (const auto& query : queries) {
        uf.union_(query[0], query[1]);
        vector<int> distances;
        for (int i = 0; i < n; i++) {
            distances.push_back(uf.getDistance(query[2], i));
        }
        result.push_back(distances);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot \alpha(n) \cdot q)$, where $n$ is the number of nodes, $\alpha(n)$ is the inverse Ackermann function, and $q$ is the number of queries. This is because we are using a union-find data structure to keep track of the connected components of the graph, which has an amortized time complexity of $O(\alpha(n))$ per operation.
> - **Space Complexity:** $O(n)$, where $n$ is the number of nodes. This is because we are storing the parent, rank, and distance arrays of the union-find data structure.
> - **Optimality proof:** The optimal solution has a time complexity of $O(n \cdot \alpha(n) \cdot q)$, which is the best possible time complexity for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Union-find data structure, inverse Ackermann function.
- Problem-solving patterns identified: Using a union-find data structure to keep track of connected components, updating distances between nodes in the same connected component.
- Optimization techniques learned: Using a union-find data structure to reduce the time complexity of the algorithm.
- Similar problems to practice: Other problems that involve using a union-find data structure to solve graph problems.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the parent, rank, and distance arrays correctly, not updating the distances between nodes in the same connected component correctly.
- Edge cases to watch for: The case where two nodes are already in the same connected component, the case where a node is not connected to any other node.
- Performance pitfalls: Using a slow algorithm to calculate the shortest distances between nodes, not using a union-find data structure to keep track of connected components.
- Testing considerations: Testing the algorithm with different inputs, including edge cases, to ensure that it is working correctly.