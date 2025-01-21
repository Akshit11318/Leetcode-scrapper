## Connecting Cities With Minimum Cost

**Problem Link:** https://leetcode.com/problems/connecting-cities-with-minimum-cost/description

**Problem Statement:**
- Input format: `n` (number of cities) and `connections` (list of edges where each edge is represented as a triplet `[city1, city2, cost]`)
- Constraints: `1 <= n <= 1000`, `0 <= connections.length <= n * (n - 1) / 2`, `1 <= city1, city2 <= n`, `1 <= cost <= 10^5`, and `city1 != city2`
- Expected output format: The minimum cost to connect all cities with roads.
- Key requirements: The graph is not necessarily connected, but the goal is to find the minimum cost to connect all cities if possible.
- Example test cases:
  - For `n = 3` and `connections = [[1,2,5],[1,3,6],[2,3,1]]`, the output should be `6`.
  - For `n = 4` and `connections = [[1,2,3],[3,4,4],[2,3,6],[1,3,2],[1,4,5]]`, the output should be `6`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of roads and calculate the total cost for each combination.
- Step-by-step breakdown of the solution:
  1. Generate all possible subsets of the `connections` list.
  2. For each subset, check if all cities are connected (i.e., the subset forms a spanning tree).
  3. Calculate the total cost of the roads in the subset.
  4. Keep track of the minimum cost found so far.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

// Function to check if all cities are connected
bool isConnected(const std::vector<std::vector<int>>& connections, int n) {
    std::vector<bool> visited(n + 1, false);
    visited[1] = true;
    int count = 1;
    std::vector<std::vector<int>> graph(n + 1);
    for (const auto& connection : connections) {
        graph[connection[0]].push_back(connection[1]);
        graph[connection[1]].push_back(connection[0]);
    }
    std::vector<int> stack = {1};
    while (!stack.empty()) {
        int city = stack.back();
        stack.pop_back();
        for (int neighbor : graph[city]) {
            if (!visited[neighbor]) {
                visited[neighbor] = true;
                stack.push_back(neighbor);
                count++;
            }
        }
    }
    return count == n;
}

int minimumCost(int n, std::vector<std::vector<int>>& connections) {
    int minCost = INT_MAX;
    int totalConnections = connections.size();
    for (int mask = 1; mask < (1 << totalConnections); mask++) {
        std::vector<std::vector<int>> subset;
        for (int i = 0; i < totalConnections; i++) {
            if (mask & (1 << i)) {
                subset.push_back(connections[i]);
            }
        }
        if (isConnected(subset, n)) {
            int cost = 0;
            for (const auto& connection : subset) {
                cost += connection[2];
            }
            minCost = std::min(minCost, cost);
        }
    }
    return minCost == INT_MAX ? -1 : minCost;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{n^2} \cdot n^2)$, where $n$ is the number of cities. This is because we generate all possible subsets of the connections and check each subset.
> - **Space Complexity:** $O(n^2)$, where $n$ is the number of cities. This is because we need to store the graph and the visited array.
> - **Why these complexities occur:** The brute force approach tries all possible combinations of roads, which leads to an exponential time complexity. The space complexity is quadratic due to the storage of the graph and the visited array.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: We can use Kruskal's algorithm to find the minimum spanning tree (MST) of the graph.
- Detailed breakdown of the approach:
  1. Sort the connections by their cost in non-decreasing order.
  2. Initialize a disjoint set data structure to keep track of the connected components.
  3. Iterate through the sorted connections and add each connection to the MST if it does not form a cycle.
  4. Calculate the total cost of the MST.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

// Disjoint set data structure
class UnionFind {
public:
    std::vector<int> parent;
    std::vector<int> rank;

    UnionFind(int n) : parent(n + 1), rank(n + 1, 0) {
        for (int i = 1; i <= n; i++) {
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

int minimumCost(int n, std::vector<std::vector<int>>& connections) {
    std::sort(connections.begin(), connections.end(), [](const std::vector<int>& a, const std::vector<int>& b) {
        return a[2] < b[2];
    });

    UnionFind uf(n);
    int cost = 0;
    int count = 0;
    for (const auto& connection : connections) {
        if (uf.find(connection[0]) != uf.find(connection[1])) {
            uf.unionSet(connection[0], connection[1]);
            cost += connection[2];
            count++;
        }
    }
    return count == n - 1 ? cost : -1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \log n + m \log m)$, where $n$ is the number of cities and $m$ is the number of connections. This is because we sort the connections and use a disjoint set data structure.
> - **Space Complexity:** $O(n + m)$, where $n$ is the number of cities and $m$ is the number of connections. This is because we need to store the disjoint set data structure and the sorted connections.
> - **Optimality proof:** Kruskal's algorithm is guaranteed to find the minimum spanning tree of a graph, which is the optimal solution to the problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Kruskal's algorithm, disjoint set data structure, sorting.
- Problem-solving patterns identified: Using a greedy approach to find the minimum spanning tree.
- Optimization techniques learned: Using a disjoint set data structure to efficiently check for cycles.
- Similar problems to practice: Minimum spanning tree, graph traversal, shortest path.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for cycles when adding connections to the MST.
- Edge cases to watch for: Handling the case where the graph is not connected.
- Performance pitfalls: Using a brute force approach or not optimizing the sorting of connections.
- Testing considerations: Testing the algorithm with different graph structures and edge cases.