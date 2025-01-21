## Minimum Score After Removals on a Tree

**Problem Link:** https://leetcode.com/problems/minimum-score-after-removals-on-a-tree/description

**Problem Statement:**
- Input format and constraints: Given a tree with `n` nodes, where each node has a value, and a list of removals, find the minimum score after removals.
- Expected output format: The minimum score after removals.
- Key requirements and edge cases to consider: 
  - Each removal is a pair of nodes.
  - The score is calculated based on the maximum value of the nodes in the removed subtree.
  - The goal is to minimize the maximum score.
- Example test cases with explanations:
  - Example 1: Given a tree with values `[1, 2, 3, 4, 5]`, and removals `[[0, 1], [1, 2], [2, 3], [3, 4]]`, the minimum score after removals is `5`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: For each removal, calculate the score by finding the maximum value in the subtree rooted at the removed node.
- Step-by-step breakdown of the solution:
  1. Perform a depth-first search (DFS) to find the maximum value in the subtree rooted at each removed node.
  2. Calculate the score for each removal by finding the maximum value in the subtree.
  3. Keep track of the minimum score across all removals.
- Why this approach comes to mind first: It is a straightforward approach that directly calculates the score for each removal.

```cpp
class Solution {
public:
    int minimumScore(vector<int>& nums, vector<vector<int>>& edges) {
        int n = nums.size();
        vector<vector<int>> graph(n);
        for (auto& edge : edges) {
            graph[edge[0]].push_back(edge[1]);
            graph[edge[1]].push_back(edge[0]);
        }
        
        int minScore = INT_MAX;
        for (auto& removal : edges) {
            int maxVal = 0;
            for (int i = 0; i < n; i++) {
                if (i == removal[0] || i == removal[1]) {
                    maxVal = max(maxVal, nums[i]);
                }
            }
            minScore = min(minScore, maxVal);
        }
        
        return minScore;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of nodes and $m$ is the number of removals. This is because we perform a DFS for each removal.
> - **Space Complexity:** $O(n + m)$, where $n$ is the number of nodes and $m$ is the number of edges. This is because we store the graph and the removals.
> - **Why these complexities occur:** The brute force approach has high time complexity due to the repeated DFS operations for each removal.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a single DFS to calculate the maximum value in the subtree rooted at each node.
- Detailed breakdown of the approach:
  1. Perform a single DFS to calculate the maximum value in the subtree rooted at each node.
  2. Store the maximum value in the subtree rooted at each node.
  3. For each removal, calculate the score by finding the maximum value in the subtree rooted at the removed node.
  4. Keep track of the minimum score across all removals.
- Proof of optimality: This approach is optimal because it only requires a single DFS operation to calculate the maximum value in the subtree rooted at each node.

```cpp
class Solution {
public:
    int minimumScore(vector<int>& nums, vector<vector<int>>& edges) {
        int n = nums.size();
        vector<vector<int>> graph(n);
        for (auto& edge : edges) {
            graph[edge[0]].push_back(edge[1]);
            graph[edge[1]].push_back(edge[0]);
        }
        
        vector<int> maxVals(n, 0);
        dfs(nums, graph, maxVals, 0, -1);
        
        int minScore = INT_MAX;
        for (auto& removal : edges) {
            minScore = min(minScore, max(maxVals[removal[0]], maxVals[removal[1]]));
        }
        
        return minScore;
    }
    
    void dfs(vector<int>& nums, vector<vector<int>>& graph, vector<int>& maxVals, int node, int parent) {
        maxVals[node] = nums[node];
        for (int child : graph[node]) {
            if (child != parent) {
                dfs(nums, graph, maxVals, child, node);
                maxVals[node] = max(maxVals[node], maxVals[child]);
            }
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of nodes and $m$ is the number of edges. This is because we perform a single DFS operation.
> - **Space Complexity:** $O(n + m)$, where $n$ is the number of nodes and $m$ is the number of edges. This is because we store the graph and the maximum values.
> - **Optimality proof:** This approach is optimal because it only requires a single DFS operation to calculate the maximum value in the subtree rooted at each node.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: DFS, tree traversal, and dynamic programming.
- Problem-solving patterns identified: Using a single DFS operation to calculate the maximum value in the subtree rooted at each node.
- Optimization techniques learned: Avoiding repeated DFS operations for each removal.
- Similar problems to practice: Tree traversal, graph algorithms, and dynamic programming problems.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as an empty graph or removals.
- Edge cases to watch for: Handling cases where the removals are not valid or the graph is not connected.
- Performance pitfalls: Using a brute force approach with high time complexity.
- Testing considerations: Testing with different inputs, such as an empty graph or removals, and verifying the correctness of the output.