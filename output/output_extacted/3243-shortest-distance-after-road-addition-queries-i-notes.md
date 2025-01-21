## Shortest Distance After Road Addition Queries I

**Problem Link:** https://leetcode.com/problems/shortest-distance-after-road-addition-queries-i/description

**Problem Statement:**
- Input format and constraints: The input consists of `n` cities, represented as nodes in a graph, and `edges` representing the roads between these cities. Each edge is weighted with a distance. The query consists of adding a new road between two cities and finding the shortest distance between all pairs of cities after the addition.
- Expected output format: The output should be a list of shortest distances between all pairs of cities after each query.
- Key requirements and edge cases to consider: The graph may contain negative weight edges, but not negative cycles. The addition of a new road should be considered for each query separately.
- Example test cases with explanations: For instance, given `n = 5`, `edges = [[0,1,10],[1,2,5],[2,3,15],[3,4,10]]`, and `queries = [[0,4,1],[1,3,1]]`, the output should be the shortest distances between all pairs of cities after each query.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to use Dijkstra's algorithm to find the shortest path between all pairs of cities before and after each query. This involves recalculating the shortest paths for all pairs of cities after each query.
- Step-by-step breakdown of the solution:
  1. Initialize the distance matrix with infinite values for all pairs of cities.
  2. For each edge, update the distance matrix with the edge's weight if the edge connects two cities directly.
  3. Apply Dijkstra's algorithm to find the shortest paths between all pairs of cities before each query.
  4. After each query, update the distance matrix with the new road's weight and reapply Dijkstra's algorithm to find the new shortest paths.
- Why this approach comes to mind first: It is a straightforward application of Dijkstra's algorithm to find the shortest paths in a weighted graph.

```cpp
#include <vector>
#include <queue>
#include <limits>

using namespace std;

const int INF = numeric_limits<int>::max();

struct Edge {
    int u, v, w;
};

vector<vector<int>> shortestDistanceAfterRoadAddition(int n, vector<vector<int>>& edges, vector<vector<int>>& queries) {
    vector<vector<int>> dist(n, vector<int>(n, INF));
    for (int i = 0; i < n; i++) dist[i][i] = 0;
    
    // Initialize distance matrix with edge weights
    for (const auto& edge : edges) {
        dist[edge[0]][edge[1]] = edge[2];
        dist[edge[1]][edge[0]] = edge[2];
    }
    
    // Apply Dijkstra's algorithm for each query
    vector<vector<int>> results;
    for (const auto& query : queries) {
        // Update distance matrix with new road
        dist[query[0]][query[1]] = query[2];
        dist[query[1]][query[0]] = query[2];
        
        // Apply Dijkstra's algorithm
        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (dist[i][k] != INF && dist[k][j] != INF) {
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
                    }
                }
            }
        }
        
        results.push_back(dist[0]);
    }
    
    return results;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(q \cdot n^3)$, where $q$ is the number of queries and $n$ is the number of cities. This is because we apply Dijkstra's algorithm for each query, and Dijkstra's algorithm has a time complexity of $O(n^2)$ in this implementation.
> - **Space Complexity:** $O(n^2)$, as we need to store the distance matrix.
> - **Why these complexities occur:** The brute force approach involves recalculating the shortest paths for all pairs of cities after each query, resulting in high time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use Floyd-Warshall algorithm to find the shortest paths between all pairs of cities in $O(n^3)$ time complexity. This algorithm is more efficient than the brute force approach because it only needs to be applied once for all queries.
- Detailed breakdown of the approach:
  1. Initialize the distance matrix with infinite values for all pairs of cities.
  2. Update the distance matrix with the edge weights.
  3. Apply Floyd-Warshall algorithm to find the shortest paths between all pairs of cities.
  4. For each query, update the distance matrix with the new road's weight and apply Floyd-Warshall algorithm again.
- Proof of optimality: The Floyd-Warshall algorithm has a time complexity of $O(n^3)$, which is optimal for finding the shortest paths between all pairs of cities in a weighted graph.

```cpp
vector<vector<int>> shortestDistanceAfterRoadAddition(int n, vector<vector<int>>& edges, vector<vector<int>>& queries) {
    vector<vector<int>> dist(n, vector<int>(n, INF));
    for (int i = 0; i < n; i++) dist[i][i] = 0;
    
    // Initialize distance matrix with edge weights
    for (const auto& edge : edges) {
        dist[edge[0]][edge[1]] = edge[2];
        dist[edge[1]][edge[0]] = edge[2];
    }
    
    // Apply Floyd-Warshall algorithm
    for (int k = 0; k < n; k++) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (dist[i][k] != INF && dist[k][j] != INF) {
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
                }
            }
        }
    }
    
    // Apply queries
    vector<vector<int>> results;
    for (const auto& query : queries) {
        // Update distance matrix with new road
        dist[query[0]][query[1]] = query[2];
        dist[query[1]][query[0]] = query[2];
        
        // Apply Floyd-Warshall algorithm again
        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (dist[i][k] != INF && dist[k][j] != INF) {
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
                    }
                }
            }
        }
        
        results.push_back(dist[0]);
    }
    
    return results;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3 + q \cdot n^2)$, where $q$ is the number of queries and $n$ is the number of cities. This is because we apply Floyd-Warshall algorithm once for all queries, and then update the distance matrix and apply Floyd-Warshall algorithm again for each query.
> - **Space Complexity:** $O(n^2)$, as we need to store the distance matrix.
> - **Optimality proof:** The Floyd-Warshall algorithm has a time complexity of $O(n^3)$, which is optimal for finding the shortest paths between all pairs of cities in a weighted graph.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Floyd-Warshall algorithm, Dijkstra's algorithm, and graph theory.
- Problem-solving patterns identified: Using dynamic programming to solve problems with overlapping subproblems.
- Optimization techniques learned: Applying Floyd-Warshall algorithm to reduce time complexity.
- Similar problems to practice: Shortest path problems in weighted graphs, such as `Single Source Shortest Path` and `All Pairs Shortest Path`.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases correctly, such as negative weight edges or negative cycles.
- Edge cases to watch for: Handling queries with new roads that connect two cities directly.
- Performance pitfalls: Not using Floyd-Warshall algorithm, which can result in high time complexity.
- Testing considerations: Testing the implementation with different inputs, including edge cases and large graphs.