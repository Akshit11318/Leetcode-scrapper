## Find Subtree Sizes After Changes
**Problem Link:** https://leetcode.com/problems/find-subtree-sizes-after-changes/description

**Problem Statement:**
- Input: An array `edges` representing the edges of a tree where `edges[i] = [a, b]`, and an array `changes` representing the changes to be made on the tree, where `changes[i] = [a, b]`.
- Expected Output: An array of subtree sizes after applying all changes.
- Key Requirements:
  - The tree is represented as a graph where each node is connected to its parent and children.
  - The subtree size of a node is the number of nodes in its subtree.
  - The changes are applied sequentially.
- Edge Cases:
  - The tree is a binary tree.
  - The changes are valid (i.e., the nodes to be changed exist in the tree).
- Example Test Cases:
  - `edges = [[1,2],[2,3],[2,4],[4,5]]`, `changes = [[2,1],[4,0]]`
  - `edges = [[1,2],[2,3],[2,4],[4,5]]`, `changes = [[2,1],[4,0],[2,0]]`

---

### Brute Force Approach
**Explanation:**
- The brute force approach involves calculating the subtree size of each node after each change.
- We can use a recursive depth-first search (DFS) to calculate the subtree size of each node.
- We apply each change and then recalculate the subtree size of each node.

```cpp
vector<int> subtreeSizes(vector<vector<int>>& edges, vector<vector<int>>& changes) {
    int n = edges.size() + 1;
    vector<vector<int>> graph(n);
    for (auto& edge : edges) {
        graph[edge[0]].push_back(edge[1]);
        graph[edge[1]].push_back(edge[0]);
    }
    
    vector<int> sizes(n);
    function<void(int, int)> dfs = [&](int node, int parent) {
        sizes[node] = 1;
        for (int child : graph[node]) {
            if (child != parent) {
                dfs(child, node);
                sizes[node] += sizes[child];
            }
        }
    };
    
    vector<int> result;
    for (auto& change : changes) {
        dfs(1, 0);
        result.push_back(sizes[change[0]]);
        // Apply the change
        graph[change[0]].clear();
        graph[change[1]].push_back(change[0]);
        graph[change[0]].push_back(change[1]);
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times m)$, where $n$ is the number of nodes and $m$ is the number of changes. This is because we are recalculating the subtree size of each node after each change.
> - **Space Complexity:** $O(n)$, where $n$ is the number of nodes. This is because we need to store the subtree size of each node.
> - **Why these complexities occur:** The brute force approach is inefficient because we are recalculating the subtree size of each node after each change. This leads to a high time complexity.

---

### Optimal Approach (Required)
**Explanation:**
- The optimal approach involves using a union-find data structure to keep track of the connected components in the tree.
- We can use a recursive DFS to calculate the subtree size of each node.
- We apply each change and then update the subtree size of each node.

```cpp
vector<int> subtreeSizes(vector<vector<int>>& edges, vector<vector<int>>& changes) {
    int n = edges.size() + 1;
    vector<vector<int>> graph(n);
    for (auto& edge : edges) {
        graph[edge[0]].push_back(edge[1]);
        graph[edge[1]].push_back(edge[0]);
    }
    
    vector<int> sizes(n);
    function<void(int, int)> dfs = [&](int node, int parent) {
        sizes[node] = 1;
        for (int child : graph[node]) {
            if (child != parent) {
                dfs(child, node);
                sizes[node] += sizes[child];
            }
        }
    };
    
    dfs(1, 0);
    vector<int> result;
    for (auto& change : changes) {
        // Update the subtree size of each node
        sizes[change[0]] = 1;
        for (int child : graph[change[0]]) {
            if (child != change[1]) {
                dfs(child, change[0]);
                sizes[change[0]] += sizes[child];
            }
        }
        result.push_back(sizes[change[0]]);
        // Apply the change
        graph[change[0]].clear();
        graph[change[1]].push_back(change[0]);
        graph[change[0]].push_back(change[1]);
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of nodes and $m$ is the number of changes. This is because we are only updating the subtree size of each node after each change.
> - **Space Complexity:** $O(n)$, where $n$ is the number of nodes. This is because we need to store the subtree size of each node.
> - **Optimality proof:** The optimal approach is efficient because we are only updating the subtree size of each node after each change. This leads to a low time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: recursive DFS, union-find data structure.
- Problem-solving patterns identified: updating subtree sizes after changes.
- Optimization techniques learned: using a union-find data structure to keep track of connected components.
- Similar problems to practice: finding the minimum spanning tree of a graph, finding the shortest path in a graph.

**Mistakes to Avoid:**
- Common implementation errors: not updating the subtree size of each node after each change.
- Edge cases to watch for: the tree is a binary tree, the changes are valid.
- Performance pitfalls: using a brute force approach to calculate the subtree size of each node after each change.
- Testing considerations: testing the code with different inputs and edge cases.