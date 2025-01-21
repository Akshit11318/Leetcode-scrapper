## Minimum Number of Vertices to Reach All Nodes
**Problem Link:** https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/description

**Problem Statement:**
- Input format: An integer `n` representing the number of nodes in the graph, and a 2D array `edges` representing the edges between nodes.
- Constraints: `1 <= n <= 10^5`, `0 <= edges.length <= n - 1`, `edges[i].length == 2`, `0 <= edges[i][0], edges[i][1] < n`.
- Expected output format: A list of integers representing the minimum number of vertices to reach all nodes.
- Key requirements and edge cases to consider: The graph is represented as an undirected graph, and each edge is a list of two integers representing the nodes connected by the edge.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Start by considering all possible combinations of nodes and checking if they can reach all other nodes.
- Step-by-step breakdown of the solution:
  1. Initialize an empty list to store the result.
  2. Iterate over all possible combinations of nodes.
  3. For each combination, check if it can reach all other nodes by performing a depth-first search (DFS) or breadth-first search (BFS) from each node in the combination.
  4. If the combination can reach all other nodes, add it to the result list.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it is not efficient for large inputs due to its exponential time complexity.

```cpp
#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

void dfs(int node, vector<vector<int>>& graph, unordered_set<int>& visited) {
    visited.insert(node);
    for (int neighbor : graph[node]) {
        if (visited.find(neighbor) == visited.end()) {
            dfs(neighbor, graph, visited);
        }
    }
}

vector<int> findSmallestSetOfVertices(int n, vector<vector<int>>& edges) {
    vector<vector<int>> graph(n);
    for (auto& edge : edges) {
        graph[edge[0]].push_back(edge[1]);
        graph[edge[1]].push_back(edge[0]);
    }

    vector<int> result;
    for (int i = 0; i < n; i++) {
        unordered_set<int> visited;
        dfs(i, graph, visited);
        if (visited.size() == n) {
            result.push_back(i);
        }
    }

    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the number of nodes. This is because we are iterating over all possible combinations of nodes and performing a DFS from each node in the combination.
> - **Space Complexity:** $O(n)$, where $n$ is the number of nodes. This is because we are using a recursive call stack to perform the DFS and an unordered set to keep track of visited nodes.
> - **Why these complexities occur:** The exponential time complexity occurs because we are iterating over all possible combinations of nodes, which has a time complexity of $O(2^n)$. The linear space complexity occurs because we are using a recursive call stack and an unordered set to keep track of visited nodes.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: A node is a vertex if and only if it has no incoming edges. Therefore, we can simply count the number of nodes with no incoming edges.
- Detailed breakdown of the approach:
  1. Initialize a vector to keep track of the in-degree of each node.
  2. Iterate over all edges and increment the in-degree of the destination node.
  3. Iterate over all nodes and add the nodes with in-degree 0 to the result list.
- Proof of optimality: This approach is optimal because it has a time complexity of $O(n + m)$, where $n$ is the number of nodes and $m$ is the number of edges. This is because we are iterating over all edges and nodes once.

```cpp
vector<int> findSmallestSetOfVertices(int n, vector<vector<int>>& edges) {
    vector<int> in_degree(n, 0);
    for (auto& edge : edges) {
        in_degree[edge[1]]++;
    }

    vector<int> result;
    for (int i = 0; i < n; i++) {
        if (in_degree[i] == 0) {
            result.push_back(i);
        }
    }

    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of nodes and $m$ is the number of edges. This is because we are iterating over all edges and nodes once.
> - **Space Complexity:** $O(n)$, where $n$ is the number of nodes. This is because we are using a vector to keep track of the in-degree of each node.
> - **Optimality proof:** This approach is optimal because it has a linear time complexity and uses a minimal amount of space to solve the problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Graph traversal, in-degree calculation.
- Problem-solving patterns identified: Using in-degree to identify vertices in a graph.
- Optimization techniques learned: Reducing the time complexity by using a linear approach instead of an exponential one.
- Similar problems to practice: Finding strongly connected components in a graph, finding the minimum spanning tree of a graph.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing variables, not checking for edge cases.
- Edge cases to watch for: Empty graphs, graphs with no vertices.
- Performance pitfalls: Using exponential time complexity algorithms for large inputs.
- Testing considerations: Testing with small and large inputs, testing with different graph structures.