## Maximum Path Quality of a Graph

**Problem Link:** https://leetcode.com/problems/maximum-path-quality-of-a-graph/description

**Problem Statement:**
- Input format: The input consists of an integer `n` representing the number of vertices in the graph, an array `edges` representing the edges of the graph where each edge is represented as an array `[u, v, q]` denoting an edge from vertex `u` to vertex `v` with a quality of `q`, and an integer `p` representing the starting vertex.
- Constraints: `1 <= n <= 100`, `0 <= edges.length <= n * (n - 1)`, `0 <= u, v, q <= 100`, and `0 <= p < n`.
- Expected output format: The function should return the maximum path quality of the graph starting from vertex `p`.
- Key requirements and edge cases to consider: The path quality is the minimum quality of all edges in the path, and the path should not contain more than `n` edges.
- Example test cases with explanations: 
  - For `n = 4`, `edges = [[0,1,10],[0,2,1],[1,2,2],[1,3,3]]`, and `p = 0`, the maximum path quality is `3`.
  - For `n = 5`, `edges = [[0,1,10],[0,2,1],[1,2,2],[1,3,3],[2,3,4]]`, and `p = 0`, the maximum path quality is `4`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To find the maximum path quality of the graph, we can try all possible paths starting from vertex `p`.
- Step-by-step breakdown of the solution: 
  1. Create an adjacency list representation of the graph.
  2. Use a recursive function to try all possible paths starting from vertex `p`.
  3. For each path, calculate the minimum quality of all edges in the path.
  4. Update the maximum path quality if the current path quality is higher.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, but it has a high time complexity due to the recursive function calls.

```cpp
#include <iostream>
#include <vector>
#include <climits>

using namespace std;

int maxPathQuality(int n, vector<vector<int>>& edges, int p) {
    vector<vector<pair<int, int>>> graph(n);
    for (auto& edge : edges) {
        graph[edge[0]].emplace_back(edge[1], edge[2]);
        graph[edge[1]].emplace_back(edge[0], edge[2]);
    }

    int maxQuality = INT_MIN;
    vector<bool> visited(n, false);
    function<void(int, int, int)> dfs = [&](int node, int quality, int depth) {
        if (depth > n) return;
        maxQuality = max(maxQuality, quality);
        visited[node] = true;
        for (auto& neighbor : graph[node]) {
            if (!visited[neighbor.first]) {
                dfs(neighbor.first, min(quality, neighbor.second), depth + 1);
            }
        }
        visited[node] = false;
    };

    dfs(p, INT_MAX, 0);
    return maxQuality;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the number of vertices in the graph. The recursive function has a time complexity of $O(2^n)$, and we iterate over all edges in the graph for each recursive call, resulting in a time complexity of $O(2^n \cdot n)$.
> - **Space Complexity:** $O(n)$, where $n$ is the number of vertices in the graph. We use a recursive function call stack of maximum depth $n$, and we store the adjacency list representation of the graph, which has a space complexity of $O(n)$.
> - **Why these complexities occur:** The time complexity occurs due to the recursive function calls, and the space complexity occurs due to the recursive function call stack and the adjacency list representation of the graph.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a depth-first search (DFS) with memoization to reduce the time complexity of the solution.
- Detailed breakdown of the approach: 
  1. Create an adjacency list representation of the graph.
  2. Use a recursive DFS function to try all possible paths starting from vertex `p`.
  3. For each path, calculate the minimum quality of all edges in the path.
  4. Use memoization to store the maximum path quality for each vertex and edge quality.
  5. Update the maximum path quality if the current path quality is higher.
- Why further optimization is impossible: The time complexity of the solution is optimal because we must try all possible paths starting from vertex `p` to find the maximum path quality.

```cpp
#include <iostream>
#include <vector>
#include <climits>

using namespace std;

int maxPathQuality(int n, vector<vector<int>>& edges, int p) {
    vector<vector<pair<int, int>>> graph(n);
    for (auto& edge : edges) {
        graph[edge[0]].emplace_back(edge[1], edge[2]);
        graph[edge[1]].emplace_back(edge[0], edge[2]);
    }

    int maxQuality = INT_MIN;
    vector<bool> visited(n, false);
    vector<vector<int>> memo(n, vector<int>(101, INT_MIN));
    function<void(int, int, int)> dfs = [&](int node, int quality, int depth) {
        if (depth > n) return;
        maxQuality = max(maxQuality, quality);
        visited[node] = true;
        for (auto& neighbor : graph[node]) {
            if (!visited[neighbor.first]) {
                int newQuality = min(quality, neighbor.second);
                if (memo[neighbor.first][newQuality] != INT_MIN) {
                    maxQuality = max(maxQuality, memo[neighbor.first][newQuality]);
                } else {
                    dfs(neighbor.first, newQuality, depth + 1);
                    memo[neighbor.first][newQuality] = maxQuality;
                }
            }
        }
        visited[node] = false;
    };

    dfs(p, 100, 0);
    return maxQuality;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the number of vertices in the graph. The recursive function has a time complexity of $O(2^n)$, and we iterate over all edges in the graph for each recursive call, resulting in a time complexity of $O(2^n \cdot n)$.
> - **Space Complexity:** $O(n^2)$, where $n$ is the number of vertices in the graph. We use a recursive function call stack of maximum depth $n$, and we store the adjacency list representation of the graph and the memoization table, which has a space complexity of $O(n^2)$.
> - **Optimality proof:** The time complexity of the solution is optimal because we must try all possible paths starting from vertex `p` to find the maximum path quality. The space complexity is also optimal because we must store the adjacency list representation of the graph and the memoization table to reduce the time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Depth-first search (DFS) and memoization.
- Problem-solving patterns identified: Using DFS to try all possible paths and using memoization to reduce the time complexity.
- Optimization techniques learned: Using memoization to store the maximum path quality for each vertex and edge quality.
- Similar problems to practice: Finding the maximum path quality in a weighted graph, finding the shortest path in a weighted graph.

**Mistakes to Avoid:**
- Common implementation errors: Not using memoization to reduce the time complexity, not checking for the base case in the recursive function.
- Edge cases to watch for: The graph may be empty, the starting vertex may not exist, the graph may contain negative-weight edges.
- Performance pitfalls: Not using memoization to reduce the time complexity, using a recursive function with a high time complexity.
- Testing considerations: Test the solution with different graphs, including empty graphs and graphs with negative-weight edges.