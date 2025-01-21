## Reachable Nodes in Subdivided Graph

**Problem Link:** https://leetcode.com/problems/reachable-nodes-in-subdivided-graph/description

**Problem Statement:**
- Input: `edges` and `maxMoves`
- Constraints: `0 <= edges.length <= 100`, `0 <= maxMoves <= 10^5`, `1 <= n <= 10^5`
- Expected output: The maximum number of nodes that can be reached.
- Key requirements and edge cases to consider:
  - The graph may contain cycles.
  - The graph may not be connected.
- Example test cases with explanations:
  - For example, if we have `edges = [[0,1,10],[0,2,1],[1,2,2]]` and `maxMoves = 6`, we can reach nodes 0, 1, and 2.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to try all possible paths and count the number of reachable nodes.
- We can use a depth-first search (DFS) or breadth-first search (BFS) to traverse the graph.
- However, this approach is not efficient because it has an exponential time complexity.

```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>

using namespace std;

int reachableNodes(vector<vector<int>>& edges, int maxMoves, int n) {
    vector<vector<pair<int, int>>> graph(n);
    for (auto& edge : edges) {
        graph[edge[0]].push_back({edge[1], edge[2]});
        graph[edge[1]].push_back({edge[0], edge[2]});
    }
    
    int count = 0;
    for (int i = 0; i < n; i++) {
        queue<pair<int, int>> q;
        vector<bool> visited(n, false);
        q.push({i, maxMoves});
        visited[i] = true;
        while (!q.empty()) {
            int node = q.front().first;
            int moves = q.front().second;
            q.pop();
            count++;
            for (auto& neighbor : graph[node]) {
                if (!visited[neighbor.first] && moves > 0) {
                    q.push({neighbor.first, moves - 1});
                    visited[neighbor.first] = true;
                }
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot (n + m) \cdot maxMoves)$, where $n$ is the number of nodes and $m$ is the number of edges. This is because we are using DFS to traverse the graph for each node.
> - **Space Complexity:** $O(n + m)$, where $n$ is the number of nodes and $m$ is the number of edges. This is because we are storing the graph in an adjacency list.
> - **Why these complexities occur:** The time complexity is high because we are trying all possible paths for each node. The space complexity is reasonable because we are storing the graph in a compact data structure.

---

### Optimal Approach (Required)

**Explanation:**
- We can use a priority queue to store the nodes to be visited, where the priority is the number of moves left.
- We can also use a `map` to store the number of new nodes that can be reached from each edge.
- We start by adding all nodes to the priority queue with the maximum number of moves.
- Then, we iterate over the edges and update the number of new nodes that can be reached from each edge.
- Finally, we return the total number of nodes that can be reached.

```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>

using namespace std;

int reachableNodes(vector<vector<int>>& edges, int maxMoves, int n) {
    vector<vector<pair<int, int>>> graph(n);
    for (auto& edge : edges) {
        graph[edge[0]].push_back({edge[1], edge[2]});
        graph[edge[1]].push_back({edge[0], edge[2]});
    }
    
    priority_queue<pair<int, int>> q;
    q.push({maxMoves, 0});
    unordered_map<int, int> visited;
    int count = 0;
    
    while (!q.empty()) {
        int moves = q.top().first;
        int node = q.top().second;
        q.pop();
        if (visited.count(node)) continue;
        visited[node] = moves;
        count++;
        
        for (auto& neighbor : graph[node]) {
            int newMoves = moves - neighbor.second;
            if (newMoves > 0 && !visited.count(neighbor.first)) {
                q.push({newMoves, neighbor.first});
            }
        }
    }
    
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O((n + m) \cdot log(n))$, where $n$ is the number of nodes and $m$ is the number of edges. This is because we are using a priority queue to store the nodes to be visited.
> - **Space Complexity:** $O(n + m)$, where $n$ is the number of nodes and $m$ is the number of edges. This is because we are storing the graph in an adjacency list and the visited nodes in a `map`.
> - **Optimality proof:** This is the optimal solution because we are using a priority queue to store the nodes to be visited, which ensures that we visit the nodes with the most moves left first. This minimizes the number of nodes that are not reachable.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: priority queue, graph traversal, and dynamic programming.
- Problem-solving patterns identified: using a priority queue to store nodes to be visited and updating the number of new nodes that can be reached from each edge.
- Optimization techniques learned: using a `map` to store the visited nodes and the number of new nodes that can be reached from each edge.
- Similar problems to practice: graph traversal, shortest path, and network flow problems.

**Mistakes to Avoid:**
- Common implementation errors: not checking for visited nodes, not updating the number of new nodes that can be reached from each edge correctly.
- Edge cases to watch for: empty graph, graph with only one node, graph with no edges.
- Performance pitfalls: using a brute force approach, not using a priority queue to store nodes to be visited.
- Testing considerations: testing with different graph structures, testing with different numbers of nodes and edges.