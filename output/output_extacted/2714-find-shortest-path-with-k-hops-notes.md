## Find Shortest Path with K Hops
**Problem Link:** https://leetcode.com/problems/find-shortest-path-with-k-hops/description

**Problem Statement:**
- Input format and constraints: Given a directed graph with `n` nodes and `edges`, find the shortest path from node `1` to node `n` that passes through exactly `k` edges.
- Expected output format: Return the length of the shortest path. If no such path exists, return `-1`.
- Key requirements and edge cases to consider: The graph is represented as an adjacency list, and the path must consist of exactly `k` edges.
- Example test cases with explanations:
  - Example 1: `n = 5`, `edges = [[0,1],[1,2],[2,3],[3,4],[1,4],[0,4]]`, `k = 3`. The shortest path from node `0` to node `4` with `3` hops is `0 -> 1 -> 2 -> 4`, which has a length of `3`.
  - Example 2: `n = 5`, `edges = [[0,1],[1,2],[2,3],[3,4],[1,4],[0,4]]`, `k = 2`. There is no path from node `0` to node `4` with exactly `2` hops.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible paths from node `1` to node `n` and check if they have exactly `k` edges.
- Step-by-step breakdown of the solution:
  1. Generate all possible paths from node `1` to node `n`.
  2. For each path, count the number of edges.
  3. If the path has exactly `k` edges, calculate its length.
  4. Keep track of the shortest path with `k` edges.
- Why this approach comes to mind first: It's a straightforward approach that tries all possibilities.

```cpp
#include <vector>
#include <queue>
#include <climits>

using namespace std;

int shortestPath(int n, vector<vector<int>>& edges, int k) {
    // Create an adjacency list
    vector<vector<int>> adj(n);
    for (auto& edge : edges) {
        adj[edge[0]].push_back(edge[1]);
    }

    // Initialize the queue with the starting node
    queue<pair<int, int>> q; // (node, hops)
    q.push({0, 0});

    int shortest = INT_MAX;

    while (!q.empty()) {
        auto [node, hops] = q.front();
        q.pop();

        // If we've reached the target node and have the correct number of hops
        if (node == n - 1 && hops == k) {
            // Update the shortest path
            shortest = min(shortest, hops);
        }

        // If we have more hops than needed, skip this path
        if (hops > k) {
            continue;
        }

        // Explore all neighbors
        for (auto& neighbor : adj[node]) {
            q.push({neighbor, hops + 1});
        }
    }

    return shortest == INT_MAX ? -1 : shortest;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^k)$, where $n$ is the number of nodes. This is because in the worst case, we're exploring all possible paths of length $k$.
> - **Space Complexity:** $O(n^k)$, for storing all the paths in the queue.
> - **Why these complexities occur:** The brute force approach tries all possible paths, which leads to exponential time and space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a breadth-first search (BFS) with a queue to explore all nodes at each hop level.
- Detailed breakdown of the approach:
  1. Initialize a queue with the starting node and its distance (0 hops).
  2. Perform BFS, exploring all neighbors at each hop level.
  3. Keep track of the shortest path with `k` hops.
- Proof of optimality: This approach is optimal because it explores all possible paths with exactly `k` hops in the shortest time possible.

```cpp
#include <vector>
#include <queue>
#include <climits>

using namespace std;

int shortestPath(int n, vector<vector<int>>& edges, int k) {
    // Create an adjacency list
    vector<vector<int>> adj(n);
    for (auto& edge : edges) {
        adj[edge[0]].push_back(edge[1]);
    }

    // Initialize the queue with the starting node
    queue<pair<int, int>> q; // (node, hops)
    q.push({0, 0});

    vector<bool> visited(n, false);
    int shortest = INT_MAX;

    while (!q.empty()) {
        int size = q.size();
        for (int i = 0; i < size; i++) {
            auto [node, hops] = q.front();
            q.pop();

            if (visited[node]) {
                continue;
            }

            visited[node] = true;

            // If we've reached the target node and have the correct number of hops
            if (node == n - 1 && hops == k) {
                // Update the shortest path
                shortest = min(shortest, hops);
            }

            // If we have more hops than needed, skip this path
            if (hops > k) {
                continue;
            }

            // Explore all neighbors
            for (auto& neighbor : adj[node]) {
                q.push({neighbor, hops + 1});
            }
        }
    }

    return shortest == INT_MAX ? -1 : shortest;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of nodes and $m$ is the number of edges. This is because we're exploring all nodes and edges once.
> - **Space Complexity:** $O(n + m)$, for storing the adjacency list and the queue.
> - **Optimality proof:** This approach is optimal because it explores all possible paths with exactly `k` hops in the shortest time possible, using a BFS with a queue.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: BFS, queue data structure, graph traversal.
- Problem-solving patterns identified: exploring all possible paths, keeping track of the shortest path.
- Optimization techniques learned: using a queue to explore all nodes at each hop level.
- Similar problems to practice: finding the shortest path in a graph, exploring all possible paths in a graph.

**Mistakes to Avoid:**
- Common implementation errors: not checking for visited nodes, not handling edge cases.
- Edge cases to watch for: empty graph, no path with `k` hops.
- Performance pitfalls: using an inefficient data structure, not optimizing the algorithm.
- Testing considerations: testing with different graph sizes, testing with different values of `k`.