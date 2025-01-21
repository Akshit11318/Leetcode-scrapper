## Critical Connections in a Network
**Problem Link:** https://leetcode.com/problems/critical-connections-in-a-network/description

**Problem Statement:**
- Input format and constraints: The input is a list of edges in the network, where each edge is represented as an array `[u, v]`, and the number of nodes `n` in the network.
- Expected output format: The output should be a list of critical connections, where each critical connection is represented as an array `[u, v]`.
- Key requirements and edge cases to consider: The graph is connected and has `n` nodes labeled from 1 to `n`. Each edge is unique and is represented as an array `[u, v]`. The graph does not have self-loops or multiple edges between any two nodes.
- Example test cases with explanations:
  - Example 1: Input: `n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]`, Output: `[[1,3]]`. Explanation: The connection between node 1 and node 3 is critical because if it is removed, the network will be disconnected.
  - Example 2: Input: `n = 2, connections = [[0,1]]`, Output: `[[0,1]]`. Explanation: The connection between node 0 and node 1 is critical because it is the only connection in the network.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to iterate over all possible connections in the network and check if removing each connection would disconnect the network.
- Step-by-step breakdown of the solution:
  1. Create an adjacency list representation of the graph.
  2. Iterate over all edges in the graph.
  3. For each edge, remove it from the graph and check if the graph is still connected using a depth-first search (DFS) or breadth-first search (BFS) algorithm.
  4. If the graph is not connected, add the edge to the list of critical connections.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, but it has a high time complexity due to the repeated removal and addition of edges.

```cpp
vector<vector<int>> criticalConnections(int n, vector<vector<int>>& connections) {
    vector<vector<int>> graph(n);
    for (auto& connection : connections) {
        graph[connection[0]].push_back(connection[1]);
        graph[connection[1]].push_back(connection[0]);
    }
    
    vector<vector<int>> critical;
    for (auto& connection : connections) {
        // Remove the edge from the graph
        graph[connection[0]].erase(remove(graph[connection[0]].begin(), graph[connection[0]].end(), connection[1]), graph[connection[0]].end());
        graph[connection[1]].erase(remove(graph[connection[1]].begin(), graph[connection[1]].end(), connection[0]), graph[connection[1]].end());
        
        // Check if the graph is still connected
        vector<bool> visited(n, false);
        visited[0] = true;
        stack<int> s;
        s.push(0);
        while (!s.empty()) {
            int node = s.top();
            s.pop();
            for (int neighbor : graph[node]) {
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    s.push(neighbor);
                }
            }
        }
        
        // If the graph is not connected, add the edge to the list of critical connections
        if (!all_of(visited.begin(), visited.end(), [](bool b) { return b; })) {
            critical.push_back(connection);
        }
        
        // Add the edge back to the graph
        graph[connection[0]].push_back(connection[1]);
        graph[connection[1]].push_back(connection[0]);
    }
    
    return critical;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot (n + m))$, where $n$ is the number of nodes and $m$ is the number of edges. This is because we are iterating over all edges and for each edge, we are performing a DFS or BFS traversal of the graph.
> - **Space Complexity:** $O(n + m)$, where $n$ is the number of nodes and $m$ is the number of edges. This is because we are storing the adjacency list representation of the graph.
> - **Why these complexities occur:** The time complexity is high because we are performing a DFS or BFS traversal of the graph for each edge. The space complexity is reasonable because we are storing the adjacency list representation of the graph.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a depth-first search (DFS) algorithm with a timer to keep track of the discovery time and the low value of each node. The low value of a node is the smallest discovery time that can be reached from the node.
- Detailed breakdown of the approach:
  1. Create an adjacency list representation of the graph.
  2. Initialize the discovery time and the low value of each node to infinity.
  3. Perform a DFS traversal of the graph, starting from node 0.
  4. For each node, update its discovery time and low value.
  5. For each edge, check if it is a critical connection by comparing the discovery time and the low value of the two nodes.
- Proof of optimality: This approach is optimal because it only requires a single DFS traversal of the graph, and it uses a timer to keep track of the discovery time and the low value of each node.

```cpp
vector<vector<int>> criticalConnections(int n, vector<vector<int>>& connections) {
    vector<vector<int>> graph(n);
    for (auto& connection : connections) {
        graph[connection[0]].push_back(connection[1]);
        graph[connection[1]].push_back(connection[0]);
    }
    
    vector<vector<int>> critical;
    vector<int> discovery(n, -1);
    vector<int> low(n, -1);
    int time = 0;
    function<void(int, int)> dfs = [&](int node, int parent) {
        discovery[node] = low[node] = time++;
        for (int neighbor : graph[node]) {
            if (discovery[neighbor] == -1) {
                dfs(neighbor, node);
                low[node] = min(low[node], low[neighbor]);
                if (low[neighbor] > discovery[node]) {
                    critical.push_back({node, neighbor});
                }
            } else if (neighbor != parent) {
                low[node] = min(low[node], discovery[neighbor]);
            }
        }
    };
    dfs(0, -1);
    
    return critical;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of nodes and $m$ is the number of edges. This is because we are performing a single DFS traversal of the graph.
> - **Space Complexity:** $O(n + m)$, where $n$ is the number of nodes and $m$ is the number of edges. This is because we are storing the adjacency list representation of the graph and the discovery time and low value of each node.
> - **Optimality proof:** This approach is optimal because it only requires a single DFS traversal of the graph, and it uses a timer to keep track of the discovery time and the low value of each node.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: DFS traversal, timer-based approach.
- Problem-solving patterns identified: Using a timer to keep track of the discovery time and the low value of each node.
- Optimization techniques learned: Reducing the time complexity by performing a single DFS traversal of the graph.
- Similar problems to practice: Finding strongly connected components, finding bridges in a graph.

**Mistakes to Avoid:**
- Common implementation errors: Not updating the discovery time and low value of each node correctly.
- Edge cases to watch for: Handling the case where the graph is not connected.
- Performance pitfalls: Using a brute force approach that has a high time complexity.
- Testing considerations: Testing the code with different input cases, including large graphs and graphs with multiple connected components.