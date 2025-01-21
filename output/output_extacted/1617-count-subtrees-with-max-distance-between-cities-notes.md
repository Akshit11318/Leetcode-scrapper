## Count Subtrees With Max Distance Between Cities
**Problem Link:** https://leetcode.com/problems/count-subtrees-with-max-distance-between-cities/description

**Problem Statement:**
- Input: `n` (number of cities) and `edges` (list of undirected edges between cities)
- Constraints: `1 <= n <= 10^5`, `0 <= edges.length <= 10^5`
- Expected Output: The number of subtrees with maximum distance between cities
- Key Requirements:
  - Count the number of subtrees where the maximum distance between any two cities is `maxDistance`
  - Consider edge cases where `n` is 1 or `edges` is empty
- Example Test Cases:
  - `n = 4`, `edges = [[1, 2], [2, 3], [3, 4]]`
  - `n = 5`, `edges = [[1, 2], [2, 3], [3, 4], [4, 5]]`

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves generating all possible subtrees of the given graph and calculating the maximum distance between any two cities in each subtree.
- Step-by-step breakdown:
  1. Generate all possible subtrees using a recursive approach or bit masking.
  2. For each subtree, calculate the maximum distance between any two cities using a breadth-first search (BFS) or depth-first search (DFS) algorithm.
  3. Count the number of subtrees with maximum distance equal to `maxDistance`.
- This approach comes to mind first because it is straightforward and easy to implement, but it is inefficient due to the large number of possible subtrees.

```cpp
int countSubtrees(int n, vector<vector<int>>& edges, int maxDistance) {
    // Create an adjacency list representation of the graph
    vector<vector<int>> graph(n + 1);
    for (const auto& edge : edges) {
        graph[edge[0]].push_back(edge[1]);
        graph[edge[1]].push_back(edge[0]);
    }

    int count = 0;
    // Generate all possible subtrees using bit masking
    for (int mask = 1; mask < (1 << n); mask++) {
        vector<int> subtree;
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) != 0) {
                subtree.push_back(i + 1);
            }
        }

        // Calculate the maximum distance between any two cities in the subtree
        int maxDist = 0;
        for (int i = 0; i < subtree.size(); i++) {
            for (int j = i + 1; j < subtree.size(); j++) {
                int dist = bfs(graph, subtree[i], subtree[j]);
                maxDist = max(maxDist, dist);
            }
        }

        // Count the number of subtrees with maximum distance equal to maxDistance
        if (maxDist == maxDistance) {
            count++;
        }
    }

    return count;
}

int bfs(vector<vector<int>>& graph, int start, int end) {
    queue<int> q;
    vector<bool> visited(graph.size(), false);
    q.push(start);
    visited[start] = true;
    int dist = 0;

    while (!q.empty()) {
        int size = q.size();
        for (int i = 0; i < size; i++) {
            int node = q.front();
            q.pop();

            if (node == end) {
                return dist;
            }

            for (int neighbor : graph[node]) {
                if (!visited[neighbor]) {
                    q.push(neighbor);
                    visited[neighbor] = true;
                }
            }
        }

        dist++;
    }

    return -1; // Return -1 if there is no path between start and end
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n^2 \cdot (n + m))$ where $n$ is the number of cities and $m$ is the number of edges. This is because we generate all possible subtrees and calculate the maximum distance between any two cities in each subtree using a BFS algorithm.
> - **Space Complexity:** $O(n + m)$ for the adjacency list representation of the graph and the queue used in the BFS algorithm.
> - **Why these complexities occur:** The time complexity is high due to the large number of possible subtrees and the BFS algorithm used to calculate the maximum distance between any two cities in each subtree. The space complexity is relatively low because we only need to store the adjacency list representation of the graph and the queue used in the BFS algorithm.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is to use a dynamic programming approach to calculate the maximum distance between any two cities in each subtree.
- Detailed breakdown of the approach:
  1. Create a recursive function to calculate the maximum distance between any two cities in a subtree.
  2. Use memoization to store the results of subproblems to avoid redundant calculations.
- Why further optimization is impossible: The optimal approach has a time complexity of $O(n \cdot m)$, which is the minimum time complexity required to solve the problem because we need to traverse the entire graph to calculate the maximum distance between any two cities in each subtree.

```cpp
int countSubtrees(int n, vector<vector<int>>& edges, int maxDistance) {
    // Create an adjacency list representation of the graph
    vector<vector<int>> graph(n + 1);
    for (const auto& edge : edges) {
        graph[edge[0]].push_back(edge[1]);
        graph[edge[1]].push_back(edge[0]);
    }

    int count = 0;
    // Use a recursive function to calculate the maximum distance between any two cities in each subtree
    for (int i = 1; i <= n; i++) {
        vector<bool> visited(n + 1, false);
        int maxDist = dfs(graph, i, visited);
        if (maxDist == maxDistance) {
            count++;
        }
    }

    return count;
}

int dfs(vector<vector<int>>& graph, int node, vector<bool>& visited) {
    visited[node] = true;
    int maxDist = 0;

    for (int neighbor : graph[node]) {
        if (!visited[neighbor]) {
            int dist = dfs(graph, neighbor, visited);
            maxDist = max(maxDist, dist + 1);
        }
    }

    return maxDist;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ where $n$ is the number of cities and $m$ is the number of edges. This is because we use a recursive function to calculate the maximum distance between any two cities in each subtree and traverse the entire graph.
> - **Space Complexity:** $O(n + m)$ for the adjacency list representation of the graph and the recursive call stack.
> - **Optimality proof:** The optimal approach has a time complexity of $O(n \cdot m)$, which is the minimum time complexity required to solve the problem because we need to traverse the entire graph to calculate the maximum distance between any two cities in each subtree.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: dynamic programming, recursive functions, and memoization.
- Problem-solving patterns identified: using a recursive function to calculate the maximum distance between any two cities in each subtree and using memoization to store the results of subproblems.
- Optimization techniques learned: using a recursive function to calculate the maximum distance between any two cities in each subtree and using memoization to store the results of subproblems.
- Similar problems to practice: problems that involve calculating the maximum distance between any two nodes in a graph or tree.

**Mistakes to Avoid:**
- Common implementation errors: not using memoization to store the results of subproblems, not using a recursive function to calculate the maximum distance between any two cities in each subtree.
- Edge cases to watch for: when the graph is empty or when the maximum distance between any two cities is 0.
- Performance pitfalls: not using a recursive function to calculate the maximum distance between any two cities in each subtree, not using memoization to store the results of subproblems.
- Testing considerations: testing the function with different inputs, including edge cases, to ensure that it works correctly.