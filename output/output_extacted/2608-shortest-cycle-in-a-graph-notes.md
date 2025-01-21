## Shortest Cycle in a Graph

**Problem Link:** [https://leetcode.com/problems/shortest-cycle-in-a-graph/description](https://leetcode.com/problems/shortest-cycle-in-a-graph/description)

**Problem Statement:**
- Input format: A graph represented as an adjacency list `n` and `edges`, where `n` is the number of nodes and `edges` is a list of edges.
- Constraints: `1 <= n <= 10^5`, `1 <= edges.length <= 10^5`, `0 <= u, v < n`, and `u != v`.
- Expected output format: The length of the shortest cycle in the graph. If no cycle exists, return `-1`.
- Key requirements and edge cases to consider:
  - Handling disconnected graphs.
  - Detecting cycles of length 2 (i.e., parallel edges).
  - Identifying the shortest cycle among multiple cycles.
- Example test cases with explanations:
  - Test case 1: `n = 5`, `edges = [[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]]`, expected output: `3`.
  - Test case 2: `n = 5`, `edges = [[0,1],[1,2],[2,3],[3,4]]`, expected output: `-1`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate over all possible combinations of edges to detect cycles.
- Step-by-step breakdown of the solution:
  1. Generate all possible combinations of edges.
  2. For each combination, check if it forms a cycle by verifying that the start node is reachable from the end node.
  3. If a cycle is detected, update the minimum cycle length.
- Why this approach comes to mind first: It's a straightforward, albeit inefficient, way to solve the problem.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int shortestCycle(int n, vector<vector<int>>& edges) {
    int minCycleLength = INT_MAX;

    // Generate all possible combinations of edges
    for (int i = 0; i < edges.size(); i++) {
        for (int j = i + 1; j < edges.size(); j++) {
            // Check if the current combination forms a cycle
            if (edges[i][0] == edges[j][1] && edges[i][1] == edges[j][0]) {
                // Update the minimum cycle length
                minCycleLength = min(minCycleLength, 2);
            }
        }
    }

    // Check for longer cycles using BFS
    for (int i = 0; i < n; i++) {
        vector<bool> visited(n, false);
        vector<int> distance(n, INT_MAX);
        queue<int> q;

        q.push(i);
        distance[i] = 0;

        while (!q.empty()) {
            int node = q.front();
            q.pop();

            for (auto& edge : edges) {
                if (edge[0] == node && !visited[edge[1]]) {
                    q.push(edge[1]);
                    distance[edge[1]] = distance[node] + 1;
                    visited[edge[1]] = true;

                    if (edge[1] == i && distance[edge[1]] > 2) {
                        minCycleLength = min(minCycleLength, distance[edge[1]]);
                    }
                }
            }
        }
    }

    return minCycleLength == INT_MAX ? -1 : minCycleLength;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3 + m^2)$, where $n$ is the number of nodes and $m$ is the number of edges. This is because we're generating all possible combinations of edges and performing BFS for each node.
> - **Space Complexity:** $O(n + m)$, where $n$ is the number of nodes and $m$ is the number of edges. This is because we're storing the adjacency list and the distance array.
> - **Why these complexities occur:** The brute force approach has high time and space complexities due to the generation of all possible combinations of edges and the use of BFS for each node.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use BFS to detect cycles and keep track of the minimum cycle length.
- Detailed breakdown of the approach:
  1. Perform BFS for each node to detect cycles.
  2. Keep track of the minimum cycle length encountered during BFS.
  3. If a cycle is detected, update the minimum cycle length.
- Proof of optimality: This approach is optimal because it uses BFS to detect cycles, which has a lower time complexity compared to generating all possible combinations of edges.

```cpp
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int shortestCycle(int n, vector<vector<int>>& edges) {
    vector<vector<int>> adjList(n);

    // Build the adjacency list
    for (auto& edge : edges) {
        adjList[edge[0]].push_back(edge[1]);
        adjList[edge[1]].push_back(edge[0]);
    }

    int minCycleLength = INT_MAX;

    // Perform BFS for each node
    for (int i = 0; i < n; i++) {
        vector<bool> visited(n, false);
        vector<int> distance(n, INT_MAX);
        queue<pair<int, int>> q;

        q.push({i, -1});
        distance[i] = 0;

        while (!q.empty()) {
            int node = q.front().first;
            int parent = q.front().second;
            q.pop();

            for (int neighbor : adjList[node]) {
                if (neighbor == parent) continue;

                if (visited[neighbor]) {
                    // Cycle detected
                    minCycleLength = min(minCycleLength, distance[node] + 1);
                } else {
                    q.push({neighbor, node});
                    distance[neighbor] = distance[node] + 1;
                    visited[neighbor] = true;
                }
            }
        }
    }

    return minCycleLength == INT_MAX ? -1 : minCycleLength;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of nodes and $m$ is the number of edges. This is because we're performing BFS for each node.
> - **Space Complexity:** $O(n + m)$, where $n$ is the number of nodes and $m$ is the number of edges. This is because we're storing the adjacency list and the distance array.
> - **Optimality proof:** This approach is optimal because it uses BFS to detect cycles, which has a lower time complexity compared to generating all possible combinations of edges.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: BFS, cycle detection, and minimum cycle length calculation.
- Problem-solving patterns identified: Using BFS to detect cycles and keeping track of the minimum cycle length.
- Optimization techniques learned: Using BFS instead of generating all possible combinations of edges.
- Similar problems to practice: Finding the shortest path in a graph, detecting cycles in a directed graph, and calculating the minimum spanning tree of a graph.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as disconnected graphs or parallel edges.
- Edge cases to watch for: Detecting cycles of length 2 and identifying the shortest cycle among multiple cycles.
- Performance pitfalls: Using inefficient algorithms, such as generating all possible combinations of edges.
- Testing considerations: Testing the implementation with various input graphs, including disconnected graphs and graphs with multiple cycles.