## All Paths From Source to Target
**Problem Link:** https://leetcode.com/problems/all-paths-from-source-to-target/description

**Problem Statement:**
- Input format and constraints: The problem takes a directed, acyclic graph (`graph`) as input where each node is represented by an integer from 0 to n-1 (n is the number of nodes), and each edge is directed from a lower-numbered node to a higher-numbered node. The goal is to find all paths from the source node (`0`) to the target node (`n-1`).
- Expected output format: A list of lists, where each sublist represents a path from the source to the target.
- Key requirements and edge cases to consider: The graph is guaranteed to be a directed acyclic graph (DAG), meaning there are no cycles. Each node has a unique value, and the edges are directed.
- Example test cases with explanations: For example, given `graph = [[1,2],[3],[3],[]]`, the function should return `[[0,1,3],[0,2,3]]`, as these are all the possible paths from node `0` to node `3`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves exploring all possible paths from the source node to the target node by recursively traversing the graph.
- Step-by-step breakdown of the solution:
  1. Start at the source node (`0`).
  2. For each neighbor of the current node, recursively explore all paths from that neighbor to the target node.
  3. When the target node is reached, add the path taken to reach it to the result list.
- Why this approach comes to mind first: This approach is straightforward and ensures that all possible paths are explored.

```cpp
class Solution {
public:
    vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph) {
        vector<vector<int>> result;
        vector<int> path;
        path.push_back(0); // Starting at node 0
        dfs(graph, 0, path, result);
        return result;
    }
    
    void dfs(vector<vector<int>>& graph, int node, vector<int>& path, vector<vector<int>>& result) {
        if (node == graph.size() - 1) { // If we've reached the target node
            result.push_back(path); // Add the current path to the result
            return;
        }
        
        for (int neighbor : graph[node]) {
            path.push_back(neighbor); // Add the neighbor to the current path
            dfs(graph, neighbor, path, result); // Recursively explore the neighbor
            path.pop_back(); // Backtrack by removing the neighbor from the path
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$ in the worst case, where $n$ is the number of nodes. This occurs because in the worst-case scenario, the graph could be a binary tree where each node has two children, leading to an exponential number of paths.
> - **Space Complexity:** $O(n)$ for the recursion stack and the space needed to store the current path. The space complexity is linear with respect to the number of nodes because the maximum depth of the recursion tree is $n$.
> - **Why these complexities occur:** The time complexity is exponential because we are exploring all possible paths in the graph, which can lead to an exponential number of paths in the worst case. The space complexity is linear because we only need to keep track of the current path and the recursion stack, both of which can grow up to a depth of $n$.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The graph is a directed acyclic graph (DAG), and we can use depth-first search (DFS) to efficiently explore all paths from the source to the target node.
- Detailed breakdown of the approach:
  1. Perform DFS starting from the source node.
  2. For each node visited, explore all its neighbors.
  3. When the target node is reached, add the path taken to reach it to the result list.
- Proof of optimality: This approach is optimal because it ensures that all possible paths are explored exactly once, without any redundant exploration. The use of DFS allows us to efficiently backtrack and explore all possible paths.

```cpp
class Solution {
public:
    vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph) {
        vector<vector<int>> result;
        vector<int> path;
        path.push_back(0); // Starting at node 0
        dfs(graph, 0, path, result);
        return result;
    }
    
    void dfs(vector<vector<int>>& graph, int node, vector<int>& path, vector<vector<int>>& result) {
        if (node == graph.size() - 1) { // If we've reached the target node
            result.push_back(path); // Add the current path to the result
            return;
        }
        
        for (int neighbor : graph[node]) {
            path.push_back(neighbor); // Add the neighbor to the current path
            dfs(graph, neighbor, path, result); // Recursively explore the neighbor
            path.pop_back(); // Backtrack by removing the neighbor from the path
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$ in the worst case, where $n$ is the number of nodes. This occurs because in the worst-case scenario, the graph could be a binary tree where each node has two children, leading to an exponential number of paths.
> - **Space Complexity:** $O(n)$ for the recursion stack and the space needed to store the current path. The space complexity is linear with respect to the number of nodes because the maximum depth of the recursion tree is $n$.
> - **Optimality proof:** The time complexity is optimal because we must explore all possible paths in the graph, and the number of paths can be exponential in the worst case. The space complexity is optimal because we only need to keep track of the current path and the recursion stack, both of which can grow up to a depth of $n$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Depth-first search (DFS), backtracking, and recursion.
- Problem-solving patterns identified: The use of DFS to explore all possible paths in a graph.
- Optimization techniques learned: The importance of avoiding redundant exploration and using efficient data structures.
- Similar problems to practice: Other graph traversal problems, such as finding the shortest path or detecting cycles.

**Mistakes to Avoid:**
- Common implementation errors: Failing to properly backtrack and remove nodes from the path, leading to incorrect results.
- Edge cases to watch for: Handling the case where the graph is empty or the target node is not reachable.
- Performance pitfalls: Failing to optimize the recursion stack and path storage, leading to excessive memory usage.
- Testing considerations: Thoroughly testing the solution with different graph structures and edge cases to ensure correctness and efficiency.