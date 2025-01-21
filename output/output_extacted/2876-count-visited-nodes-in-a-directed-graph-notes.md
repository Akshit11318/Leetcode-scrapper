## Count Visited Nodes in a Directed Graph

**Problem Link:** https://leetcode.com/problems/count-visited-nodes-in-a-directed-graph/description

**Problem Statement:**
- Input format: An integer `n` representing the number of nodes in the graph, a list of edges `edges` where each edge is a pair of integers `(u, v)` representing a directed edge from `u` to `v`, and a list of nodes `visited` which are initially visited.
- Constraints: `1 <= n <= 10^5`, `0 <= edges.length <= 10^5`, `1 <= visited.length <= n`.
- Expected output format: The number of nodes that can be visited.
- Key requirements and edge cases to consider: 
    - All nodes are numbered from 0 to `n - 1`.
    - The graph may contain cycles.
    - Initially, only nodes in the `visited` list are visited.
- Example test cases with explanations:
    - For `n = 3`, `edges = [[0, 1], [0, 2], [1, 2]]`, `visited = [0]`, the output is 3 because starting from node 0, all nodes can be visited.
    - For `n = 3`, `edges = [[0, 1], [1, 2], [2, 0]]`, `visited = [0]`, the output is 3 because all nodes can be visited from node 0.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Start from each visited node and perform a depth-first search (DFS) or breadth-first search (BFS) to find all reachable nodes.
- Step-by-step breakdown of the solution:
    1. Create an adjacency list representation of the graph.
    2. For each visited node, perform a DFS or BFS to mark all reachable nodes as visited.
    3. Count the total number of visited nodes.
- Why this approach comes to mind first: It directly addresses the problem by simulating the process of visiting nodes from the given starting points.

```cpp
#include <vector>
#include <queue>
using namespace std;

int countVisitedNodes(int n, vector<vector<int>>& edges, vector<int>& visited) {
    // Create adjacency list
    vector<vector<int>> graph(n);
    for (auto& edge : edges) {
        graph[edge[0]].push_back(edge[1]);
    }

    // Initialize visited set
    vector<bool> isVisited(n, false);
    for (int node : visited) {
        isVisited[node] = true;
    }

    // Perform BFS from each visited node
    queue<int> q;
    for (int node : visited) {
        q.push(node);
    }
    while (!q.empty()) {
        int node = q.front();
        q.pop();
        for (int neighbor : graph[node]) {
            if (!isVisited[neighbor]) {
                isVisited[neighbor] = true;
                q.push(neighbor);
            }
        }
    }

    // Count visited nodes
    int count = 0;
    for (bool visit : isVisited) {
        if (visit) count++;
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$ where $n$ is the number of nodes and $m$ is the number of edges, because we visit each node and edge once.
> - **Space Complexity:** $O(n + m)$ for storing the adjacency list and the visited set.
> - **Why these complexities occur:** The time complexity is linear because we perform a constant amount of work for each node and edge. The space complexity is also linear because in the worst case, we might need to store all nodes and edges in our data structures.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The problem can be solved using a single pass of DFS or BFS from all visited nodes simultaneously, similar to the brute force approach. However, we can optimize the solution by directly counting the reachable nodes without needing to explicitly mark them as visited in a separate step.
- Detailed breakdown of the approach:
    1. Create an adjacency list representation of the graph.
    2. Initialize a count of visited nodes.
    3. Perform DFS or BFS from all visited nodes, incrementing the count for each newly reachable node.
- Proof of optimality: This approach is optimal because it visits each node and edge at most once, resulting in a linear time complexity.

```cpp
#include <vector>
#include <queue>
using namespace std;

int countVisitedNodes(int n, vector<vector<int>>& edges, vector<int>& visited) {
    // Create adjacency list
    vector<vector<int>> graph(n);
    for (auto& edge : edges) {
        graph[edge[0]].push_back(edge[1]);
    }

    // Perform BFS from all visited nodes
    vector<bool> isVisited(n, false);
    for (int node : visited) {
        isVisited[node] = true;
    }
    queue<int> q;
    for (int node : visited) {
        q.push(node);
    }
    int count = visited.size(); // Count visited nodes
    while (!q.empty()) {
        int node = q.front();
        q.pop();
        for (int neighbor : graph[node]) {
            if (!isVisited[neighbor]) {
                isVisited[neighbor] = true;
                q.push(neighbor);
                count++; // Increment count for new node
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of nodes and $m$ is the number of edges, because we visit each node and edge once.
> - **Space Complexity:** $O(n + m)$ for storing the adjacency list and the visited set.
> - **Optimality proof:** This approach is optimal because it achieves the best possible time complexity for this problem by visiting each node and edge at most once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Graph traversal (DFS, BFS), adjacency list representation.
- Problem-solving patterns identified: Using graph traversal to find reachable nodes.
- Optimization techniques learned: Avoiding unnecessary work by directly counting reachable nodes.
- Similar problems to practice: Other graph traversal problems, such as finding connected components or the shortest path.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle edge cases (e.g., empty graph, no visited nodes).
- Edge cases to watch for: Graphs with cycles, self-loops, or isolated nodes.
- Performance pitfalls: Using inefficient data structures (e.g., adjacency matrix for sparse graphs).
- Testing considerations: Thoroughly testing with various graph structures and visited node sets.