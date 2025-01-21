## Modify Graph Edge Weights
**Problem Link:** https://leetcode.com/problems/modify-graph-edge-weights/description

**Problem Statement:**
- Input format and constraints: Given a graph represented as an adjacency list `n` and `edges`, where `n` is the number of nodes in the graph and `edges` is a list of edges in the graph. Each edge is represented as a list of three integers `[u, v, weight]`, where `u` and `v` are the nodes connected by the edge and `weight` is the weight of the edge. We also have a list of operations `operations`, where each operation is a list of three integers `[u, v, weight]`, representing the modification to be made to the edge between nodes `u` and `v`.
- Expected output format: The modified graph after applying all operations.
- Key requirements and edge cases to consider: If an edge does not exist between two nodes, we need to add it with the given weight. If an edge already exists, we need to update its weight.
- Example test cases with explanations: For example, given a graph with nodes 0, 1, and 2, and edges `[[0, 1, 2], [1, 2, 3]]`, and operations `[[0, 1, 1], [1, 2, 4]]`, the modified graph should have edges `[[0, 1, 1], [1, 2, 4]]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can iterate over each operation and update the corresponding edge in the graph. If the edge does not exist, we add it to the graph.
- Step-by-step breakdown of the solution:
  1. Initialize an empty graph as an adjacency list.
  2. Iterate over each edge in the `edges` list and add it to the graph.
  3. Iterate over each operation in the `operations` list.
  4. For each operation, check if an edge already exists between the two nodes. If it does, update its weight. If not, add a new edge to the graph.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, as it directly implements the problem statement.

```cpp
#include <vector>
#include <unordered_map>

struct Edge {
    int weight;
};

std::vector<std::vector<Edge>> modifyGraph(int n, std::vector<std::vector<int>>& edges, std::vector<std::vector<int>>& operations) {
    std::vector<std::vector<Edge>> graph(n);
    for (const auto& edge : edges) {
        int u = edge[0];
        int v = edge[1];
        int weight = edge[2];
        graph[u].push_back({weight});
        graph[v].push_back({weight}); // Assuming the graph is undirected
    }
    
    for (const auto& operation : operations) {
        int u = operation[0];
        int v = operation[1];
        int weight = operation[2];
        
        // Find the edge between u and v and update its weight
        for (auto& edge : graph[u]) {
            if (edge.weight == weight) {
                edge.weight = weight;
                break;
            }
        }
        
        for (auto& edge : graph[v]) {
            if (edge.weight == weight) {
                edge.weight = weight;
                break;
            }
        }
    }
    
    return graph;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m + k)$, where $n$ is the number of nodes, $m$ is the number of edges, and $k$ is the number of operations. This is because we iterate over each edge and each operation once.
> - **Space Complexity:** $O(n + m)$, where $n$ is the number of nodes and $m$ is the number of edges. This is because we store each edge in the graph.
> - **Why these complexities occur:** The time complexity occurs because we iterate over each edge and each operation. The space complexity occurs because we store each edge in the graph.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use an adjacency list to represent the graph and update the edges in place.
- Detailed breakdown of the approach:
  1. Initialize an empty graph as an adjacency list.
  2. Iterate over each edge in the `edges` list and add it to the graph.
  3. Iterate over each operation in the `operations` list.
  4. For each operation, check if an edge already exists between the two nodes. If it does, update its weight. If not, add a new edge to the graph.
- Why further optimization is impossible: This approach already has the optimal time and space complexity.

```cpp
#include <vector>
#include <unordered_map>

struct Edge {
    int v;
    int weight;
};

std::vector<std::vector<Edge>> modifyGraph(int n, std::vector<std::vector<int>>& edges, std::vector<std::vector<int>>& operations) {
    std::vector<std::vector<Edge>> graph(n);
    for (const auto& edge : edges) {
        int u = edge[0];
        int v = edge[1];
        int weight = edge[2];
        graph[u].push_back({v, weight});
        graph[v].push_back({u, weight}); // Assuming the graph is undirected
    }
    
    for (const auto& operation : operations) {
        int u = operation[0];
        int v = operation[1];
        int weight = operation[2];
        
        // Find the edge between u and v and update its weight
        for (auto& edge : graph[u]) {
            if (edge.v == v) {
                edge.weight = weight;
                break;
            }
        }
        
        for (auto& edge : graph[v]) {
            if (edge.v == u) {
                edge.weight = weight;
                break;
            }
        }
    }
    
    return graph;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m + k)$, where $n$ is the number of nodes, $m$ is the number of edges, and $k$ is the number of operations. This is because we iterate over each edge and each operation once.
> - **Space Complexity:** $O(n + m)$, where $n$ is the number of nodes and $m$ is the number of edges. This is because we store each edge in the graph.
> - **Optimality proof:** This approach already has the optimal time and space complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Graph representation using adjacency lists, updating edges in a graph.
- Problem-solving patterns identified: Iterating over each edge and each operation to update the graph.
- Optimization techniques learned: Using an adjacency list to represent the graph and updating edges in place.
- Similar problems to practice: Graph problems that involve updating edges or nodes.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if an edge already exists before adding a new one.
- Edge cases to watch for: When the graph is empty or when there are no operations.
- Performance pitfalls: Using a slow data structure to represent the graph.
- Testing considerations: Testing the function with different inputs and edge cases.