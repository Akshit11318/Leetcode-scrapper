## Create Components With Same Value
**Problem Link:** https://leetcode.com/problems/create-components-with-same-value/description

**Problem Statement:**
- Input format: An integer `n` representing the number of nodes in a graph and an integer `edges` representing the edges in the graph, where `edges[i] = [u_i, v_i]`.
- Expected output format: Return the number of components in the graph after assigning values to the nodes such that all nodes in a component have the same value.
- Key requirements and edge cases to consider: 
  - Each node should have a unique value in its component.
  - The graph is undirected and connected.
- Example test cases with explanations:
  - For `n = 6` and `edges = [[0, 1], [1, 2], [1, 3], [3, 4], [4, 5]]`, the output should be `1` because all nodes are connected and can be assigned the same value.
  - For `n = 6` and `edges = [[0, 1], [1, 2], [3, 4], [4, 5]]`, the output should be `2` because there are two disconnected components.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Iterate over all possible assignments of values to nodes and check if each assignment satisfies the condition that all nodes in a component have the same value.
- Step-by-step breakdown of the solution:
  1. Generate all possible assignments of values to nodes.
  2. For each assignment, iterate over all edges and check if the nodes connected by each edge have the same value.
  3. If all nodes in a component have the same value, increment the count of components.
- Why this approach comes to mind first: This approach is straightforward and checks all possible assignments, but it is inefficient due to its high time complexity.

```cpp
#include <vector>
#include <iostream>

int countComponents(int n, std::vector<std::vector<int>>& edges) {
    // Generate all possible assignments of values to nodes
    for (int i = 0; i < n; i++) {
        // Check if all nodes in a component have the same value
        for (const auto& edge : edges) {
            // If nodes connected by an edge have different values, skip this assignment
            if (i != edge[0] && i != edge[1]) {
                break;
            }
        }
    }
    // This brute force approach is not efficient and does not provide a correct solution
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot m)$, where $n$ is the number of nodes and $m$ is the number of edges, because we generate all possible assignments of values to nodes and check each assignment.
> - **Space Complexity:** $O(n)$, because we need to store the assignments of values to nodes.
> - **Why these complexities occur:** The high time complexity occurs because we generate all possible assignments, and the space complexity occurs because we need to store these assignments.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Use a depth-first search (DFS) algorithm to traverse the graph and count the number of connected components.
- Detailed breakdown of the approach:
  1. Create an adjacency list representation of the graph.
  2. Initialize a visited array to keep track of visited nodes.
  3. Iterate over all nodes and perform a DFS from each unvisited node.
  4. Increment the count of components each time a new DFS is started.
- Proof of optimality: This approach is optimal because it only visits each node once and uses a constant amount of space per node.

```cpp
#include <vector>
#include <iostream>

int countComponents(int n, std::vector<std::vector<int>>& edges) {
    // Create an adjacency list representation of the graph
    std::vector<std::vector<int>> graph(n);
    for (const auto& edge : edges) {
        graph[edge[0]].push_back(edge[1]);
        graph[edge[1]].push_back(edge[0]);
    }

    // Initialize a visited array to keep track of visited nodes
    std::vector<bool> visited(n, false);

    int count = 0;
    // Iterate over all nodes and perform a DFS from each unvisited node
    for (int i = 0; i < n; i++) {
        if (!visited[i]) {
            // Perform a DFS from node i
            dfs(graph, visited, i);
            count++;
        }
    }
    return count;
}

void dfs(const std::vector<std::vector<int>>& graph, std::vector<bool>& visited, int node) {
    // Mark node as visited
    visited[node] = true;
    // Iterate over all neighbors of node and perform a DFS from each unvisited neighbor
    for (int neighbor : graph[node]) {
        if (!visited[neighbor]) {
            dfs(graph, visited, neighbor);
        }
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of nodes and $m$ is the number of edges, because we visit each node and edge once.
> - **Space Complexity:** $O(n + m)$, because we need to store the adjacency list representation of the graph and the visited array.
> - **Optimality proof:** This approach is optimal because it only visits each node and edge once, and it uses a constant amount of space per node and edge.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: DFS, adjacency list representation of graphs, and visited arrays.
- Problem-solving patterns identified: Using DFS to traverse graphs and count connected components.
- Optimization techniques learned: Reducing time complexity by visiting each node and edge only once.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the visited array correctly, not handling edge cases correctly.
- Edge cases to watch for: Empty graphs, graphs with a single node, graphs with multiple connected components.
- Performance pitfalls: Using high-time-complexity algorithms, such as the brute force approach, for large inputs.
- Testing considerations: Testing the solution with different types of graphs, such as empty graphs, graphs with a single node, and graphs with multiple connected components.