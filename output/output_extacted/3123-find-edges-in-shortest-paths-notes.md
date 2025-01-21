## Find Edges in Shortest Paths
**Problem Link:** https://leetcode.com/problems/find-edges-in-shortest-paths/description

**Problem Statement:**
- Input format and constraints: Given a directed graph `edges` where each element is a tuple of `(u, v, w)` representing a directed edge from `u` to `v` with weight `w`, and an integer `k`.
- Expected output format: Find all the edges that are on the shortest path from node `0` to all other nodes, and return them in any order.
- Key requirements and edge cases to consider: 
    - The graph may contain cycles.
    - The graph may contain multiple edges between the same pair of nodes.
    - The graph may not be connected.
- Example test cases with explanations:
    - `edges = [[0,1,1],[1,2,1],[2,0,1]], k = 2` should return `[[0,1,1],[1,2,1]]`.
    - `edges = [[0,1,1],[1,2,1],[2,0,1]], k = 3` should return `[[0,1,1],[1,2,1],[2,0,1]]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can use a brute force approach by iterating over all possible paths from node `0` to all other nodes and checking if the path is the shortest.
- Step-by-step breakdown of the solution:
    1. Create an adjacency list representation of the graph.
    2. Use a recursive function to generate all possible paths from node `0` to all other nodes.
    3. For each path, calculate the total weight and check if it is the shortest.
    4. If it is the shortest, add the edges in the path to the result.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, but it is not efficient for large graphs.

```cpp
#include <vector>
#include <queue>
#include <unordered_map>
#include <limits>

using namespace std;

vector<vector<int>> findShortestPaths(vector<vector<int>>& edges, int k) {
    unordered_map<int, vector<pair<int, int>>> graph;
    for (auto& edge : edges) {
        graph[edge[0]].push_back({edge[1], edge[2]});
    }

    vector<vector<int>> result;
    vector<bool> visited(edges.size(), false);
    vector<int> dist(edges.size(), numeric_limits<int>::max());
    dist[0] = 0;

    queue<pair<int, int>> q;
    q.push({0, 0});

    while (!q.empty()) {
        int node = q.front().first;
        int weight = q.front().second;
        q.pop();

        if (visited[node]) continue;

        visited[node] = true;

        for (auto& neighbor : graph[node]) {
            if (weight + neighbor.second < dist[neighbor.first]) {
                dist[neighbor.first] = weight + neighbor.second;
                q.push({neighbor.first, dist[neighbor.first]});
            }
        }
    }

    for (auto& edge : edges) {
        if (dist[edge[0]] + edge[2] == dist[edge[1]]) {
            result.push_back({edge[0], edge[1], edge[2]});
        }
    }

    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(|E| + |V| \log |V|)$, where $|E|$ is the number of edges and $|V|$ is the number of vertices.
> - **Space Complexity:** $O(|E| + |V|)$.
> - **Why these complexities occur:** The time complexity is due to the use of a priority queue and the space complexity is due to the storage of the adjacency list and the result.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use Dijkstra's algorithm to find the shortest path from node `0` to all other nodes.
- Detailed breakdown of the approach:
    1. Create an adjacency list representation of the graph.
    2. Use Dijkstra's algorithm to find the shortest path from node `0` to all other nodes.
    3. For each edge in the graph, check if it is on the shortest path from node `0` to the destination node.
- Proof of optimality: Dijkstra's algorithm is optimal for finding the shortest path in a weighted graph.

```cpp
#include <vector>
#include <queue>
#include <unordered_map>
#include <limits>

using namespace std;

vector<vector<int>> findShortestPaths(vector<vector<int>>& edges, int k) {
    unordered_map<int, vector<pair<int, int>>> graph;
    for (auto& edge : edges) {
        graph[edge[0]].push_back({edge[1], edge[2]});
    }

    vector<vector<int>> result;
    vector<int> dist(edges.size(), numeric_limits<int>::max());
    dist[0] = 0;

    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> q;
    q.push({0, 0});

    while (!q.empty()) {
        int node = q.top().second;
        int weight = q.top().first;
        q.pop();

        for (auto& neighbor : graph[node]) {
            if (weight + neighbor.second < dist[neighbor.first]) {
                dist[neighbor.first] = weight + neighbor.second;
                q.push({dist[neighbor.first], neighbor.first});
            }
        }
    }

    for (auto& edge : edges) {
        if (dist[edge[0]] + edge[2] == dist[edge[1]]) {
            result.push_back({edge[0], edge[1], edge[2]});
        }
    }

    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(|E| + |V| \log |V|)$, where $|E|$ is the number of edges and $|V|$ is the number of vertices.
> - **Space Complexity:** $O(|E| + |V|)$.
> - **Optimality proof:** Dijkstra's algorithm is optimal for finding the shortest path in a weighted graph.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dijkstra's algorithm, priority queues.
- Problem-solving patterns identified: using Dijkstra's algorithm to find the shortest path in a weighted graph.
- Optimization techniques learned: using a priority queue to improve the efficiency of Dijkstra's algorithm.
- Similar problems to practice: finding the shortest path in an unweighted graph, finding the minimum spanning tree of a graph.

**Mistakes to Avoid:**
- Common implementation errors: not handling the case where the graph is not connected, not checking for negative weight edges.
- Edge cases to watch for: handling the case where the graph has multiple edges between the same pair of nodes.
- Performance pitfalls: not using a priority queue to improve the efficiency of Dijkstra's algorithm.
- Testing considerations: testing the algorithm on graphs with different structures and weights.