## Number of Ways to Arrive at Destination
**Problem Link:** https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/description

**Problem Statement:**
- Input format and constraints: You are given a list of `n` nodes and a list of `edges` where each edge is represented as a pair of nodes and a weight.
- Expected output format: The number of ways to reach the destination node.
- Key requirements and edge cases to consider: The graph can be weighted and directed.
- Example test cases with explanations:
  - For a graph with nodes 0, 1, 2 and edges [(0,1,1), (0,2,1), (1,2,1)], there are 2 ways to reach node 2 from node 0.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To find the number of ways to reach the destination node, we can try all possible paths from the source node to the destination node.
- Step-by-step breakdown of the solution:
  1. Create an adjacency list representation of the graph.
  2. Perform a depth-first search (DFS) from the source node to the destination node, counting the number of paths.
- Why this approach comes to mind first: It is a straightforward and intuitive solution, but it can be inefficient for large graphs.

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    int countPaths(vector<vector<int>>& edges, int n, int source, int destination) {
        vector<vector<pair<int, int>>> graph(n);
        for (auto& edge : edges) {
            graph[edge[0]].emplace_back(edge[1], edge[2]);
        }

        int count = 0;
        function<void(int, int, int)> dfs = [&](int node, int dist, int dest) {
            if (node == dest) {
                count++;
                return;
            }
            for (auto& neighbor : graph[node]) {
                if (neighbor.first != source && dist + neighbor.second >= 0) {
                    dfs(neighbor.first, dist + neighbor.second, dest);
                }
            }
        };

        dfs(source, 0, destination);
        return count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, where n is the number of nodes, because in the worst case, we might have to explore all possible paths.
> - **Space Complexity:** $O(n)$, for the recursion stack.
> - **Why these complexities occur:** The brute force approach explores all possible paths, resulting in exponential time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use dynamic programming to store the number of ways to reach each node and avoid redundant calculations.
- Detailed breakdown of the approach:
  1. Create a DP table `dp` where `dp[i]` represents the number of ways to reach node `i`.
  2. Initialize `dp[source] = 1`, since there is one way to reach the source node (i.e., starting at the source node).
  3. Perform a topological sorting of the graph.
  4. For each node in the topological order, update `dp[node]` by summing the number of ways to reach its predecessors.
- Proof of optimality: This approach ensures that we count each path exactly once, and we avoid redundant calculations by storing the results in the DP table.

```cpp
class Solution {
public:
    int countPaths(vector<vector<int>>& edges, int n, int source, int destination) {
        vector<vector<int>> graph(n);
        vector<int> indegree(n);
        for (auto& edge : edges) {
            graph[edge[0]].push_back(edge[1]);
            indegree[edge[1]]++;
        }

        vector<int> dp(n);
        dp[source] = 1;
        queue<int> q;
        for (int i = 0; i < n; i++) {
            if (indegree[i] == 0) {
                q.push(i);
            }
        }

        while (!q.empty()) {
            int node = q.front();
            q.pop();
            for (int neighbor : graph[node]) {
                dp[neighbor] += dp[node];
                indegree[neighbor]--;
                if (indegree[neighbor] == 0) {
                    q.push(neighbor);
                }
            }
        }

        return dp[destination];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where n is the number of nodes and m is the number of edges, because we perform a constant amount of work for each node and edge.
> - **Space Complexity:** $O(n + m)$, for the graph representation and DP table.
> - **Optimality proof:** This approach ensures that we count each path exactly once, and we avoid redundant calculations by storing the results in the DP table.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, topological sorting.
- Problem-solving patterns identified: Counting paths in a graph.
- Optimization techniques learned: Using DP to avoid redundant calculations.
- Similar problems to practice: Counting paths in a weighted graph, finding the shortest path in a graph.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the DP table correctly, not handling cycles in the graph.
- Edge cases to watch for: Empty graph, graph with no paths to the destination node.
- Performance pitfalls: Using a brute force approach for large graphs.
- Testing considerations: Test the solution with different graph structures and edge cases.