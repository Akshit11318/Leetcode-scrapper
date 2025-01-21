## Find Center of Star Graph
**Problem Link:** https://leetcode.com/problems/find-center-of-star-graph/description

**Problem Statement:**
- Input format: `edges` - a list of edges in the star graph, where each edge is a pair of nodes.
- Constraints: The graph is a star graph, meaning it has a central node connected to all other nodes.
- Expected output format: The node that is the center of the star graph.
- Key requirements and edge cases to consider: 
    - The graph may have any number of nodes, but it is guaranteed to be a star graph.
    - The input edges may be in any order.
- Example test cases with explanations:
    - For example, if the input is `[[1,2],[2,3],[4,2]]`, the output should be `2`, because node `2` is the center of the star graph.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To find the center of the star graph, we can iterate over all nodes and check if they are connected to all other nodes.
- Step-by-step breakdown of the solution:
    1. Iterate over all nodes in the graph.
    2. For each node, check if it is connected to all other nodes.
    3. If a node is connected to all other nodes, it is the center of the star graph.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it may not be efficient for large graphs.

```cpp
int findCenter(vector<vector<int>>& edges) {
    int n = edges.size() + 1;
    vector<vector<int>> graph(n);
    for (auto& edge : edges) {
        graph[edge[0] - 1].push_back(edge[1] - 1);
        graph[edge[1] - 1].push_back(edge[0] - 1);
    }
    for (int i = 0; i < n; i++) {
        bool isCenter = true;
        for (int j = 0; j < n; j++) {
            if (i != j && find(graph[i].begin(), graph[i].end(), j) == graph[i].end()) {
                isCenter = false;
                break;
            }
        }
        if (isCenter) {
            return i + 1;
        }
    }
    return -1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of nodes in the graph. This is because we are iterating over all nodes and checking if they are connected to all other nodes.
> - **Space Complexity:** $O(n)$, where $n$ is the number of nodes in the graph. This is because we are storing the adjacency list of the graph.
> - **Why these complexities occur:** These complexities occur because we are using a brute force approach to find the center of the star graph.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Since the graph is a star graph, the center node must be connected to all other nodes. Therefore, we can simply find the node that appears most frequently in the edges.
- Detailed breakdown of the approach:
    1. Count the frequency of each node in the edges.
    2. Find the node with the maximum frequency.
- Proof of optimality: This approach is optimal because it has a time complexity of $O(n)$, which is the best possible time complexity for this problem.
- Why further optimization is impossible: Further optimization is impossible because we must at least read the input edges once, which takes $O(n)$ time.

```cpp
int findCenter(vector<vector<int>>& edges) {
    int count[edges.size() + 1] = {0};
    for (auto& edge : edges) {
        count[edge[0]]++;
        count[edge[1]]++;
    }
    int maxCount = 0, center = 0;
    for (int i = 1; i <= edges.size() + 1; i++) {
        if (count[i] > maxCount) {
            maxCount = count[i];
            center = i;
        }
    }
    return center;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the graph. This is because we are counting the frequency of each node in the edges.
> - **Space Complexity:** $O(n)$, where $n$ is the number of nodes in the graph. This is because we are storing the frequency of each node.
> - **Optimality proof:** This approach is optimal because it has a time complexity of $O(n)$, which is the best possible time complexity for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The importance of understanding the properties of the input data and using them to optimize the solution.
- Problem-solving patterns identified: The use of frequency counting to find the center of a star graph.
- Optimization techniques learned: The importance of avoiding unnecessary iterations and using efficient data structures.
- Similar problems to practice: Other graph problems that involve finding a specific node or edge.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing variables correctly, not checking for edge cases.
- Edge cases to watch for: The input graph may be empty, or it may have only one node.
- Performance pitfalls: Using a brute force approach that has a high time complexity.
- Testing considerations: Test the solution with different input graphs, including empty graphs and graphs with only one node.