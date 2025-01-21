## Maximum Subtree of the Same Color

**Problem Link:** https://leetcode.com/problems/maximum-subtree-of-the-same-color/description

**Problem Statement:**
- Input format: Given a tree where each node has a color, and an integer `color` of type `int`.
- Constraints: The number of nodes in the tree will be in the range `[1, 10^5]`.
- Expected output format: The maximum number of nodes in a subtree that has the same color as the given `color`.
- Key requirements and edge cases to consider:
  - The tree is represented as an adjacency list where each index `i` represents a node and the value at each index `i` is a list of its child node indices.
  - Each node has a color represented by an integer.
- Example test cases with explanations:
  - For a tree with colors `[1,2,3,4,5]` and edges `[[0,1],[0,2],[1,3],[1,4]]`, and given color `1`, the maximum subtree size with the same color is `1`.
  - For a tree with colors `[1,4,4,4]` and edges `[[0,1],[0,2],[0,3]]`, and given color `4`, the maximum subtree size with the same color is `3`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Check every possible subtree to see if all its nodes have the same color as the given color.
- Step-by-step breakdown of the solution:
  1. Iterate over all nodes in the tree.
  2. For each node, perform a depth-first search (DFS) to traverse all subtrees rooted at this node.
  3. During DFS, count the number of nodes in the current subtree that have the same color as the given color.
  4. If all nodes in the subtree have the same color, update the maximum subtree size.
- Why this approach comes to mind first: It's straightforward to think of checking every possible subtree to solve the problem.

```cpp
class Solution {
public:
    int maxSubtreeColor(int color, vector<vector<int>>& edges, vector<int>& colors) {
        int n = colors.size();
        vector<vector<int>> graph(n);
        for (auto& edge : edges) {
            graph[edge[0]].push_back(edge[1]);
            graph[edge[1]].push_back(edge[0]);
        }
        
        int max_size = 0;
        for (int i = 0; i < n; ++i) {
            int size = dfs(graph, colors, i, color);
            max_size = max(max_size, size);
        }
        
        return max_size;
    }
    
    int dfs(vector<vector<int>>& graph, vector<int>& colors, int node, int color) {
        if (colors[node] != color) return 0;
        
        int size = 1;
        for (int child : graph[node]) {
            size += dfs(graph, colors, child, color);
        }
        
        return size;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ because in the worst case, we're performing DFS from every node.
> - **Space Complexity:** $O(n)$ for the recursive call stack.
> - **Why these complexities occur:** The brute force approach is inefficient because it involves a lot of repeated work, especially in the case of a highly connected tree where many nodes are revisited multiple times.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of performing DFS from every node, we can perform DFS only once from the root node and keep track of the maximum subtree size seen so far.
- Detailed breakdown of the approach:
  1. Perform DFS from the root node.
  2. During DFS, for each node, count the number of nodes in the subtree rooted at this node that have the same color as the given color.
  3. Update the maximum subtree size if the current subtree size is larger.
- Proof of optimality: This approach is optimal because it visits each node exactly once, avoiding the redundant work of the brute force approach.

```cpp
class Solution {
public:
    int maxSubtreeColor(int color, vector<vector<int>>& edges, vector<int>& colors) {
        int n = colors.size();
        vector<vector<int>> graph(n);
        for (auto& edge : edges) {
            graph[edge[0]].push_back(edge[1]);
            graph[edge[1]].push_back(edge[0]);
        }
        
        int max_size = 0;
        dfs(graph, colors, 0, color, max_size);
        
        return max_size;
    }
    
    int dfs(vector<vector<int>>& graph, vector<int>& colors, int node, int color, int& max_size) {
        if (colors[node] != color) return 0;
        
        int size = 1;
        for (int child : graph[node]) {
            size += dfs(graph, colors, child, color, max_size);
        }
        
        max_size = max(max_size, size);
        return size;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ because we visit each node exactly once.
> - **Space Complexity:** $O(n)$ for the recursive call stack.
> - **Optimality proof:** This approach is optimal because it achieves the best possible time complexity for this problem by avoiding redundant work.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Depth-First Search (DFS), tree traversal, and optimization techniques.
- Problem-solving patterns identified: Avoiding redundant work by visiting each node exactly once.
- Optimization techniques learned: Using a single pass through the tree to find the maximum subtree size.
- Similar problems to practice: Other tree-related problems, such as finding the diameter of a tree or the maximum path sum.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as an empty tree or a tree with a single node.
- Edge cases to watch for: Trees with highly connected nodes, which can lead to redundant work if not handled properly.
- Performance pitfalls: Using inefficient algorithms, such as the brute force approach, which can lead to high time complexities.
- Testing considerations: Test the solution with various tree structures and edge cases to ensure correctness and efficiency.