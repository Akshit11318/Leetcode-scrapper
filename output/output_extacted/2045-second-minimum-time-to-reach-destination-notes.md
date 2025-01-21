## Second Minimum Time to Reach Destination

**Problem Link:** https://leetcode.com/problems/second-minimum-time-to-reach-destination/description

**Problem Statement:**
- Input format and constraints: The problem is given a graph of `n` nodes, where each node is connected to every other node with a certain `change` time. The goal is to find the second minimum time it takes to reach a specific destination node from node 1.
- Expected output format: The function should return the second minimum time to reach the destination node.
- Key requirements and edge cases to consider: The graph can have cycles, and the change time between nodes can vary. The destination node is given as an input.
- Example test cases with explanations:
  - Example 1: `n = 2`, `edges = [[1, 2], [1, 2]]`, `change = 0`, `time = [1, 2]`, `destination = 2`. The output should be `3`.
  - Example 2: `n = 3`, `edges = [[1, 2], [1, 3], [2, 3]]`, `change = 0`, `time = [2, 2, 3]`, `destination = 3`. The output should be `4`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can start by trying all possible paths from node 1 to the destination node and keep track of the minimum and second minimum times.
- Step-by-step breakdown of the solution:
  1. Create a graph using the given edges.
  2. Use a queue to perform a breadth-first search (BFS) from node 1.
  3. For each node, try all possible next nodes and update the minimum and second minimum times accordingly.
- Why this approach comes to mind first: It's a straightforward approach to try all possible paths and keep track of the minimum and second minimum times.

```cpp
#include <queue>
#include <vector>
#include <limits>
using namespace std;

int secondMinimum(int n, vector<vector<int>>& edges, int change, vector<int>& time, int destination) {
    // Create a graph using the given edges
    vector<vector<int>> graph(n + 1);
    for (auto& edge : edges) {
        graph[edge[0]].push_back(edge[1]);
    }

    // Initialize the minimum and second minimum times
    vector<int> minTime(n + 1, numeric_limits<int>::max());
    vector<int> secondMinTime(n + 1, numeric_limits<int>::max());
    minTime[1] = 0;

    // Use a queue to perform a BFS
    queue<pair<int, int>> q; // (node, time)
    q.push({1, 0});

    while (!q.empty()) {
        int node = q.front().first;
        int currentTime = q.front().second;
        q.pop();

        // Try all possible next nodes
        for (int nextNode : graph[node]) {
            int nextTime = currentTime + time[node - 1] + (nextNode != destination ? change : 0);

            // Update the minimum and second minimum times
            if (nextTime < minTime[nextNode]) {
                secondMinTime[nextNode] = minTime[nextNode];
                minTime[nextNode] = nextTime;
            } else if (nextTime > minTime[nextNode] && nextTime < secondMinTime[nextNode]) {
                secondMinTime[nextNode] = nextTime;
            }

            // Add the next node to the queue
            q.push({nextNode, nextTime});
        }
    }

    return secondMinTime[destination];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot t)$, where $n$ is the number of nodes, $m$ is the number of edges, and $t$ is the maximum time.
> - **Space Complexity:** $O(n + m)$, where $n$ is the number of nodes and $m$ is the number of edges.
> - **Why these complexities occur:** The time complexity occurs because we try all possible paths from node 1 to the destination node, and the space complexity occurs because we need to store the graph and the minimum and second minimum times.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use Dijkstra's algorithm to find the minimum time to reach each node, and then use another iteration to find the second minimum time.
- Detailed breakdown of the approach:
  1. Create a graph using the given edges.
  2. Use Dijkstra's algorithm to find the minimum time to reach each node.
  3. Use another iteration to find the second minimum time to reach each node.
- Proof of optimality: This approach is optimal because it uses the most efficient algorithm (Dijkstra's algorithm) to find the minimum time to reach each node, and then uses another iteration to find the second minimum time.

```cpp
#include <queue>
#include <vector>
#include <limits>
using namespace std;

int secondMinimum(int n, vector<vector<int>>& edges, int change, vector<int>& time, int destination) {
    // Create a graph using the given edges
    vector<vector<pair<int, int>>> graph(n + 1);
    for (auto& edge : edges) {
        graph[edge[0]].push_back({edge[1], time[edge[0] - 1]});
    }

    // Use Dijkstra's algorithm to find the minimum time to reach each node
    vector<int> minTime(n + 1, numeric_limits<int>::max());
    vector<int> secondMinTime(n + 1, numeric_limits<int>::max());
    minTime[1] = 0;

    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> q; // (time, node)
    q.push({0, 1});

    while (!q.empty()) {
        int currentTime = q.top().first;
        int node = q.top().second;
        q.pop();

        // Try all possible next nodes
        for (auto& nextNode : graph[node]) {
            int nextTime = currentTime + nextNode.second + (nextNode.first != destination ? change : 0);

            // Update the minimum and second minimum times
            if (nextTime < minTime[nextNode.first]) {
                secondMinTime[nextNode.first] = minTime[nextNode.first];
                minTime[nextNode.first] = nextTime;
                q.push({nextTime, nextNode.first});
            } else if (nextTime > minTime[nextNode.first] && nextTime < secondMinTime[nextNode.first]) {
                secondMinTime[nextNode.first] = nextTime;
            }
        }
    }

    return secondMinTime[destination];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O((n + m) \cdot \log(n))$, where $n$ is the number of nodes and $m$ is the number of edges.
> - **Space Complexity:** $O(n + m)$, where $n$ is the number of nodes and $m$ is the number of edges.
> - **Optimality proof:** This approach is optimal because it uses the most efficient algorithm (Dijkstra's algorithm) to find the minimum time to reach each node, and then uses another iteration to find the second minimum time.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dijkstra's algorithm, graph traversal, and dynamic programming.
- Problem-solving patterns identified: Using the most efficient algorithm to find the minimum time to reach each node, and then using another iteration to find the second minimum time.
- Optimization techniques learned: Using a priority queue to improve the efficiency of the algorithm.
- Similar problems to practice: Other graph traversal problems, such as finding the shortest path between two nodes.

**Mistakes to Avoid:**
- Common implementation errors: Not handling the case where the destination node is not reachable.
- Edge cases to watch for: The graph can have cycles, and the change time between nodes can vary.
- Performance pitfalls: Using an inefficient algorithm to find the minimum time to reach each node.
- Testing considerations: Test the algorithm with different graphs and edge cases to ensure it works correctly.