## Path with Maximum Probability

**Problem Link:** https://leetcode.com/problems/path-with-maximum-probability/description

**Problem Statement:**
- Input format and constraints: The input is represented by `n`, the number of nodes in a graph, and `edges`, a list of undirected edges with their corresponding probabilities. The graph is represented as an adjacency list.
- Expected output format: The output is the maximum probability of reaching the target node from the start node.
- Key requirements and edge cases to consider: The graph may contain cycles, and the probability of reaching a node is the maximum probability of reaching any of its neighbors multiplied by the probability of the edge between them.
- Example test cases with explanations: For example, given `n = 3`, `edges = [[0,1,0.5],[1,2,0.5],[0,2,0.2]]`, and `start = 0`, `end = 2`, the maximum probability of reaching node 2 from node 0 is `0.5 * 0.5 = 0.25`, which is the maximum probability of reaching node 2.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves calculating the probability of reaching each node from the start node by considering all possible paths.
- Step-by-step breakdown of the solution:
  1. Initialize a `dist` array to store the maximum probability of reaching each node.
  2. Use a priority queue to keep track of nodes to visit, where the priority is the maximum probability of reaching the node.
  3. For each node, update the maximum probability of reaching its neighbors.
- Why this approach comes to mind first: This approach is intuitive because it considers all possible paths and calculates the maximum probability of reaching each node.

```cpp
#include <queue>
#include <vector>
using namespace std;

double maxProbability(int n, vector<vector<int>>& edges, double p[], int start, int end) {
    vector<vector<pair<int, double>>> graph(n);
    for (auto& edge : edges) {
        graph[edge[0]].emplace_back(edge[1], edge[2]);
        graph[edge[1]].emplace_back(edge[0], edge[2]);
    }
    
    vector<double> dist(n, 0);
    dist[start] = 1;
    priority_queue<pair<double, int>, vector<pair<double, int>>, less<>> pq;
    pq.emplace(1, start);
    
    while (!pq.empty()) {
        auto [prob, node] = pq.top();
        pq.pop();
        if (prob < dist[node]) continue;
        
        for (auto& [neighbor, edge_prob] : graph[node]) {
            double new_prob = prob * edge_prob;
            if (new_prob > dist[neighbor]) {
                dist[neighbor] = new_prob;
                pq.emplace(new_prob, neighbor);
            }
        }
    }
    
    return dist[end];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m \log n)$, where $n$ is the number of nodes and $m$ is the number of edges. The priority queue operations take $O(\log n)$ time, and we perform these operations for each edge.
> - **Space Complexity:** $O(n + m)$, where $n$ is the number of nodes and $m$ is the number of edges. We store the graph as an adjacency list, which requires $O(n + m)$ space.
> - **Why these complexities occur:** The time complexity occurs because we use a priority queue to keep track of nodes to visit, and the space complexity occurs because we store the graph as an adjacency list.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution involves using Dijkstra's algorithm with a priority queue to keep track of nodes to visit, where the priority is the maximum probability of reaching the node.
- Detailed breakdown of the approach:
  1. Initialize a `dist` array to store the maximum probability of reaching each node.
  2. Use a priority queue to keep track of nodes to visit, where the priority is the maximum probability of reaching the node.
  3. For each node, update the maximum probability of reaching its neighbors.
- Proof of optimality: This approach is optimal because it considers all possible paths and calculates the maximum probability of reaching each node.

```cpp
#include <queue>
#include <vector>
using namespace std;

double maxProbability(int n, vector<vector<int>>& edges, double p[], int start, int end) {
    vector<vector<pair<int, double>>> graph(n);
    for (int i = 0; i < edges.size(); i++) {
        graph[edges[i][0]].emplace_back(edges[i][1], p[i]);
        graph[edges[i][1]].emplace_back(edges[i][0], p[i]);
    }
    
    vector<double> dist(n, 0);
    dist[start] = 1;
    priority_queue<pair<double, int>, vector<pair<double, int>>, less<>> pq;
    pq.emplace(1, start);
    
    while (!pq.empty()) {
        auto [prob, node] = pq.top();
        pq.pop();
        if (prob < dist[node]) continue;
        
        for (auto& [neighbor, edge_prob] : graph[node]) {
            double new_prob = prob * edge_prob;
            if (new_prob > dist[neighbor]) {
                dist[neighbor] = new_prob;
                pq.emplace(new_prob, neighbor);
            }
        }
    }
    
    return dist[end];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m \log n)$, where $n$ is the number of nodes and $m$ is the number of edges. The priority queue operations take $O(\log n)$ time, and we perform these operations for each edge.
> - **Space Complexity:** $O(n + m)$, where $n$ is the number of nodes and $m$ is the number of edges. We store the graph as an adjacency list, which requires $O(n + m)$ space.
> - **Optimality proof:** This approach is optimal because it considers all possible paths and calculates the maximum probability of reaching each node.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dijkstra's algorithm, priority queue, graph traversal.
- Problem-solving patterns identified: Using a priority queue to keep track of nodes to visit, where the priority is the maximum probability of reaching the node.
- Optimization techniques learned: Using a priority queue to reduce the number of nodes to visit.
- Similar problems to practice: Shortest path problems, maximum flow problems.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as an empty graph or a graph with no edges.
- Edge cases to watch for: Handling cycles in the graph, handling nodes with no outgoing edges.
- Performance pitfalls: Not using a priority queue to keep track of nodes to visit, which can lead to exponential time complexity.
- Testing considerations: Testing the solution with different graph structures, such as a graph with a single node, a graph with multiple connected components, and a graph with cycles.