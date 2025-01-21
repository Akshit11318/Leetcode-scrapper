## Most Profitable Path in a Tree

**Problem Link:** https://leetcode.com/problems/most-profitable-path-in-a-tree/description

**Problem Statement:**
- Input format and constraints: The input is a tree represented as an adjacency list `edges` and an array of profits `profits`. Each index in `profits` corresponds to a node in the tree.
- Expected output format: The function should return the maximum profit that can be obtained by traversing a path in the tree.
- Key requirements and edge cases to consider: The path can start and end at any node, and it can be of any length. However, each node can only be visited once.
- Example test cases with explanations:
  - Example 1:
    - Input: `edges = [[0,1],[1,2],[1,3],[3,4]], profits = [5,8,7,3,2]`
    - Output: `19`
    - Explanation: The most profitable path is `1 -> 3 -> 4 -> 0`, which has a total profit of `8 + 7 + 2 + 2 = 19`.
  - Example 2:
    - Input: `edges = [[0,1],[1,2],[1,3],[3,4]], profits = [1,1,1,1,1]`
    - Output: `4`
    - Explanation: The most profitable path is `0 -> 1 -> 3 -> 4`, which has a total profit of `1 + 1 + 1 + 1 = 4`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to use a brute force method to find all possible paths in the tree and calculate their profits.
- Step-by-step breakdown of the solution:
  1. Generate all possible paths in the tree.
  2. For each path, calculate the total profit by summing the profits of all nodes in the path.
  3. Keep track of the maximum profit found so far.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it is not efficient for large trees because it has to generate all possible paths.

```cpp
void dfs(vector<vector<int>>& edges, vector<int>& profits, int node, vector<bool>& visited, vector<int>& path, int& maxProfit) {
    visited[node] = true;
    path.push_back(node);
    int currentProfit = 0;
    for (int i : path) {
        currentProfit += profits[i];
    }
    maxProfit = max(maxProfit, currentProfit);
    for (int next : edges[node]) {
        if (!visited[next]) {
            dfs(edges, profits, next, visited, path, maxProfit);
        }
    }
    path.pop_back();
    visited[node] = false;
}

int mostProfitablePath(vector<vector<int>>& edges, vector<int>& profits) {
    int n = profits.size();
    vector<vector<int>> adj(n);
    for (vector<int>& edge : edges) {
        adj[edge[0]].push_back(edge[1]);
        adj[edge[1]].push_back(edge[0]);
    }
    int maxProfit = 0;
    vector<bool> visited(n, false);
    vector<int> path;
    for (int i = 0; i < n; i++) {
        dfs(adj, profits, i, visited, path, maxProfit);
    }
    return maxProfit;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot 2^n)$, where $n$ is the number of nodes in the tree. This is because in the worst case, we have to generate all possible paths, which is $2^n$.
> - **Space Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. This is because we need to store the visited nodes and the current path.
> - **Why these complexities occur:** The time complexity occurs because we are generating all possible paths, and the space complexity occurs because we need to store the visited nodes and the current path.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a depth-first search (DFS) to find the maximum profit path. We start at each node and recursively explore all possible paths, keeping track of the maximum profit found so far.
- Detailed breakdown of the approach:
  1. Start at each node in the tree.
  2. Recursively explore all possible paths from the current node, keeping track of the maximum profit found so far.
  3. Use a `maxGain` array to store the maximum gain for each node, where `maxGain[i]` is the maximum profit that can be obtained by traversing a path that starts at node `i`.
- Proof of optimality: This approach is optimal because it explores all possible paths in the tree and keeps track of the maximum profit found so far.

```cpp
int maxProfit = 0;
vector<int> maxGain;

int dfs(int node, int parent) {
    int maxVal = 0;
    for (int child : adj[node]) {
        if (child != parent) {
            int val = dfs(child, node);
            maxVal = max(maxVal, val);
        }
    }
    maxGain[node] = max(maxGain[node], maxVal + profits[node]);
    maxProfit = max(maxProfit, maxGain[node]);
    return maxGain[node];
}

int mostProfitablePath(vector<vector<int>>& edges, vector<int>& profits) {
    int n = profits.size();
    adj.resize(n);
    maxGain.resize(n);
    for (vector<int>& edge : edges) {
        adj[edge[0]].push_back(edge[1]);
        adj[edge[1]].push_back(edge[0]);
    }
    for (int i = 0; i < n; i++) {
        dfs(i, -1);
    }
    return maxProfit;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. This is because we visit each node once.
> - **Space Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. This is because we need to store the `maxGain` array and the adjacency list.
> - **Optimality proof:** This approach is optimal because it explores all possible paths in the tree and keeps track of the maximum profit found so far.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: DFS, dynamic programming.
- Problem-solving patterns identified: using a `maxGain` array to store the maximum gain for each node.
- Optimization techniques learned: using DFS to explore all possible paths in the tree.
- Similar problems to practice: finding the longest path in a tree, finding the shortest path in a tree.

**Mistakes to Avoid:**
- Common implementation errors: not initializing the `maxGain` array, not updating the `maxProfit` variable correctly.
- Edge cases to watch for: handling the case where the tree is empty, handling the case where the tree has only one node.
- Performance pitfalls: using a brute force approach to find all possible paths in the tree.
- Testing considerations: testing the function with different inputs, testing the function with edge cases.