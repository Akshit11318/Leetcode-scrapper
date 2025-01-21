## Sum of Distances in Tree

**Problem Link:** https://leetcode.com/problems/sum-of-distances-in-tree/description

**Problem Statement:**
- Input format: An integer `n` and an array of edges `edges` representing an undirected tree.
- Constraints: The tree has `n` nodes labeled from 0 to `n-1`, and there are `n-1` edges in the tree.
- Expected output format: An array of length `n` where the `i-th` element is the sum of distances from node `i` to all other nodes in the tree.
- Key requirements and edge cases to consider: The tree is connected and undirected, and the input is guaranteed to form a valid tree.
- Example test cases with explanations:
  - For a tree with nodes 0, 1, and 2, and edges [[0,1],[0,2]], the sum of distances from node 0 to all other nodes is 2 (1 to node 1 + 1 to node 2), from node 1 to all other nodes is 3 (1 to node 0 + 2 to node 2), and from node 2 to all other nodes is 3 (1 to node 0 + 2 to node 1).

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To find the sum of distances from each node to all other nodes, we can use a brute force approach by performing a depth-first search (DFS) from each node to all other nodes and summing up the distances.
- Step-by-step breakdown of the solution:
  1. Initialize an array `res` of length `n` to store the sum of distances from each node to all other nodes.
  2. Iterate over each node `i` in the tree.
  3. For each node `i`, perform a DFS from node `i` to all other nodes and calculate the sum of distances.
  4. Update the `res` array with the calculated sum of distances for node `i`.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it is not efficient for large trees due to its high time complexity.

```cpp
void dfs(int node, int parent, vector<vector<int>>& edges, vector<int>& res, int& sum) {
    sum++;
    for (int neighbor : edges[node]) {
        if (neighbor != parent) {
            dfs(neighbor, node, edges, res, sum);
        }
    }
}

vector<int> sumOfDistancesInTree(int n, vector<vector<int>>& edges) {
    vector<int> res(n, 0);
    vector<vector<int>> graph(n);
    for (auto& edge : edges) {
        graph[edge[0]].push_back(edge[1]);
        graph[edge[1]].push_back(edge[0]);
    }
    for (int i = 0; i < n; i++) {
        int sum = 0;
        dfs(i, -1, graph, res, sum);
        res[i] = sum;
    }
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of nodes in the tree, because we are performing a DFS from each node to all other nodes.
> - **Space Complexity:** $O(n)$, where $n$ is the number of nodes in the tree, because we need to store the `res` array and the graph.
> - **Why these complexities occur:** The high time complexity occurs because we are performing a DFS from each node to all other nodes, resulting in a quadratic number of operations. The space complexity occurs because we need to store the graph and the `res` array.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a single DFS traversal to calculate the sum of distances from each node to all other nodes.
- Detailed breakdown of the approach:
  1. Initialize an array `count` of length `n` to store the number of nodes in the subtree rooted at each node.
  2. Initialize an array `res` of length `n` to store the sum of distances from each node to all other nodes.
  3. Perform a DFS traversal from an arbitrary node (e.g., node 0) and calculate the `count` array.
  4. Perform another DFS traversal from the same node and calculate the `res` array using the `count` array.
- Proof of optimality: This approach is optimal because we are only performing two DFS traversals, resulting in a linear time complexity.
- Why further optimization is impossible: We must visit each node at least once to calculate the sum of distances, so a linear time complexity is the best we can achieve.

```cpp
void dfs1(int node, int parent, vector<vector<int>>& graph, vector<int>& count) {
    count[node] = 1;
    for (int neighbor : graph[node]) {
        if (neighbor != parent) {
            dfs1(neighbor, node, graph, count);
            count[node] += count[neighbor];
        }
    }
}

void dfs2(int node, int parent, vector<vector<int>>& graph, vector<int>& res, vector<int>& count, int n) {
    for (int neighbor : graph[node]) {
        if (neighbor != parent) {
            res[neighbor] = res[node] - count[neighbor] + (n - count[neighbor]);
            dfs2(neighbor, node, graph, res, count, n);
        }
    }
}

vector<int> sumOfDistancesInTree(int n, vector<vector<int>>& edges) {
    vector<vector<int>> graph(n);
    for (auto& edge : edges) {
        graph[edge[0]].push_back(edge[1]);
        graph[edge[1]].push_back(edge[0]);
    }
    vector<int> count(n, 0);
    vector<int> res(n, 0);
    dfs1(0, -1, graph, count);
    res[0] = n - 1;
    dfs2(0, -1, graph, res, count, n);
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree, because we are performing two DFS traversals.
> - **Space Complexity:** $O(n)$, where $n$ is the number of nodes in the tree, because we need to store the `count` and `res` arrays.
> - **Optimality proof:** The time complexity is optimal because we are only performing two DFS traversals, resulting in a linear time complexity. The space complexity is also optimal because we need to store the `count` and `res` arrays.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: DFS traversal, tree traversal, and dynamic programming.
- Problem-solving patterns identified: Using a single DFS traversal to calculate the sum of distances from each node to all other nodes.
- Optimization techniques learned: Reducing the time complexity from quadratic to linear by using a single DFS traversal.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the `count` and `res` arrays correctly, or not updating the `res` array correctly during the DFS traversal.
- Edge cases to watch for: Handling the case where the tree is empty or has only one node.
- Performance pitfalls: Not using a single DFS traversal to calculate the sum of distances, resulting in a high time complexity.
- Testing considerations: Testing the solution with different tree structures and node counts to ensure correctness and efficiency.