## Network Delay Time
**Problem Link:** https://leetcode.com/problems/network-delay-time/description

**Problem Statement:**
- Input format: `times` - a list of edges in the form of `[u, v, w]`, `n` - the number of nodes in the network, `k` - the node where the signal starts.
- Expected output format: The maximum delay time to send a signal to all nodes. If it's impossible, return `-1`.
- Key requirements and edge cases to consider: 
  - There can be multiple edges between two nodes with different weights.
  - There might be nodes that are not reachable from the starting node.
  - The graph can be represented as a weighted, directed graph.
- Example test cases with explanations:
  - `times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2` should return `2` because the signal reaches all nodes in 2 units of time.
  - `times = [[1,2,1]], n = 2, k = 1` should return `1` because the signal reaches the second node in 1 unit of time.
  - `times = [[1,2,1],[2,3,1],[3,4,1]], n = 4, k = 3` should return `-1` because it's impossible to reach node 1 from node 3.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: To calculate the delay time, we can try to find the shortest path from the starting node to all other nodes using all possible paths.
- Step-by-step breakdown of the solution:
  1. Create an adjacency list representation of the graph.
  2. Use a recursive function to explore all possible paths from the starting node to all other nodes, keeping track of the maximum delay time.
- Why this approach comes to mind first: It seems straightforward to explore all possible paths and keep track of the maximum delay time. However, this approach is inefficient and does not guarantee finding the shortest path.

```cpp
#include <vector>
#include <climits>
using namespace std;

class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        // Create adjacency list
        vector<vector<pair<int, int>>> graph(n + 1);
        for (auto& time : times) {
            graph[time[0]].emplace_back(time[1], time[2]);
        }
        
        int maxDelay = 0;
        vector<bool> visited(n + 1, false);
        
        function<void(int, int)> dfs = [&](int node, int delay) {
            visited[node] = true;
            maxDelay = max(maxDelay, delay);
            for (auto& neighbor : graph[node]) {
                if (!visited[neighbor.first]) {
                    dfs(neighbor.first, delay + neighbor.second);
                }
            }
            visited[node] = false; // Backtrack
        };
        
        dfs(k, 0);
        
        return maxDelay == INT_MAX ? -1 : maxDelay;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$ because we are exploring all possible paths using recursion. This is inefficient and not scalable for large inputs.
> - **Space Complexity:** $O(n)$ for the recursion stack.
> - **Why these complexities occur:** The brute force approach explores all possible paths, leading to exponential time complexity.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Using Dijkstra's algorithm to find the shortest path from the starting node to all other nodes in the graph.
- Detailed breakdown of the approach:
  1. Create an adjacency list representation of the graph.
  2. Initialize the distance to the starting node as 0 and all other nodes as infinity.
  3. Use a priority queue to select the node with the minimum distance that has not been processed yet.
  4. Update the distances of the neighbors of the selected node if a shorter path is found.
- Proof of optimality: Dijkstra's algorithm is guaranteed to find the shortest path to all nodes in the graph.

```cpp
#include <vector>
#include <queue>
#include <climits>
using namespace std;

class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        // Create adjacency list
        vector<vector<pair<int, int>>> graph(n + 1);
        for (auto& time : times) {
            graph[time[0]].emplace_back(time[1], time[2]);
        }
        
        // Initialize distances
        vector<int> distances(n + 1, INT_MAX);
        distances[k] = 0;
        
        // Priority queue
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> pq;
        pq.emplace(0, k);
        
        while (!pq.empty()) {
            auto [delay, node] = pq.top();
            pq.pop();
            
            for (auto& neighbor : graph[node]) {
                if (delay + neighbor.second < distances[neighbor.first]) {
                    distances[neighbor.first] = delay + neighbor.second;
                    pq.emplace(distances[neighbor.first], neighbor.first);
                }
            }
        }
        
        int maxDelay = 0;
        for (int i = 1; i <= n; i++) {
            if (distances[i] == INT_MAX) return -1;
            maxDelay = max(maxDelay, distances[i]);
        }
        
        return maxDelay;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O((n + m) \log n)$ where $n$ is the number of nodes and $m$ is the number of edges, because we use a priority queue to select the node with the minimum distance.
> - **Space Complexity:** $O(n + m)$ for the adjacency list and priority queue.
> - **Optimality proof:** Dijkstra's algorithm is guaranteed to find the shortest path to all nodes in the graph, making it the optimal solution.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dijkstra's algorithm, priority queues, and graph traversal.
- Problem-solving patterns identified: Using the right data structures (e.g., priority queues) to optimize the solution.
- Optimization techniques learned: Applying Dijkstra's algorithm to find the shortest path in a graph.
- Similar problems to practice: Other graph traversal and shortest path problems.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases (e.g., unreachable nodes) or not using the correct data structures.
- Edge cases to watch for: Nodes that are not reachable from the starting node.
- Performance pitfalls: Using inefficient algorithms (e.g., brute force) for large inputs.
- Testing considerations: Test the solution with different inputs, including edge cases, to ensure correctness and efficiency.