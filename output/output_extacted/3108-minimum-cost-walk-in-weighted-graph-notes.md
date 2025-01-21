## Minimum Cost Walk in Weighted Graph

**Problem Link:** https://leetcode.com/problems/minimum-cost-walk-in-weighted-graph/description

**Problem Statement:**
- Given a weighted graph, find the minimum cost walk from a source node to all other nodes.
- Input format and constraints: The graph is represented as an adjacency list, and the weights are non-negative integers.
- Expected output format: The minimum cost to reach each node from the source node.
- Key requirements and edge cases to consider: The graph may be disconnected, and the source node may not be reachable from all nodes.
- Example test cases with explanations:
  - A simple connected graph with positive weights.
  - A graph with negative weights (not applicable in this case since the problem statement does not mention negative weights).
  - A disconnected graph with multiple connected components.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Use a simple iterative approach to calculate the minimum cost to reach each node from the source node.
- Step-by-step breakdown of the solution:
  1. Initialize the minimum cost to reach the source node as 0, and all other nodes as infinity.
  2. Iterate over all edges in the graph, and for each edge, update the minimum cost to reach the destination node if a shorter path is found.
  3. Repeat step 2 until no further updates are made, indicating that the minimum cost to reach all nodes has been calculated.
- Why this approach comes to mind first: It is a straightforward and intuitive approach to solving the problem.

```cpp
#include <iostream>
#include <vector>
#include <limits>

using namespace std;

const int INF = numeric_limits<int>::max();

void minCostWalk(vector<vector<pair<int, int>>>& graph, int source) {
    int n = graph.size();
    vector<int> minCost(n, INF);
    minCost[source] = 0;

    bool updated;
    do {
        updated = false;
        for (int i = 0; i < n; i++) {
            for (const auto& edge : graph[i]) {
                int destination = edge.first;
                int weight = edge.second;
                if (minCost[i] != INF && minCost[i] + weight < minCost[destination]) {
                    minCost[destination] = minCost[i] + weight;
                    updated = true;
                }
            }
        }
    } while (updated);

    for (int i = 0; i < n; i++) {
        if (minCost[i] == INF) {
            cout << "INF ";
        } else {
            cout << minCost[i] << " ";
        }
    }
    cout << endl;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(|E| \cdot |V|)$, where $|E|$ is the number of edges and $|V|$ is the number of vertices, because in the worst case, we need to iterate over all edges for each vertex.
> - **Space Complexity:** $O(|V|)$, because we need to store the minimum cost to reach each vertex.
> - **Why these complexities occur:** The time complexity occurs because we need to iterate over all edges in the graph, and for each edge, we need to update the minimum cost to reach the destination vertex. The space complexity occurs because we need to store the minimum cost to reach each vertex.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use Dijkstra's algorithm, which is a well-known algorithm for finding the shortest path in a graph.
- Detailed breakdown of the approach:
  1. Initialize the minimum cost to reach the source node as 0, and all other nodes as infinity.
  2. Use a priority queue to store the nodes to be processed, with the node having the minimum cost at the top of the queue.
  3. While the queue is not empty, extract the node with the minimum cost from the queue, and update the minimum cost to reach its neighbors if a shorter path is found.
- Proof of optimality: Dijkstra's algorithm is proven to be optimal for finding the shortest path in a graph with non-negative weights.
- Why further optimization is impossible: Dijkstra's algorithm has a time complexity of $O(|E| + |V| \log |V|)$, which is the best possible time complexity for this problem.

```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <limits>

using namespace std;

const int INF = numeric_limits<int>::max();

void minCostWalk(vector<vector<pair<int, int>>>& graph, int source) {
    int n = graph.size();
    vector<int> minCost(n, INF);
    minCost[source] = 0;

    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push({0, source});

    while (!pq.empty()) {
        int cost = pq.top().first;
        int node = pq.top().second;
        pq.pop();

        if (cost > minCost[node]) {
            continue;
        }

        for (const auto& edge : graph[node]) {
            int destination = edge.first;
            int weight = edge.second;
            if (cost + weight < minCost[destination]) {
                minCost[destination] = cost + weight;
                pq.push({minCost[destination], destination});
            }
        }
    }

    for (int i = 0; i < n; i++) {
        if (minCost[i] == INF) {
            cout << "INF ";
        } else {
            cout << minCost[i] << " ";
        }
    }
    cout << endl;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(|E| + |V| \log |V|)$, where $|E|$ is the number of edges and $|V|$ is the number of vertices, because we use a priority queue to store the nodes to be processed.
> - **Space Complexity:** $O(|V| + |E|)$, because we need to store the minimum cost to reach each vertex and the edges in the graph.
> - **Optimality proof:** Dijkstra's algorithm is proven to be optimal for finding the shortest path in a graph with non-negative weights.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dijkstra's algorithm, priority queue.
- Problem-solving patterns identified: Using a priority queue to store the nodes to be processed.
- Optimization techniques learned: Using Dijkstra's algorithm to find the shortest path in a graph.
- Similar problems to practice: Finding the shortest path in a graph with negative weights, finding the minimum spanning tree of a graph.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if the node has already been processed before updating its minimum cost.
- Edge cases to watch for: The graph may be disconnected, and the source node may not be reachable from all nodes.
- Performance pitfalls: Using a brute force approach instead of Dijkstra's algorithm.
- Testing considerations: Test the algorithm with different types of graphs, including connected and disconnected graphs, and graphs with different types of weights.