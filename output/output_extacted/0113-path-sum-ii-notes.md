## Path Sum II

**Problem Link:** [https://leetcode.com/problems/path-sum-ii/description](https://leetcode.com/problems/path-sum-ii/description)

**Problem Statement:**
- Input format and constraints: Given the root of a binary tree and an integer `targetSum`, return all root-to-leaf paths where the sum of the node values equals `targetSum`. The binary tree has at most `100` nodes, and the values of the nodes are in the range `[-100, 100]`.
- Expected output format: A list of lists, where each sublist represents a path from the root to a leaf node that sums up to `targetSum`.
- Key requirements and edge cases to consider: The tree can be empty, or there might be no paths that sum up to `targetSum`. The solution should handle these cases efficiently.
- Example test cases with explanations:
  - Example 1: Given the binary tree `root = [5,4,8,11,null,13,4,7,2,null,null,5,1]` and `targetSum = 22`, the output should be `[[5,4,11,2],[5,8,4,5]]`.
  - Example 2: Given the binary tree `root = [1,2,3]` and `targetSum = 5`, the output should be `[]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The simplest way to solve this problem is to traverse the binary tree using a depth-first search (DFS) and check every path from the root to a leaf node to see if its sum equals `targetSum`.
- Step-by-step breakdown of the solution:
  1. Define a helper function for DFS that takes a node, the current path, and the current sum.
  2. If the current node is a leaf node and the current sum equals `targetSum`, add the current path to the result.
  3. Otherwise, recursively call the DFS function for the left and right children of the current node, updating the current path and sum accordingly.
- Why this approach comes to mind first: It's a straightforward, intuitive method that checks all possible paths, ensuring no valid path is missed.

```cpp
class Solution {
public:
    vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
        vector<vector<int>> result;
        vector<int> path;
        dfs(root, path, 0, targetSum, result);
        return result;
    }
    
    void dfs(TreeNode* node, vector<int>& path, int currentSum, int targetSum, vector<vector<int>>& result) {
        if (!node) return;
        
        path.push_back(node->val);
        currentSum += node->val;
        
        if (!node->left && !node->right && currentSum == targetSum) {
            result.push_back(path);
        } else {
            dfs(node->left, path, currentSum, targetSum, result);
            dfs(node->right, path, currentSum, targetSum, result);
        }
        
        path.pop_back();
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the tree, since in the worst case, we visit each node once.
> - **Space Complexity:** $O(N)$, as in the worst case (a skewed tree), the recursion call stack and the path vector can grow up to $N$ levels deep.
> - **Why these complexities occur:** These complexities are due to the nature of DFS, which explores as far as possible along each branch before backtracking.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal approach is essentially the same as the brute force approach, as we must explore all paths in the tree to find those that sum up to `targetSum`. However, we can optimize the code slightly by avoiding unnecessary copies of vectors and ensuring we handle edge cases efficiently.
- Detailed breakdown of the approach: We use DFS with a recursive helper function, passing by reference where possible to avoid unnecessary copies, and check for the base case (a leaf node with the target sum) as soon as possible.
- Proof of optimality: This approach is optimal because it visits each node exactly once, which is necessary to find all paths that sum up to `targetSum`.
- Why further optimization is impossible: Since we must check every path, and the number of paths in a binary tree of $N$ nodes can be up to $2^N$ in the worst case (a complete binary tree), any algorithm must have at least a time complexity of $O(2^N)$ in the worst case. However, our algorithm achieves $O(N)$ time complexity because it prunes branches as soon as the sum exceeds the target or reaches a leaf node, making it as efficient as possible for this problem.

```cpp
class Solution {
public:
    vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
        vector<vector<int>> result;
        vector<int> path;
        dfs(root, path, targetSum, result);
        return result;
    }
    
    void dfs(TreeNode* node, vector<int>& path, int targetSum, vector<vector<int>>& result) {
        if (!node) return;
        
        targetSum -= node->val;
        path.push_back(node->val);
        
        if (!node->left && !node->right && targetSum == 0) {
            result.push_back(path);
        } else {
            dfs(node->left, path, targetSum, result);
            dfs(node->right, path, targetSum, result);
        }
        
        path.pop_back();
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the tree, as we visit each node once.
> - **Space Complexity:** $O(N)$, due to the recursion call stack and the path vector.
> - **Optimality proof:** The algorithm is optimal because it must visit each node at least once to find all valid paths, and it does so efficiently by avoiding unnecessary work.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Depth-First Search (DFS), recursion, and path finding in binary trees.
- Problem-solving patterns identified: Breaking down problems into smaller sub-problems (in this case, exploring each branch of the tree) and using recursion to solve them.
- Optimization techniques learned: Avoiding unnecessary copies of data structures, handling edge cases efficiently, and pruning branches in search algorithms.
- Similar problems to practice: Other path-finding problems in graphs or trees, such as finding the shortest path between two nodes.

**Mistakes to Avoid:**
- Common implementation errors: Failing to handle edge cases (like an empty tree), not updating the path or sum correctly during recursion, and not checking for the base case (reaching a leaf node) properly.
- Edge cases to watch for: Empty trees, trees with a single node, and trees where no path sums up to the target.
- Performance pitfalls: Using inefficient data structures or algorithms that result in higher than necessary time or space complexity.
- Testing considerations: Thoroughly testing the solution with various inputs, including edge cases, to ensure correctness and efficiency.