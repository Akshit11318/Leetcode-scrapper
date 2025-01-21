## Minimum Time to Collect All Apples in a Tree

**Problem Link:** https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/description

**Problem Statement:**
- Input: A tree represented as a `vector<vector<int>>` where each index `i` represents a node, and the value at that index is a vector of its child nodes. Also, a `vector<bool>` `hasApple` where `hasApple[i]` is `true` if there is an apple on the tree at node `i`, and `false` otherwise.
- Output: The minimum time required to collect all apples.
- Key requirements and edge cases:
  - The tree is connected.
  - Each node has at most two children.
  - `1 <= n <= 10^5`, where `n` is the number of nodes in the tree.
- Example test cases with explanations:
  - If the tree has apples only at leaf nodes, the minimum time is the sum of distances from the root to each apple.
  - If the tree has no apples, the minimum time is 0.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: For each node with an apple, calculate the distance from the root to that node. Sum these distances to get the total time required to collect all apples.
- Step-by-step breakdown:
  1. Perform a depth-first search (DFS) to find all nodes with apples.
  2. For each node with an apple, calculate its distance from the root.
  3. Sum these distances to get the total time.
- Why this approach comes to mind first: It directly addresses the requirement to collect all apples, considering the structure of the tree.

```cpp
class Solution {
public:
    int minTime(int n, vector<vector<int>>& edges, vector<bool>& hasApple) {
        vector<vector<int>> graph(n);
        for (auto& edge : edges) {
            graph[edge[0]].push_back(edge[1]);
            graph[edge[1]].push_back(edge[0]);
        }
        
        function<int(int, int)> dfs = [&](int node, int parent) {
            int time = 0;
            for (int child : graph[node]) {
                if (child != parent) {
                    int childTime = dfs(child, node);
                    if (childTime > 0 || hasApple[child]) {
                        time += childTime + 2;
                    }
                }
            }
            return time;
        };
        
        return dfs(0, -1);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. Each node is visited once during the DFS.
> - **Space Complexity:** $O(n)$, for the recursive call stack and the graph representation.
> - **Why these complexities occur:** The DFS visits each node once, resulting in linear time complexity. The space complexity is due to the recursive call stack and the storage needed for the graph.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: The minimum time required to collect all apples is the sum of the distances from the root to each apple, considering that moving from a parent to a child takes 2 units of time (one unit to move down and one unit to move up).
- Detailed breakdown: The optimal approach still involves a DFS but optimizes by only considering nodes that have apples or are on the path to apples.
- Proof of optimality: This approach is optimal because it only counts the necessary paths to collect all apples, without unnecessary traversals.
- Why further optimization is impossible: Any algorithm must at least visit each node with an apple and its ancestors, which this approach does efficiently.

```cpp
class Solution {
public:
    int minTime(int n, vector<vector<int>>& edges, vector<bool>& hasApple) {
        vector<vector<int>> graph(n);
        for (auto& edge : edges) {
            graph[edge[0]].push_back(edge[1]);
            graph[edge[1]].push_back(edge[0]);
        }
        
        function<int(int, int)> dfs = [&](int node, int parent) {
            int time = 0;
            for (int child : graph[node]) {
                if (child != parent) {
                    int childTime = dfs(child, node);
                    if (childTime > 0 || hasApple[child]) {
                        time += childTime + 2;
                    }
                }
            }
            return time;
        };
        
        return dfs(0, -1);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, as each node is visited once.
> - **Space Complexity:** $O(n)$, for the recursive call stack and graph storage.
> - **Optimality proof:** The approach only counts the distances to nodes with apples and their necessary paths, ensuring no unnecessary traversals.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: DFS, tree traversal, and optimization by considering only relevant paths.
- Problem-solving patterns: Identifying the minimum required actions (in this case, moving to collect apples) and optimizing the approach based on the problem constraints.
- Optimization techniques: Eliminating unnecessary operations by only considering nodes that contribute to the outcome.
- Similar problems to practice: Other tree traversal and optimization problems, such as finding the diameter of a tree or the minimum path between two nodes.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly handling the base case of the recursion or missing the optimization step.
- Edge cases to watch for: Empty trees, trees with no apples, and trees with apples only at the root.
- Performance pitfalls: Unnecessary traversals or not optimizing the recursive function calls.
- Testing considerations: Ensure to test with various tree structures and apple distributions to cover all edge cases.