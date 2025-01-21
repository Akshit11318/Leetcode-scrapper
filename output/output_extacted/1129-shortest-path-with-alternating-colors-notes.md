## Shortest Path with Alternating Colors

**Problem Link:** https://leetcode.com/problems/shortest-path-with-alternating-colors/description

**Problem Statement:**
- Input format: Given a graph `n` and edges `edges` where `edges[i] = [a, b]` indicates that there is a directed edge from node `a` to node `b`, find the length of the shortest path that visits nodes with alternating colors.
- Constraints: `1 <= n <= 100`, `0 <= edges.length <= 300`, `0 <= a, b <= n`, `a != b`.
- Expected output format: An array of two integers representing the length of the shortest path that starts with a red node and a blue node, respectively.
- Key requirements and edge cases to consider: Handling cycles, ensuring alternating colors, and dealing with disconnected graphs.
- Example test cases with explanations:
  - Example 1: `n = 3`, `edges = [[0,1],[0,2]]`. The output is `[1, -1]` because there is a path of length 1 starting from node 0 (red) to node 1 (blue), but no path starting from a blue node.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Perform a depth-first search (DFS) or breadth-first search (BFS) from each node, keeping track of the color of the previous node to ensure alternating colors.
- Step-by-step breakdown of the solution:
  1. Initialize a queue with all nodes as starting points.
  2. For each node, perform a BFS, keeping track of the previous node's color.
  3. If a node with the same color as the previous node is encountered, skip it.
  4. Update the shortest path length if a shorter path to a node with a different color is found.
- Why this approach comes to mind first: It's a straightforward way to explore all possible paths in the graph while considering the constraint of alternating colors.

```cpp
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

vector<int> shortestAlternatingPaths(int n, vector<vector<int>>& edges) {
    vector<vector<pair<int, int>>> graph(n);
    for (auto& edge : edges) {
        graph[edge[0]].emplace_back(edge[1], 0); // 0 represents red
        graph[edge[1]].emplace_back(edge[0], 1); // 1 represents blue
    }

    vector<int> redDist(n, INT_MAX), blueDist(n, INT_MAX);
    redDist[0] = 0; blueDist[0] = 0;

    queue<pair<int, int>> qRed, qBlue; // node, color
    qRed.push({0, 0}); qBlue.push({0, 1});

    while (!qRed.empty() || !qBlue.empty()) {
        if (!qRed.empty()) {
            auto node = qRed.front(); qRed.pop();
            for (auto& neighbor : graph[node.first]) {
                if (neighbor.second != node.second && redDist[neighbor.first] > node.second + 1) {
                    redDist[neighbor.first] = node.second + 1;
                    qRed.push({neighbor.first, neighbor.second});
                }
            }
        }
        if (!qBlue.empty()) {
            auto node = qBlue.front(); qBlue.pop();
            for (auto& neighbor : graph[node.first]) {
                if (neighbor.second != node.second && blueDist[neighbor.first] > node.second + 1) {
                    blueDist[neighbor.first] = node.second + 1;
                    qBlue.push({neighbor.first, neighbor.second});
                }
            }
        }
    }

    vector<int> result(n);
    for (int i = 0; i < n; ++i) {
        if (redDist[i] == INT_MAX) result[i] = -1;
        else result[i] = redDist[i];
    }
    for (int i = 0; i < n; ++i) {
        if (blueDist[i] == INT_MAX) result[i] = -1;
        else if (result[i] == -1) result[i] = blueDist[i];
        else result[i] = min(result[i], blueDist[i]);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of nodes and $m$ is the number of edges, because in the worst case, we visit each node and edge once.
> - **Space Complexity:** $O(n + m)$, for storing the graph and the distances.
> - **Why these complexities occur:** The graph traversal (BFS) dictates the time complexity, while storing the graph and distances contributes to the space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Utilize a more efficient data structure to store and update distances.
- Detailed breakdown of the approach:
  1. Initialize two queues for BFS, one starting from red nodes and one from blue nodes.
  2. Use a `vector<vector<int>>` to store the graph, where each inner vector represents the neighbors of a node.
  3. Perform BFS, updating the distances as shorter paths are found.
- Proof of optimality: This approach visits each node and edge at most once, ensuring the minimum time complexity for graph traversal problems.

```cpp
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

vector<int> shortestAlternatingPaths(int n, vector<vector<int>>& edges) {
    vector<vector<pair<int, int>>> graph(n);
    for (auto& edge : edges) {
        graph[edge[0]].emplace_back(edge[1], 0); // 0 represents red
        graph[edge[1]].emplace_back(edge[0], 1); // 1 represents blue
    }

    vector<vector<int>> dist(n, vector<int>(2, INT_MAX));
    dist[0][0] = 0; dist[0][1] = 0;

    queue<pair<int, int>> q; // node, color
    q.push({0, 0}); q.push({0, 1});

    while (!q.empty()) {
        auto node = q.front(); q.pop();
        for (auto& neighbor : graph[node.first]) {
            if (neighbor.second != node.second && dist[neighbor.first][neighbor.second] > dist[node.first][node.second] + 1) {
                dist[neighbor.first][neighbor.second] = dist[node.first][node.second] + 1;
                q.push({neighbor.first, neighbor.second});
            }
        }
    }

    vector<int> result(2);
    for (int i = 0; i < n; ++i) {
        if (dist[i][0] == INT_MAX) result[0] = -1;
        else if (result[0] == -1 || result[0] > dist[i][0]) result[0] = dist[i][0];
        if (dist[i][1] == INT_MAX) result[1] = -1;
        else if (result[1] == -1 || result[1] > dist[i][1]) result[1] = dist[i][1];
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of nodes and $m$ is the number of edges.
> - **Space Complexity:** $O(n + m)$, for storing the graph and distances.
> - **Optimality proof:** The algorithm visits each node and edge once, achieving the minimum time complexity for graph traversal.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Graph traversal (BFS), using queues for efficient traversal, and updating distances for shortest paths.
- Problem-solving patterns identified: Breaking down the problem into smaller sub-problems (red and blue paths), using data structures for efficient storage and update of distances.
- Optimization techniques learned: Using the most efficient data structures and algorithms for the problem, minimizing the number of operations.
- Similar problems to practice: Other graph traversal problems, such as finding the shortest path between two nodes, or detecting cycles in a graph.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases properly, such as an empty graph or a graph with no paths.
- Edge cases to watch for: Disconnected graphs, cycles, and nodes with no neighbors.
- Performance pitfalls: Using inefficient data structures or algorithms, leading to high time or space complexity.
- Testing considerations: Thoroughly testing the algorithm with different inputs, including edge cases, to ensure correctness and efficiency.