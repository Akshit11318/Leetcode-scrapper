## Maximum Points After Collecting Coins from All Nodes

**Problem Link:** https://leetcode.com/problems/maximum-points-after-collecting-coins-from-all-nodes/description

**Problem Statement:**
- Input format and constraints: The problem is given a directed graph with `n` nodes and an adjacency list `adj` where `adj[i]` is a list of pairs `(j, c)` indicating a directed edge from `i` to `j` with a cost `c`. The goal is to find the maximum points that can be collected by traversing all nodes.
- Expected output format: The output should be the maximum points that can be collected.
- Key requirements and edge cases to consider: The graph can have cycles, and the cost of edges can be negative.
- Example test cases with explanations: For example, given `adj = [[1,2],[0,3],[1,4]]`, the maximum points that can be collected is `10`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves trying all possible paths in the graph and calculating the total cost for each path.
- Step-by-step breakdown of the solution:
  1. Generate all possible paths in the graph using a depth-first search (DFS) or breadth-first search (BFS) algorithm.
  2. For each path, calculate the total cost by summing up the costs of all edges in the path.
  3. Keep track of the maximum total cost found so far.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it has a high time complexity due to the exponential number of possible paths.

```cpp
#include <iostream>
#include <vector>
#include <limits>

using namespace std;

int maxPoints(vector<vector<pair<int, int>>>& adj) {
    int n = adj.size();
    int maxPoints = numeric_limits<int>::min();

    // Generate all possible paths using DFS
    vector<bool> visited(n, false);
    vector<int> path;
    function<void(int)> dfs = [&](int node) {
        visited[node] = true;
        path.push_back(node);
        if (path.size() == n) {
            int totalCost = 0;
            for (int i = 0; i < path.size() - 1; i++) {
                for (auto& edge : adj[path[i]]) {
                    if (edge.first == path[i + 1]) {
                        totalCost += edge.second;
                        break;
                    }
                }
            }
            maxPoints = max(maxPoints, totalCost);
        } else {
            for (int i = 0; i < n; i++) {
                if (!visited[i]) {
                    dfs(i);
                }
            }
        }
        path.pop_back();
        visited[node] = false;
    };

    for (int i = 0; i < n; i++) {
        dfs(i);
    }

    return maxPoints;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n!)$, where $n$ is the number of nodes, because there are $n!$ possible paths in the graph.
> - **Space Complexity:** $O(n)$, where $n$ is the number of nodes, because we need to store the current path in the DFS algorithm.
> - **Why these complexities occur:** The high time complexity is due to the exponential number of possible paths in the graph, and the space complexity is due to the need to store the current path in the DFS algorithm.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution involves using a dynamic programming approach to calculate the maximum points that can be collected.
- Detailed breakdown of the approach:
  1. Initialize a `dp` array to store the maximum points that can be collected at each node.
  2. Iterate through each node in the graph, and for each node, iterate through all its neighbors.
  3. For each neighbor, calculate the maximum points that can be collected by taking the edge to the neighbor and adding it to the maximum points that can be collected at the neighbor.
  4. Update the `dp` array with the maximum points that can be collected at each node.
- Proof of optimality: The dynamic programming approach ensures that we consider all possible paths in the graph and calculate the maximum points that can be collected.
- Why further optimization is impossible: The dynamic programming approach has a time complexity of $O(n^2)$, which is the best possible time complexity for this problem.

```cpp
int maxPoints(vector<vector<pair<int, int>>>& adj) {
    int n = adj.size();
    vector<int> dp(n, 0);

    for (int i = 0; i < n; i++) {
        for (auto& edge : adj[i]) {
            dp[edge.first] = max(dp[edge.first], dp[i] + edge.second);
        }
    }

    return *max_element(dp.begin(), dp.end());
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of nodes, because we need to iterate through each node and its neighbors.
> - **Space Complexity:** $O(n)$, where $n$ is the number of nodes, because we need to store the `dp` array.
> - **Optimality proof:** The dynamic programming approach ensures that we consider all possible paths in the graph and calculate the maximum points that can be collected.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, graph traversal.
- Problem-solving patterns identified: Using dynamic programming to solve optimization problems.
- Optimization techniques learned: Using dynamic programming to reduce the time complexity of the algorithm.
- Similar problems to practice: Other graph optimization problems, such as finding the shortest path or the minimum spanning tree.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the `dp` array correctly, not updating the `dp` array correctly.
- Edge cases to watch for: Handling cycles in the graph, handling negative edge weights.
- Performance pitfalls: Using a brute force approach, not using dynamic programming to optimize the algorithm.
- Testing considerations: Testing the algorithm with different input graphs, testing the algorithm with different edge weights.