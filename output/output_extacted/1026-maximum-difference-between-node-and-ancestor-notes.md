## Maximum Difference Between Node and Ancestor

**Problem Link:** https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description

**Problem Statement:**
- Input format and constraints: The input is the root of a binary tree where each node has a value. The constraint is to find the maximum difference between the value of a node and the value of its ancestor.
- Expected output format: The output should be an integer representing the maximum difference between the value of a node and the value of its ancestor.
- Key requirements and edge cases to consider: We need to consider all possible paths in the tree and calculate the maximum difference for each node with its ancestors.
- Example test cases with explanations: For example, given the binary tree with root `[8,3,10,1,6,14,4,7,13]`, the maximum difference between a node and its ancestor is `13`, which can be obtained by the path `8 -> 3 -> 10 -> 14`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To solve this problem, we can use a brute force approach where we calculate the maximum difference for each node with all its ancestors.
- Step-by-step breakdown of the solution:
  1. Perform a depth-first search (DFS) on the binary tree.
  2. For each node, calculate the maximum difference between its value and the values of all its ancestors.
  3. Update the maximum difference if a larger difference is found.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, but it has a high time complexity due to the repeated calculations for each node.

```cpp
class Solution {
public:
    int maxAncestorDiff(TreeNode* root) {
        int maxDiff = 0;
        vector<int> ancestors;
        
        function<void(TreeNode*, vector<int>)> dfs = 
            [&](TreeNode* node, vector<int> ancestors) {
                if (!node) return;
                int minAncestor = INT_MAX;
                int maxAncestor = INT_MIN;
                for (int ancestor : ancestors) {
                    minAncestor = min(minAncestor, ancestor);
                    maxAncestor = max(maxAncestor, ancestor);
                }
                maxDiff = max(maxDiff, maxAncestor - node->val);
                maxDiff = max(maxDiff, node->val - minAncestor);
                ancestors.push_back(node->val);
                dfs(node->left, ancestors);
                dfs(node->right, ancestors);
                ancestors.pop_back();
            };
        
        dfs(root, ancestors);
        return maxDiff;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot h)$, where $n$ is the number of nodes and $h$ is the height of the tree, because we perform DFS and calculate the maximum difference for each node with all its ancestors.
> - **Space Complexity:** $O(h)$, because we use a recursive function call stack with a maximum depth of $h$.
> - **Why these complexities occur:** The time complexity is high due to the repeated calculations for each node, and the space complexity is due to the recursive function call stack.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can maintain two variables, `minSoFar` and `maxSoFar`, to keep track of the minimum and maximum values seen so far in the path from the root to the current node.
- Detailed breakdown of the approach:
  1. Perform a depth-first search (DFS) on the binary tree.
  2. For each node, update `minSoFar` and `maxSoFar` with the minimum and maximum values seen so far in the path.
  3. Calculate the maximum difference between the current node's value and `minSoFar` and `maxSoFar`.
  4. Update the maximum difference if a larger difference is found.
- Proof of optimality: This approach is optimal because we only need to keep track of the minimum and maximum values seen so far in the path, which reduces the time complexity to $O(n)$.

```cpp
class Solution {
public:
    int maxAncestorDiff(TreeNode* root) {
        int maxDiff = 0;
        
        function<void(TreeNode*, int, int)> dfs = 
            [&](TreeNode* node, int minSoFar, int maxSoFar) {
                if (!node) return;
                maxDiff = max(maxDiff, maxSoFar - node->val);
                maxDiff = max(maxDiff, node->val - minSoFar);
                dfs(node->left, min(minSoFar, node->val), max(maxSoFar, node->val));
                dfs(node->right, min(minSoFar, node->val), max(maxSoFar, node->val));
            };
        
        dfs(root, root->val, root->val);
        return maxDiff;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes, because we perform DFS and calculate the maximum difference for each node in constant time.
> - **Space Complexity:** $O(h)$, because we use a recursive function call stack with a maximum depth of $h$.
> - **Optimality proof:** This approach is optimal because we only need to keep track of the minimum and maximum values seen so far in the path, which reduces the time complexity to $O(n)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Depth-first search (DFS) and maintaining minimum and maximum values seen so far in the path.
- Problem-solving patterns identified: Using recursive functions to perform DFS and keeping track of minimum and maximum values.
- Optimization techniques learned: Reducing the time complexity by keeping track of minimum and maximum values seen so far in the path.
- Similar problems to practice: Other problems that involve performing DFS and keeping track of minimum and maximum values.

**Mistakes to Avoid:**
- Common implementation errors: Not updating the minimum and maximum values correctly, or not calculating the maximum difference correctly.
- Edge cases to watch for: Handling the case where the tree is empty, or where the tree has only one node.
- Performance pitfalls: Using a brute force approach that has a high time complexity.
- Testing considerations: Testing the solution with different input cases, including edge cases, to ensure that it works correctly.