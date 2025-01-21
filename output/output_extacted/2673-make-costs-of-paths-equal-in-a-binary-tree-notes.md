## Make Costs of Paths Equal in a Binary Tree

**Problem Link:** https://leetcode.com/problems/make-costs-of-paths-equal-in-a-binary-tree/description

**Problem Statement:**
- Input: A binary tree where each node has a unique value and a cost to reach that node from its parent.
- Constraints: The tree is not empty, and the number of nodes in the tree is in the range [1, 10^5].
- Expected Output: The minimum cost to make all paths from the root to a leaf node have the same cost.
- Key Requirements: Find the minimum cost to adjust the costs of edges in the tree such that all paths from the root to a leaf node have the same cost.
- Edge Cases: Consider the case where the tree has only one node, or all nodes have the same value.

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of adjusting the costs of edges to make all paths have the same cost.
- Step-by-step breakdown of the solution:
  1. Calculate the cost of each path from the root to a leaf node.
  2. Try all possible combinations of adjusting the costs of edges to make all paths have the same cost.
  3. Calculate the total cost of adjusting the edges for each combination.
  4. Find the minimum total cost among all combinations.

```cpp
class Solution {
public:
    int minCost = INT_MAX;
    void dfs(TreeNode* node, int currentCost, int targetCost, vector<int>& values) {
        if (!node) return;
        if (!node->left && !node->right) {
            minCost = min(minCost, abs(currentCost - targetCost));
            return;
        }
        dfs(node->left, currentCost + node->val, targetCost, values);
        dfs(node->right, currentCost + node->val, targetCost, values);
    }
    int minCost(int targetCost, TreeNode* root) {
        vector<int> values;
        dfs(root, 0, targetCost, values);
        return minCost;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, where $n$ is the number of nodes in the tree. This is because we try all possible combinations of adjusting the costs of edges.
> - **Space Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. This is because we need to store the costs of each path.
> - **Why these complexities occur:** The brute force approach has high time complexity because it tries all possible combinations of adjusting the costs of edges, resulting in exponential time complexity. The space complexity is linear because we need to store the costs of each path.

### Optimal Approach (Required)

**Explanation:**
- Key insight: We can use a hashmap to store the frequency of each cost and find the cost that appears most frequently.
- Detailed breakdown of the approach:
  1. Calculate the cost of each path from the root to a leaf node and store it in a hashmap.
  2. Find the cost that appears most frequently in the hashmap.
  3. Calculate the total cost of adjusting the edges to make all paths have the same cost as the most frequent cost.

```cpp
class Solution {
public:
    int minCost(int targetCost, TreeNode* root) {
        unordered_map<int, int> costCount;
        int minCost = INT_MAX;
        dfs(root, 0, costCount);
        for (auto& pair : costCount) {
            minCost = min(minCost, pair.second * abs(pair.first - targetCost));
        }
        return minCost;
    }
    void dfs(TreeNode* node, int currentCost, unordered_map<int, int>& costCount) {
        if (!node) return;
        if (!node->left && !node->right) {
            costCount[currentCost + node->val]++;
            return;
        }
        dfs(node->left, currentCost + node->val, costCount);
        dfs(node->right, currentCost + node->val, costCount);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. This is because we visit each node once.
> - **Space Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. This is because we need to store the costs of each path in the hashmap.
> - **Optimality proof:** This approach is optimal because it visits each node once and uses a hashmap to store the frequency of each cost, resulting in linear time complexity.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a hashmap to store the frequency of each cost and finding the cost that appears most frequently.
- Problem-solving patterns identified: Using a brute force approach to understand the problem and then optimizing it using a hashmap.
- Optimization techniques learned: Using a hashmap to store the frequency of each cost and finding the cost that appears most frequently.
- Similar problems to practice: Problems that involve finding the most frequent element in a dataset.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the hashmap correctly or not handling the case where the tree has only one node.
- Edge cases to watch for: The case where the tree has only one node or all nodes have the same value.
- Performance pitfalls: Using a brute force approach that tries all possible combinations of adjusting the costs of edges, resulting in exponential time complexity.
- Testing considerations: Testing the solution with different inputs and edge cases to ensure it works correctly.