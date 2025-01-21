## Reachable Nodes With Restrictions

**Problem Link:** https://leetcode.com/problems/reachable-nodes-with-restrictions/description

**Problem Statement:**
- Input format and constraints: Given a graph represented as an adjacency list `edges` and a list of restricted nodes `restricted`, find the number of reachable nodes from a given node `n` and a list of edges `edges` where `edges[i] = [a, b]`.
- Expected output format: The number of reachable nodes.
- Key requirements and edge cases to consider: 
    - A node is considered reachable if there are no restrictions on the path to the node.
    - The graph may contain cycles.
    - The graph may not be connected.
- Example test cases with explanations:
    - Example 1: `n = 7`, `edges = [[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]]`, `restricted = [4,5]`. The number of reachable nodes is 4.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Start by exploring all possible paths from the given node.
- Step-by-step breakdown of the solution:
    1. Create an adjacency list representation of the graph.
    2. Perform a depth-first search (DFS) from each node to explore all reachable nodes.
    3. Keep track of the number of reachable nodes.
- Why this approach comes to mind first: It is a straightforward approach to explore all possible paths in the graph.

```cpp
#include <vector>
#include <unordered_set>

using namespace std;

int reachableNodes(vector<vector<int>>& edges, int n, vector<int>& restricted) {
    // Create an adjacency list representation of the graph
    vector<vector<int>> graph(n);
    for (const auto& edge : edges) {
        graph[edge[0]].push_back(edge[1]);
        graph[edge[1]].push_back(edge[0]);
    }

    // Perform DFS from each node to explore all reachable nodes
    unordered_set<int> visited;
    for (int i = 0; i < n; ++i) {
        if (visited.find(i) == visited.end() && find(restricted.begin(), restricted.end(), i) == restricted.end()) {
            dfs(graph, i, visited, restricted);
        }
    }

    // Return the number of reachable nodes
    return visited.size();
}

void dfs(const vector<vector<int>>& graph, int node, unordered_set<int>& visited, const vector<int>& restricted) {
    visited.insert(node);
    for (int neighbor : graph[node]) {
        if (visited.find(neighbor) == visited.end() && find(restricted.begin(), restricted.end(), neighbor) == restricted.end()) {
            dfs(graph, neighbor, visited, restricted);
        }
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$ where $n$ is the number of nodes and $m$ is the number of edges, since we visit each node and edge once.
> - **Space Complexity:** $O(n + m)$ for the adjacency list representation of the graph and the visited set.
> - **Why these complexities occur:** The time complexity occurs because we perform a DFS traversal of the graph, and the space complexity occurs because we need to store the adjacency list representation of the graph and the visited set.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a single DFS traversal to explore all reachable nodes, starting from node 0.
- Detailed breakdown of the approach:
    1. Create an adjacency list representation of the graph.
    2. Perform a DFS traversal from node 0 to explore all reachable nodes.
    3. Keep track of the number of reachable nodes.
- Proof of optimality: This approach is optimal because we only need to perform a single DFS traversal to explore all reachable nodes.

```cpp
#include <vector>
#include <unordered_set>

using namespace std;

int reachableNodes(vector<vector<int>>& edges, int n, vector<int>& restricted) {
    // Create an adjacency list representation of the graph
    vector<vector<int>> graph(n);
    for (const auto& edge : edges) {
        graph[edge[0]].push_back(edge[1]);
        graph[edge[1]].push_back(edge[0]);
    }

    // Perform DFS traversal from node 0 to explore all reachable nodes
    unordered_set<int> visited;
    dfs(graph, 0, visited, restricted);

    // Return the number of reachable nodes
    return visited.size();
}

void dfs(const vector<vector<int>>& graph, int node, unordered_set<int>& visited, const vector<int>& restricted) {
    visited.insert(node);
    for (int neighbor : graph[node]) {
        if (visited.find(neighbor) == visited.end() && find(restricted.begin(), restricted.end(), neighbor) == restricted.end()) {
            dfs(graph, neighbor, visited, restricted);
        }
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$ where $n$ is the number of nodes and $m$ is the number of edges, since we visit each node and edge once.
> - **Space Complexity:** $O(n + m)$ for the adjacency list representation of the graph and the visited set.
> - **Optimality proof:** This approach is optimal because we only need to perform a single DFS traversal to explore all reachable nodes.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: DFS traversal, adjacency list representation of a graph.
- Problem-solving patterns identified: Using a single DFS traversal to explore all reachable nodes.
- Optimization techniques learned: Reducing the number of DFS traversals from $n$ to 1.
- Similar problems to practice: Graph traversal problems, such as finding the shortest path between two nodes.

**Mistakes to Avoid:**
- Common implementation errors: Not handling the case where a node has no neighbors.
- Edge cases to watch for: Empty graph, graph with no edges.
- Performance pitfalls: Using an inefficient data structure, such as a linked list, to represent the graph.
- Testing considerations: Testing the function with different graph structures, such as a graph with cycles or a graph that is not connected.