## Number of Restricted Paths from First to Last Node

**Problem Link:** https://leetcode.com/problems/number-of-restricted-paths-from-first-to-last-node/description

**Problem Statement:**
- Input format: `n` nodes and `edges` list of pairs representing undirected edges between nodes.
- Constraints: $1 \leq n \leq 10^5$, $1 \leq edges.length \leq 10^5$, $1 \leq u, v \leq n$.
- Expected output format: The number of restricted paths from node `1` to node `n`.
- Key requirements and edge cases to consider: All edges are undirected and have a weight of 1. A restricted path is a path that starts at node `1` and ends at node `n` with the condition that for any node $i$ that is visited, all nodes $j$ with $i < j \leq n$ must be visited before any node $k$ with $k < i$ is revisited.
- Example test cases with explanations:
  - Example 1: `n = 5`, `edges = [[1,2],[2,3],[5,4],[4,3],[1,4],[2,5]]`. The answer is `3` because the restricted paths are `[1,2,3,4,5]`, `[1,2,5,4,3]`, and `[1,4,3,2,5]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible paths from node `1` to node `n` and check each path to see if it's restricted.
- Step-by-step breakdown of the solution:
  1. Create a graph from the edges.
  2. Perform a depth-first search (DFS) to generate all possible paths from node `1` to node `n`.
  3. For each generated path, check if it's restricted by verifying that for any node $i$ that is visited, all nodes $j$ with $i < j \leq n$ must be visited before any node $k$ with $k < i$ is revisited.
- Why this approach comes to mind first: It's a straightforward way to generate and check all possible paths, but it's inefficient due to the large number of paths that need to be generated and checked.

```cpp
#include <iostream>
#include <vector>

using namespace std;

// Function to check if a path is restricted
bool isRestrictedPath(vector<int>& path, int n) {
    for (int i = 0; i < path.size(); i++) {
        for (int j = i + 1; j < path.size(); j++) {
            if (path[j] < path[i]) return false;
        }
    }
    return true;
}

// Function to generate all possible paths using DFS
void dfs(int node, vector<int>& path, vector<vector<int>>& graph, vector<vector<int>>& allPaths) {
    path.push_back(node);
    if (node == graph.size() - 1) {
        allPaths.push_back(path);
    } else {
        for (int neighbor : graph[node]) {
            dfs(neighbor, path, graph, allPaths);
        }
    }
    path.pop_back();
}

// Brute force function
int bruteForce(int n, vector<vector<int>>& edges) {
    vector<vector<int>> graph(n);
    for (auto& edge : edges) {
        graph[edge[0] - 1].push_back(edge[1] - 1);
        graph[edge[1] - 1].push_back(edge[0] - 1);
    }
    
    vector<vector<int>> allPaths;
    vector<int> path;
    dfs(0, path, graph, allPaths);
    
    int count = 0;
    for (auto& path : allPaths) {
        if (isRestrictedPath(path, n)) count++;
    }
    
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$ because in the worst case, we generate all possible paths of length up to $n$, and for each path, we perform a linear scan to check if it's restricted.
> - **Space Complexity:** $O(2^n \cdot n)$ for storing all generated paths.
> - **Why these complexities occur:** The brute force approach is inefficient due to the exponential number of paths that need to be generated and checked.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Realize that the problem can be solved using a topological sorting approach combined with dynamic programming to count the number of restricted paths.
- Detailed breakdown of the approach:
  1. Perform a topological sort on the graph to ensure that nodes are visited in a linear order that respects the directed edges.
  2. Use dynamic programming to count the number of restricted paths. For each node $i$, maintain a count $dp[i]$ of the number of restricted paths from node $1$ to node $i$.
  3. For each node $i$, iterate over its neighbors and update $dp[i]$ by adding the number of restricted paths to its neighbors.
- Proof of optimality: This approach is optimal because it avoids the exponential overhead of generating all possible paths and instead uses dynamic programming to efficiently count the number of restricted paths.

```cpp
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

// Function to perform topological sorting
vector<int> topologicalSort(int n, vector<vector<int>>& edges) {
    vector<int> inDegree(n, 0);
    vector<vector<int>> graph(n);
    for (auto& edge : edges) {
        graph[edge[0] - 1].push_back(edge[1] - 1);
        inDegree[edge[1] - 1]++;
    }
    
    queue<int> q;
    for (int i = 0; i < n; i++) {
        if (inDegree[i] == 0) q.push(i);
    }
    
    vector<int> order;
    while (!q.empty()) {
        int node = q.front();
        q.pop();
        order.push_back(node);
        for (int neighbor : graph[node]) {
            inDegree[neighbor]--;
            if (inDegree[neighbor] == 0) q.push(neighbor);
        }
    }
    
    return order;
}

// Optimal function
int optimal(int n, vector<vector<int>>& edges) {
    vector<int> order = topologicalSort(n, edges);
    vector<int> dp(n, 0);
    dp[0] = 1;
    
    vector<vector<int>> graph(n);
    for (auto& edge : edges) {
        graph[edge[0] - 1].push_back(edge[1] - 1);
    }
    
    for (int node : order) {
        for (int neighbor : graph[node]) {
            dp[neighbor] += dp[node];
        }
    }
    
    return dp[n - 1];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$ where $n$ is the number of nodes and $m$ is the number of edges, because we perform a topological sort and then iterate over the graph once to update the dynamic programming table.
> - **Space Complexity:** $O(n + m)$ for storing the graph and the dynamic programming table.
> - **Optimality proof:** This approach is optimal because it uses a linear-time topological sorting algorithm and then updates the dynamic programming table in linear time, avoiding the exponential overhead of generating all possible paths.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Topological sorting and dynamic programming.
- Problem-solving patterns identified: Using dynamic programming to count the number of paths in a graph.
- Optimization techniques learned: Avoiding the exponential overhead of generating all possible paths by using dynamic programming.
- Similar problems to practice: Other graph problems that involve counting paths or finding restricted paths.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to update the dynamic programming table correctly.
- Edge cases to watch for: Handling the case where the graph is empty or has no edges.
- Performance pitfalls: Using an exponential-time algorithm to generate all possible paths.
- Testing considerations: Testing the algorithm on large graphs to ensure it scales correctly.